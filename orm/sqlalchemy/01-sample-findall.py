from sqlalchemy import select
from orm.sqlalchemy.config.db import engine, Base, SessionLocal
from orm.sqlalchemy.mapped.person import Person

# Crear las tablas si no existen
# Se recomienda quitarlo para producción porque ya existen las tablas y en desarrollo no
Base.metadata.create_all(engine)

# Listar Personas
with SessionLocal() as session:
    # people = session.query(Person).all()
    stmt = select(Person)
    people = session.scalars(stmt).all()
    print(type(people))
    for p in people:
        print(p)
