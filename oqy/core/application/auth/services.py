from django.contrib.auth.hashers import make_password, check_password
from core.domain.entities import User
from core.domain.repositories import UserRepository
from typing import Optional


class AuthenticationService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def register_user(self, username: str, email: str, password: str) -> User:
        hashed_password = make_password(password)
        return self.user_repository.create_user(username, email, hashed_password)

    def authorize_user(self, username: str, password: str) -> Optional[User]:
        user = self.user_repository.get_user_by_username(username)
        if user and check_password(password, user.password):
            return user
        return None

    def get_user_by_id(self, user_id: int) -> Optional[User]:
        return self.user_repository.get_user_by_id(user_id)
