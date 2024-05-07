#Pablo Dario Jimenez Nu*o 21310143

# Definición de reglas
reglas = {
    "Regla1": {"P", "Q"},
    "Regla2": {"Q", "R"},
    "Regla3": {"R", "S"},
    "Regla4": {"T", "U"}
}

# Definición de hechos iniciales
hechos = {"P", "T"}

# Encadenamiento hacia adelante
def forward_chaining(reglas, hechos):
    nuevos_hechos = set()
    while True:
        cambios = False
        # Iterar sobre todas las reglas
        for regla, consecuente in reglas.items():
            # Verificar si todos los antecedentes de la regla están en los hechos
            if all(antecedente in hechos for antecedente in consecuente) and regla not in hechos:
                # Si todos los antecedentes están en los hechos y la regla no está en los hechos,
                # agregar la regla a los nuevos hechos
                nuevos_hechos.add(regla)
                cambios = True
        # Si no hubo cambios en esta iteración, salir del bucle
        if not cambios:
            break
        # Actualizar los hechos con los nuevos hechos derivados
        hechos.update(nuevos_hechos)
    return hechos

# Ejecutar encadenamiento hacia adelante
resultado_fd = forward_chaining(reglas, hechos)
print("Hechos derivados por encadenamiento hacia adelante:", resultado_fd)



