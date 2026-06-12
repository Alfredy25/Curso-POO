from sqlalchemy.exc import SQLAlchemyError

from orm.sqlalchemy.config.db import engine, Base, SessionLocal
from orm.sqlalchemy.mapped.person import Person

# Crear las tablas si no existen
# Se recomienda quitarlo para producción porque ya existen las tablas y en desarrollo no
Base.metadata.create_all(engine)

# Listar Personas
with SessionLocal() as session:
    try:
        person_edit = Person(id=4, age=46)
        person_edit.name = 'Jose'
        person_edit.email = 'jose@correo.com'
        session.merge(person_edit)
        session.commit()
    except SQLAlchemyError as e:
        session.rollback()
        print("Error al insertar registro:", str(e))




