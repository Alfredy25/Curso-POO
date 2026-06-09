from typing import Optional, List

from feuh.gestion_almacen.models.producto import Producto


class Limpieza(Producto):

    def __init__(self, nombre: Optional[str], precio: Optional[float],
                 componentes: List[str], tipo_uso: Optional[str], litros: Optional[int]):
        super().__init__(nombre, precio)
        self._componentes: List[str] = componentes
        self._tipo_uso = tipo_uso
        self._litros = litros

    @property
    def litros(self):
        return self._litros

    @property
    def componentes(self):
        return self._componentes

    @property
    def tipo_uso(self):
        return self._tipo_uso


    def __str__(self) -> str:
        return (super().__str__() +
                f'\nComponentes químicos: {", ".join(self._componentes)}'
                f'\nTipo de uso: {self._tipo_uso}'
                f'\nLitros: {self._litros}L\n')

