from typing import Optional

from feuh.sample.oop.inheritance.models.person import Person


class Student(Person):

    def __init__(self, first_name : str| None = None,
                 last_name : Optional[str] = None,
                 email: Optional[str] = None,
                 institucion: Optional[str] = None,
                 math_grade: float = 0.00,
                 language_grade: float = 0.00,
                 history_grade: float = 0.00):

        super().__init__(first_name, last_name, email)
        self.institucion = institucion
        self.math_grade = math_grade
        self.language_grade = language_grade
        self.history_grade = history_grade

    def greet(self):
        return f'{super().greet()} soy {self.first_name} un estudiante y estudio en {self.institucion}'

    def speak(self):
        return 'El alumno hace una pregunta al profesor'

    def write_blackboard(self):
        return 'El alumno desarrolla un tema en la pizarra'

    def calculate_averange(self) -> float:
        return (self.math_grade + self.language_grade + self.history_grade) / 3

    def __str__(self):
        return (super().__str__() +
                f'\ninstitucion={self.institucion}, '
                f'nota_matematicas={self.math_grade}, '
                f'nota_lenguaje={self.language_grade}, '
                f'nota_de_historia={self.history_grade}, '
                f'promedio={self.calculate_averange():.2f}')






