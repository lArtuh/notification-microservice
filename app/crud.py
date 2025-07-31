from sqlalchemy.orm import Session
from app import models, schemas


def create_notification(db: Session, data: schemas.NotificationCreate):
    notif = models.Notification(**data.dict())
    db.add(notif)
    db.commit()
    db.refresh(notif)
    return notif


def get_notifications(db: Session, recipient: str):
    return db.query(models.Notification).filter(models.Notification.recipient == recipient).all()
