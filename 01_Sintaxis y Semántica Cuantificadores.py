#Pablo Dario Jimenez Nu*o 21310143

# Definición de una lista de números
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Definición de una lista de estudiantes y sus calificaciones
estudiantes = {
    "Juan": [90, 85, 88],
    "María": [75, 80, 82],
    "Pedro": [60, 70, 65],
    "Ana": [95, 92, 98]
}

# Cuantificador universal: Todos los números son mayores que 0
cuantificador_universal_numeros = all(numero > 0 for numero in numeros)
print("¿Todos los números son mayores que 0?", cuantificador_universal_numeros)

# Cuantificador existencial: Al menos un número es par
cuantificador_existencial_numeros = any(numero % 2 == 0 for numero in numeros)
print("¿Al menos un número es par?", cuantificador_existencial_numeros)

# Cuantificador universal: Todos los estudiantes tienen un promedio mayor o igual a 80
cuantificador_universal_estudiantes = all(sum(calificaciones) / len(calificaciones) >= 80 for calificaciones in estudiantes.values())
print("¿Todos los estudiantes tienen un promedio mayor o igual a 80?", cuantificador_universal_estudiantes)

# Cuantificador existencial: Al menos un estudiante tiene una calificación menor a 70
cuantificador_existencial_estudiantes = any(min(calificaciones) < 70 for calificaciones in estudiantes.values())
print("¿Al menos un estudiante tiene una calificación menor a 70?", cuantificador_existencial_estudiantes)
