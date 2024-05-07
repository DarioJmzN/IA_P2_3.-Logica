#Pablo Dario Jimenez Nu*o 21310143

import random

# Función objetivo: ejemplo de función a optimizar (minimizar)
def funcion_objetivo(solucion):
    # En este ejemplo, la función objetivo es la suma de los elementos de la solución
    return sum(solucion)

# Generador de vecinos: perturba ligeramente la solución actual
def generar_vecino(solucion):
    # Selecciona un índice aleatorio para cambiar su valor
    indice = random.randint(0, len(solucion) - 1)
    # Genera una solución vecina perturbando ligeramente la solución actual
    vecino = list(solucion)
    vecino[indice] = 1 - vecino[indice]  # Cambia el valor en el índice seleccionado
    return vecino

# Algoritmo de Hill Climbing
def hill_climbing(funcion_objetivo, generar_vecino, longitud_solucion, iteraciones_maximas):
    # Genera una solución aleatoria como punto de partida
    solucion_actual = [random.randint(0, 1) for _ in range(longitud_solucion)]
    valor_actual = funcion_objetivo(solucion_actual)
    
    # Itera para mejorar la solución
    for _ in range(iteraciones_maximas):
        # Genera un vecino
        vecino = generar_vecino(solucion_actual)
        # Calcula el valor del vecino
        valor_vecino = funcion_objetivo(vecino)
        
        # Si el vecino es mejor que la solución actual, actualiza la solución actual
        if valor_vecino < valor_actual:
            solucion_actual = vecino
            valor_actual = valor_vecino
    
    # Devuelve la mejor solución encontrada
    return solucion_actual, valor_actual

# Parámetros del algoritmo
longitud_solucion = 10  # Longitud de la solución
iteraciones_maximas = 1000  # Número máximo de iteraciones

# Ejecución del algoritmo de Hill Climbing
solucion_optima, valor_optimo = hill_climbing(funcion_objetivo, generar_vecino, longitud_solucion, iteraciones_maximas)

# Mostrar la solución óptima
print("Solución óptima encontrada:", solucion_optima)
print("Valor óptimo encontrado:", valor_optimo)





