from typing import Optional

from feuh.gestion_almacen.models.producto import Producto


class Fruta(Producto):
    def __init__(self,nombre: Optional[str], precio: Optional[float],
                 peso: Optional[float], tipo_fruta: Optional[str],
                 color: Optional[str]):
        super().__init__(nombre, precio)
        self._peso = peso
        self._tipo_fruta = tipo_fruta
        self._color = color

    @property
    def color(self):
        return self._color

    @property
    def peso(self):
        return self._peso

    @property
    def tipo_fruta(self):
        return self._tipo_fruta

    def __str__(self) -> str:
        return (super().__str__() +
                f'\nPeso: {self._peso}kg'
                f'\nTipo de fruta: {self._tipo_fruta}'
                f'\nColor: {self._color}\n')




