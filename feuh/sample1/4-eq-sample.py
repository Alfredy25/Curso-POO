from datetime import date

from feuh.poo.car.car import Car
from feuh.poo.car.engine import Engine, EngineType
from feuh.poo.car.fuel_tank import FuelTank

car = Car('Mazda', 'BT-50', 'Blanco', Engine(3.0, EngineType.DIESEL), FuelTank(50))
car2 = Car('Mazda', 'BT-50', 'Blanco', Engine(3.0, EngineType.DIESEL), FuelTank(50))
car3 = car
date_now = date.today()

print(car is car2)
print(car == car2)
print(car == date_now)