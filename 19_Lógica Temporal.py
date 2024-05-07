#Pablo Dario Jimenez Nu*o 21310143

from templog import TemporalLogic

# Crear una instancia de lógica temporal
tl = TemporalLogic()

# Definir una expresión temporal
expresion_temporal = "G(F p)"

# Evaluar la expresión temporal
resultado = tl.eval(expresion_temporal, {"p": [False, False, True, True, True]})

# Imprimir el resultado
print("La expresión temporal es", "verdadera" if resultado else "falsa")












