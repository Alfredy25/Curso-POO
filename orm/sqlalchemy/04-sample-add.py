from sqlalchemy.exc import SQLAlchemyError

from orm.sqlalchemy.config.db import engine, Base, SessionLocal
from orm.sqlalchemy.mapped.person import Person

# Crear las tablas si no existen
# Se recomienda quitarlo para producción porque ya existen las tablas y en desarrollo no
Base.metadata.create_all(engine)

# Listar Personas
with SessionLocal() as session:
    try:
        person = Person()
        person.name = 'Lalo'
        person.lastname = 'Doe'
        person.email = 'lalo@correo.com'
        person.age = 20

        session.add(person)
        session.commit()
        print(person)

        # session.refresh(person)
        # print(person)
        print("Nuevo registro creado:", person)
    except SQLAlchemyError as e:
        session.rollback()
        print("Error al insertar registro:", str(e))




