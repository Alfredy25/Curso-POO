from typing import TypeVar, Generic, Iterable, List, Iterator
from dataclasses import dataclass

from feuh.sample.oop.generic.bolsaSupermercado.clases_hijas import Fruta, Limpieza, NoPerecible, Lacteo

T = TypeVar('T',Fruta,Limpieza,NoPerecible,Lacteo)

@dataclass
class BolsaSupermercado(Generic[T], Iterable[T]):
    capacity: int = 5

    def __post_init__(self):
        self.__items: List[T] = []

    def add_producto(self, producto: T) -> 'BolsaSupermercado':
        if len(self.__items) >= self.capacity:
            raise ValueError('Capacidad de la bolsa superada')
        else:
            self.__items.append(producto)
        return self

    def get_productos(self) -> List[T]:
        return self.__items

    def __iter__(self) -> Iterator[T]:
        return iter(self.__items)

    def __len__(self) -> int:
        return len(self.__items)