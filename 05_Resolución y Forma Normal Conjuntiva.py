#Pablo Dario Jimenez Nu*o 21310143

from sympy import symbols, Not, Or, And, Implies, satisfiable

# Definición de símbolos proposicionales
p, q, r = symbols('p q r')

# Definición de algunas fórmulas lógicas
formula1 = Implies(p, q)                          # p => q
formula2 = Implies(Or(p, q), And(p, q))           # (p ∨ q) => (p ∧ q)
formula3 = Implies(Or(Not(p), q), Or(p, q))       # (¬p ∨ q) => (p ∨ q)

# Convertir las fórmulas a Forma Normal Conjuntiva (CNF)
cnf_formula1 = formula1.to_cnf()
cnf_formula2 = formula2.to_cnf()
cnf_formula3 = formula3.to_cnf()

print("CNF de la fórmula 1:", cnf_formula1)
print("CNF de la fórmula 2:", cnf_formula2)
print("CNF de la fórmula 3:", cnf_formula3)

# Verificando la satisfacibilidad de las fórmulas CNF
satisfacible1 = satisfiable(cnf_formula1)
satisfacible2 = satisfiable(cnf_formula2)
satisfacible3 = satisfiable(cnf_formula3)

print("¿La fórmula 1 en CNF es satisfacible?", satisfacible1)
print("¿La fórmula 2 en CNF es satisfacible?", satisfacible2)
print("¿La fórmula 3 en CNF es satisfacible?", satisfacible3)



