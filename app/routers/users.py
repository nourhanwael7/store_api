from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.dependencies.db import get_db
from app.schemas.user import UserCreate
from app.services.user_service import UserService

router = APIRouter(prefix="/users", tags=["Users"])

user_service = UserService()

@router.post("/")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return user_service.create_user(db, user)