
from desingpattern.observer.investor.corporation import Corporation
from desingpattern.observer.investor.investor import Investor

# --- Ejecución del programa (Main) ---
if __name__ == "__main__":
    # 1. Crear una corporación en la bolsa (Apple en este caso)
    apple_stock = Corporation("AAPL", 150.00)
    google_stock = Corporation("GOOGL", 2800.00)

    # 2. Crear 3 inversionistas
    investor_1 = Investor("Carlos Mendoza")
    investor_2 = Investor("Ana Gómez")
    investor_3 = Investor("David Vega")


    # 3. Suscribir (attach) a los inversionistas para que observen la corporación
    print("--- Registrando inversionistas en la bolsa ---")
    apple_stock.attach(investor_1)
    apple_stock.attach(investor_2)
    apple_stock.attach(investor_3)

    google_stock.attach(investor_1)

    # 4. Cambiar el precio de la acción (esto disparará las notificaciones)
    apple_stock.price = 155.50
    apple_stock.price = 152.10

    # 5. Un inversionista decide darse de baja (detach)
    print("\n--- Carlos Mendoza decide dejar de seguir las acciones de AAPL ---")
    apple_stock.detach(investor_1)

    # 6. El precio cambia de nuevo, solo Ana y David reciben la notificación
    apple_stock.price = 158.00
    google_stock.price = 200.00