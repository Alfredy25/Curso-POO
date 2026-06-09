from abc import ABC

from feuh.sample.oop.abstractclass.catalogo.electronico_contrato import ElectronicoContrato
from feuh.sample.oop.abstractclass.catalogo.product import Producto


class Electronico(ElectronicoContrato, Producto, ABC):
    def __init__(self, fabricante: str, precio: float):
        super().__init__(precio)
        self._fabricante = fabricante

    def get_fabricante(self):
        return self._fabricante

    def __str__(self):
        return f'Fabricante: {self._fabricante}\nPrecio: ${self.get_precio()}'
