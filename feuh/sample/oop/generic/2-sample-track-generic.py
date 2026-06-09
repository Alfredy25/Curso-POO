from feuh.sample.oop.generic.truck.models.animal import Animal, AnimalType
from feuh.sample.oop.generic.truck.models.car import Car
from feuh.sample.oop.generic.truck.models.machinery import Machinery
from feuh.sample.oop.generic.truck.models.truck import Truck

horses_Transport: Truck[Animal] = Truck(5)
horses_Transport.add(Animal('Peregrino',AnimalType.CABALLO))
horses_Transport.add(Animal('Grillo',AnimalType.CABALLO))
horses_Transport.add(Animal('Topocalma',AnimalType.BOVINO))
horses_Transport.add(Animal('Longotoma',AnimalType.CABALLO))


for item in horses_Transport:
    print(f'{item.name} tipo: {item.type.value}')

machines_transport: Truck[Machinery] = Truck(3)

machines_transport.add(Machinery('Bulldozer'))
machines_transport.add(Machinery('Grua Horquilla'))
machines_transport.add(Machinery('Perforadora'))

for item in machines_transport:
    print(f'tipo: {item.type}')


car_transport: Truck[Car] = Truck(3)
car_transport.add(Car('Toyota'))
car_transport.add(Car('Mitsubishi'))
car_transport.add(Car('Chevrolet'))

for item in car_transport:
    print(f'tipo: {item.brand}')

machines_transports2 = Truck[Machinery](4)
machines_transports2.add(Machinery('Toyota'))
machines_transports2.add(Machinery('Toyota'))
machines_transports2.add(Machinery('Toyota'))
machines_transports2.add(Machinery('Toyota'))
for item in machines_transports2:
    print(f'Tipo {item.type}')
