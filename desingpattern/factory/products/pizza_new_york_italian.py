from desingpattern.factory.products.pizza_product import PizzaProduct

class PizzaNewYorkItalian(PizzaProduct):
    def __init__(self):
        super().__init__("Pizza italiana New York","Masa gruesa", "salsa de tomate italiano con carne",
            _ingredients=["queso mozzarella","aceitunas","jamon","choricillo","champiniones"]
        )

    def cook(self) -> None:
        print("Cocinando por 10 minutos a 200 grados")

    def cut(self) -> None:
        print("Cortando la pizza en pequenos triangulos")