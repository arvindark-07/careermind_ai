# 🧠 CareerMind AI

### A Long-Term Memory Career Agent

CareerMind AI is an AI-powered career assistant that creates a persistent, personalized memory of a user's professional journey.

Instead of treating every conversation as a separate interaction, CareerMind AI remembers the user's:

* 📄 Resume
* 💻 Technical skills
* 🚀 Projects
* 🎓 Education
* 🏆 Certifications
* 💼 Experience
* 🎯 Career goals
* 💬 Previous conversations
* ⭐ Career and internship preferences

The system combines **resume information + long-term memory + conversation history + an LLM** to provide personalized career guidance.

---

# 🎯 Problem Statement

Most AI career assistants provide generic answers because they do not maintain meaningful long-term context about the user.

For example, a student might tell an AI:

> I want to get an AI/ML internship.

Later, the student might say:

> I know Python and SQL, but I am weak in machine learning.

Without persistent memory, the user may have to repeat this information in future conversations.

CareerMind AI solves this by maintaining a **long-term career memory**.

---

# 💡 Our Solution

CareerMind AI creates a continuously evolving career profile for every user.

```text
                  USER
                   │
                   ▼
             Upload Resume
                   │
                   ▼
           ┌───────────────┐
           │ Resume Parser │
           └───────┬───────┘
                   │
                   ▼
        ┌──────────────────────┐
        │ Career Profile       │
        │                      │
        │ Skills               │
        │ Projects             │
        │ Education            │
        │ Certifications       │
        │ Experience           │
        └──────────┬───────────┘
                   │
                   ▼
          ┌─────────────────┐
          │ Hindsight       │
          │ Long-Term       │
          │ Memory          │
          └────────┬────────┘
                   │
                   │
             User Conversation
                   │
                   ▼
          ┌─────────────────┐
          │ Memory Recall   │
          └────────┬────────┘
                   │
                   ▼
          ┌─────────────────┐
          │ Groq LLM        │
          │ GPT-OSS-20B     │
          └────────┬────────┘
                   │
                   ▼
        Personalized Career Advice
```

---

# ✨ Core Features

## 📄 Resume Understanding

The user uploads a PDF resume.

CareerMind AI extracts relevant information such as:

* Programming languages
* Web technologies
* Databases
* Core CS concepts
* Projects
* Education
* Certifications
* Experience
* Strengths

The extracted information is converted into structured profile information and memories.

---

# 🧠 Long-Term Memory

CareerMind AI uses **Hindsight** as its long-term memory layer.

Example:

```text
User:
I want to get an AI/ML internship.
```

CareerMind stores this information.

Later:

```text
User:
What do you remember about my career goal?
```

CareerMind can recall:

```text
The user wants to get an AI/ML internship.
```

This allows the agent to maintain continuity across conversations.

---

# 💬 Personalized AI Chat

Users can ask questions such as:

```text
What should I focus on for my next internship?
```

```text
What skills should I improve?
```

```text
What projects should I build?
```

```text
What do you remember about me?
```

```text
Am I ready for an AI/ML internship?
```

The agent uses the user's career context to generate personalized answers.

---

# 🎯 Career Gap Identification

CareerMind AI can use the user's existing profile and career goal to identify areas that may need improvement.

Example:

```text
Current Profile

Python
Java
C
SQL
Git
GitHub
Web Development
Multiple Projects

Career Goal

AI/ML Internship
```

The agent can identify relevant areas such as:

```text
Machine Learning fundamentals
Data Science
Model development
ML projects
Model deployment
```

and provide practical learning steps.

---

# 🏗️ Complete System Architecture

