from app.models.user import User
from app.schemas.user import UserCreate
from app.repositories.base_repository import BaseRepository


class UserRepository(BaseRepository):

    def get_user_by_username(self, username: str):
        return self.db.query(User).filter(User.username == username).first()

    def create_user(self, user: UserCreate):

        db_user = User(**user.model_dump())
        return self.add(db_user)