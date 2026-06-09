from typing import Iterable, TypeVar

from feuh.sample.oop.generic.customer import Customer

T = TypeVar('T', Customer, int)
def from_arrary_to_list(items: Iterable[T]) -> list[T]:
    return list(items)

customers: set[Customer] = {Customer('Juan','Doe')}
customers.add(Customer('Alfredo', 'Hernandez'))
customers.add(Customer('Alfredo', 'Hernandez'))
print(customers)
numbers: set[int] = {1,2,3,4,5}

customers_list = from_arrary_to_list(customers)
numbers_list = from_arrary_to_list(numbers)

for c in customers_list:
    print(c)

for n in numbers_list:
    print(n)

print(customers_list)