```text
                         ┌─────────────────────┐
                         │       USER          │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │   React Frontend    │
                         │                     │
                         │ Resume Upload       │
                         │ Career Profile      │
                         │ Chat Interface      │
                         │ Memory Display      │
                         └──────────┬──────────┘
                                    │
                                  HTTP
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │   FastAPI Backend   │
                         │                     │
                         │ API Routes          │
                         │ Business Logic      │
                         │ Resume Processing   │
                         └───────┬─────┬───────┘
                                 │     │
                     ┌───────────┘     └─────────────┐
                     ▼                               ▼
            ┌─────────────────┐             ┌─────────────────┐
            │ SQLite Database │             │ Hindsight       │
            │                 │             │                 │
            │ Users           │             │ Long-Term       │
            │ Resumes         │             │ Memory          │
            │ Memories        │             │                 │
            │ Conversations   │             └────────┬────────┘
            └─────────────────┘                      │
                                                     ▼
                                            ┌─────────────────┐
                                            │    Groq LLM     │
                                            │                 │
                                            │ openai/         │
                                            │ gpt-oss-20b     │
                                            └────────┬────────┘
                                                     │
                                                     ▼
                                            AI Career Response
```

---

# 🧩 Technology Stack

## Frontend

* React
* Vite
* JavaScript
* HTML
* CSS
* Fetch API

## Backend

* Python
* FastAPI
* Uvicorn
* SQLAlchemy
* SQLite

## AI

* Groq API
* `openai/gpt-oss-20b`

## Long-Term Memory

* Hindsight

## Resume Processing

* PyPDF

## Environment Configuration

* python-dotenv

---

# 📁 Complete Project Structure

```text
CareerMindAI/
│
├── README.md
│
├── CareerMind_AI_Backend/
│   │
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py
│   │   ├── config.py
│   │   ├── database.py
│   │   ├── models.py
│   │   ├── resume_parser.py
│   │   ├── hindsight.py
│   │   └── llm.py
│   │
│   ├── requirements.txt
│   ├── .env
│   ├── .env.example
│   ├── .gitignore
│   └── careermind.db
│
└── CareerMind_AI_Frontend/
    │
    ├── src/
    │   ├── components/
    │   ├── pages/
    │   ├── App.jsx
    │   ├── main.jsx
    │   └── ...
    │
    ├── public/
    ├── index.html
    ├── package.json
    ├── package-lock.json
    └── vite.config.js
```

---

# ⚙️ Prerequisites

Install the following:

### Python

Python 3.13 recommended.

Check:

```powershell
python --version
```

or:

```powershell
py --version
```

### Node.js

Node.js 20+ recommended.

Check:

```powershell
node --version
```

Current development environment:

```text
Node.js v24.11.0
npm 11.6.1
```

---

# 🐍 Backend Installation

Open PowerShell.

Go to the project:

```powershell
cd "C:\Users\DELL\Downloads\CareerMindAI"
```

Go to backend:

```powershell
cd .\CareerMind_AI_Backend
```

---

## Create Virtual Environment

```powershell
py -3.13 -m venv .venv
```

Activate:

```powershell
.\.venv\Scripts\Activate.ps1
```

You should see:

```text
(.venv)
```

in the terminal.

---

## Install Backend Dependencies

```powershell
pip install -r requirements.txt
```

If required:

```powershell
pip install groq
```

---

# 🔐 Environment Configuration

Create:

```text
CareerMind_AI_Backend/.env
```

Add:

```env
GROQ_API_KEY=YOUR_GROQ_API_KEY
GROQ_MODEL=openai/gpt-oss-20b

HINDSIGHT_API_KEY=YOUR_HINDSIGHT_API_KEY
HINDSIGHT_BASE_URL=https://api.hindsight.vectorize.io
HINDSIGHT_BANK_ID=careermind

DATABASE_URL=sqlite:///./careermind.db

MAX_UPLOAD_MB=10
```

### Important

Never commit the real `.env` file to GitHub.

Your `.gitignore` should contain:

```text
.env
.venv/
__pycache__/
*.pyc
careermind.db
```

---

# ▶️ Start Backend

From:

```text
CareerMind_AI_Backend
```

run:

```powershell
uvicorn app.main:app --reload
```

Backend:

```text
http://127.0.0.1:8000
```

Swagger API documentation:

