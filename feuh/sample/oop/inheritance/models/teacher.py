from typing import Optional

from feuh.sample.oop.inheritance.models.person import Person
from feuh.sample.oop.inheritance.models.subject import Subject


class Teacher(Person):

    def __init__(self, first_name : str| None = None,
                 last_name : Optional[str] = None,
                 email: Optional[str] = None,
                 subject: Optional[Subject] = None):

        super().__init__(first_name, last_name, email)
        self.subject = subject

    def greet(self):
        return f'{super().greet()} soy el profesor(a) {self.first_name}, realizo clases de la asignatura {self.subject}'

    def __str__(self):
        return super().__str__() + f'\nasignatura={self.subject}'




