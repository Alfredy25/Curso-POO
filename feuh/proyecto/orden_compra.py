from datetime import datetime
from typing import Optional, List
from feuh.proyecto.cliente import Cliente
from feuh.proyecto.producto import Producto


class OrdenCompra:
    _lastId = 0

    def __init__(self, description):
        OrdenCompra._lastId += 1
        self.__id: int = OrdenCompra._lastId
        self.__description: str = description
        self.__date: Optional[datetime] = None
        self.__customer: Optional[Cliente] = None
        self.__products: List[Producto] = []

    @property
    def id(self) -> int:
        return self.__id

    @property
    def description(self) -> str:
        return self.__description

    @property
    def date(self) -> Optional[datetime]:
        return self.__date

    @date.setter
    def date(self, value: datetime)  -> None:
        self.__date = value

    @property
    def customer (self) -> Optional[Cliente]:
        return self.__customer

    @customer.setter
    def customer(self, value: Cliente) -> None:
        self.__customer = value

    @property
    def products (self) -> List[Producto]:
        return self.__products

    def add_product(self, product : Producto) -> TypeError | OrdenCompra:
        if len(self.products) >= 4:
            raise TypeError('No se pueden agregar mas de 4 productos')
        self.__products.append(product)
        return self

    def __str__(self):
        return f'products: {self.products}'

    def grand_total(self) -> float | int:
        return sum(p.precio for p in self.products)





