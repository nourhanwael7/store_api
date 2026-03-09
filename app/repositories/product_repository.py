from sqlalchemy.orm import Session
from app.models.product import Product
from app.schemas.product import ProductCreate


class ProductRepository:

    def create_product(self, db: Session, product: ProductCreate):

        db_product = Product(**product.dict())

        db.add(db_product)
        db.commit()
        db.refresh(db_product)

        return db_product

    def get_products(self, db: Session, skip: int = 0, limit: int = 10):
        return db.query(Product).offset(skip).limit(limit).all() 

    def get_products_by_category(self, db: Session, category_id: int):

        return db.query(Product).filter(Product.category_id == category_id).all()