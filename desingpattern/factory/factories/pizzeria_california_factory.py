from desingpattern.factory.factories.pizzeria_zone_abstract_factory import PizzeriaZoneAbstractFactory
from desingpattern.factory.products.pizza_california_cheese import PizzaCaliforniaCheese
from desingpattern.factory.products.pizza_california_vegerarian import PizzaCaliforniaVegetarian


class PizzeriaCaliforniaFactory(PizzeriaZoneAbstractFactory):

    def create_pizza(self, pizza_type: str):
        match pizza_type:
            case "cheese":
                return PizzaCaliforniaCheese()
            case "vegetarian":
                return PizzaCaliforniaVegetarian()
            case _:
                return None
