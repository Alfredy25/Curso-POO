from feuh.sample.oop.abstractclass.catalogo.libro import Libro
from datetime import datetime

class Comic(Libro):
    def __init__(self, precio: float, fecha_publicacion: datetime,
                 autor: str, titulo: str, editorial: str, personaje: str):
        super().__init__(precio, fecha_publicacion, autor, titulo, editorial)
        self._personaje = personaje

    @property
    def personaje(self):
        return self._personaje

    def __str__(self):
        return super().__str__() + f'\nPersonaje: {self.personaje}'