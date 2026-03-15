from app.models.category import Category
from app.repositories.base_repository import BaseRepository


class CategoryRepository(BaseRepository):

    def create_category(self, category):

        db_category = Category(**category.model_dump())
        return self.add(db_category)

    def get_categories(self):
        return self.get_all(Category)