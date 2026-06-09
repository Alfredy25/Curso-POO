from typing import List, Optional

from desingpattern.observer.api.observer import Observer
from desingpattern.observer.api.subject import Subject


# --- Observable Abstracto ---
class Observable(Subject):
    """
    La corporación de la bolsa que posee un estado (precio de la acción)
    y notifica a los inversionistas cuando este cambia.
    """
    def __init__(self):
        self._observers: List[Observer] = []

    def attach(self, observer: Observer):
        print('Agregando nuevo observer')
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer: Observer):
        self._observers.remove(observer)

    def notify_observers(self, obj: Optional[object] = None):
        # Enviamos la actualización a cada observador registrado
        print('Notificando a los observers')
        for observer in self._observers:
            observer.update(self, obj)
