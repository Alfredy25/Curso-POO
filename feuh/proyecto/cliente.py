
class Cliente:
    def __init__(self, nombre: str, apellido: str):
        self.__nombre = nombre
        self.__apellido = apellido

    @property
    def nombre(self) -> str:
        return self.__nombre

    @property
    def apellido(self) -> str:
        return self.__apellido
