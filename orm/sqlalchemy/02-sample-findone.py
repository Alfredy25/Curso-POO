from sqlalchemy import select
from orm.sqlalchemy.config.db import engine, Base, SessionLocal
from orm.sqlalchemy.mapped.person import Person

# Crear las tablas si no existen
# Se recomienda quitarlo para producción porque ya existen las tablas y en desarrollo no
Base.metadata.create_all(engine)

# Listar Personas
with SessionLocal() as session:
    stmt = select(Person).where(Person.id == 1)
    person = session.scalar(stmt)
    print(type(person))
    print(person)

    stmt = select(Person).where(Person.id == 10)
    person = session.scalars(stmt).first() # devuelve None si no existe o mejor dicho si no retorna nada
    print(person)

    """
    Si son varios lanza una exepcion por encontrar mas de un resultado y 
    si el resultado es que no se encontró devuelve none
    si el resultado es uno entonces retorna el objeto
    """
    stmt = select(Person).where(Person.id == 3)
    person = session.execute(stmt).scalar_one_or_none()
    print(person)


