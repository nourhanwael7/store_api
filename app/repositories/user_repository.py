from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate


class UserRepository:

    def get_user_by_username(self, db: Session, username: str):
        return db.query(User).filter(User.username == username).first()

    def create_user(self, db: Session, user: UserCreate):

        db_user = User(**user.dict())

        db.add(db_user)
        db.commit()
        db.refresh(db_user)

        return db_user