from desingpattern.factory.products.pizza_product import PizzaProduct
from dataclasses import dataclass

@dataclass
class PizzaNewYorkVegetarian(PizzaProduct):
    def __init__(self):
        super().__init__(
            _name="Pizza vegetariana New York",
            _dough="Masa integral vegana",
            _sauce="salsa de tomate",
            _ingredients=[
                "queso vegano",
                "tomate",
                "aceitunas",
                "espinacas",
                "berenjenas"
            ]
        )

    def cook(self) -> None:
        print("Cocinando 150 grados por 25 minutos")

    def cut(self) -> None:
        print("Cortando las pizza en rebanadas cuadradas")