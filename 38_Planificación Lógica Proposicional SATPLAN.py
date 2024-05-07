#Pablo Dario Jimenez Nu*o 21310143

from pysat.solvers import Glucose3

class Accion:
    def __init__(self, nombre, precondiciones, efectos):
        self.nombre = nombre  # Nombre de la acción
        self.precondiciones = precondiciones  # Precondiciones de la acción
        self.efectos = efectos  # Efectos de la acción

class SATPlan:
    def __init__(self, acciones, estado_inicial, estado_meta):
        self.acciones = acciones
        self.estado_inicial = estado_inicial
        self.estado_meta = estado_meta

    def planificar(self):
        solver = Glucose3()

        # Crear variables para cada acción en cada nivel de planificación
        variables_acciones = {}  # Diccionario para almacenar las variables de las acciones
        for nivel in range(len(self.acciones) + 1):
            for accion in self.acciones:
                variables_acciones[(nivel, accion.nombre)] = solver.new_var()

        # Agregar cláusulas para el estado inicial
        for literal in self.estado_inicial:
            solver.add_clause([literal])

        # Agregar cláusulas para la meta
        for literal in self.estado_meta:
            solver.add_clause([-literal])

        # Agregar cláusulas para la transición entre niveles
        for nivel in range(len(self.acciones)):
            for accion in self.acciones:
                if self.accion_es_aplicable(accion, nivel):
                    # Obtener las precondiciones y efectos de la acción
                    precondiciones = [literal for literal in accion.precondiciones if (nivel, literal) in variables_acciones]
                    efectos = [literal for literal in accion.efectos if (nivel + 1, literal) in variables_acciones]

                    # Agregar cláusulas para la transición de nivel
                    for literal in efectos:
                        clause = precondiciones + [-literal]
                        solver.add_clause(clause)

        # Resolver el problema SAT
        if solver.solve():
            plan = self.extraer_plan(solver, variables_acciones)
            return plan
        else:
            return None

    def accion_es_aplicable(self, accion, nivel):
        return all(precondicion in self.estado_inicial for precondicion in accion.precondiciones)

    def extraer_plan(self, solver, variables_acciones):
        plan = []
        nivel_actual = 0

        while True:
            acciones_nivel_actual = [accion for (nivel, accion), var in variables_acciones.items() if nivel == nivel_actual and solver.get_model()[var]]
            if not acciones_nivel_actual:
                break
            plan.append(acciones_nivel_actual[0])
            nivel_actual += 1

        return plan

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

# Crear instancia de SATPlan y planificar
sat_plan = SATPlan(acciones, estado_inicial, estado_meta)
plan = sat_plan.planificar()

# Imprimir el plan resultante
if plan:
    print("Plan encontrado:")
    for accion in plan:
        print(accion.nombre)
else:
    print("No se puede planificar para alcanzar el estado meta.")









