from sqlalchemy import select
from orm.sqlalchemy.config.db import engine, Base, SessionLocal
from orm.sqlalchemy.mapped.person import Person

# Crear las tablas si no existen
# Se recomienda quitarlo para producción porque ya existen las tablas y en desarrollo no
Base.metadata.create_all(engine)

# Listar Personas
with SessionLocal() as session:
    person = session.get(Person, 1)
    person2 = session.get(Person, 2)
    person3 = session.get(Person, 3)
    person4 = session.get(Person, 2)
    print(person)
    print(person2)
    print(person3)
    print(person4)
    # índica son la misma persona el mismo objeto hace la búsqueda de forma eficiente guardando en memoria las consultas
    print(person4 is person2)




