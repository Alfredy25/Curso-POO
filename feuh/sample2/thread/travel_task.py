import time
from dataclasses import dataclass
from random import random


@dataclass
class TravelTask:
    name: str

    def arrancar(self):
        for i in range(10):
            print(f'{i} - {self.name}')
            time.sleep(random())
        print(f'Finalmente voy a viajar a: {self.name}')

