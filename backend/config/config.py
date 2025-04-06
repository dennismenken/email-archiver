import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY")
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///data/email_archiver.db")
    DATABASE_DIR = os.getenv("DATABASE_DIR", "data")
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
    # Add more configuration variables as needed

config = Config()