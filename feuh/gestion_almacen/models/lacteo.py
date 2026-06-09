from typing import Optional

from feuh.gestion_almacen.models.producto import Producto


class Lacteo(Producto):
    def __init__(self, nombre: Optional[str], precio: Optional[float],
                 cantidad: Optional[int] = None,contenido_grasa: Optional[float] = None,
                 proteinas: Optional[float] = None):
        super().__init__(nombre, precio)
        self._cantidad = cantidad
        self._contenido_grasa = contenido_grasa
        self._proteinas = proteinas

    @property
    def contenido_grasa(self):
        return self._contenido_grasa

    @property
    def cantidad(self):
        return self._cantidad

    @property
    def proteinas(self):
        return self._proteinas

    def __str__(self) -> str:
        return (super().__str__() +
                f'\nCantidad: {self._cantidad}{"L" if self.cantidad <= 2 else "g"}'
                f'\nContenido de grasa: {self._contenido_grasa}%'
                f'\nproteinas: {self._proteinas}\n')