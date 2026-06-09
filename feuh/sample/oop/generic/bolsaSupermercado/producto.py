from dataclasses import dataclass

@dataclass
class Producto:
    _nombre: str
    _precio: float

    @property
    def nombre(self):
        return self._nombre

    @property
    def precio(self):
        return self._precio


