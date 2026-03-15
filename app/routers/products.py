from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.dependencies.db import get_db

from app.schemas.product import ProductCreate
from app.services.product_service import ProductService

router = APIRouter(prefix="/products", tags=["Products"])


@router.post("/")
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    product_service = ProductService(db)
    return product_service.create_product(product)


@router.get("/")
def get_products(
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db)
):
    product_service = ProductService(db)
    return product_service.get_products(skip, limit)