from sqlalchemy.orm import Session


class BaseRepository:

    def __init__(self, db: Session):
        self.db = db

    def add(self, obj):
        self.db.add(obj)
        self.db.commit()
        self.db.refresh(obj)
        return obj

    def get_all(self, model):
        return self.db.query(model).all()

    def get_by_id(self, model, id: int):
        return self.db.query(model).filter(model.id == id).first()