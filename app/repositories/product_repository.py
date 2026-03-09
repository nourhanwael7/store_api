from sqlalchemy.orm import Session
from app.models.product import Product
from app.schemas.product import ProductCreate


def create_product(db: Session, product: ProductCreate):

    db_product = Product(**product.dict())

    db.add(db_product)
    db.commit()
    db.refresh(db_product)

    return db_product


def get_products(db: Session):

    return db.query(Product).all()


def get_products_by_category(db: Session, category_id: int):

    return db.query(Product).filter(Product.category_id == category_id).all()