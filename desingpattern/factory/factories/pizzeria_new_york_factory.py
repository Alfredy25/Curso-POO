from desingpattern.factory.factories.pizzeria_zone_abstract_factory import PizzeriaZoneAbstractFactory
from desingpattern.factory.products.pizza_new_york_italian import PizzaNewYorkItalian
from desingpattern.factory.products.pizza_new_york_pepperoni import PizzaNewYorkPepperoni
from desingpattern.factory.products.pizza_new_york_vegetariana import PizzaNewYorkVegetarian


class PizzeriaNewYorkFactory(PizzeriaZoneAbstractFactory):

    def create_pizza(self, pizza_type: str):
        match pizza_type.lower():
            case "vegetarian":
                return PizzaNewYorkVegetarian()
            case "pepperoni":
                return PizzaNewYorkPepperoni()
            case "italian":
                return PizzaNewYorkItalian()
            case _:
                return None