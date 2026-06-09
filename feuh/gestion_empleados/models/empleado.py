from typing import Optional

from feuh.gestion_empleados.models.persona import Persona


class Empleado(Persona):
    def __init__(self, first_name: Optional[str] = None,
                 last_name: Optional[str] = None,
                 rfc: Optional[str] = None,
                 remuneration: float = 0.00,
                 department: Optional[str] = None):

        super().__init__(first_name, last_name,rfc)
        self._remuneration: int | float = remuneration
        self._department: str = department

    @property
    def remuneration(self) -> float | int | None:
        return self._remuneration

    @property
    def departament(self) -> str | None:
        return self._department

    def increase_salary(self, percentage: float | int = 0.00):
        if isinstance(percentage, float):
            self._remuneration *= (percentage + 1)
            return self._remuneration
        elif isinstance(percentage, int):
            percentage_new = percentage / 100
            self._remuneration *= (percentage_new + 1)
            return self._remuneration
        else:
            raise TypeError("Solo se reciben tipos enteros y de punto flotante")

    def __str__(self):
        return f'{super().__str__()}\nSalario: ${self._remuneration:.2f}, Departamento: {self._department}'









