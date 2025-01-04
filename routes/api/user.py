from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from controllers.api.user import create_user, get_users, SessionLocal
from models.user import User

router = APIRouter()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/user")
def add_user(first_name: str, db: Session = Depends(get_db)):
    return create_user(db=db, first_name=first_name)

@router.get("/users")
def list_users(db: Session = Depends(get_db)):
    return get_users(db=db)
