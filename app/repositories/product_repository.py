from app.models.product import Product
from app.schemas.product import ProductCreate
from app.repositories.base_repository import BaseRepository


class ProductRepository(BaseRepository):

    def create_product(self, product: ProductCreate):

        db_product = Product(**product.model_dump())
        return self.add(db_product)

    def get_products(self, skip: int = 0, limit: int = 10):
        return self.db.query(Product).offset(skip).limit(limit).all()

    def get_products_by_category(self, category_id: int):
        return self.db.query(Product).filter(Product.category_id == category_id).all()