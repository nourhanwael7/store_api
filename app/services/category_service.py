from sqlalchemy.orm import Session
from app.schemas.category import CategoryCreate
from app.repositories import category_repository


class CategoryService:

    def create_category(self, db: Session, category: CategoryCreate):
        return category_repository.create_category(db, category)

    def get_categories(self, db: Session):
        return category_repository.get_categories(db)