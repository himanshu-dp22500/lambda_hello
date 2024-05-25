from datetime import datetime
from uuid import uuid4

from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Message(Base):
    __tablename__ = 'message'

    id = Column(String(255), primary_key=True, default=lambda: str(uuid4()))
    created_at = Column(DateTime, default=datetime.now)
    text = Column(String(255))
