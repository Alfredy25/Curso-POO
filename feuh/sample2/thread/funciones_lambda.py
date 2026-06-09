import threading
import time

def cuadrado(x):
    return x**2

def desayunar():
    print("Iniciando Desayunar...")
    time.sleep(3)
    print("Finalizando mi desayuno...")

def tomar_cafe():
    print("Iniciando TomarCafe...")
    time.sleep(4)
    print("Finalizando la toma de cafe...")

def estudiar():
    print("Iniciando Estudio...")
    time.sleep(5)
    print("Finalizando el estudio...")

print(cuadrado(5))

cuadrado_lambda = lambda x: x ** 2
print(f'El cuadrado de 2: {cuadrado_lambda(2)}')
print(f'El cuadrado de 4: {cuadrado_lambda(4)}')

inicio = time.perf_counter()

thread1 = threading.Thread(target=desayunar, args=())
thread1.start()
thread2 = threading.Thread(target=tomar_cafe, args=())
thread2.start()
thread3 = threading.Thread(target=estudiar, args=())
thread3.start()


# desayunar()
# tomar_cafe()
# estudiar()

print(threading.active_count())
print(threading.enumerate())
thread1.join()
thread2.join()
thread3.join()

fin = time.perf_counter()
tiempo = fin-inicio
print(tiempo)
