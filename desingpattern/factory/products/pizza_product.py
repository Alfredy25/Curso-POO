from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import List


@dataclass
class PizzaProduct(ABC):
    _name: str
    _dough: str
    _sauce: str
    _ingredients: List[str] = field(default_factory=list)

    @property
    def name(self):
        return self._name

    def prepare(self):
        print(f"🍕 Preparando pizza: {self._name}")
        print(f"🥖 Masa: {self._dough}")
        print(f"🧀 Ingredientes: {', '.join(self._ingredients)}")

    @abstractmethod
    def cook(self):
        pass

    @abstractmethod
    def cut(self):
        pass

    def pack(self) -> None:
        print(f"Empacando pizza '{self._name}' en su caja oficial")