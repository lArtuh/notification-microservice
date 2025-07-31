from pydantic import BaseModel
from datetime import datetime


class NotificationCreate(BaseModel):
    message: str
    recipient: str


class NotificationResponse(BaseModel):
    id: int
    message: str
    recipient: str
    read: bool
    timestamp: datetime

    class Config:
        orm_mode = True
