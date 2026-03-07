from sqlalchemy.orm import Session
from app.crud import product_crud
from app.schemas.product import ProductCreate


def create_product(db: Session, product: ProductCreate):

    return product_crud.create_product(db, product)


def get_products(db: Session):

    return product_crud.get_products(db)


def get_products_by_category(db: Session, category_id: int):

    return product_crud.get_products_by_category(db, category_id)