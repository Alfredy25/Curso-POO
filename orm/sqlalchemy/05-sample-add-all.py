from sqlalchemy.exc import SQLAlchemyError

from orm.sqlalchemy.config.db import engine, Base, SessionLocal
from orm.sqlalchemy.mapped.person import Person

# Crear las tablas si no existen
# Se recomienda quitarlo para producción porque ya existen las tablas y en desarrollo no
Base.metadata.create_all(engine)

# Listar Personas
with SessionLocal() as session:
    try:
        persons = [Person(name='Bruce', lastname='Roe', email='bruce@correo.com', age=50),
                   Person(name='Pepa', lastname='Gonzalez', email='pepa@correo.com', age=25)]

        session.add_all(persons)
        session.commit()
        print(persons)
        # session.refresh(person)
        # print(person)
    except SQLAlchemyError as e:
        session.rollback()
        print("Error al insertar registro:", str(e))




