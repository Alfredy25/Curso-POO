# --- Observadores Concretos (Concrete Observers) ---
from desingpattern.observer.api.observer import Observer
from desingpattern.observer.user.user_repository import UserRepository


class WelcomeEmailNotification(Observer):
    """Envía un correo electrónico de bienvenida al usuario recién registrado."""
    def update(self,subject: UserRepository, user: dict):
        name = user["name"]
        email = user['email']
        print(f"📧 [Email Usuario] Enviando correo a <{email}>: "
              f"¡Hola {name}! Tu cuenta ha sido creada con éxito. Bienvenid@.")