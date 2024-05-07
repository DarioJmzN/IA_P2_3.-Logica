#Pablo Dario Jimenez Nu*o 21310143

class Regla:
    def __init__(self, antecedente, consecuente):
        self.antecedente = antecedente  # El antecedente de la regla
        self.consecuente = consecuente  # El consecuente de la regla

class Nodo:
    def __init__(self, nombre, conexiones=None):
        self.nombre = nombre  # El nombre del nodo
        self.conexiones = conexiones if conexiones else []  # Las conexiones del nodo a otros nodos

class RedSemantica:
    def __init__(self):
        self.nodos = []  # Lista para almacenar los nodos de la red semántica

    def agregar_nodo(self, nodo):
        self.nodos.append(nodo)  # Método para agregar un nodo a la red semántica

# Definir algunas reglas
regla1 = Regla("gato", "animal")  # Si algo es un gato, entonces es un animal
regla2 = Regla("perro", "animal")  # Si algo es un perro, entonces es un animal

# Definir nodos de una red semántica
animal = Nodo("animal")  # Nodo "animal"
mamifero = Nodo("mamífero", conexiones=[animal])  # Nodo "mamífero" conectado al nodo "animal"
gato = Nodo("gato", conexiones=[mamifero])  # Nodo "gato" conectado al nodo "mamífero"
perro = Nodo("perro", conexiones=[mamifero])  # Nodo "perro" conectado al nodo "mamífero"

# Crear una red semántica y agregar nodos
red_semantica = RedSemantica()
red_semantica.agregar_nodo(animal)
red_semantica.agregar_nodo(mamifero)
red_semantica.agregar_nodo(gato)
red_semantica.agregar_nodo(perro)

# Imprimir la red semántica
print("Red Semántica:")
for nodo in red_semantica.nodos:
    print("- Nodo:", nodo.nombre)
    print("  Conexiones:", [conexion.nombre for conexion in nodo.conexiones])

















