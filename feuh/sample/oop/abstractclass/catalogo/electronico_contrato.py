from abc import ABC, abstractmethod


class ElectronicoContrato(ABC):

    @abstractmethod
    def get_fabricante(self):
        ...

