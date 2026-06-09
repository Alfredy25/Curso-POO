# --- Observadores Concretos (Concrete Observers) ---
from desingpattern.observer.api.observer import Observer
from desingpattern.observer.user.user_repository import UserRepository


class AdminAlertNotification(Observer):
    """Notifica al administrador del sistema que hay un nuevo usuario en la plataforma."""
    def update(self,subject: UserRepository, user: dict):
        name = user['name']
        print(f"🚨 [Email Admin] Enviando alerta a <admin@sistema.com>: "
              f"Nuevo registro detectado en la plataforma. Usuario: '{name}'.")