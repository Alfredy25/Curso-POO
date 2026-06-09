from desingpattern.factory.products.pizza_product import PizzaProduct


class PizzaCaliforniaVegetarian(PizzaProduct):
    def __init__(self):
        super().__init__("Pizza California Vegetariana",
            "Masa delgada Light",
            "salsa bbq Light",
            ["queso mozzarella","aceitunas","espinacas","cebolla","berenjenas","choclo"]
        )

    def cook(self):
        print("Cocinando por 25 minutos a 180 grados")

    def cut(self):
        print("Cortando la pizza en rebanadas rectangulares")