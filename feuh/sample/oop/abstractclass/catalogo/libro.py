from datetime import datetime

from feuh.sample.oop.abstractclass.catalogo.libro_contrato import LibroContrato
from feuh.sample.oop.abstractclass.catalogo.product import Producto


class Libro(Producto, LibroContrato):
    def __init__(self, precio: float, fecha_publicacion: datetime,
                 autor: str, titulo: str, editorial: str):
        super().__init__(precio)
        self._fecha_publicacion = fecha_publicacion
        self._autor = autor
        self._titulo = titulo
        self._editorial = editorial

    def get_fecha_publicacion(self):
        return self._fecha_publicacion

    def get_author(self):
        return self._autor

    def get_titulo(self):
        return self._titulo

    def get_editorial(self):
        return self._editorial

    def get_precio_venta(self):
        return self.get_precio() * 1.10

    def __str__(self):
        return (f'Libro: {self.get_titulo()}'
                f'\nAutor: {self.get_author()}'
                f'\nPrecio: ${self.get_precio():.2f}'
                f'\nFecha de Publicación: {self.get_fecha_publicacion().strftime('%d/%m/%Y')}'
                f'\nEditorial: {self.get_editorial()}')