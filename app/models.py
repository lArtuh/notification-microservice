from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()


class Notification(Base):
    __tablename__ = "notifications"

    id = Column(Integer, primary_key=True, index=True)
    message = Column(String, nullable=False)
    recipient = Column(String, nullable=False)
    read = Column(Boolean, default=False)
    timestamp = Column(DateTime, default=datetime.utcnow)
