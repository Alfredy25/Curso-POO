from typing import List

from proyecto_crud.models.user import User
from proyecto_crud.repositories.user_repository import UserRepositoryInterface


class UserRepositoryImpl(UserRepositoryInterface):

    def find_all(self) -> List[User]:
        pass

    def find_by_id(self, user_id: int) -> User:
        pass

    def save(self, user: User) -> User:
        pass

    def remove(self, user_id: int) -> bool:
        pass