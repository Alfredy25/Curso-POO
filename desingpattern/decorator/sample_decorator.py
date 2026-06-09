from abc import ABC, abstractmethod


# Interfaz
class Formatteable(ABC):
    @abstractmethod
    def format(self) -> str:
        pass


# Clase concreta base
class Text(Formatteable):
    def __init__(self, content: str):
        self.content = content

    def format(self) -> str:
        return self.content


# Decorador abstracto
class TextDecorator(Formatteable, ABC):
    def __init__(self, wrapped: Formatteable):
        self.wrapped = wrapped

    @abstractmethod
    def format(self) -> str:
        pass


# Decorador concreto: convierte a mayúsculas
class UppercaseDecorator(TextDecorator):
    def format(self) -> str:
        return self.wrapped.format().upper()


# Decorador concreto: invierte el texto
class ReverseDecorator(TextDecorator):
    def format(self) -> str:
        return self.wrapped.format()[::-1]


# Decorador concreto: reemplaza espacios por guiones bajos
class ReplaceSpaceDecorator(TextDecorator):
    def format(self) -> str:
        return self.wrapped.format().replace(" ", "_")


# Decorador concreto: subraya el texto con una línea inferior
class UnderLineDecorator(TextDecorator):
    def format(self) -> str:
        text = self.wrapped.format()
        underline = "-" * len(text)
        return f"{text}\n{underline}"


# Programa principal
if __name__ == "__main__":
    texto = Text("Hola que tal Andres!")

    # Aplicar decoradores en cadena
    texto_decorado = UnderLineDecorator(
        ReplaceSpaceDecorator(
            ReverseDecorator(
                UppercaseDecorator(texto)
            )
        )
    )

    # Mostrar resultado final
    print(texto_decorado.format())