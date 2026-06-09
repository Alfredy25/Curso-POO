from feuh.sample.oop.abstractclass.catalogo.electronico import Electronico


class TvLcd(Electronico):
    def __init__(self, fabricante: str, precio: float, pulgadas: int):
        super().__init__(fabricante, precio)
        self._pulgadas = pulgadas

    @property
    def pulgadas(self):
        return self._pulgadas

    def get_precio_venta(self):
        return self.get_precio() * 1.25


