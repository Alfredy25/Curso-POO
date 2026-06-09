from typing import Optional


class Producto:
    def __init__(self, nombre: Optional[str] = None, precio: Optional[float] = None):
        self.nombre = nombre
        self.precio = precio

    def __str__(self) -> str:
        return f'Nombre: {self.nombre}\nPrecio: ${self.precio} MXN'





