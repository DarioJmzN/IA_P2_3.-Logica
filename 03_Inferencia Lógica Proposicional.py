#Pablo Dario Jimenez Nu*o 21310143

from sympy import symbols, Not, And, Or, Implies, satisfiable

# Definición de símbolos proposicionales
p, q, r = symbols('p q r')

# Definición de algunas fórmulas lógicas
formula1 = Implies(p, q)
formula2 = And(p, q)
formula3 = Or(p, q)
formula4 = Not(p)

# Evaluación de las fórmulas con valores de verdad específicos
valores_verdad = {
    p: True,
    q: False
}

print("La fórmula 1 es verdadera:", formula1.subs(valores_verdad))
print("La fórmula 2 es verdadera:", formula2.subs(valores_verdad))
print("La fórmula 3 es verdadera:", formula3.subs(valores_verdad))
print("La fórmula 4 es verdadera:", formula4.subs(valores_verdad))

# Comprobación de la satisfacibilidad de una fórmula
formula5 = Or(p, Not(p))
satisfacible = satisfiable(formula5)
print("La fórmula 5 es satisfacible:", satisfacible)

