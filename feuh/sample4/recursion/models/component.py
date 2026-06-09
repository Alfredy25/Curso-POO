from dataclasses import dataclass, field
from typing import List, ClassVar


@dataclass
class Component:

    name: str
    children: List['Component'] = field(default_factory=list)
    level: int = 0

    def add_children(self, c: 'Component') -> 'Component':
        self.children.append(c)
        return self

    def has_children(self) -> bool:
        # return len(self.children) > 0
        return bool(self.children)

#
# @dataclass
# class Producto:
#     _contador: ClassVar[int] = 0
#     id: int = field(init=False, compare=False) #no se pasa en constructor
#     nombre: str
#     precio: float
#
#     # No se pasa en el constructor
#     impuesto: float = field(default=0.16, init=False)
#
#     # No aparece en print
#     costo_interno: float = field(default=10.0, repr=False)
#
#     # No se usa en comparaciones (==)
#     codigo: int = field(default=0, compare=False)
#
#     # Lista independiente por instancia
#     tags: list = field(default_factory=list)
#
#     def __post_init__(self):
#         type(self)._contador += 1
#         self.id = type(self)._contador
#
#
# p1 = Producto("Laptop", 1000, codigo=1)
# p2 = Producto("Laptop", 1000, codigo=2)
#
# print(p1 == p2)
#
# tipo = type(p1)
# print(tipo)
#
#
# @dataclass
# class Base:
#     id: int = field(init=False)
#     _contador: ClassVar[int] = 0
#
#     def __post_init__(self):
#         type(self)._contador += 1
#         self.id = type(self)._contador
#
#
# @dataclass
# class Hijo(Base):
#     _contador: ClassVar[int] = 0
#     pass
#
#
# a = Base()
# b = Hijo()
# c = Hijo()
#
# print(a.id)  # 1
# print(b.id)  # 1
# print(c.id)  # 2

