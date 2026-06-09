from feuh.sample.oop.abstractclass.catalogo.producto_contrato import ProductContrato


class Producto(ProductContrato):
    def __init__(self, precio: float):
        self._precio = precio
        self._precio_venta = 0.0 # pendiente validar


    def get_precio(self) -> float:
        return self._precio

    def get_precio_venta(self):
        ...

