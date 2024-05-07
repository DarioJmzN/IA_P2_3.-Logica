#Pablo Dario Jimenez Nu*o 21310143

class ObjetoMental:
    def __init__(self, nombre):
        self.nombre = nombre

class Creencia(ObjetoMental):
    def __init__(self, nombre, contenido):
        super().__init__(nombre)
        self.contenido = contenido

class Evento:
    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion
        self.creencias = []

    def agregar_creencia(self, creencia):
        self.creencias.append(creencia)

# Crear objetos mentales
creencia1 = Creencia("Creencia1", "Los gatos son animales domésticos.")
creencia2 = Creencia("Creencia2", "El sol sale por el este.")

# Crear un evento
evento = Evento("Evento1", "Observación matutina.")

# Agregar creencias al evento
evento.agregar_creencia(creencia1)
evento.agregar_creencia(creencia2)

# Imprimir información del evento y sus creencias
print("Evento:", evento.nombre)
print("Descripción:", evento.descripcion)
print("Creencias:")
for creencia in evento.creencias:
    print("- Nombre:", creencia.nombre)
    print("  Contenido:", creencia.contenido)



)

















