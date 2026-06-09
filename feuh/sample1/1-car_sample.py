from feuh.poo.car.car import Car
from feuh.poo.car.engine import Engine, EngineType
from feuh.poo.car.color import Color

car = Car('Subaru')
car.color = Color.GRAY
car.cylinder = 1.5
car.model = 'Impreza modificado'
print(car.color.value)
print(car.details())
print(car.cylinder)
print(car.accelerate_and_brake(4000,120))


# print(car._Car__manufacturer) no es buena practica

mazda = Car('Mazda','3','Blanco',Engine(2.0, EngineType.GASOLINE))
mazda.engine.cylinder = 3.0
print(mazda.details())
print(mazda.engine.cylinder)
print(car)
print(repr(car))
print(mazda.accelerate(3000,100))
print(mazda.brake())
print(f'kilometros por litros: {mazda.calculate_consumption(300, 60)}')
print(f'kilometros por litros: {mazda.calculate_consumption(300, 0.6)}')

