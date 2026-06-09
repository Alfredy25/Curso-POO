from datetime import datetime
from decimal import Decimal

from database_api.sample.api.database_connection import DatabaseConnection
from database_api.sample.api.models.product import Product
from database_api.sample.api.repositories.product_repository_impl import ProductRepository

if __name__ == '__main__':
    product_repo = ProductRepository()

    # Buscar todos los productos
    result = product_repo.find_all()
    print("Lista de productos:")
    for product in result:
        print(f"ID: {product.id} | Nombre: {product.name} | Precio: {product.price} | Fecha: {product.created_at}")

    # Buscar un producto por ID
    print("\nBuscar producto por ID:")
    product = product_repo.find_by_id(3)

    if product:
        print(
            f"ID: {product.id} | "
            f"Nombre: {product.name} | "
            f"Precio: {product.price} | "
            f"Fecha: {product.created_at}"
        )
    else:
        print("Producto no encontrado")

    # Crear nuevo producto
    new_product = Product(
        id=None,
        name="Hamburguesa Palta tomate",
        price=Decimal(550),
        created_at=datetime.now(),
    )

    saved_product = product_repo.save(new_product)
    print("Producto creado:", saved_product)

    # saved_product = product_repo.find_by_id(4)

    # Editar el producto recién creado
    saved_product.name = "Hamburguesa Premium"
    saved_product.price = Decimal(850)
    saved_product = product_repo.save(saved_product)
    print("Producto Editado:", saved_product)

    product = Product(id=None, name="Bebida Cola", price=Decimal(550), created_at=datetime.now())
    saved = product_repo.save(product)
    print("Producto creado:", saved)

    deleted = product_repo.remove(saved.id)
    if deleted:
        print(f'Producto con id={saved.id} eliminado correctamente')
    else:
        print("No se encoentró el productoa eliminar")

    # Verificar
    result = product_repo.find_by_id(saved.id)
    print("Consulta después del remove:", result)
    conn = DatabaseConnection()
    conn.close_connection()
