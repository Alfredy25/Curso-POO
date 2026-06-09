from abc import ABC

from feuh.sample.oop.abstractclass.mamiferos.mamifero import Mamifero


class Canino(Mamifero,ABC):
    def __init__(self, habitad: str, altura: float,
                 largo: float, peso: float, nombre_cientifico: str,
                 color: str, tamano_colmillos: float) -> None:
        super().__init__(habitad, altura, largo, peso, nombre_cientifico)
        self._color = color
        self._tamano_colmillos = tamano_colmillos

    @property
    def color(self):
        return self._color

    @property
    def tamano_colmillos(self):
        return self._tamano_colmillos