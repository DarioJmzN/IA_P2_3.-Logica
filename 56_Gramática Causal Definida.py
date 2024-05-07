#Pablo Dario Jimenez Nu*o 21310143
class GramaticaCausalDefinida:
    def __init__(self):
        self.reglas = []

    def agregar_regla(self, causa, efecto):
        self.reglas.append((causa, efecto))

    def verificar_causalidad(self, evento1, evento2):
        for causa, efecto in self.reglas:
            if causa == evento1 and efecto == evento2:
                return True
        return False

# Ejemplo de uso:
gramatica = GramaticaCausalDefinida()

# Agregar reglas de causalidad
gramatica.agregar_regla('lluvia', 'crecimiento_cesped')
gramatica.agregar_regla('riego', 'crecimiento_cesped')
gramatica.agregar_regla('corte_cesped', 'aspecto_cuidado')

# Verificar causalidad entre eventos
print("¿La lluvia causa el crecimiento del césped?", gramatica.verificar_causalidad('lluvia', 'crecimiento_cesped'))
print("¿El riego causa el crecimiento del césped?", gramatica.verificar_causalidad('riego', 'crecimiento_cesped'))
print("¿El corte del césped causa un aspecto cuidado?", gramatica.verificar_causalidad('corte_cesped', 'aspecto_cuidado'))
