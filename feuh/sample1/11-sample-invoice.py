from feuh.invoice.app.models.customer import Customer
from feuh.invoice.app.models.invoice import Invoice
from feuh.invoice.app.models.item import Item
from feuh.invoice.app.models.item import Product

# Se crea cliente
customer = Customer('Andres', 'Guzman', '44444-5')
description = input('Ingrese una descripcion de la factura: ')

# se crea la factura con una descripcion y se le pasa el cliente
invoice = Invoice(description, customer)

for _ in range(5):
    name = input('Ingrese el nombre de producto: ')
    price = float(input('Ingrese el precio del producto: '))
    # creacion del producto
    product = Product(name, price)

    # se agregan los productos a un Item
    quantity = int(input('Ingrese la cantidad: '))
    # se agrega el item a la factura
    invoice.add_item(Item(quantity,product))

# se imprime el detalle
print(invoice)