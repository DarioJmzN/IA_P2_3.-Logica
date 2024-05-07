#Pablo Dario Jimenez Nu*o 21310143

from sympy import symbols, Implies, Equivalent, satisfiable, satisfiable, simplify_logic

# Definición de símbolos proposicionales
p, q, r = symbols('p q r')

# Definición de algunas fórmulas lógicas
formula1 = Equivalent(p, q)  # p <=> q
formula2 = Implies(p, q)      # p => q
formula3 = Implies(q, p)      # q => p
formula4 = Implies(p, p)      # p => p

# Verificando la equivalencia entre dos fórmulas
es_equivalente = formula1.equals(formula2)
print("¿La fórmula 1 es equivalente a la fórmula 2?", es_equivalente)

# Verificando la validez de una fórmula
es_valida = formula4.is_valid()
print("¿La fórmula 4 es válida?", es_valida)

# Verificando la satisfacibilidad de una fórmula
satisfacible = satisfiable(formula3)
print("¿La fórmula 3 es satisfacible?", satisfacible)

# Simplificando una fórmula lógica
formula5 = p & (~p | q)
simplificada = simplify_logic(formula5)
print("La fórmula 5 simplificada es:", simplificada)


