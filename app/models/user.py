# auth models
from sqlalchemy import Column, Integer, String, Boolean
from core.config import Base
import uuid

class User(Base):
    __tablename__ = 'user_account'

    id: int = Column(Integer, default=uuid.uuid4, primary_key=True, index=True)
    name: str = Column(String(30), index=True)
    password: str = Column(String(255))
    email: str = Column(String(255))

