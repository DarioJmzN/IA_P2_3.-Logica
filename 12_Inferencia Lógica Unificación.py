#Pablo Dario Jimenez Nu*o 21310143

def unificar(termino1, termino2, sustitucion={}):
    # Si la sustitución ya tiene unificación, se devuelve
    if sustitucion is None:
        return None
    # Si los términos son idénticos, se devuelve la sustitución actual
    if termino1 == termino2:
        return sustitucion
    # Si uno de los términos es una variable, se realiza la unificación
    if es_variable(termino1):
        return unificar_variable(termino1, termino2, sustitucion)
    elif es_variable(termino2):
        return unificar_variable(termino2, termino1, sustitucion)
    # Si los términos son compuestos, se descomponen y se intenta unificar recursivamente
    if es_compuesto(termino1) and es_compuesto(termino2):
        return unificar(termino1[1:], termino2[1:], unificar(termino1[0], termino2[0], sustitucion))
    # Si los términos son diferentes y ninguno es una variable, la unificación falla
    return None

def es_variable(termino):
    return isinstance(termino, str) and termino.islower()

def es_compuesto(termino):
    return isinstance(termino, list)

def unificar_variable(variable, termino, sustitucion):
    if variable in sustitucion:
        return unificar(sustitucion[variable], termino, sustitucion)
    elif termino in sustitucion:
        return unificar(variable, sustitucion[termino], sustitucion)
    else:
        sustitucion[variable] = termino
        return sustitucion

# Ejemplo de uso
sustitucion = unificar(["x", "y"], ["a", "b"])
print("Sustitución:", sustitucion)








