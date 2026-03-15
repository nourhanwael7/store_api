from sqlalchemy.orm import Session
from app.schemas.product import ProductCreate
from app.repositories.product_repository import ProductRepository


class ProductService:

    def __init__(self, db: Session):
        self.db = db
        self.product_repository = ProductRepository()

    def create_product(self, product: ProductCreate):
        return self.product_repository.create_product(self.db, product)

    def get_products(self, skip: int = 0, limit: int = 10):
        return self.product_repository.get_products(self.db, skip, limit)

    def get_products_by_category(self, category_id: int):
        return self.product_repository.get_products_by_category(self.db, category_id)