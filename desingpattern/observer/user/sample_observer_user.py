from desingpattern.observer.user.admin_alert_observer import AdminAlertNotification
from desingpattern.observer.user.log_record_observer import LogRecordObserver
from desingpattern.observer.user.user_repository import UserRepository, User
from desingpattern.observer.user.welcome_email_observer import WelcomeEmailNotification


# --- Ejecución del programa (Main) ---
if __name__ == "__main__":
    # 1. Instanciar el repositorio de usuarios
    user_repository = UserRepository()

    # 2. Instanciar los 3 servicios observadores
    welcome_service = WelcomeEmailNotification()
    admin_alert_service = AdminAlertNotification()
    logger_service = LogRecordObserver()

    # 3. Registrar los observadores en el repositorio
    print("--- Inicializando y suscribiendo servicios del sistema ---")
    user_repository.attach(welcome_service)
    user_repository.attach(admin_alert_service)
    user_repository.attach(logger_service)

    # 4. Crear un nuevo usuario (esto disparará automáticamente los 3 servicios)
    user_data: dict = {"name":"juan_perez", "email":"juan.perez@example.com"}
    user_repository.create_user(user_data)

    user = User("maria_gomez","maria.g02@example.com")
    # 5. Crear otro usuario para ver el flujo repetirse
    user_repository.create_user(user)