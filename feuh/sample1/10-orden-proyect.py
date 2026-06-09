from datetime import datetime

from feuh.proyecto.cliente import Cliente
from feuh.proyecto.orden_compra import OrdenCompra
from feuh.proyecto.producto import Producto

orden1 = OrdenCompra('Orden 1')
orden1.date = datetime(2026,5,8,11,15)
orden1.customer = Cliente('Juan', 'Hernandez')
orden2 = OrdenCompra('Orden 2')
orden2.date = datetime(2026,5,8,12,30)
orden2.customer = Cliente('Alfredo', 'Gonzalez')
orden3 = OrdenCompra('Orden 3')
orden3.date = datetime(2026,5,8,18,15)
orden3.customer = Cliente('Liam', 'Garcia')

product_1 = Producto('Barcel', 'Takis Fuego', 20.00)
product_2 = Producto('Bimbo', 'Pan Blanco Grande', 45.00)
product_3 = Producto('La Costeña', 'Frijoles Negros Refritos', 28.50)
product_4 = Producto('Gamesa', 'Galletas María', 24.00)
product_5 = Producto('Nestlé', 'Leche Evaporada', 19.50)
product_6 = Producto('Herdez', 'Salsa Roja Casera', 22.00)
product_7 = Producto('Lala', 'Leche Entera 1L', 26.00)
product_8 = Producto('La Moderna', 'Espagueti 200g', 12.50)
product_9 = Producto('San Juan', 'Huevo Blanco Docena', 52.00)
product_10 = Producto('Maseca', 'Harina de Maíz 1kg', 24.50)
product_11 = Producto('Kellogg’s', 'Corn Flakes 400g', 58.00)
product_12 = Producto('Nescafé', 'Café Clásico 120g', 75.00)

orden1.add_product(product_1)
orden1.add_product(product_2)
orden1.add_product(product_3)
orden1.add_product(product_4)

orden2.add_product(product_5)
orden2.add_product(product_6)
orden2.add_product(product_7)
orden2.add_product(product_8)

orden3.add_product(product_9)
orden3.add_product(product_10)
orden3.add_product(product_11)
orden3.add_product(product_12)

orders = [orden1, orden2, orden3]

for order in orders:
    order_print = f'''Orden #{order.id}
{order.description}\tdate:{order.date} 
cliente: {order.customer.nombre} {order.customer.apellido}
Productos:
    fabricante\tnombre_product\tprecio\n'''
    products = [(product.fabricante, product.nombre, product.precio) for product in order.products]
    for product in products:
        fabricante, nombre, precio = product
        order_print += f'\t{fabricante}\t{nombre}\t{precio}\n'
    order_print += f'Total: {str(order.grand_total())}\n\n'
    print(order_print)





