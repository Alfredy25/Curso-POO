from abc import ABC, abstractmethod
from typing import List, Optional
from database_api.sample.api.models.product import Product


class ProductRepositoryInterface(ABC):

    @abstractmethod
    def find_all(self) -> List[Product]:
        ...

    @abstractmethod
    def find_by_id(self, product_id: int) -> Optional[Product]:
        ...

    @abstractmethod
    def save(self, product: Product) -> Product:
        ...

    @abstractmethod
    def remove(self, product_id: int) -> bool:
        ...