from typing import List, Optional

import mysql.connector

from proyecto_crud.database.database_connection import ConexionBaseDatos
from proyecto_crud.models.user import User
from proyecto_crud.repositories.user_repository import UserRepositoryInterface


class UserRepositoryImpl(UserRepositoryInterface):

    def __init__(self):
        self._db = ConexionBaseDatos()

    def find_all(self) -> List[User]:
        connection = self._db.get_connection()
        users: List[User] = []
        sql = "SELECT user_id, username, password, email FROM users"
        try:
            with connection.cursor() as cursor:
                cursor.execute(sql)
                for user_id, username, password, email in cursor.fetchall():
                    users.append(User(user_id, username, password, email))
        except mysql.connector.Error as error:
            print("Error al conectar o consultar la base de datos", error)
            print(error.__class__.__name__)
        return users


    def find_by_id(self, user_id: int) -> Optional[User]:
        connection = self._db.get_connection()
        sql = "SELECT user_id, username, password, email FROM users WHERE user_id = %s"
        try:
            with connection.cursor() as cursor:
                cursor.execute(sql, (user_id,))
                row = cursor.fetchone()
                if row:
                    (user_id, username, password, email) = row
                    return User(user_id, username, password, email)
            return None

        except mysql.connector.Error as error:
            print("Error al conectar o consultar la base de datos", error)
            print(error.__class__.__name__)


    def save(self, user: User) -> Optional[User]:
        connection = self._db.get_connection()
        if user.id is not None and user.id > 0:
            # UPDATE
            sql = """
                UPDATE users
                SET username=%s, password=%s, email=%s
                WHERE user_id = %s
            """
            values = (user.username, user.password, user.email, user.id)
            print("Usuario para actualizar: ", user.username)
        else:
            #INSERT
            sql = """
            INSERT INTO users (username, password, email)
            VALUES (%s, %s, %s)
            """
            values = (user.username, user.password, user.email)
            print("Usuario nuevo: ", user.username)
        try:
            with connection.cursor() as cursor:
                cursor.execute(sql, values)
                connection.commit()

                # Si es un insert asignar el id generado al objeto
                if cursor.lastrowid: #Id del último registro insertado
                    user.id = cursor.lastrowid

            return user
        except mysql.connector.Error as error:
            print("Error al conectar o consultar la base de datos", error)
            print(error.__class__.__name__)
            return None

    def remove(self, user_id: int) -> bool:
        connection = self._db.get_connection()

        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM users WHERE user_id = %s", (user_id,))
            connection.commit()
            return cursor.rowcount == 1 # cuántas filas fueron afectadas por la última operación SQL.
