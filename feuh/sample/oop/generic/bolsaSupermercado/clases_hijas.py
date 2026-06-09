from feuh.sample.oop.generic.bolsaSupermercado.producto import Producto
from dataclasses import dataclass

@dataclass
class Lacteo(Producto):
    _cantidad: int
    _proteinas: int

    @property
    def cantidad(self):
        return self._cantidad

    @property
    def proteinas(self):
        return self._proteinas

@dataclass
class Fruta(Producto):
    _peso: float
    _color: str

    @property
    def peso(self):
        return self._peso

    @property
    def color(self):
        return self._color

@dataclass
class Limpieza(Producto):
    _componentes: str
    _litros: float

    @property
    def componentes(self):
        return self._componentes

    @property
    def litros(self):
        return self._litros

@dataclass
class NoPerecible(Producto):
    _contenido: int
    _calorias: int

    @property
    def contenido(self):
        return self._contenido

    @property
    def calorias(self):
        return self._calorias

