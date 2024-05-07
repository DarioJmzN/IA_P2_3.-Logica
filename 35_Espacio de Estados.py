#Pablo Dario Jimenez Nu*o 21310143

class Estado:
    def __init__(self, nombre, acciones):
        self.nombre = nombre  # Nombre del estado
        self.acciones = acciones  # Acciones disponibles desde este estado

class Accion:
    def __init__(self, nombre, estado_destino):
        self.nombre = nombre  # Nombre de la acción
        self.estado_destino = estado_destino  # Estado al que lleva esta acción

class EspacioEstados:
    def __init__(self, estados):
        self.estados = estados  # Lista de estados en el espacio de estados

# Definir los estados y las acciones
estado_A = Estado("A", [])
estado_B = Estado("B", [])
estado_C = Estado("C", [])
accion_A_B = Accion("A_B", estado_B)
accion_B_C = Accion("B_C", estado_C)
accion_C_A = Accion("C_A", estado_A)

# Establecer las acciones disponibles para cada estado
estado_A.acciones = [accion_A_B]
estado_B.acciones = [accion_B_C]
estado_C.acciones = [accion_C_A]

# Crear el espacio de estados
espacio_estados = EspacioEstados([estado_A, estado_B, estado_C])

# Imprimir el espacio de estados y las acciones disponibles desde cada estado
for estado in espacio_estados.estados:
    print("Estado:", estado.nombre)
    print("Acciones disponibles:")
    for accion in estado.acciones:
        print("-", accion.nombre, "->", accion.estado_destino.nombre)
    print()




















