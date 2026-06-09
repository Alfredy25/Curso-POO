from feuh.sample.oop.abstractclass.form.input_form import InputForm
from feuh.sample.oop.abstractclass.form.select_form import SelectForm, Option
from feuh.sample.oop.abstractclass.form.text_area_form import TextareaForm

username = InputForm('username')
password = InputForm('password', 'password')
email = InputForm('email', 'email')
age = InputForm('age', 'number')

experience = TextareaForm('experience', 5,9)

programming = SelectForm('programming')
programming.add_option(Option('1', 'Java'))
programming.add_option(Option('2', 'Python').set_selected())
programming.add_option(Option('3', 'JavaScript'))
programming.add_option(Option('4', 'TypeScript'))

username.set_value('Johndoe')
password.set_value('sdfjklsf12')
email.set_value('john.doe@coreo.es')
age.set_value('28')
experience.set_value('Hola tengo más de 20 años de experiencia ...')

elements = [
    username,
    password,
    email,
    age,
    experience,
    programming
]
for e in elements:
    print(e.draw_html())
    print('<br>')