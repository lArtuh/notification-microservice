from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import schemas, crud
from app.database import get_db

router = APIRouter()


@router.post("/", response_model=schemas.NotificationResponse)
def create_notification(data: schemas.NotificationCreate, db: Session = Depends(get_db)):
    return crud.create_notification(db, data)


@router.get("/{recipient}", response_model=list[schemas.NotificationResponse])
def list_notifications(recipient: str, db: Session = Depends(get_db)):
    return crud.get_notifications(db, recipient)
