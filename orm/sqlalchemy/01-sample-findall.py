
from orm.sqlalchemy.config.db import engine, Base, SessionLocal
from orm.sqlalchemy.mapped.person import Person

# Crar las tablas si no existen
Base.metadata.create_all(engine)

# Listar Personas
with SessionLocal() as session:
    people = session.query(Person).all()
    for p in people:
        print(p)
