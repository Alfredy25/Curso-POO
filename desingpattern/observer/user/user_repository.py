# --- Sujeto Concreto (UserRepository) ---
from dataclasses import dataclass
from typing import List

from desingpattern.observer.api.observable import Observable


@dataclass
class User:
    name: str
    email: str


class UserRepository(Observable):
    """
    El repositorio encargado de la persistencia de usuarios.
    Hereda de Observable para notificar los eventos del ciclo de vida.
    """

    def __init__(self):
        super().__init__()
        # Simulación de una base de datos en memoria
        self._users_db: List[dict] = []

    def create_user(self, user_data: dict | User):
        print(f"\n[BD] Guardando el usuario en la base de datos...")
        if isinstance(user_data, User):
            user_data = {"name": user_data.name,"email": user_data.email}
        # Estructura del nuevo usuario
        self._users_db.append(user_data)

        # Una vez guardado con éxito, notificamos a todos los interesados
        self.notify_observers(user_data)
        return user_data