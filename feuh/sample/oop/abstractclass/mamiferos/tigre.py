from feuh.sample.oop.abstractclass.mamiferos.felino import Felino


class Tigre(Felino):
    def __init__(self, habitad: str, altura: float, largo: float, peso: float, nombre_cientifico: str,
                 tamano_garras: float, velocidad: int, especie_tigre: str) -> None:
        super().__init__(habitad, altura, largo, peso, nombre_cientifico, tamano_garras, velocidad)
        self._especie_tigre = especie_tigre

    def comer(self) -> str:
        return f'EL tigre {self._especie_tigre} es un carnivoro solitario que caza Ciervos, Jabalíes etc'

    def comunicarse(self) -> str:
        return f'El tigre {self._especie_tigre} se comunica mediante rugidos marcando territorio en {self.habitad} con olor (orina)'

    def correr(self) -> str:
        return f'corriendo a {self.velocidad}km/h de forma explosiva por su peso de {self.peso}kg su carreta es corta no persigue a grandes distancias'

    def dormir(self) -> str:
        return f'El tigre {self._especie_tigre} duerme entre 12 y 16 horas en {self.habitad} descansando normalmente cerca del agua'

    def __str__(self):
        return (super().__str__() +
                f'\nespecie de tigre: {self._especie_tigre}')