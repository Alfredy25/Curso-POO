from feuh.poo.car.car import Car
from feuh.poo.car.color import Color
from feuh.poo.constants import Constants
from feuh.poo.car.engine import Engine, EngineType
from feuh.poo.car.fuel_tank import FuelTank

Car.set_license_plate_color(Color.PURPLE)
car = Car.empty()
print(car)

car1 = Car.basic('Mazda', '3')
print(car1)

car2 = Car.with_color('Citroen', 'C3', Color.GRAY)
print(car2)

car3 = Car.with_cylinder('Subaru','Legacy', Color.RED, Engine(3.00, EngineType.DIESEL))
print(car3)

car4 = Car.full_spec('Mazda', 'BT-50', Color.RED, Engine(3.00, EngineType.DIESEL), FuelTank(50))
print(car4)

car5 = Car.only_tank('Subaru', 'Impreza',FuelTank(50))
print(car5)

car6 = Car.only_color('Subaru', Color.BLACK)
print(car6)
print(Car.get_license_plate_color().value)

speed_max_highway = Constants.MAX_SPEED_HIGHWAY
print(speed_max_highway)
print(Constants.MAX_SPEED_HIGHWAY)

# for color in Color:
#     print(color)
#     print(color.name)
#     print(color.value)
#
# Color.RED = 'roojo'
# print(Color.RED)