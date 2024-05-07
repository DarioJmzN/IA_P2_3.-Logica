#Pablo Dario Jimenez Nu*o 21310143

import numpy as np

class NodoArbolDecision:
    def __init__(self, caracteristica=None, resultado=None):
        self.caracteristica = caracteristica  # Índice de la característica que se divide en este nodo
        self.resultado = resultado  # Resultado de la clasificación si es un nodo hoja
        self.hijos = {}  # Diccionario para almacenar los nodos hijos (valor_caracteristica: NodoArbolDecision)

class ID3ArbolDecision:
    def __init__(self):
        pass

    def calcular_entropia(self, y):
        clases, conteo_clases = np.unique(y, return_counts=True)
        probabilidad_clases = conteo_clases / len(y)
        entropia = -np.sum(probabilidad_clases * np.log2(probabilidad_clases))
        return entropia

    def encontrar_mejor_caracteristica(self, X, y):
        mejor_ganancia = 0
        mejor_caracteristica = None
        entropia_padre = self.calcular_entropia(y)

        for caracteristica in range(X.shape[1]):
            valores_caracteristica = np.unique(X[:, caracteristica])
            entropia_hijo = 0
            for valor in valores_caracteristica:
                y_subset = y[X[:, caracteristica] == valor]
                probabilidad_valor = len(y_subset) / len(y)
                entropia_hijo += probabilidad_valor * self.calcular_entropia(y_subset)
            ganancia_informacion = entropia_padre - entropia_hijo
            if ganancia_informacion > mejor_ganancia:
                mejor_ganancia = ganancia_informacion
                mejor_caracteristica = caracteristica
        return mejor_caracteristica

    def construir_arbol(self, X, y, caracteristicas):
        if len(np.unique(y)) == 1:
            return NodoArbolDecision(resultado=y[0])

        if len(caracteristicas) == 0:
            clase_mas_comun = np.argmax(np.bincount(y))
            return NodoArbolDecision(resultado=clase_mas_comun)

        mejor_caracteristica = self.encontrar_mejor_caracteristica(X, y)
        nodo = NodoArbolDecision(caracteristica=mejor_caracteristica)

        valores_caracteristica = np.unique(X[:, mejor_caracteristica])
        for valor in valores_caracteristica:
            indice_filas_con_valor = X[:, mejor_caracteristica] == valor
            X_subset = X[indice_filas_con_valor]
            y_subset = y[indice_filas_con_valor]
            sub_caracteristicas = caracteristicas[caracteristicas != mejor_caracteristica]
            nodo.hijos[valor] = self.construir_arbol(X_subset, y_subset, sub_caracteristicas)

        return nodo

    def entrenar(self, X, y):
        caracteristicas = np.arange(X.shape[1])
        self.raiz = self.construir_arbol(X, y, caracteristicas)

    def predecir_muestra(self, muestra, nodo=None):
        if nodo is None:
            nodo = self.raiz

        if nodo.resultado is not None:
            return nodo.resultado

        caracteristica_valor = muestra[nodo.caracteristica]
        if caracteristica_valor not in nodo.hijos:
            return np.argmax(np.bincount(y))
        else:
            nuevo_nodo = nodo.hijos[caracteristica_valor]
            return self.predecir_muestra(muestra, nuevo_nodo)

    def predecir(self, X):
        predicciones = []
        for muestra in X:
            predicciones.append(self.predecir_muestra(muestra))
        return np.array(predicciones)

# Ejemplo de uso:
# Datos de ejemplo
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([0, 0, 1, 1])

# Construir y entrenar el árbol de decisión ID3
id3_arbol = ID3ArbolDecision()
id3_arbol.entrenar(X, y)

# Realizar predicciones en nuevos datos
nuevos_datos = np.array([[0, 0], [1, 1], [1, 0]])
predicciones = id3_arbol.predecir(nuevos_datos)
print("Predicciones:", predicciones)
