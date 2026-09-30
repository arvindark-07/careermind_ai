import json
from fastapi import FastAPI,UploadFile,File,Depends,HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from .database import Base,engine,get_db
from .models import User,Resume,Memory,Conversation
from .resume_parser import pdf_to_text,extract_profile
from .hindsight import HindsightMemory
from .llm import generate_answer
from .config import MAX_UPLOAD_MB
Base.metadata.create_all(bind=engine)
app=FastAPI(title='CareerMind AI',version='1.0.0')
app.add_middleware(CORSMiddleware,allow_origins=['*'],allow_credentials=True,allow_methods=['*'],allow_headers=['*'])
mem=HindsightMemory()
def user(db,id):
    u=db.query(User).filter(User.id==id).first()
    if not u: raise HTTPException(404,'User not found')
    return u
@app.get('/health')
def health(): return {'status':'ok','agent':'CareerMind AI','memory_provider':'hindsight' if mem.enabled else 'sqlite_fallback'}
@app.post('/users')
def create_user(name:str,email:str,db:Session=Depends(get_db)):
    u=db.query(User).filter(User.email==email).first()
    if u:return {'id':u.id,'name':u.name,'email':u.email}
    u=User(name=name,email=email);db.add(u);db.commit();db.refresh(u);return {'id':u.id,'name':u.name,'email':u.email}
@app.post('/users/{user_id}/resume')
async def upload_resume(user_id:int,file:UploadFile=File(...),db:Session=Depends(get_db)):
    user(db,user_id)
    if not file.filename.lower().endswith('.pdf'):raise HTTPException(400,'Please upload a PDF resume')
    data=await file.read()
    if len(data)>MAX_UPLOAD_MB*1024*1024:raise HTTPException(413,'Resume file too large')
    text=pdf_to_text(data);profile=extract_profile(text)
    r=Resume(user_id=user_id,filename=file.filename,raw_text=text,extracted_json=json.dumps(profile));db.add(r)
    for k,v in profile.items():
        if k!='text_preview' and v:
            c=f'Resume {k}: {v}';db.add(Memory(user_id=user_id,content=c,source='resume'));await mem.retain(user_id,c)
    db.commit();db.refresh(r)
    return {'resume_id':r.id,'filename':r.filename,'profile':profile}
@app.get('/users/{user_id}/resume')
def latest_resume(user_id:int,db:Session=Depends(get_db)):
    user(db,user_id);r=db.query(Resume).filter(Resume.user_id==user_id).order_by(Resume.created_at.desc()).first()
    if not r:raise HTTPException(404,'No resume uploaded')
    return {'resume_id':r.id,'filename':r.filename,'profile':json.loads(r.extracted_json)}
@app.post('/users/{user_id}/memory')
async def remember(user_id:int,content:str,source:str='conversation',db:Session=Depends(get_db)):
    user(db,user_id);m=Memory(user_id=user_id,content=content,source=source);db.add(m);db.commit();db.refresh(m);remote=await mem.retain(user_id,content);return {'id':m.id,'remote':remote}
@app.get('/users/{user_id}/memories')
def memories(user_id:int,db:Session=Depends(get_db)):
    user(db,user_id); rows=db.query(Memory).filter(Memory.user_id==user_id).order_by(Memory.created_at.desc()).limit(50).all();return {'memories':[{'id':x.id,'content':x.content,'source':x.source} for x in rows]}
@app.post('/users/{user_id}/chat')
async def chat(user_id:int,message:str,db:Session=Depends(get_db)):
    user(db,user_id);r=db.query(Resume).filter(Resume.user_id==user_id).order_by(Resume.created_at.desc()).first();profile=json.loads(r.extracted_json) if r else {}
    local=db.query(Memory).filter(Memory.user_id==user_id).order_by(Memory.created_at.desc()).limit(20).all();remote=await mem.recall(user_id,message);used=list(dict.fromkeys([x.content for x in local]+remote))[:12]
    rows=db.query(Conversation).filter(Conversation.user_id==user_id).order_by(Conversation.created_at.desc()).limit(10).all();history=[{'role':x.role,'content':x.content} for x in reversed(rows)]
    db.add(Conversation(user_id=user_id,role='user',content=message));answer=await generate_answer(message,profile,used,history);db.add(Conversation(user_id=user_id,role='assistant',content=answer))
    if message.lower().startswith(('remember that','remember ','my goal is','i prefer')):
        db.add(Memory(user_id=user_id,content=message,source='conversation'));await mem.retain(user_id,message)
    db.commit();return {'answer':answer,'memories_used':used[:8]}
@app.get('/users/{user_id}/history')
def history(user_id:int,db:Session=Depends(get_db)):
    user(db,user_id);rows=db.query(Conversation).filter(Conversation.user_id==user_id).order_by(Conversation.created_at.asc()).all();return {'messages':[{'role':x.role,'content':x.content} for x in rows]}
