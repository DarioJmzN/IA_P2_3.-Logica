#Pablo Dario Jimenez Nu*o 21310143

class Accion:
    def __init__(self, nombre, precondiciones=None, efectos=None):
        self.nombre = nombre  # Nombre de la acción
        self.precondiciones = precondiciones if precondiciones else []  # Lista de precondiciones (opcional)
        self.efectos = efectos if efectos else []  # Lista de efectos (opcional)

class Situacion:
    def __init__(self, nombre, acciones=None):
        self.nombre = nombre  # Nombre de la situación
        self.acciones = acciones if acciones else []  # Lista de acciones en la situación (opcional)

class Evento:
    def __init__(self, nombre, situacion, momento):
        self.nombre = nombre  # Nombre del evento
        self.situacion = situacion  # Situación asociada al evento
        self.momento = momento  # Momento en el que ocurre el evento

# Definir acciones
comprar = Accion("Comprar", precondiciones=["Tener dinero"], efectos=["Tener objeto"])
vender = Accion("Vender", precondiciones=["Tener objeto"], efectos=["Tener dinero"])

# Definir situaciones
compra_venta = Situacion("Compra-Venta", acciones=[comprar, vender])

# Definir eventos
evento1 = Evento("Evento 1", compra_venta, "Mañana")
evento2 = Evento("Evento 2", compra_venta, "Tarde")

# Imprimir información sobre los eventos
print("Evento:", evento1.nombre)
print("  Situación:", evento1.situacion.nombre)
print("  Momento:", evento1.momento)

print("\nEvento:", evento2.nombre)
print("  Situación:", evento2.situacion.nombre)
print("  Momento:", evento2.momento)


)

















