# auth models
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.dialects.postgresql import UUID
from app.core.config import Base
import uuid

class User(Base):
    __tablename__ = 'user_account'

    id: uuid.UUID = Column(UUID(as_uuid=True), default=uuid.uuid4, primary_key=True, index=True)
    username: str = Column(String(30), index=True)
    password: str = Column(String(40))
    email: str = Column(String(255), unique=True)
    color_theme: str = Column(String(10),)
    font_theme: str = Column(String(10))

