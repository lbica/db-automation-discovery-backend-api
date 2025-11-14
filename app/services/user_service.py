from sqlalchemy.orm import Session
from app.repositories.user_repository import UserRepository
from app.dtos.userdto import UserCreate, UserUpdate

class UserService:
    @staticmethod
    def list_users(db: Session):
        return UserRepository.get_all(db)

    @staticmethod
    def create_user(db: Session, user_in: UserCreate):
        return UserRepository.create(db, user_in)

    @staticmethod
    def update_user(db: Session, user_id: int, user_in: UserUpdate):
        user = UserRepository.get_by_id(db, user_id)
        if not user:
            return None
        return UserRepository.update(db, user, user_in)

    @staticmethod
    def delete_user(db: Session, user_id: int):
        user = UserRepository.get_by_id(db, user_id)
        if not user:
            return None
        UserRepository.delete(db, user)
        return user
