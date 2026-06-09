from typing import Optional

from feuh.sample.oop.inheritance.models.student import Student


class InternationalStudent(Student):
    def __init__(self, first_name : str| None = None,
                 last_name : Optional[str] = None,
                 email: Optional[str] = None,
                 institucion: Optional[str] = None,
                 math_grade: float = 0.00,
                 language_grade: float = 0.00,
                 history_grade: float = 0.00,
                 country: str | None = None,
                 foreing_language_grade: float = 0.00):

        super().__init__(first_name, last_name, email,
                         institucion,
                         math_grade,
                         language_grade,
                         history_grade)
        self.country = country
        self.foreing_language_grade = foreing_language_grade

    def greet(self):
        return f'{super().greet()} soy extranjero del pais {self.country}'

    def calculate_averange(self) -> float:
        base_sum = super().calculate_averange() * 3
        return (base_sum + self.foreing_language_grade) / 4

    def __str__(self):
        return (f'{super().__str__()}\n'
                f'nota_de_idioma={self.foreing_language_grade}, '
                f'pais={self.country}')





