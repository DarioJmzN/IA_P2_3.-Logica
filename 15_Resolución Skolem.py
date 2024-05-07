#Pablo Dario Jimenez Nu*o 21310143

def skolemizar(formula):
    skolemizado = []
    variables = set()
    for literal in formula:
        if isinstance(literal, tuple):
            variables.update(literal)
    skolem_variables = {var: f"sk_{i}" for i, var in enumerate(variables)}
    for literal in formula:
        if isinstance(literal, tuple):
            skolemizado.append(tuple(skolem_variables[var] for var in literal))
        else:
            skolemizado.append(literal)
    return skolemizado, skolem_variables

def resolver(clausula1, clausula2):
    resolvente = []
    for literal1 in clausula1:
        for literal2 in clausula2:
            if (literal1[0] == '~' and literal2[0] != '~' and literal1[1:] == literal2) or \
               (literal1[0] != '~' and literal2[0] == '~' and literal1 == literal2[1:]):
                resolvente.extend(clausula1 + clausula2)
                resolvente.remove(literal1)
                resolvente.remove(literal2)
    return list(set(resolvente))

# Ejemplo de uso
clausula1 = [('~', 'P', 'x'), ('~', 'Q', 'y')]
clausula2 = [('R', 'x', 'y')]
print("Clausula 1:", clausula1)
print("Clausula 2:", clausula2)

# Skolemización
skolemizada1, skolem_variables1 = skolemizar(clausula1)
skolemizada2, skolem_variables2 = skolemizar(clausula2)
print("Clausula 1 Skolemizada:", skolemizada1)
print("Clausula 2 Skolemizada:", skolemizada2)
print("Mapeo de variables para Clausula 1:", skolem_variables1)
print("Mapeo de variables para Clausula 2:", skolem_variables2)

# Resolución
resolvente = resolver(skolemizada1, skolemizada2)
print("Resolvente:", resolvente)








