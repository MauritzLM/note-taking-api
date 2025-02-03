# note model
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from app.core.config import Base
from sqlalchemy.dialects.postgresql import UUID, ARRAY
import uuid

class Note(Base):
    __tablename__ = 'notes'

    id: uuid.UUID = Column(UUID(as_uuid=True), default=uuid.uuid4, primary_key=True, index=True)
    title: str = Column(String(255), index=True)
    text: str = Column(String)
    isArchived: bool = Column(Boolean, default=False)
    author: uuid.UUID = Column(UUID(as_uuid=True), ForeignKey('user_account.id'))
    tags = Column(ARRAY(String), default=[])