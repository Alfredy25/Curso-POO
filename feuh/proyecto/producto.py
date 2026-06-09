
class Producto:

    def __init__(self, fabricante: str, nombre: str, precio: float | int):
        self.__fabricante: str = fabricante
        self.__nombre: str = nombre
        self.__precio: float | int = precio

    @property
    def fabricante(self):
        return self.__fabricante

    @property
    def nombre(self):
        return self.__nombre

    @property
    def precio(self):
        return self.__precio