```text
http://127.0.0.1:8000/docs
```

---

# 🎨 Frontend Installation

Open a **second terminal**.

Go to:

```powershell
cd "C:\Users\DELL\Downloads\CareerMindAI\CareerMind_AI_Frontend"
```

Install dependencies:

```powershell
npm install
```

Start Vite:

```powershell
npm run dev
```

Frontend:

```text
http://localhost:5173/
```

---

# 🔌 Frontend → Backend Connection

The frontend communicates with the FastAPI backend:

```javascript
const API_BASE_URL = "http://127.0.0.1:8000";
```

For the current hackathon demo, the user ID can be:

```javascript
const USER_ID = 1;
```

---

# 📡 API Endpoints

## Health

```http
GET /health
```

Example:

```text
http://127.0.0.1:8000/health
```

---

## Create User

```http
POST /users
```

Parameters:

```text
name
email
```

Example:

```text
POST /users?name=Demo%20User&email=demo@example.com
```

---

## Upload Resume

```http
POST /users/{user_id}/resume
```

Example:

```text
POST /users/1/resume
```

The endpoint:

1. Validates the PDF.
2. Reads the uploaded file.
3. Extracts text.
4. Extracts profile information.
5. Stores the resume in SQLite.
6. Creates resume memories.
7. Sends relevant memories to Hindsight.

---

## Get Resume

```http
GET /users/{user_id}/resume
```

Example:

```text
GET /users/1/resume
```

---

## Store Memory

```http
POST /users/{user_id}/memory
```

Example:

```text
POST /users/1/memory
```

Example content:

```text
My career goal is to get an AI/ML internship.
```

---

## Get Memories

```http
GET /users/{user_id}/memories
```

Example:

```text
GET /users/1/memories
```

---

## Chat

```http
POST /users/{user_id}/chat
```

Example:

```text
POST /users/1/chat
```

Message:

```text
What should I focus on for my next AI/ML internship?
```

The backend performs:

```text
Current Question
      ↓
Resume Profile
      ↓
Local Memories
      ↓
Hindsight Recall
      ↓
Conversation History
      ↓
Groq LLM
      ↓
Personalized Answer
```

---

## Conversation History

```http
GET /users/{user_id}/history
```

Example:

```text
GET /users/1/history
```

---

# 🧠 Memory Architecture

CareerMind AI uses two complementary memory layers.

## SQLite

SQLite stores application data such as:

```text
Users
Resumes
Memories
Conversations
```

## Hindsight

Hindsight provides long-term memory capabilities.

The application sends meaningful career information to Hindsight and recalls relevant memories when the user asks questions.

This allows the agent to maintain context beyond a single conversation.

---

# 🔄 Memory Example

### First interaction

```text
User:
I want to focus on AI/ML internships.
```

CareerMind stores the information.

### Second interaction

```text
User:
I know Python but I need to improve my machine learning skills.
```

CareerMind stores this information as additional context.

### Later

```text
User:
What should I learn next?
```

CareerMind can combine:

```text
Career Goal
+
Existing Skills
+
Skill Gaps
+
Previous Conversations
+
Resume
```

to produce a personalized answer.

---

# 🤖 LLM Architecture

The LLM receives four major context sources:

```text
1. Resume / Profile

2. Long-Term Memories

3. Previous Conversation

4. Current User Question
```

Conceptually:

```text
                 Resume
                    │
                    ▼
             ┌─────────────┐
Memory ─────►│             │
             │ CareerMind  │◄──── Conversation
             │    Agent    │
             │             │
Question ───►│             │
             └──────┬──────┘
                    │
                    ▼
                 Groq LLM
                    │
                    ▼
            Personalized Answer
```

---

# 🧪 Backend Testing

Open:

```text
http://127.0.0.1:8000/docs
```

## Test 1 — Health

Run:

```http
GET /health
```

Expected:

```json
{
  "status": "ok",
  "agent": "CareerMind AI"
}
```

---

## Test 2 — Create User

Create a demo user.

