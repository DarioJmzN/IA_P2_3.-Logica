#Pablo Dario Jimenez Nu*o 21310143

import numpy as np

class NodoArbolRegresion:
    def __init__(self, caracteristica=None, umbral=None, valor=None):
        self.caracteristica = caracteristica  # Índice de la característica que se divide en este nodo
        self.umbral = umbral  # Umbral para dividir la característica
        self.valor = valor  # Valor de la predicción si es un nodo hoja
        self.izquierda = None  # Subárbol para valores menores o iguales al umbral
        self.derecha = None  # Subárbol para valores mayores al umbral

class M5ArbolRegresion:
    def __init__(self, max_profundidad=5, min_muestras_split=2):
        self.max_profundidad = max_profundidad
        self.min_muestras_split = min_muestras_split

    def calcular_error_promedio(self, y):
        return np.mean((y - np.mean(y))**2)

    def encontrar_mejor_division(self, X, y):
        mejor_error = float('inf')
        mejor_caracteristica, mejor_umbral = None, None
        for caracteristica in range(X.shape[1]):
            valores_unicos = np.unique(X[:, caracteristica])
            for umbral in valores_unicos:
                y_izquierda = y[X[:, caracteristica] <= umbral]
                y_derecha = y[X[:, caracteristica] > umbral]
                if len(y_izquierda) >= self.min_muestras_split and len(y_derecha) >= self.min_muestras_split:
                    error = self.calcular_error_promedio(y_izquierda) + self.calcular_error_promedio(y_derecha)
                    if error < mejor_error:
                        mejor_error = error
                        mejor_caracteristica = caracteristica
                        mejor_umbral = umbral
        return mejor_caracteristica, mejor_umbral

    def construir_arbol(self, X, y, profundidad=0):
        if profundidad >= self.max_profundidad or len(np.unique(y)) == 1:
            return NodoArbolRegresion(valor=np.mean(y))

        mejor_caracteristica, mejor_umbral = self.encontrar_mejor_division(X, y)
        if mejor_caracteristica is None:
            return NodoArbolRegresion(valor=np.mean(y))

        nodo = NodoArbolRegresion(caracteristica=mejor_caracteristica, umbral=mejor_umbral)
        X_izquierda, y_izquierda = X[X[:, mejor_caracteristica] <= mejor_umbral], y[X[:, mejor_caracteristica] <= mejor_umbral]
        X_derecha, y_derecha = X[X[:, mejor_caracteristica] > mejor_umbral], y[X[:, mejor_caracteristica] > mejor_umbral]

        nodo.izquierda = self.construir_arbol(X_izquierda, y_izquierda, profundidad + 1)
        nodo.derecha = self.construir_arbol(X_derecha, y_derecha, profundidad + 1)
        return nodo

    def entrenar(self, X, y):
        self.raiz = self.construir_arbol(X, y)

    def predecir_muestra(self, muestra, nodo=None):
        if nodo is None:
            nodo = self.raiz

        if nodo.valor is not None:
            return nodo.valor

        if muestra[nodo.caracteristica] <= nodo.umbral:
            return self.predecir_muestra(muestra, nodo.izquierda)
        else:
            return self.predecir_muestra(muestra, nodo.derecha)

    def predecir(self, X):
        predicciones = []
        for muestra in X:
            predicciones.append(self.predecir_muestra(muestra))
        return np.array(predicciones)

# Ejemplo de uso:
# Datos de ejemplo
X = np.array([[0], [1], [2], [3], [4], [5]])
y = np.array([1, 2, 3, 4, 5, 6])

# Construir y entrenar el árbol de regresión M5
m5_arbol = M5ArbolRegresion()
m5_arbol.entrenar(X, y)

# Realizar predicciones en nuevos datos
nuevos_datos = np.array([[1.5], [3.5]])
predicciones = m5_arbol.predecir(nuevos_datos)
print("Predicciones:", predicciones)

