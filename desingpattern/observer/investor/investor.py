# --- Observador Concreto (Concrete Observer) ---
from desingpattern.observer.api.observer import Observer
from desingpattern.observer.investor.corporation import Corporation

# --- Observable Concreto ---
class Investor(Observer):
    """
    El inversionista que se registra en la corporación para
    recibir alertas de precio.
    """
    def __init__(self, name: str):
        self.name = name

    def update(self, subject: Corporation, obj: object | None) -> None:
        # La notificación y los textos se muestran en español
        notificacion = f"Notificación para {self.name}: La acción de {subject.symbol} ahora vale ${subject.price:.2f}, con data adicional {obj}"
        print(notificacion)