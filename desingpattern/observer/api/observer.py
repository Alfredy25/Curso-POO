from __future__ import annotations
# --- Interfaz del Observador (Observer) ---
from abc import ABC, abstractmethod
from typing import Optional


class Observer(ABC):
    """
    Interfaz que deben implementar todos los objetos que quieren
    ser notificados de los cambios en el Subject.
    """
    @abstractmethod
    def update(self, subject: 'Subject', obj: Optional[object]) -> None:
        pass