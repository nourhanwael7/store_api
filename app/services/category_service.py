from sqlalchemy.orm import Session
from app.crud import category_crud
from app.schemas.category import CategoryCreate


def create_category(db: Session, category: CategoryCreate):

    return category_crud.create_category(db, category)


def get_categories(db: Session):

    return category_crud.get_categories(db)