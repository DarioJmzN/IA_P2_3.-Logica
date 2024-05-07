#Pablo Dario Jimenez Nu*o 21310143

# Definición de reglas de diagnóstico
reglas_diagnostico = {
    "Regla1": {"fiebre", "tos", "dolor_de_garganta"},
    "Regla2": {"fiebre", "dolor_de_cabeza"},
    "Regla3": {"fiebre", "perdida_de_olfato"},
    "Regla4": {"fiebre", "perdida_de_gusto"}
}

# Definición de reglas causales
reglas_causales = {
    "fiebre": "Resfriado común",
    "tos": "Resfriado común",
    "dolor_de_garganta": "Resfriado común",
    "dolor_de_cabeza": "Gripe",
    "perdida_de_olfato": "COVID-19",
    "perdida_de_gusto": "COVID-19"
}

# Función para realizar diagnóstico basado en reglas
def diagnosticar_sintomas(sintomas):
    for regla, antecedentes in reglas_diagnostico.items():
        if antecedentes.issubset(sintomas):
            return regla
    return "No se puede diagnosticar con las reglas actuales."

# Función para encontrar la causa probable basada en los síntomas
def encontrar_causa(sintomas):
    for sintoma in sintomas:
        if sintoma in reglas_causales:
            return reglas_causales[sintoma]
    return "Causa desconocida"

# Ejemplo de uso
sintomas_paciente = {"fiebre", "tos"}
diagnostico = diagnosticar_sintomas(sintomas_paciente)
causa_probable = encontrar_causa(sintomas_paciente)

print("Diagnóstico basado en los síntomas:", diagnostico)
print("Causa probable basada en los síntomas:", causa_probable)






