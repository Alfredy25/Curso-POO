from feuh.sample.oop.abstractclass.catalogo.electronico import Electronico


class Iphone(Electronico):
    def __init__(self, fabricante: str, precio: float, color: str, modelo: str):
        super().__init__(fabricante, precio)
        self._color = color
        self._modelo = modelo

    @property
    def color(self):
        return self._color

    @property
    def modelo(self):
        return self._modelo

    def get_precio_venta(self):
        return self.get_precio() * 1.2

    def __str__(self):
        return f'{super().__str__()}\nColor: {self.color}\nModelo: {self.modelo}'
