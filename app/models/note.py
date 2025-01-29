# note model
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from core.config import Base
import uuid

class note(Base):
    __tablename__ = 'notes'

    id: int = Column(Integer, default=uuid.uuid4, primary_key=True, index=True)
    title: str = Column(String(255), index=True)
    text: str = Column(String)
    isArchived: bool = Column(Boolean, default=False)
    author: int = Column(Integer, ForeignKey='user_account.id')