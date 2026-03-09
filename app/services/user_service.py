from sqlalchemy.orm import Session
from app.schemas.user import UserCreate
from app.repositories.user_repository import UserRepository


class UserService:

    def __init__(self):
        self.user_repository = UserRepository()

    def create_user(self, db: Session, user: UserCreate):

        existing_user = self.user_repository.get_user_by_username(db, user.username)

        if existing_user:
            raise Exception("Username already exists")

        return self.user_repository.create_user(db, user)