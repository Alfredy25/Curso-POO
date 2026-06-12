from sqlalchemy.exc import SQLAlchemyError

from orm.sqlalchemy.config.db import engine, Base, SessionLocal
from orm.sqlalchemy.mapped.person import Person

# Crear las tablas si no existen
# Se recomienda quitarlo para producción porque ya existen las tablas y en desarrollo no
Base.metadata.create_all(engine)

# Listar Personas
with SessionLocal() as session:
    try:
        person_edit = session.get(Person, 4)
        if not person_edit:
            raise ValueError(f"Person with id {4} not found in bbdd")

        person_edit.name = 'Pepito'
        person_edit.email = 'pepito@correo.com'
        session.commit()
    except SQLAlchemyError as e:
        session.rollback()
        print("Error al insertar registro:", str(e))




