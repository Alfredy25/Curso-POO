from feuh.sample.oop.inheritance.models.international_student import InternationalStudent
from feuh.sample.oop.inheritance.models.person import Person
from feuh.sample.oop.inheritance.models.student import Student
from feuh.sample.oop.inheritance.models.subject import Subject
from feuh.sample.oop.inheritance.models.teacher import Teacher

def print_person(person: Person):
    print('Imprimiendo datos en común del tipo Persona')
    print(f'Nombre: {person.first_name} Apellido: {person.last_name}, Email: {person.email}')

    if isinstance(person, Student):
        print('Imprimiendo datos del tipo Student:')
        print(f'Institucion: {person.institucion}')
        print(f'Nota Matematicas: {person.math_grade}')
        print(f'Nota Historia: {person.history_grade}')
        print(f'Nota Lenguaje: {person.language_grade}')

        if isinstance(person, InternationalStudent):
            print('Imprimiendo datos del tipo estudiante International:')
            print(f'Nota Idiomas: {person.foreing_language_grade}')
            print(f'Pais: {person.country}')
        print('=' * 30, 'Sobre escritura método calculate_averange', '=' * 30)
        print(f'Promedio: {person.calculate_averange():.2f}')
        print('=' * 30, 'Sobre escritura método write_blackboard', '=' * 30)
        print(person.write_blackboard())


    if isinstance(person, Teacher):
        print('Imprimiendo datos del tipo Teacher:')
        print(f'Asignatura: {person.subject}')

    print('='*30, 'Sobre escritura método greet', '='*30)
    print(person.greet())
    print('='*30, 'Sobre escritura método speek', '='*30)
    print(person.speak())



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

# print('Estudiante',student.first_name, student.last_name, student.email, student.institucion)
# print(f'Profesor {teacher.first_name} {teacher.last_name}:  {teacher.subject.value}')

persons = [student, international_student, teacher]
for p in persons:
    print_person(p)
    print('='*100)

