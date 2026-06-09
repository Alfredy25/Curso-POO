from abc import ABC, abstractmethod

# =========================
# Interfaz Configurable
# =========================
class Configurable(ABC):

    @abstractmethod
    def get_base_price(self):
        pass

    @abstractmethod
    def get_ingredients(self):
        pass


# =========================
# Implementación base Coffee
# =========================
class Coffee(Configurable):

    def __init__(self, name, base_price):
        self.name = name
        self.base_price = base_price

    def get_base_price(self):
        return self.base_price

    def get_ingredients(self):
        return [self.name]


# =========================
# Clase abstracta Decorator
# =========================
class CoffeeDecorator(Configurable):

    def __init__(self, coffee: Configurable):
        self._coffee = coffee

    @abstractmethod
    def get_base_price(self):
        pass

    @abstractmethod
    def get_ingredients(self):
        pass


# =========================
# Decoradores concretos
# =========================
class WithCreamDecorator(CoffeeDecorator):

    def get_base_price(self):
        return self._coffee.get_base_price() + 5.0

    def get_ingredients(self):
        return self._coffee.get_ingredients() + ["Cream"]


class WithMilkDecorator(CoffeeDecorator):

    def get_base_price(self):
        return self._coffee.get_base_price() + 3.0

    def get_ingredients(self):
        return self._coffee.get_ingredients() + ["Milk"]


class WithChocolateDecorator(CoffeeDecorator):

    def get_base_price(self):
        return self._coffee.get_base_price() + 4.0

    def get_ingredients(self):
        return self._coffee.get_ingredients() + ["Chocolate"]


# =========================
# Programa principal
# =========================
def print_coffee(coffee, name):
    print(f"{name}:")
    print(f"  Precio final: ${coffee.get_base_price():.2f}")
    print(f"  Ingredientes: {', '.join(coffee.get_ingredients())}")
    print()


if __name__ == "__main__":

    # Café Espresso (simple)
    cafe_espresso = Coffee("Espresso", 20.0)

    # Café Mocha = Espresso + Milk + Chocolate
    cafe_mocha = WithChocolateDecorator(
                WithMilkDecorator(
                    Coffee("Espresso", 20.0)
                )
            )

    # Café Cappuccino = Espresso + Milk + Cream
    cafe_cappuccino = WithCreamDecorator(
                    WithMilkDecorator(
                        Coffee("Espresso", 20.0)
                    )
                  )


    # Mostrar resultados
    print_coffee(cafe_espresso, "Espresso")
    print_coffee(cafe_cappuccino, "Cappuccino")
    print_coffee(cafe_mocha, "Mocha")