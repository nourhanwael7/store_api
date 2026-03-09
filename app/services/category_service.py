from sqlalchemy.orm import Session
from app.schemas.category import CategoryCreate
from app.repositories.category_repository import CategoryRepository


class CategoryService:

    def __init__(self):
        self.category_repository = CategoryRepository()

    def create_category(self, db: Session, category: CategoryCreate):
        return self.category_repository.create_category(db, category)

    def get_categories(self, db: Session):
        return self.category_repository.get_categories(db)