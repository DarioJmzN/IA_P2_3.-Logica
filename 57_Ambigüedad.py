#Pablo Dario Jimenez Nu*o 21310143

class AmbiguedadDefinida:
    def __init__(self):
        self.palabras = {}

    def agregar_palabra(self, palabra, significados):
        self.palabras[palabra] = significados

    def obtener_significados(self, palabra):
        return self.palabras.get(palabra, "La palabra no está en la lista de ambigüedad.")

# Ejemplo de uso:
ambiguedad = AmbiguedadDefinida()

# Agregar palabras con múltiples significados
ambiguedad.agregar_palabra("banco", ["institución financiera", "asiento"])

# Obtener los significados de una palabra
print("Significados de 'banco':", ambiguedad.obtener_significados("banco"))
print("Significados de 'coche':", ambiguedad.obtener_significados("coche"))

