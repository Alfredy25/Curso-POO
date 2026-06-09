from typing import Optional

from feuh.gestion_empleados.models.empleado import Empleado


class Gerente(Empleado):
    def __init__(self, first_name: Optional[str] = None,
                 last_name: Optional[str] = None,
                 rfc: Optional[str] = None,
                 remuneration: float = 0.00,
                 department: Optional[str] = None,
                 budget: float = 0.00):

        super().__init__(first_name, last_name, rfc, remuneration, department)
        self._budget: float = budget

    @property
    def budget(self) -> float:
        return self._budget

    @budget.setter
    def budget(self, value: float):
        self._budget = value

    def __str__(self):
        return super().__str__() + f'\nPresupuesto asignado: ${self._budget:.2f}'




