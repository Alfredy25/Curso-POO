from abc import ABC, abstractmethod


class Mamifero(ABC):
    def __init__(self,habitad: str, altura: float, largo: float,
                 peso: float, nombre_cientifico: str):
        self._habitad = habitad
        self._altura = altura
        self._largo = largo
        self._peso = peso
        self._nombre_cientifico = nombre_cientifico

    @property
    def habitad(self):
        return self._habitad

    @property
    def altura(self):
        return self._altura

    @property
    def largo(self):
        return self._largo

    @property
    def peso(self):
        return self._peso

    @property
    def nombre_cientifico(self):
        return self._nombre_cientifico

    @abstractmethod
    def comer(self) -> str:
        ...

    @abstractmethod
    def dormir(self) -> str:
        ...

    @abstractmethod
    def correr(self) -> str:
        ...

    @abstractmethod
    def comunicarse(self) -> str:
        ...

