#Pablo Dario Jimenez Nu*o 21310143

class Accion:
    def __init__(self, nombre, precondiciones, efectos):
        self.nombre = nombre  # Nombre de la acción
        self.precondiciones = precondiciones  # Precondiciones de la acción
        self.efectos = efectos  # Efectos de la acción

class PlanificadorOrdenParcial:
    def __init__(self, acciones):
        self.acciones = acciones  # Lista de acciones disponibles

    def planificar(self, estado_inicial, estado_meta):
        plan = []  # Plan inicialmente vacío
        acciones_aplicadas = set()  # Conjunto de acciones ya aplicadas
        estado_actual = estado_inicial  # Estado inicial

        # Mientras no hayamos alcanzado el estado meta
        while not self.estado_satisface_meta(estado_actual, estado_meta):
            # Encontrar una acción aplicable
            accion_aplicable = self.encontrar_accion_aplicable(estado_actual, acciones_aplicadas)

            # Si no se puede encontrar ninguna acción aplicable, no se puede planificar
            if accion_aplicable is None:
                return None

            # Aplicar la acción y actualizar el estado
            plan.append(accion_aplicable)
            estado_actual = self.aplicar_efectos(estado_actual, accion_aplicable)
            acciones_aplicadas.add(accion_aplicable)

        return plan

    def encontrar_accion_aplicable(self, estado, acciones_aplicadas):
        for accion in self.acciones:
            if accion not in acciones_aplicadas and self.accion_es_aplicable(estado, accion):
                return accion
        return None

    def accion_es_aplicable(self, estado, accion):
        return all(precondicion in estado for precondicion in accion.precondiciones)

    def aplicar_efectos(self, estado, accion):
        nuevo_estado = estado.copy()
        for efecto in accion.efectos:
            nuevo_estado.add(efecto)
        return nuevo_estado

    def estado_satisface_meta(self, estado, estado_meta):
        return estado >= estado_meta

# Definir acciones
acciones = [
    Accion("mover_robot_A_B", {"robot_en_A"}, {"robot_en_B"}),
    Accion("mover_robot_B_C", {"robot_en_B"}, {"robot_en_C"}),
    Accion("cargar_paquete", {"robot_en_B"}, {"paquete_cargado"}),
    Accion("entregar_paquete", {"robot_en_C", "paquete_cargado"}, {"paquete_entregado"})
]

# Definir el estado inicial y el estado meta
estado_inicial = {"robot_en_A"}
estado_meta = {"robot_en_C", "paquete_entregado"}

# Crear el planificador de orden parcial y planificar
planificador = PlanificadorOrdenParcial(acciones)
plan = planificador.planificar(estado_inicial, estado_meta)

# Imprimir el plan resultante
if plan is not None:
    print("Plan encontrado:")
    for accion in plan:
        print(accion.nombre)
else:
    print("No se puede planificar para alcanzar el estado meta.")

















