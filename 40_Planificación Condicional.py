#Pablo Dario Jimenez Nu*o 21310143

class Accion:
    def __init__(self, nombre, precondiciones, efectos):
        self.nombre = nombre  # Nombre de la acción
        self.precondiciones = precondiciones  # Precondiciones de la acción
        self.efectos = efectos  # Efectos de la acción

class PlanificadorCondicional:
    def __init__(self, acciones, estado_inicial, estado_meta):
        self.acciones = acciones
        self.estado_inicial = estado_inicial
        self.estado_meta = estado_meta

    def planificar(self):
        plan = []  # Lista para almacenar el plan
        estado_actual = self.estado_inicial.copy()  # Copia del estado inicial

        while not self.estado_satisface_meta(estado_actual):
            accion_aplicable = self.encontrar_accion_aplicable(estado_actual)
            if accion_aplicable is None:
                return None  # Si no se puede encontrar una acción aplicable, no se puede planificar
            plan.append(accion_aplicable)  # Agrega la acción al plan
            estado_actual.update(accion_aplicable.efectos)  # Actualiza el estado actual con los efectos de la acción

        return plan

    def encontrar_accion_aplicable(self, estado):
        for accion in self.acciones:
            if accion.precondiciones.issubset(estado):
                return accion
        return None  # Si no se encuentra ninguna acción aplicable, devuelve None

    def estado_satisface_meta(self, estado):
        return self.estado_meta.issubset(estado)

# Definir acciones
acciones = [
    Accion("mover_robot_A_B", {"robot_en_A"}, {"robot_en_B"}),
    Accion("mover_robot_B_C", {"robot_en_B"}, {"robot_en_C"}),
    Accion("cargar_paquete", {"robot_en_B"}, {"paquete_cargado"}),
    Accion("entregar_paquete", {"robot_en_C", "paquete_cargado"}, {"paquete_entregado"})
]

# Definir estados iniciales y objetivo
estado_inicial = {"robot_en_A"}
estado_meta = {"robot_en_C", "paquete_entregado"}

# Crear instancia de PlanificadorCondicional y planificar
planificador = PlanificadorCondicional(acciones, estado_inicial, estado_meta)
plan = planificador.planificar()

# Imprimir el plan resultante
if plan:
    print("Plan encontrado:")
    for accion in plan:
        print(accion.nombre)
else:
    print("No se puede planificar para alcanzar el estado meta.")

