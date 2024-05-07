#Pablo Dario Jimenez Nu*o 21310143

# Definición de una lista de números
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Cuantificador universal: Todos los números son mayores que 0
cuantificador_universal = all(numero > 0 for numero in numeros)
print("¿Todos los números son mayores que 0?", cuantificador_universal)

# Cuantificador existencial: Al menos un número es par
cuantificador_existencial = any(numero % 2 == 0 for numero in numeros)
print("¿Al menos un número es par?", cuantificador_existencial)

# Cuantificador universal modificado: Todos los números son menores que 20
cuantificador_universal_modificado = all(numero < 20 for numero in numeros)
print("¿Todos los números son menores que 20?", cuantificador_universal_modificado)

# Cuantificador existencial modificado: Al menos un número es mayor que 10
cuantificador_existencial_modificado = any(numero > 10 for numero in numeros)
print("¿Al menos un número es mayor que 10?", cuantificador_existencial_modificado)