Example:

```text
Name: Demo User
Email: demo@example.com
```

Record the returned user ID.

For the current demo:

```text
USER_ID = 1
```

---

## Test 3 — Add Memory

Run:

```http
POST /users/1/memory
```

Content:

```text
My career goal is to get an AI/ML internship. I know Python, SQL, Java and C. I want to improve my machine learning skills and build more AI projects.
```

---

## Test 4 — Verify Memory

Run:

```http
GET /users/1/memories
```

Verify that the career goal appears.

---

## Test 5 — Test Hindsight Recall

Run:

```http
POST /users/1/chat
```

Message:

```text
What do you remember about my career goal?
```

Check:

```json
"memories_used": [...]
```

The response should contain relevant career information.

---

## Test 6 — Upload Resume

Use:

```http
POST /users/1/resume
```

Upload your PDF resume.

Then:

```http
GET /users/1/resume
```

Verify the extracted profile.

---

## Test 7 — Personalized Career Advice

Ask:

```text
What should I focus on for my next AI/ML internship?
```

The answer should use the user's resume and memory.

---

# 🎬 Recommended Hackathon Demo

The entire demo can be completed in a few minutes.

## Step 1 — Open CareerMind AI

Show:

```text
CareerMind AI
Your Long-Term Career Agent
```

---

## Step 2 — Upload Resume

Upload the user's PDF resume.

Show the extracted:

```text
Skills
Projects
Education
Certifications
Experience
```

---

## Step 3 — Set Career Goal

Tell the agent:

```text
I want to get an AI/ML internship.
```

---

## Step 4 — Have a Conversation

Say:

```text
I know Python and SQL, but I need to improve my machine learning skills.
```

The agent stores this information.

---

## Step 5 — Demonstrate Long-Term Memory

Ask:

```text
What do you remember about my career goal?
```

The agent recalls the information.

---

## Step 6 — Demonstrate Personalization

Ask:

```text
What should I focus on for my next AI/ML internship?
```

CareerMind combines:

```text
Resume
+
Skills
+
Projects
+
Career Goal
+
Long-Term Memory
+
Conversation History
```

and generates personalized guidance.

---

# 📊 Example Career Profile

A sample profile may contain:

```text
Programming:
Python
Java
C
SQL

Web:
HTML
CSS
JavaScript

Database:
MySQL

Core CS:
Data Structures
OOP
DBMS
Operating Systems

Software Engineering:
SDLC
Testing
Debugging
REST APIs

Tools:
Git
GitHub
VS Code
```

Example projects:

```text
JARVIS Voice AI Assistant
AIR Mouse Using Hand Gestures
Blockchain-Based Gaming Application
E-Commerce Website
```

Example certifications:

```text
Python Essentials – Cisco
Google AI Certificate
Google Prompting Essentials
SAP Code Unnati Innovation Marathon
```

---

# 🔐 Security Considerations

API keys must remain on the backend.

Never write:

```javascript
const GROQ_API_KEY = "gsk_...";
```

inside the React frontend.

Instead:

```text
React Frontend
      │
      ▼
FastAPI Backend
      │
      ├── Groq API
      │
      └── Hindsight API
```

The `.env` file should never be committed to source control.

---

# 🚀 Future Enhancements

CareerMind AI can be extended with:

## Authentication

* User signup
* Login
* Multiple user accounts
* Secure sessions

## Career Intelligence

* Job description analysis
* Job matching
* Internship recommendations
* Skill gap analysis
* Career roadmaps

## Learning

* Personalized learning plans
* Course recommendations
* Progress tracking
* Project recommendations

## Interview Preparation

* Mock interviews
* Technical interview questions
* HR interview preparation
* Interview feedback

## Resume Intelligence

* ATS analysis
* Resume improvement
* Job-specific resume customization
* Cover letter generation

## Deployment

* Cloud backend
* PostgreSQL
* Docker
* CI/CD
* Production authentication

---

# 🏆 Project Differentiator

