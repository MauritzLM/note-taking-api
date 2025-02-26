from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os
from dotenv import load_dotenv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[3]

env_path = load_dotenv(os.path.join(BASE_DIR, '.env'))
load_dotenv(env_path)

# db connection
DATABASE_URL = os.environ.get('DATABASE_URL')

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()