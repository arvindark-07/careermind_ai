from datetime import datetime
from sqlalchemy import Column,Integer,String,Text,DateTime,ForeignKey
from .database import Base
class User(Base):
    __tablename__='users'; id=Column(Integer,primary_key=True); email=Column(String(255),unique=True,index=True,nullable=False); name=Column(String(255),nullable=False); created_at=Column(DateTime,default=datetime.utcnow)
class Resume(Base):
    __tablename__='resumes'; id=Column(Integer,primary_key=True); user_id=Column(Integer,ForeignKey('users.id'),index=True,nullable=False); filename=Column(String(255),nullable=False); raw_text=Column(Text,default=''); extracted_json=Column(Text,default='{}'); created_at=Column(DateTime,default=datetime.utcnow)
class Memory(Base):
    __tablename__='memories'; id=Column(Integer,primary_key=True); user_id=Column(Integer,ForeignKey('users.id'),index=True,nullable=False); content=Column(Text,nullable=False); source=Column(String(50),default='conversation'); created_at=Column(DateTime,default=datetime.utcnow)
class Conversation(Base):
    __tablename__='conversations'; id=Column(Integer,primary_key=True); user_id=Column(Integer,ForeignKey('users.id'),index=True,nullable=False); role=Column(String(20),nullable=False); content=Column(Text,nullable=False); created_at=Column(DateTime,default=datetime.utcnow)
