#Pablo Dario Jimenez Nu*o 21310143

class Categoria:
    def __init__(self, nombre):
        self.nombre = nombre  # Nombre de la categoría
        self.objetos = []  # Lista para almacenar los objetos pertenecientes a la categoría

    def agregar_objeto(self, objeto):
        self.objetos.append(objeto)  # Método para agregar un objeto a la categoría

class Objeto:
    def __init__(self, nombre):
        self.nombre = nombre  # Nombre del objeto

# Definir categorías
animal = Categoria("Animal")  # Crear una categoría "Animal"
vehiculo = Categoria("Vehículo")  # Crear una categoría "Vehículo"

# Definir objetos
perro = Objeto("Perro")  # Crear un objeto "Perro"
gato = Objeto("Gato")  # Crear un objeto "Gato"
coche = Objeto("Coche")  # Crear un objeto "Coche"
moto = Objeto("Moto")  # Crear un objeto "Moto"

# Agregar objetos a las categorías
animal.agregar_objeto(perro)  # Agregar el perro a la categoría "Animal"
animal.agregar_objeto(gato)  # Agregar el gato a la categoría "Animal"
vehiculo.agregar_objeto(coche)  # Agregar el coche a la categoría "Vehículo"
vehiculo.agregar_objeto(moto)  # Agregar la moto a la categoría "Vehículo"

# Imprimir la estructura de la taxonomía
print("Categoría:", animal.nombre)
print("  Objetos:")
for obj in animal.objetos:
    print("   -", obj.nombre)  # Imprimir el nombre de cada objeto en la categoría "Animal"

print("Categoría:", vehiculo.nombre)
print("  Objetos:")
for obj in vehiculo.objetos:
    print("   -", obj.nombre)  # Imprimir el nombre de cada objeto en la categoría "Vehículo"

)

















