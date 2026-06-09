from feuh.sample.oop.abstractclass.mamiferos.felino import Felino


class Leon(Felino):

    def __init__(self, habitad: str, altura: float, largo: float, peso: float, nombre_cientifico: str,
                 tamano_garras: float, velocidad: int,
                 numero_manada: int, potencia_rugido_decibel: float) -> None:
        super().__init__(habitad, altura, largo, peso, nombre_cientifico, tamano_garras, velocidad)
        self._numero_manada = numero_manada
        self._potencia_rugido = potencia_rugido_decibel

    def comer(self) -> str:
        return f'El león caza junto a su grupo de {self._numero_manada} individuos en las llanuras de {self.habitad}'

    def dormir(self) -> str:
        return f'El león {self.nombre_cientifico} duerme entre 16 - 20 hrs en {self.habitad}'

    def correr(self) -> str:
        return f'El leon {self.nombre_cientifico} corre en {self.habitad} a una velocidad de {self.velocidad}km/h'

    def comunicarse(self) -> str:
        return f'{self.nombre_cientifico} ruge a {self._potencia_rugido}dB para poder ubicar a su manada de {self._numero_manada} leones'

    def __str__(self):
        return (super().__str__() +
                f'\nManada de {self._numero_manada} leones'
                f'\nRugido de {self._potencia_rugido}dB')



