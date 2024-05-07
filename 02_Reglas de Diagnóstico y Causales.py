#Pablo Dario Jimenez Nu*o 21310143

# Definición de una serie de síntomas y posibles diagnósticos
sintomas = {
    "fiebre": ["gripe", "COVID-19", "resfriado"],
    "tos": ["gripe", "COVID-19", "resfriado"],
    "dolor_de_garganta": ["gripe", "COVID-19", "resfriado"],
    "dolor_de_cabeza": ["gripe", "resfriado"],
    "perdida_de_olfato": ["COVID-19"],
    "perdida_de_gusto": ["COVID-19"]
}

# Definición de una función para realizar un diagnóstico basado en los síntomas
def diagnosticar(sintomas):
    posibles_diagnosticos = set()
    for sintoma, enfermedades in sintomas.items():
        for enfermedad in enfermedades:
            posibles_diagnosticos.add(enfermedad)
    return posibles_diagnosticos

# Definición de una función para identificar las posibles causas de un síntoma
def causas_de_sintoma(sintoma):
    if sintoma in sintomas:
        return sintomas[sintoma]
    else:
        return ["No se encontraron causas conocidas para este síntoma."]

# Ejemplo de diagnóstico basado en síntomas
sintomas_paciente = {
    "fiebre": True,
    "tos": True,
    "dolor_de_garganta": False,
    "dolor_de_cabeza": True
}

diagnostico = diagnosticar(sintomas_paciente)
print("Posibles diagnósticos basados en los síntomas del paciente:", diagnostico)

# Ejemplo de identificación de causas de un síntoma específico
sintoma_especifico = "perdida_de_olfato"
causas = causas_de_sintoma(sintoma_especifico)
print("Posibles causas de", sintoma_especifico + ":", causas)

