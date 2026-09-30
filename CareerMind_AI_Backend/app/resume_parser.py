import io,re
from pypdf import PdfReader
SKILLS=['Python','Java','C','C++','JavaScript','TypeScript','HTML','CSS','React','FastAPI','Flask','Django','MySQL','PostgreSQL','MongoDB','Power BI','Excel','Machine Learning','Deep Learning','Generative AI','Artificial Intelligence','Data Analytics','Data Visualization','SQL','Git','GitHub','Figma','Canva','TensorFlow','PyTorch','OpenCV','NLP','Prompt Engineering','AWS','Azure','Docker']
def pdf_to_text(data):
    return '\n'.join((p.extract_text() or '') for p in PdfReader(io.BytesIO(data)).pages)
def extract_profile(text):
    lower=text.lower(); skills=[s for s in SKILLS if s.lower() in lower]
    lines=[x.strip() for x in text.splitlines() if x.strip()]
    def grab(words):
        out=[]; active=False
        headers={'skills','education','projects','project','certifications','certificates','experience','internships','internship','achievements','interests','objective'}
        for line in lines:
            low=line.lower().strip(' :-')
            if any(w in low for w in words): active=True; continue
            if active and low in headers and not any(w in low for w in words): active=False
            if active and len(out)<20: out.append(line)
        return out
    return {'skills':skills,'education':grab(['education']),'projects':grab(['projects','project']),'certifications':grab(['certifications','certificates']),'experience':grab(['experience','internships','internship']),'text_preview':re.sub(r'\s+',' ',text)[:1000]}
