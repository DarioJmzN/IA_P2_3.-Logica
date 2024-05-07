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
        for regla, consecuente in reglas.items():
            if all(antecedente in hechos for antecedente in consecuente) and regla not in hechos:
                nuevos_hechos.add(regla)
                cambios = True
        if not cambios:
            break
        hechos.update(nuevos_hechos)
    return hechos

# Ejemplo de uso
resultado_fd = forward_chaining(reglas, hechos)
print("Hechos derivados por encadenamiento hacia adelante:", resultado_fd)









