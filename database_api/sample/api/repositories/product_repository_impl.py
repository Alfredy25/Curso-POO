from typing import Optional, List

import mysql.connector
from database_api.sample.api.database_connection import DatabaseConnection
from database_api.sample.api.models.category import Category
from database_api.sample.api.models.product import Product
from database_api.sample.api.repositories.product_repository import ProductRepositoryInterface


class ProductRepository(ProductRepositoryInterface):
    def find_all(self) -> List[Product]:
        db = DatabaseConnection()
        connection = db.get_connection()
        products: List[Product] = []
        sql = """
            SELECT p.id, p.name, p.price, p.created_at,
                    c.id AS category_id, c.name AS category_name
            FROM products p
            JOIN categories c ON c.id = p.category_id
            ORDER BY p.id
        """
        try:
            # with db.get_connection() as connection:
            with connection.cursor() as cursor:
                # Ejecutar consulta
                cursor.execute(sql)
                # Recuperar resultados
                for product_id, name, price, create_at, cid, cname in cursor.fetchall():
                    products.append(Product(product_id, name, price, create_at, Category(cid, cname)))

        except mysql.connector.Error as e:
            print("Error al conectar o consultar la base de datos:\n", e)
            print(e.__class__.__name__)

        return products

    def find_by_id(self, product_id: int) -> Optional[Product]:
        connection = DatabaseConnection().get_connection()
        sql = """
            SELECT p.id, p.name, p.price, p.created_at,
                c.id AS category_id, c.name AS category_name
            FROM products p
            JOIN categories c ON c.id = p.category_id
            WHERE p.id = %s
        """
        with connection.cursor() as cursor:
            cursor.execute(
                sql,
                (product_id,)
            )
            row = cursor.fetchone()

            if row:
                (pid,name,price,created_at, cid, cname) = row
                return Product(
                    id=pid,
                    name=name,
                    price=price,
                    created_at=created_at,
                    category=Category(cid, cname)
                )
        return None

    def save(self, product: Product) -> Product:
        connection = DatabaseConnection().get_connection()
        if product.id is not None and product.id > 0:
            # UPDATE
            sql = """
                UPDATE products 
                SET name = %s, price=%s, category_id = %s
                WHERE id = %s
            """
            values = (product.name, product.price, product.category.id,product.id)
        else:
            # INSERT
            sql = """
                  INSERT INTO products (name, price, created_at, category_id)
                  VALUES (%s, %s, %s, %s)
                  """
            values = (product.name, product.price, product.created_at, product.category.id)
        with connection.cursor() as cursor:
            cursor.execute(sql, values)
            connection.commit()

            # Si es un insert asignar el id generado al objeto
            if cursor.lastrowid:
                product.id = cursor.lastrowid

        return product

    def remove(self, product_id: int) -> bool:
        connection = DatabaseConnection().get_connection()

        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM products WHERE id = %s", (product_id,))
            connection.commit()
            return cursor.rowcount > 0 # cuántas filas fueron afectadas por la última operación SQL.