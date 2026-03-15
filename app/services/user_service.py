from sqlalchemy.orm import Session
from app.schemas.user import UserCreate
from app.repositories.user_repository import UserRepository


class UserService:

    def __init__(self, db: Session):
        self.db = db
        self.user_repository = UserRepository()

    def create_user(self, user: UserCreate):

        existing_user = self.user_repository.get_user_by_username(self.db, user.username)

        if existing_user:
            raise Exception("Username already exists")

        return self.user_repository.create_user(self.db, user)