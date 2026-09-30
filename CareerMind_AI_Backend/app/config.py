import os
from dotenv import load_dotenv

load_dotenv()

APP_NAME = "CareerMind AI"

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "sqlite:///./careermind.db"
)

# Groq
GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")
GROQ_MODEL = os.getenv(
    "GROQ_MODEL",
    "llama-3.3-70b-versatile"
)

# Hindsight
HINDSIGHT_API_KEY = os.getenv("HINDSIGHT_API_KEY", "")
HINDSIGHT_BASE_URL = os.getenv(
    "HINDSIGHT_BASE_URL",
    "https://api.hindsight.vectorize.io"
)
HINDSIGHT_BANK_ID = os.getenv(
    "HINDSIGHT_BANK_ID",
    "careermind"
)

MAX_UPLOAD_MB = int(
    os.getenv("MAX_UPLOAD_MB", "10")
)