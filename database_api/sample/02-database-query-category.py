from datetime import datetime
from decimal import Decimal

from database_api.sample.api.database_connection import DatabaseConnection
from database_api.sample.api.models.category import Category
from database_api.sample.api.models.product import Product
from database_api.sample.api.repositories.product_repository_impl import ProductRepository

if __name__ == '__main__':
    product_repo = ProductRepository()

    # Buscar todos los productos
    result = product_repo.find_all()
    print("Lista de productos:")
    for product in result:
        print(f"ID: {product.id} | "
              f"Nombre: {product.name} | "
              f"Precio: {product.price} | "
              f"Fecha: {product.created_at} | "
              f"Categoria: {product.category}")

    # Crear producto en categoría 2 (por ejemplo, "Comidas")
    p = Product(
        id=None,
        name="Hamburguesa Doble",
        price=Decimal(720),
        created_at=datetime.now(),
        category=Category(id=2, name="Comidas"),
    )
    p = product_repo.save(p)
    print("Creado:", p)

    # Cambiar nombre, precio y mover a categoría 3 ( por ejemplo, "Promos")
    p.name = "Hamburguesa Dobre Promo"
    p.price = Decimal(680)
    p.category = Category(id=3, name="Promos")
    p = product_repo.save(p)
    print("Actualizado:", p)

    # Consultar
    print("find_by_id:", product_repo.find_by_id(p.id))
    print("find_all:", product_repo.find_all()[:10])

    conn = DatabaseConnection()
    conn.close_connection()
