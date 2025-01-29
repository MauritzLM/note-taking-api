from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# db connection
# Replace with your PostgreSQL connection string
DATABASE_URL = "postgresql://postgres:Rei7VinDicAtiO79@localhost:5432/fastapi_test"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()