#Pablo Dario Jimenez Nu*o 21310143

class Tarea:
    def __init__(self, nombre, precondiciones=None, sub_tareas=None):
        self.nombre = nombre
        self.precondiciones = precondiciones if precondiciones else []
        self.sub_tareas = sub_tareas if sub_tareas else []

class HTNPlanner:
    def __init__(self, tarea_raiz):
        self.tarea_raiz = tarea_raiz

    def planificar(self):
        plan = []
        self._planificar_recursivo(self.tarea_raiz, plan)
        return plan

    def _planificar_recursivo(self, tarea, plan):
        if tarea.sub_tareas:  # Si la tarea tiene sub-tareas, planifica cada sub-tarea recursivamente
            for sub_tarea in tarea.sub_tareas:
                self._planificar_recursivo(sub_tarea, plan)
        else:  # Si la tarea no tiene sub-tareas, agrega la tarea al plan
            plan.append(tarea)

# Definir las tareas jerárquicas
tarea_raiz = Tarea("Misión",
                   sub_tareas=[Tarea("Reconocimiento", precondiciones=["Equipamiento"]),
                               Tarea("Ataque", precondiciones=["Equipamiento", "Información"]),
                               Tarea("Extracción", precondiciones=["Equipamiento", "Información"])])

tarea_reconocimiento = tarea_raiz.sub_tareas[0]
tarea_reconocimiento.sub_tareas.append(Tarea("Recopilar Información", precondiciones=["Equipamiento"]))
tarea_reconocimiento.sub_tareas.append(Tarea("Analizar Información", precondiciones=["Equipamiento"]))

tarea_ataque = tarea_raiz.sub_tareas[1]
tarea_ataque.sub_tareas.append(Tarea("Asalto", precondiciones=["Información"]))
tarea_ataque.sub_tareas.append(Tarea("Destruir", precondiciones=["Información"]))

tarea_extraccion = tarea_raiz.sub_tareas[2]
tarea_extraccion.sub_tareas.append(Tarea("Recoger Objetivo", precondiciones=["Información"]))
tarea_extraccion.sub_tareas.append(Tarea("Retirarse", precondiciones=["Información"]))

# Planificar con HTN
planner = HTNPlanner(tarea_raiz)
plan = planner.planificar()

# Imprimir el plan
print("Plan encontrado:")
for tarea in plan:
    print(tarea.nombre)
