from feuh.gestion_empleados.models.cliente import Cliente
from feuh.gestion_empleados.models.empleado import Empleado
from feuh.gestion_empleados.models.gerente import Gerente

gerente = Gerente('Juan', 'Hernández', 'JUGZ090520HF4', 20000, 'Operaciones')
gerente.budget = 90000
print(gerente)
print()
empleado = Empleado('Carlos', 'Gonzalez', 'CAGZ060592HF5', 9000, 'Operaciones')
empleado.increase_salary(15)
print(empleado)
print()

cliente = Cliente('Alfredo', 'Martinez', 'HEHA020592YH4', 15000)
print(cliente)
