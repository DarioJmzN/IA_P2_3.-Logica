#Pablo Dario Jimenez Nu*o 21310143

from pyknow import *

class MiAgente(DefFacts):
    @Fact()
    def datos_iniciales(self):
        self.assert_fact(Fact(tiene_plumas=True))
        self.assert_fact(Fact(puede_volar=True))
        self.assert_fact(Fact(puede_nadar=False))

class ReglasNoMonotonicas(KnowledgeEngine):
    @Rule(AND(Fact(tiene_plumas=True), NOT(Fact(puede_volar=True))))
    def pinguino(self):
        print("El animal es un pingüino.")

    @Rule(AND(Fact(tiene_plumas=True), Fact(puede_volar=True)))
    def ave(self):
        print("El animal es un ave.")

# Crear un agente y cargar los datos iniciales
agente = MiAgente()

# Ejecutar las reglas no monótonas
reglas_no_monotonicas = ReglasNoMonotonicas()
reglas_no_monotonicas.reset()  # Reiniciar el motor de reglas
reglas_no_monotonicas.declare(agente.facts())  # Cargar los datos iniciales
reglas_no_monotonicas.run()  # Ejecutar las reglas no monótonas













