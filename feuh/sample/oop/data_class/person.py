from dataclasses import dataclass
from typing import ClassVar


@dataclass(order=True)
class Person:
    name: str
    lastname: str
    count: ClassVar[int] = 0

person1 = Person('Alfredo', 'Hernandez')
person2 = Person('John', 'Doe')
person3 = Person('John', 'Doe')

print(person1.name)
print(person1)
print(person2)
print(person1 == person2)
print(person2 == person3)

Person.count += 2
print(person1.count)
print(person2.count)
print(person3.count)