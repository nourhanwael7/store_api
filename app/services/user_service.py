from sqlalchemy.orm import Session
from app.crud import user_crud
from app.schemas.user import UserCreate


def create_user(db: Session, user: UserCreate):

    existing_user = user_crud.get_user_by_username(db, user.username)

    if existing_user:
        raise Exception("Username already exists")

    return user_crud.create_user(db, user)



    