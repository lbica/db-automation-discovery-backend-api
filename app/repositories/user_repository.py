from sqlalchemy.orm import Session
from app.models.user import User
from app.dtos.userdto import UserCreate, UserUpdate
from passlib.hash import bcrypt

class UserRepository:
    @staticmethod
    def get_all(db: Session):
        return db.query(User).all()

    @staticmethod
    def get_by_id(db: Session, user_id: int):
        return db.query(User).filter(User.id == user_id).first()

    @staticmethod
    def create(db: Session, user_in: UserCreate):
        user = User(
            name=user_in.name,
            email=user_in.email,
            password=bcrypt.hash(user_in.password),
        )
        db.add(user)
        db.commit()
        db.refresh(user)
        return user

    @staticmethod
    def update(db: Session, db_user: User, user_in: UserUpdate):
        for field, value in user_in.dict(exclude_unset=True).items():
            setattr(db_user, field, value)
        db.commit()
        db.refresh(db_user)
        return db_user

    @staticmethod
    def delete(db: Session, db_user: User):
        db.delete(db_user)
        db.commit()
