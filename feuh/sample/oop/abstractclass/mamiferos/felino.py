from abc import ABC

from feuh.sample.oop.abstractclass.mamiferos.mamifero import Mamifero


class Felino(Mamifero,ABC):
    def __init__(self, habitad: str, altura: float, largo: float,
                 peso: float, nombre_cientifico: str,
                 tamano_garras: float, velocidad: int) -> None:
        super().__init__(habitad, altura, largo, peso, nombre_cientifico)
        self._tamano_garras = tamano_garras
        self._velocidad = velocidad

    @property
    def tamano_garras(self):
        return self._tamano_garras

    @property
    def velocidad(self):
        return self._velocidad

    def __str__(self):
        return (f'Habitad: {self.habitad}\nAltura: {self.altura}m'
                f'\nlargo: {self.largo}m\nPeso: {self.peso}kg'
                f'\nNombre cientifico: {self.nombre_cientifico}'
                f'\nTamaño garras: {self._tamano_garras}cm, Velocidad: {self._velocidad}km/h')

