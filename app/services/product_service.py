from sqlalchemy.orm import Session
from app.schemas.product import ProductCreate
from app.repositories.product_repository import ProductRepository


class ProductService:

    def __init__(self):
        self.product_repository = ProductRepository()

    def create_product(self, db: Session, product: ProductCreate):
        return self.product_repository.create_product(db, product)

    def get_products(self, db: Session):
        return self.product_repository.get_products(db)

    def get_products_by_category(self, db: Session, category_id: int):
        return self.product_repository.get_products_by_category(db, category_id)