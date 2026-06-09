from desingpattern.observer.api.observable import Observable


class Corporation(Observable):
    """
    La corporación de la bolsa que posee un estado (precio de la acción)
    y notifica a los inversionistas cuando este cambia.
    """
    def __init__(self, symbol: str, price: float):
        super().__init__()
        self._symbol = symbol
        self._price = price

    @property
    def symbol(self) -> str:
        return self._symbol

    # Propiedad para manejar el precio y disparar la notificación al cambiar
    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, new_price: float):
        print(f"\n[Bolsa] El precio de {self._symbol} cambió a ${new_price:.2f}")
        self._price = new_price
        self.notify_observers('ejemplo de enviar algo al inversionista')
