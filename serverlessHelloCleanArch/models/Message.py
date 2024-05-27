from datetime import datetime
from enum import Enum
from uuid import uuid4

from sqlalchemy import Column, DateTime
from sqlalchemy import Enum as SQLEnum
from sqlalchemy import Integer, String
from sqlalchemy.ext.declarative import declarative_base


class MessageType(Enum):
    HELLO = "HELLO"
    BYE = "BYE"


Base = declarative_base()


class Message(Base):
    __tablename__ = "message"

    id = Column(String(255), primary_key=True, default=lambda: str(uuid4()))
    created_at = Column(DateTime, default=datetime.now)
    text = Column(String(255), nullable=False)
    message_type = Column(SQLEnum(MessageType), nullable=True)