CareerMind AI is not designed to be just another chatbot.

Its core concept is:

```text
              NORMAL CHATBOT

Question
   ↓
Answer
   ↓
Conversation Ends


              CAREERMIND AI

Resume
   ↓
Career Profile
   ↓
Long-Term Memory
   ↓
Conversations
   ↓
New Information
   ↓
Updated Career Context
   ↓
Better Personalized Guidance
```

The system becomes more useful as the user's career context grows.

---

# 📌 Current Development Status

```text
Backend
████████████████████ 100%

Resume Parsing
████████████████████ 100%

SQLite
████████████████████ 100%

Hindsight Memory
████████████████████ 100%

Groq LLM
████████████████████ 100%

Chat API
████████████████████ 100%

Frontend
████████████████░░░░ 80%

Frontend ↔ Backend
██████████████░░░░░░ 70%

Hackathon Demo
███████████████░░░░░ 75%
```

---

# 🛠️ Troubleshooting

## `404 Not Found` on memory endpoint

Make sure the user ID exists.

Example:

```text
POST /users/1/memory
```

If user `1` does not exist, create the user first.

---

## Frontend cannot connect to backend

Check that both servers are running.

Backend:

```text
http://127.0.0.1:8000
```

Frontend:

```text
http://localhost:5173
```

Test:

```text
http://127.0.0.1:8000/health
```

---

## Groq model error

Check `.env`:

```env
GROQ_MODEL=openai/gpt-oss-20b
```

Restart the backend after changing environment variables.

---

## Hindsight not working

Check:

```env
HINDSIGHT_API_KEY=YOUR_HINDSIGHT_API_KEY
HINDSIGHT_BASE_URL=https://api.hindsight.vectorize.io
HINDSIGHT_BANK_ID=careermind
```

Restart FastAPI after changing `.env`.

---

## PDF upload error

Make sure:

* File is a PDF.
* File is below the configured size limit.
* Backend is running.
* `pypdf` is installed.

---

# 🚀 Quick Start

For a new machine:

## Terminal 1 — Backend

```powershell
cd "C:\Users\DELL\Downloads\CareerMindAI\CareerMind_AI_Backend"

py -3.13 -m venv .venv

.\.venv\Scripts\Activate.ps1

pip install -r requirements.txt

uvicorn app.main:app --reload
```

Backend:

```text
http://127.0.0.1:8000
```

---

## Terminal 2 — Frontend

```powershell
cd "C:\Users\DELL\Downloads\CareerMindAI\CareerMind_AI_Frontend"

npm install

npm run dev
```

Frontend:

```text
http://localhost:5173
```

---

# 🔗 Application URLs

| Component    | URL                            |
| ------------ | ------------------------------ |
| Frontend     | `http://localhost:5173`        |
| Backend      | `http://127.0.0.1:8000`        |
| FastAPI Docs | `http://127.0.0.1:8000/docs`   |
| Health Check | `http://127.0.0.1:8000/health` |

---

# 🎯 One-Line Project Description

> **CareerMind AI is a long-term memory career agent that understands a user's resume, remembers their career goals and conversations, and uses that context to provide personalized career guidance.**

---

# 🧠 Project Vision

CareerMind AI aims to become a **personal career companion** that grows with the user.

Instead of repeatedly explaining:

```text
Who am I?
What skills do I have?
What projects have I built?
What is my career goal?
What am I learning?
What do I need to improve?
```

the user can simply continue the conversation.

**CareerMind remembers.**

---

# 👥 Project Information

**Project Name:** CareerMind AI

**Category:** AI Agent / Long-Term Memory / Career Technology

**Primary Use Case:** Personalized career and internship guidance

**Frontend:** React + Vite

**Backend:** FastAPI + Python

**LLM:** Groq

**Memory:** Hindsight

**Database:** SQLite

**Resume Processing:** PyPDF

**Development Type:** Hackathon Project

---

# 📜 License

This project is developed as a hackathon project for educational, demonstration, and development purposes.
