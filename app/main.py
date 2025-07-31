from fastapi import FastAPI
from app.routers import notifications
from app.models import Base
from app.database import engine

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "Notification microservice is running"}

app.include_router(notifications.router,
                   prefix="/notifications", tags=["Notifications"])
