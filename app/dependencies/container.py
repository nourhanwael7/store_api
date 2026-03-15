from fastapi import Depends
from sqlalchemy.orm import Session
from app.core.database import SessionLocal

from app.services.category_service import CategoryService
from app.services.product_service import ProductService
from app.services.user_service import UserService


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_category_service(db: Session = Depends(get_db)):
    return CategoryService(db)


def get_product_service(db: Session = Depends(get_db)):
    return ProductService(db)


def get_user_service(db: Session = Depends(get_db)):
    return UserService(db)