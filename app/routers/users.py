from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.dependencies.db import get_db
from app.schemas.user import UserCreate
from app.services import user_service

router = APIRouter(prefix="/users", tags=["Users"])





@router.post("/")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return user_service.create_user(db, user)