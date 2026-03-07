from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import SessionLocal
from app.schemas.product import ProductCreate
from app.services import product_service

router = APIRouter(prefix="/products", tags=["Products"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/")
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    return product_service.create_product(db, product)


@router.get("/")
def get_products(category_id: int = None, db: Session = Depends(get_db)):

    if category_id:
        return product_service.get_products_by_category(db, category_id)

    return product_service.get_products(db)