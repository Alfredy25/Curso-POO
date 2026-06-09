from typing import Optional


class Persona:
    def __init__(self, first_name: Optional[str] = None,
                 last_name: Optional[str] = None,
                 rfc: Optional[str] = None):

        self._first_name: str = first_name
        self._last_name: str = last_name
        self._rfc: str = rfc

    @property
    def first_name(self):
        return self._first_name

    @property
    def last_name(self):
        return self._last_name

    @property
    def rfc(self):
        return self._rfc

    def __str__(self):
        return f'Nombre: {self._first_name} Apellido: {self._last_name}, RFC: {self._rfc}'











