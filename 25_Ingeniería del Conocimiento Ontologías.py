#Pablo Dario Jimenez Nu*o 21310143

from owlready2 import *

# Crear una ontología
onto = get_ontology("http://www.ontologiaanimales.com/animales.owl")

# Definir las clases
with onto:
    class Animal(Thing):
        pass

    class Mamifero(Animal):
        pass

    class Ave(Animal):
        pass

# Definir propiedades
with onto:
    class tiene_patas(Animal >> Literal):
        pass

    class pone_huevos(Ave >> bool):
        pass

# Crear instancias
leon = Mamifero()
leon.tiene_patas = True

aguila = Ave()
aguila.pone_huevos = True

# Guardar la ontología
onto.save("animales.owl")

















