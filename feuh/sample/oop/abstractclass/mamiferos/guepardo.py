from feuh.sample.oop.abstractclass.mamiferos.felino import Felino


class Guepardo(Felino):

    def __init__(self, habitad: str, altura: float, largo: float, peso: float, nombre_cientifico: str,
                 tamano_garras: float, velocidad: int) -> None:
        super().__init__(habitad, altura, largo, peso, nombre_cientifico, tamano_garras, velocidad)

    def comer(self) -> str:
        return f'El Guepardo ({self.nombre_cientifico}) es un carnivoro caza Gacelas con su estrateguia de usar su velocidad de {self.velocidad}km/h derribando a la presa haicendola tropezar'

    def comunicarse(self) -> str:
        return f'El Guepardo hace sonidos como Chillidos, Maullidos y usa su contacto visual y corporal'

    def correr(self) -> str:
        return f'El Guepardo corre a una velocidad de {self.velocidad}km/h haciendo ataques sorpresa'

    def dormir(self) -> str:
        return f'El Guepardo duerme entre 12-15 hrs en {self.habitad} pero muy alertas porque son vulnerables a otros depredadores'

    def __str__(self):
        return super().__str__()




