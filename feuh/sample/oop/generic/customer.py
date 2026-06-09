from dataclasses import dataclass

@dataclass
class Customer:
    name: str
    last_name: str

    def __hash__(self):
        return hash((self.name, self.last_name))



