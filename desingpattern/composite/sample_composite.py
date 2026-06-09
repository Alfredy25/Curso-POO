from abc import ABC, abstractmethod


# --- Componente ---
class Component(ABC):
    """
    La clase abstracta que define la interfaz común para los componentes
    simples (File) y los compuestos (Directory).
    """

    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def show(self, indent: int = 0):
        """Muestra el elemento actual con su nivel de tabulación."""
        pass

    @abstractmethod
    def search(self, name: str) -> bool:
        """Busca recursivamente un elemento por su nombre y devuelve True o False."""
        pass

# --- Hoja (Leaf) ---
class File(Component):
    """
    Representa los objetos finales del sistema. Un archivo no puede
    tener elementos hijos.
    """

    def show(self, indent: int = 0):
        # Multiplicamos el espacio por el nivel de indentación para el formato visual
        print("  " * indent + f"📄 {self.name}")

    def search(self, name: str) -> bool:
        # Un archivo solo comprueba si su propio nombre coincide con la búsqueda
        return self.name == name


# --- Compuesto (Composite) ---
class Directory(Component):
    """
    Representa un componente complejo que puede contener hijos (tanto archivos como subdirectorios).
    """

    def __init__(self, name: str):
        super().__init__(name)
        # Lista para almacenar los hijos que sean de tipo Component
        self._children: list[Component] = []

    def add(self, component: Component):
        """Agrega un archivo o carpeta al directorio."""
        self._children.append(component)

    def remove(self, component: Component):
        """Elimina un archivo o carpeta del directorio."""
        self._children.remove(component)

    def show(self, indent: int = 0):
        # Muestra el nombre del directorio actual
        print("  " * indent + f"📁 {self.name}/")

        # Delega recursivamente el trabajo de mostrar a cada uno de sus hijos,
        # aumentando el nivel de tabulación para los elementos internos.
        for child in self._children:
            child.show(indent + 1)

    def search(self, name: str) -> bool:
        # 1. Comprobar si el directorio actual es el que buscamos
        if self.name == name:
            return True

        # 2. Si no es este directorio, buscar recursivamente en cada uno de sus hijos
        for child in self._children:
            if child.search(name):  # Si el hijo (sea archivo o carpeta) lo encuentra, devolvemos True
                return True

        # 3. Si se recorrieron todos los hijos y ninguno lo encontró
        return False


# --- Ejecución del programa ---
if __name__ == "__main__":
    # 1. Crear la estructura del sistema de archivos
    root_dir = Directory("Documentos")

    file1 = File("Curriculum.pdf")
    file2 = File("Presupuesto.xlsx")
    root_dir.add(file1)
    root_dir.add(file2)

    photos_dir = Directory("Fotos")
    photo1 = File("Vacaciones.png")
    photo2 = File("Perfil.jpg")
    photos_dir.add(photo1)
    photos_dir.add(photo2)
    root_dir.add(photos_dir)

    work_dir = Directory("Trabajo")
    project_dir = Directory("Proyecto_Final")
    code_file = File("main.py")
    readme_file = File("README.md")

    project_dir.add(code_file)
    project_dir.add(readme_file)
    work_dir.add(project_dir)
    root_dir.add(work_dir)

    # 2. Mostrar la estructura completa
    print("=== Estructura del Sistema de Archivos ===")
    root_dir.show()
    print("\n" + "=" * 40 + "\n")

    # 3. Ejemplos de Búsqueda recursiva
    print("=== Ejemplos de Búsqueda ===")

    # Caso A: Buscar un archivo en la raíz
    search_1 = "Curriculum.pdf"
    print(f"¿Existe el archivo '{search_1}'? -> {root_dir.search(search_1)}")

    # Caso B: Buscar un subdirectorio intermedio
    search_2 = "Fotos"
    print(f"¿Existe el directorio '{search_2}'? -> {root_dir.search(search_2)}")

    # Caso C: Buscar un archivo metido profundamente en subdirectorios (Documentos/Trabajo/Proyecto_Final/main.py)
    search_3 = "main.py"
    print(f"¿Existe el archivo profundo '{search_3}'? -> {root_dir.search(search_3)}")

    # Caso D: Buscar algo que no existe en ningún lado
    search_4 = "Tesis.docx"
    print(f"¿Existe el archivo '{search_4}'? -> {root_dir.search(search_4)}")

    # Caso E: Probar el método search directamente desde una instancia de Archivo (Hoja)
    print(f"¿El archivo concreto file1 se llama 'Curriculum.pdf'? -> {file1.search('Curriculum.pdf')}")
    print(f"¿El archivo concreto file1 se llama 'main.py'? -> {file1.search('main.py')}")