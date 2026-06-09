from typing import Optional

from feuh.gestion_empleados.models.persona import Persona


class Cliente(Persona):
    _last_id = 0

    def __init__(self, first_name: Optional[str] = None,
                 last_name: Optional[str] = None,
                 rfc: Optional[str] = None,
                 credit_limit: Optional[int | float] = None):

        super().__init__(first_name, last_name, rfc)
        Cliente._last_id += 1
        self._client_id: int = Cliente._last_id
        self._credit_limit: int = credit_limit

    @property
    def cliente_id(self) -> int:
        return self._client_id

    @property
    def credit_limit(self) -> Optional[int | float]:
        return self._credit_limit

    def __str__(self):
        return f'ID_Cliente: {self._client_id}\n' + super().__str__() + f'\nLimite de credito: ${self._credit_limit:.2f}'






