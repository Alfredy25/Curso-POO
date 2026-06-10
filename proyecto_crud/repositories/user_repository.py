from abc import ABC, abstractmethod
from typing import List
from proyecto_crud.models.user import User


class UserRepositoryInterface(ABC):
    @abstractmethod
    def find_all(self) -> List[User]:
        ...

    @abstractmethod
    def find_by_id(self, user_id: int) -> User:
        ...

    @abstractmethod
    def save(self, user: User) -> User:
        ...
    @abstractmethod
    def remove(self, user_id: int) -> bool:
        ...



