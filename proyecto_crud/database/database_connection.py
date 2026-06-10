from threading import Lock

import mysql.connector
from mysql.connector import Error


class ConexionBaseDatos:
    _isinstance = None
    _lock = Lock()

    def __new__(cls, *args, **kwargs):
        if not cls._isinstance:
            with cls._lock:
                if not cls._isinstance:
                    cls._isinstance = super().__new__(cls)
        return cls._isinstance

    def __init__(self, host="localhost", user="root", password="admin", database="python_course"):
        if not hasattr(self, "_connection"):
            try:
                self._connection = mysql.connector.connect(
                    host=host,
                    user=user,
                    password=password,
                    database=database
                )
                print("Conexión establecida con la base de datos.")
            except Error as e:
                print("Error al conectar a la base de datos:", e)
                self._connection = None

    def get_connection(self):
        return self._connection

    def close_connection(self):
        if self._connection and self._connection.is_connected():
            self._connection.close()
            print("Conexión cerrada.")
            self._connection = None
            ConexionBaseDatos._instance = None





