#Pablo Dario Jimenez Nu*o 21310143

from modal_logic_parser import parse, evaluate

# Definir una expresión modal
expresion_modal = "[]P -> P"

# Analizar la expresión modal
arbol_sintactico = parse(expresion_modal)

# Evaluar la expresión modal
resultado = evaluate(arbol_sintactico)

# Imprimir el resultado
print("La expresión modal es", "verdadera" if resultado else "falsa")











