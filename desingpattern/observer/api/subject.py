from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Optional


# --- Interfaz del Sujeto (Subject) ---
class Subject(ABC):
    """
    Interfaz que define los métodos para mantener y notificar
    a los observadores.
    """
    @abstractmethod
    def attach(self, observer: 'Observer'):
        pass

    @abstractmethod
    def detach(self, observer: 'Observer'):
        pass

    @abstractmethod
    def notify_observers(self, obj: Optional[object] = None):
        pass