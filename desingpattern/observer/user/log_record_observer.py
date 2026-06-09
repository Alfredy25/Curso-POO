# --- Observadores Concretos (Concrete Observers) ---
from desingpattern.observer.api.observer import Observer
from desingpattern.observer.user.user_repository import UserRepository


class LogRecordObserver(Observer):
    """Registra la actividad en los archivos de log del sistema con fines de auditoría."""
    def update(self, subject: UserRepository, user: dict):
        name = user['name']
        email = user['email']
        print(f"📝 [Logs del Sistema] INFO: Usuario registrado exitosamente. "
              f"Datos guardados -> [Username: {name} | Email: {email}]")