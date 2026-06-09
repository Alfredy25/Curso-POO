from desingpattern.factory.products.pizza_product import PizzaProduct


class PizzaCaliforniaCheese(PizzaProduct):
    def __init__(self):
        super().__init__(
            _name="Pizza California Queso",
            _dough="Masa a la piedra delgada",
            _sauce="Salsa de tomate con rucula",
            _ingredients=[
                "Extra queso Mozzarella",
                "Cebolla",
                "queso azul"
            ]
        )

    def cook(self):
        print("Cocinando a 35 min a 100 grados")

    def cut(self):
        print("Cortando la pizza en pequeños triangulos")