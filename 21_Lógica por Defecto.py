#Pablo Dario Jimenez Nu*o 21310143

class LogicaPorDefecto:
    def __init__(self):
        self.hechos = {}  # Diccionario para almacenar los hechos conocidos

    def agregar_hecho(self, hecho, valor):
        self.hechos[hecho] = valor  # Método para agregar un nuevo hecho al agente

    def consultar(self, consulta):
        if consulta in self.hechos:  # Verificar si la consulta está presente en los hechos conocidos
            return self.hechos[consulta]  # Si está presente, devolver el valor del hecho
        else:
            return "No se encuentra información sobre la consulta. Se aplicará lógica por defecto."
            # Si la consulta no está presente, indicar que se aplicará lógica por defecto

# Crear un agente de lógica por defecto
agente = LogicaPorDefecto()

# Agregar algunos hechos al agente
agente.agregar_hecho("puede_volar", True)
agente.agregar_hecho("tiene_plumas", True)
# El hecho "puede_nadar" no se agrega intencionalmente para demostrar lógica por defecto

# Consultas al agente de lógica por defecto
print("¿El animal puede volar?", agente.consultar("puede_volar"))
print("¿El animal tiene plumas?", agente.consultar("tiene_plumas"))
print("¿El animal puede nadar?", agente.consultar("puede_nadar"))














