from feuh.sample.oop.exeption.calculator.calculator import Calculator
from feuh.sample.oop.exeption.calculator.division_by_zero_exception import DivisionByZeroException
from feuh.sample.oop.exeption.calculator.number_format_exeption import NumberFormatException

calculator = Calculator()
numerator = input('ingrese un entero numerador: ')
denominador = input('ingrese un entero denominador: ')

try:
    division = calculator.divide(numerator, denominador)
    print('division=', division)

    division2 = calculator.divide('45', '50')
    division3 = calculator.divide(10, 5)

    print('division2=', division2)
    print('division3=', division3)
    division4 = calculator.divide(4, 0)

except NumberFormatException as e:
    print('ERROR: Ingrese un número valido ',e)
except DivisionByZeroException as e:
    print('ERROR: valor infinito ',e)
except ValueError as e:
    print(f'Mensaje de error nativo ValueError: {e}')
except Exception as e:
    print(e)

finally:
    print('es opcional pero se ejecuta siempre con el error o si todo sale bien')

print('Continuamos con el flujo normal de la app')
