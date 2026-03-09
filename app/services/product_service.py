from sqlalchemy.orm import Session
from app.schemas.product import ProductCreate
from app.repositories import product_repository


class ProductService:

    def create_product(self, db: Session, product: ProductCreate):
        return product_repository.create_product(db, product)

    def get_products(self, db: Session):
        return product_repository.get_products(db)

    def get_products_by_category(self, db: Session, category_id: int):
        return product_repository.get_products_by_category(db, category_id)