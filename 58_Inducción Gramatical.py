#Pablo Dario Jimenez Nu*o 21310143

class InduccionGramatical:
    def __init__(self):
        self.gramatica = {}

    def inducir_gramatica(self, secuencias):
        for secuencia in secuencias:
            for i in range(len(secuencia) - 1):
                lhs = secuencia[i]
                rhs = secuencia[i + 1]
                if lhs not in self.gramatica:
                    self.gramatica[lhs] = set()
                self.gramatica[lhs].add(rhs)

    def obtener_gramatica(self):
        return self.gramatica

# Ejemplo de uso:
secuencias = [['a', 'b', 'c'], ['a', 'c', 'd'], ['b', 'd', 'e']]
inductor = InduccionGramatical()
inductor.inducir_gramatica(secuencias)
gramatica_inducida = inductor.obtener_gramatica()
print("Gramática inducida:", gramatica_inducida)


