from sqlalchemy import delete
from sqlalchemy.exc import SQLAlchemyError

from orm.sqlalchemy.config.db import engine, Base, SessionLocal
from orm.sqlalchemy.mapped.person import Person

# Crear las tablas si no existen
# Se recomienda quitarlo para producción porque ya existen las tablas y en desarrollo no
Base.metadata.create_all(engine)

# Listar Personas
with SessionLocal() as session:
    try:
        stmt = delete(Person).where(Person.id == 5)
        session.execute(stmt)
        session.commit()
    except SQLAlchemyError as e:
        session.rollback()
        print("Error al insertar registro:", str(e))




