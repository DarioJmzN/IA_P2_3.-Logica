#Pablo Dario Jimenez Nu*o 21310143

class Estado:
    def __init__(self, variables):
        self.variables = variables  # Variables que describen el estado

    def __str__(self):
        return str(self.variables)

class Accion:
    def __init__(self, nombre, precondiciones, efectos):
        self.nombre = nombre  # Nombre de la acción
        self.precondiciones = precondiciones  # Precondiciones de la acción
        self.efectos = efectos  # Efectos de la acción

class Problema:
    def __init__(self, estado_inicial, estado_meta, acciones):
        self.estado_inicial = estado_inicial  # Estado inicial del problema
        self.estado_meta = estado_meta  # Estado meta del problema
        self.acciones = acciones  # Acciones posibles en el problema

def STRIPS(problema):
    plan = []
    estado_actual = problema.estado_inicial
    while estado_actual != problema.estado_meta:
        accion = seleccionar_accion(problema, estado_actual)
        plan.append(accion)
        estado_actual = aplicar_efectos(estado_actual, accion)
    return plan

def seleccionar_accion(problema, estado_actual):
    for accion in problema.acciones:
        if all(precondicion in estado_actual.variables for precondicion in accion.precondiciones):
            return accion

def aplicar_efectos(estado_actual, accion):
    nuevo_estado = estado_actual.variables.copy()
    for efecto in accion.efectos:
        nuevo_estado.add(efecto)
    return Estado(nuevo_estado)

# Definir estados
estado_inicial = Estado({"robot_en_A"})
estado_meta = Estado({"robot_en_C"})

# Definir acciones
acciones = [
    Accion("mover_robot_A_B", {"robot_en_A"}, {"robot_en_B"}),
    Accion("mover_robot_B_C", {"robot_en_B"}, {"robot_en_C"})
]

# Definir problema
problema = Problema(estado_inicial, estado_meta, acciones)

# Resolver el problema usando STRIPS
plan_STRIPS = STRIPS(problema)

# Imprimir el plan
print("Plan generado por STRIPS:")
for accion in plan_STRIPS:
    print(accion.nombre)



















