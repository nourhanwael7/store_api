from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.dependencies.db import get_db

from app.schemas.category import CategoryCreate
from app.services.category_service import CategoryService

router = APIRouter(prefix="/categories", tags=["Categories"])


@router.post("/")
def create_category(category: CategoryCreate, db: Session = Depends(get_db)):
    category_service = CategoryService(db)
    return category_service.create_category(category)


@router.get("/")
def get_categories(db: Session = Depends(get_db)):
    category_service = CategoryService(db)
    return category_service.get_categories()