# Notification Microservice

This is a lightweight microservice built with FastAPI to manage user notifications. It supports:

- Creating notifications
- Listing notifications by recipient

## Endpoints

- `POST /notifications/`: Create a notification
- `GET /notifications/{recipient}`: Get all notifications for a specific recipient

## Technology Stack

- FastAPI
- SQLite (via SQLAlchemy)
- Pydantic

## Deployment

Ready for deployment on Render.