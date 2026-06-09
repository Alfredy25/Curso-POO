from desingpattern.factory.products.pizza_product import PizzaProduct


class PizzaNewYorkPepperoni(PizzaProduct):
    def __init__(self):
        super().__init__(
            _name="Pizza Pepperoni New York",
            _dough="Masa delgada a la piedra",
            _sauce="salsa de tomate",
            _ingredients=[
                "queso mozzarella",
                "extra pepperoni",
                "aceitunas"
            ]
        )

    def cook(self):
        print("Cocinando por 40 minutos a 90 grados C")

    def cut(self):
        print("Cortando la pizza en triangulos")