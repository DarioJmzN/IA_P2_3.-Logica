#Pablo Dario Jimenez Nu*o 21310143

class Accion:
    def __init__(self, nombre, precondiciones, efectos):
        self.nombre = nombre  # Nombre de la acción
        self.precondiciones = precondiciones  # Precondiciones de la acción
        self.efectos = efectos  # Efectos de la acción

class GraphPlan:
    def __init__(self, acciones, estados_init, estados_goal):
        self.acciones = acciones
        self.estados_init = estados_init
        self.estados_goal = estados_goal

    def planificar(self):
        nivel = 0
        niveles = [[self.estados_init]]  # Inicializar el primer nivel con el estado inicial
        acciones_por_nivel = [[] for _ in range(len(self.acciones) + 1)]  # Inicializar lista de acciones por nivel

        while True:
            # Extender el grafo hasta alcanzar un punto fijo
            while True:
                if self.todos_estados_satisfechos(niveles[nivel]):
                    break  # Si todos los estados en el nivel están satisfechos, detener la extensión
                niveles.append(self.expandir(niveles[nivel], acciones_por_nivel[nivel]))
                nivel += 1

            # Verificar si la meta se puede alcanzar
            if self.goal_es_satisfacible(niveles[nivel]):
                return self.construir_plan(niveles, acciones_por_nivel)

            # Si no se puede alcanzar la meta, agregar un nuevo nivel
            niveles.append([])
            nivel += 1

    def expandir(self, estados, acciones_anteriores):
        nuevos_estados = set()  # Conjunto para almacenar los nuevos estados en este nivel
        nuevas_acciones = set()  # Conjunto para almacenar las nuevas acciones en este nivel

        for accion in self.acciones:
            # Verificar si la acción es aplicable en este nivel
            if self.accion_es_aplicable(estados, accion):
                nuevos_estados.update(accion.efectos)  # Agregar los efectos de la acción
                nuevas_acciones.add(accion)  # Agregar la acción a este nivel

        # Eliminar los estados que ya han sido satisfechos por acciones anteriores
        nuevos_estados -= set.union(*[accion.precondiciones for accion in acciones_anteriores])

        return nuevos_estados

    def todos_estados_satisfechos(self, estados):
        return all(estado in estados for estado in self.estados_goal)

    def goal_es_satisfacible(self, estados):
        return all(estado in estados for estado in self.estados_goal)

    def accion_es_aplicable(self, estados, accion):
        return accion.precondiciones.issubset(estados)

    def construir_plan(self, niveles, acciones_por_nivel):
        plan = []
        nivel_actual = len(niveles) - 2

        while nivel_actual >= 0:
            # Obtener acciones que satisfacen el nivel actual
            acciones_satisfactorias = [accion for accion in acciones_por_nivel[nivel_actual] if accion.efectos.issubset(niveles[nivel_actual + 1])]

            # Elegir una acción para agregar al plan (podría ser arbitraria)
            accion_elegida = acciones_satisfactorias[0]

            plan.insert(0, accion_elegida)  # Agregar la acción al principio del plan
            nivel_actual -= 1

        return plan

# Definir acciones
acciones = [
    Accion("mover_robot_A_B", {"robot_en_A"}, {"robot_en_B"}),
    Accion("mover_robot_B_C", {"robot_en_B"}, {"robot_en_C"}),
    Accion("cargar_paquete", {"robot_en_B"}, {"paquete_cargado"}),
    Accion("entregar_paquete", {"robot_en_C", "paquete_cargado"}, {"paquete_entregado"})
]

# Definir estados iniciales y objetivo
estados_iniciales = {"robot_en_A"}
estados_meta = {"robot_en_C", "paquete_entregado"}

# Crear instancia de GraphPlan y planificar
graph_plan = GraphPlan(acciones, estados_iniciales, estados_meta)
plan = graph_plan.planificar()

# Imprimir el plan resultante
if plan:
    print("Plan encontrado:")
    for accion in plan:
        print(accion.nombre)
else:
    print("No se puede planificar para alcanzar el estado meta.")










