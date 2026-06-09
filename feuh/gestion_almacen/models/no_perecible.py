from typing import Optional

from feuh.gestion_almacen.models.producto import Producto


class NoPerecible(Producto):

    def __init__(self, nombre: Optional[str] = None, precio: Optional[float] = None,
                 contenido: Optional[int] = None, tipo_envase: Optional[str] = None,
                 calorias: Optional[int] = None):
        super().__init__(nombre, precio)
        self._contenido = contenido
        self._tipo_envase = tipo_envase
        self._calorias = calorias

    @property
    def calorias(self):
        return self._calorias

    @property
    def contenido(self):
        return self._contenido

    @property
    def tipo_envase(self):
        return self._tipo_envase

    def __str__(self) -> str:
        return (super().__str__() +
                f'\nContenido: {self._contenido}g'
                f'\nTipo de envase: {self._tipo_envase}'
                f'\nCalorías: {self._calorias}\n')