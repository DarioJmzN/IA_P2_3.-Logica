#Pablo Dario Jimenez Nu*o 21310143

class AgenteLogico:
    def __init__(self):
        self.hechos = {}

    def agregar_hecho(self, hecho, valor):
        self.hechos[hecho] = valor

    def consultar(self, consulta):
        if consulta in self.hechos:
            return self.hechos[consulta]
        else:
            return "No se encuentra información sobre la consulta."

# Crear un agente lógico
agente = AgenteLogico()

# Agregar algunos hechos
agente.agregar_hecho("puede_volar", True)
agente.agregar_hecho("tiene_plumas", True)
agente.agregar_hecho("puede_nadar", False)

# Consultas al agente lógico
print("¿El animal puede volar?", agente.consultar("puede_volar"))
print("¿El animal tiene plumas?", agente.consultar("tiene_plumas"))
print("¿El animal puede nadar?", agente.consultar("puede_nadar"))
print("¿El animal es mamífero?", agente.consultar("es_mamifero"))









