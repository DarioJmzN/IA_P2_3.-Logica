#Pablo Dario Jimenez Nu*o 21310143

# Definición de reglas de producción
reglas = [
    {"temperatura": "alta", "humedad": "alta"}: "Aire Acondicionado",
    {"temperatura": "alta", "humedad": "normal"}: "Ventilador",
    {"temperatura": "normal", "humedad": "alta"}: "Desumificador",
    {"temperatura": "normal", "humedad": "normal"}: "Ninguna acción necesaria"
]

# Función para inferir la acción a tomar
def inferir_accion(entrada, reglas):
    for condiciones, accion in reglas.items():
        if all(entrada[condicion] == valor for condicion, valor in condiciones.items()):
            return accion
    return "No se pudo inferir ninguna acción"

# Ejemplo de uso
condiciones_actuales = {"temperatura": "alta", "humedad": "alta"}
accion_recomendada = inferir_accion(condiciones_actuales, reglas)

print("Condiciones actuales:", condiciones_actuales)
print("Acción recomendada:", accion_recomendada)







