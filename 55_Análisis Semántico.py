#Pablo Dario Jimenez Nu*o 21310143
class AnalizadorSemantico:
    def __init__(self, expresion, variables):
        self.expresion = expresion
        self.variables = variables

    def evaluar(self):
        try:
            return eval(self.expresion, self.variables)
        except NameError as e:
            variable_faltante = str(e).split("'")[1]
            raise ValueError(f"Variable no definida: {variable_faltante}")

# Ejemplo de uso:
variables = {'x': 5, 'y': 3}
expresion = "x + y * 2"

analizador = AnalizadorSemantico(expresion, variables)
resultado = analizador.evaluar()
print("Resultado:", resultado)
