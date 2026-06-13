from orm.sqlalchemy.config.db import SessionLocal
from orm.sqlalchemy.mapped.person import Person
from orm.sqlalchemy.repositories.person_repository import PersonRepository

# Ejemplo de uso (main)
if __name__ == '__main__':
    repo = PersonRepository(SessionLocal)

    # CREATE
    print("=== CREATE ===")
    p = Person(name="Juan", lastname="Paulo", email="juan.perez@example.com", age=30)
    p2 = Person(name="Odete", lastname="Gonzalez", email="odete@example.com", age=18)

    try:
        p = repo.save(p)
        p2 = repo.save(p2)
        print("Creado:", p)
        print("Creado:", p2)
    except Exception as e:
        print(e)
        print("Error al crear:", e)

    # READ ALL
    print("\n=== FIND ALL ===")
    try:
        for person in repo.find_all():
            print(person)
    except Exception as e:
        print("Error al listar:", e)

    # UPDATE
    print("\n=== UPDATE ===")
    try:
        if p2.id:
            p2.age = 19
            p2.name = "Odete Evangeline"
            p2 = repo.save(p2)
            print("Actualizado:", p2)
    except Exception as e:
        print("Error al actualizar:", e)

     # DELETE
    print("\n=== DELETE ===")
    try:
        ok = repo.remove(p.id if p.id else -1)
        print("Eliminado?", ok)

    except Exception as e:
        print("Error al eliminar:", e)


    # Confirmación final
    print("\n=== FIND ALL ===")
    try:
        for person in repo.find_all():
            print(person)
    except Exception as e:
        print("Error al listar final:", e)




