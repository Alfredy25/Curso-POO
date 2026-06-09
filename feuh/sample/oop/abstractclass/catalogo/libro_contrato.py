from abc import ABC, abstractmethod


class LibroContrato(ABC):

    @abstractmethod
    def get_fecha_publicacion(self):
        ...

    @abstractmethod
    def get_author(self):
        ...

    @abstractmethod
    def get_titulo(self):
        ...

    @abstractmethod
    def get_editorial(self):
        ...