from sqlalchemy.orm import Session
from app.repositories import user_repository
from app.schemas.user import UserCreate


class UserService:

    def create_user(self, db: Session, user: UserCreate):

        existing_user = user_repository.get_user_by_username(db, user.username)

        if existing_user:
            raise Exception("Username already exists")

        return user_repository.create_user(db, user)



    