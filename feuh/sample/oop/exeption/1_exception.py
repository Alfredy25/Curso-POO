
try:
    divisor = int(input('ingrese un numero divisor: '))
    division = 10 / divisor
    print('division=', division)
except ValueError as e:
    print('se detecto una excepcion: ingrese un valor númerico valido:',e)
except ZeroDivisionError as e:
    print('capturamos la exception en tiempo de ejecucion:',e)
except Exception as e:
    print('Ocurrio otro error', e)
finally:
    print('es opcional pero se ejecuta siempre con el error o si todo sale bien')
print('Continuamos con el flujo normal de la app')
