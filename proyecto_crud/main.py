from proyecto_crud.database.database_connection import ConexionBaseDatos
from proyecto_crud.models.user import User
from proyecto_crud.repositories.user_repository_impl import UserRepositoryImpl

# crear conexión al repositorio
repo = UserRepositoryImpl()

# Creación de usuario para agregar a la bd
usuario1 = User(None, "Alfredo", "heloword123","alfred@gmail.com")
usuario2 = User(None, "Rodolfo", "rodo2123", "rodo12@gmail.com")
usuario3 = User(None, "Antonio", "toño123", "antonio12@gmail.com")

# Guardar usuarios en la bd
print("Guardando Usuarios")
usuario1 = repo.save(usuario1)
usuario2 = repo.save(usuario2)
usuario3 = repo.save(usuario3)

# Imprimir usuarios guardados
users = repo.find_all()
print("Listar Usuarios")
for user in users:
    print(user)

# Actualizar un usuario existente
usuario1.email = "alfredin1234@gmail.com"
usuario1 = repo.save(usuario1)
print("Usuario actualizado")
print(usuario1)


if repo.remove(usuario3.id):
    print("Usuario eliminado: ", usuario3)

print("listar usuarios de nuevo para revisar los cambios")
users = repo.find_all()
for user in users:
    print(user)

bd = ConexionBaseDatos()
bd.close_connection()
