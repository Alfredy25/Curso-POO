from feuh.sample.oop.inheritance.models.international_student import InternationalStudent
from feuh.sample.oop.inheritance.models.person import Person
from feuh.sample.oop.inheritance.models.student import Student
from feuh.sample.oop.inheritance.models.subject import Subject
from feuh.sample.oop.inheritance.models.teacher import Teacher

def print_person(person: Person):
   print(person)


student = Student('Alfredo','Henandez')
student.email = 'correo@gmail.com'
student.institucion = 'Universidad Nacional'
student.language_grade = 9.00
student.history_grade = 7.85
student.math_grade = 8.3

international_student = InternationalStudent('John','Doe',
                                             'peter@gmail.com',
                                             'Instituto Internacional',
                                             8.00,6.00,10,
                                             'Australia',
                                             9.97)

teacher = Teacher('Maria','Roe','profe@gmail.com',Subject.FISICA)

persons = [student, international_student, teacher]
for p in persons:
    print_person(p)
    print('='*100)

