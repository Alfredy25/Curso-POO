from abc import ABC, abstractmethod


class ProductContrato(ABC):

    @abstractmethod
    def get_precio(self):
        ...

    @abstractmethod
    def get_precio_venta(self):
        ...