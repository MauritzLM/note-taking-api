import app.models.note as notes
import app.models.user as users
from app.core.config import engine, SessionLocal
from sqlalchemy.orm import Session
from typing import Annotated
from fastapi import Depends

# db connection
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]