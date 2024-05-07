#Pablo Dario Jimenez Nu*o 21310143

import numpy as np

# Clase para representar un nodo en la lista de decisión
class NodoListaDecision:
    def __init__(self, umbral=None, caracteristica=None, resultado=None):
        self.umbral = umbral  # Umbral de división para la característica
        self.caracteristica = caracteristica  # Índice de la característica que se divide en este nodo
        self.resultado = resultado  # Resultado de la clasificación si es un nodo hoja
        self.izquierda = None  # Subárbol para valores menores o iguales al umbral
        self.derecha = None  # Subárbol para valores mayores al umbral

# Clase para representar la lista de decisión K-DL
class ListaDecisionKD:
    def __init__(self, k=1):
        self.k = k  # Parámetro k para controlar la división mínima en cada nodo

    # Método para dividir un nodo basado en la ganancia de información
    def dividir_nodo(self, X, y):
        n_muestras, n_caracteristicas = X.shape
        mejor_ganancia = 0
        mejor_caracteristica = None
        mejor_umbral = None
        # Iterar sobre todas las características y umbrales posibles
        for caracteristica in range(n_caracteristicas):
            valores_unicos = np.unique(X[:, caracteristica])
            for umbral in valores_unicos:
                # Dividir los datos en izquierda y derecha según el umbral
                izquierda_indices = np.where(X[:, caracteristica] <= umbral)[0]
                derecha_indices = np.where(X[:, caracteristica] > umbral)[0]
                # Verificar si hay suficientes muestras en ambos lados para dividir
                if len(izquierda_indices) < self.k or len(derecha_indices) < self.k:
                    continue
                # Calcular la ganancia de información para esta división
                y_izquierda = y[izquierda_indices]
                y_derecha = y[derecha_indices]
                ganancia = self.calcular_ganancia_informacion(y, y_izquierda, y_derecha)
                # Actualizar la mejor ganancia si es mayor que la actual
                if ganancia > mejor_ganancia:
                    mejor_ganancia = ganancia
                    mejor_caracteristica = caracteristica
                    mejor_umbral = umbral
        return mejor_caracteristica, mejor_umbral

    # Método para calcular la ganancia de información
    def calcular_ganancia_informacion(self, y, y_izquierda, y_derecha):
        n = len(y)
        n_izquierda = len(y_izquierda)
        n_derecha = len(y_derecha)
        # Calcular la entropía del nodo padre
        entropia_padre = self.calcular_entropia(y)
        # Calcular la entropía de los nodos hijos
        entropia_hijo_izquierda = self.calcular_entropia(y_izquierda)
        entropia_hijo_derecha = self.calcular_entropia(y_derecha)
        # Calcular la ganancia de información
        ganancia = entropia_padre - (n_izquierda / n * entropia_hijo_izquierda + n_derecha / n * entropia_hijo_derecha)
        return ganancia

    # Método para calcular la entropía de un conjunto de etiquetas
    def calcular_entropia(self, y):
        _, conteo_clases = np.unique(y, return_counts=True)
        probabilidad_clases = conteo_clases / len(y)
        entropia = -np.sum(probabilidad_clases * np.log2(probabilidad_clases))
        return entropia

    # Método para construir el árbol de la lista de decisión
    def construir_arbol(self, X, y):
        # Caso base: si todas las etiquetas son iguales, devolver un nodo hoja con esa etiqueta
        if len(np.unique(y)) == 1:
            return NodoListaDecision(resultado=np.unique(y)[0])
        # Dividir el nodo en función de la mejor ganancia de información
        mejor_caracteristica, mejor_umbral = self.dividir_nodo(X, y)
        # Si no se puede realizar una división, devolver un nodo hoja con la clase mayoritaria
        if mejor_caracteristica is None:
            return NodoListaDecision(resultado=np.argmax(np.bincount(y)))
        # Crear un nodo con la característica y umbral óptimos
        nodo = NodoListaDecision(caracteristica=mejor_caracteristica, umbral=mejor_umbral)
        # Dividir los datos en función de la característica y umbral óptimos
        izquierda_indices = np.where(X[:, mejor_caracteristica] <= mejor_umbral)[0]
        derecha_indices = np.where(X[:, mejor_caracteristica] > mejor_umbral)[0]
        # Construir recursivamente los subárboles izquierdo y derecho
        nodo.izquierda = self.construir_arbol(X[izquierda_indices], y[izquierda_indices])
        nodo.derecha = self.construir_arbol(X[derecha_indices], y[derecha_indices])
        return nodo

    # Método para entrenar el modelo de lista de decisión
    def entrenar(self, X, y):
        self.raiz = self.construir_arbol(X, y)

    # Método auxiliar para predecir la clase de una muestra utilizando el árbol
    def predecir_muestra(self, muestra, nodo=None):
        if nodo is None:
            nodo = self.raiz
        # Si es un nodo hoja, devolver el resultado
        if nodo.resultado is not None:
            return nodo.resultado
        # Si la muestra pertenece al lado izquierdo del nodo, buscar en el subárbol izquierdo
        if muestra[nodo.caracteristica] <= nodo.umbral:
            return self.predecir_muestra(muestra, nodo.izquierda)
        # Si la muestra pertenece al lado derecho del nodo, buscar en el subárbol derecho
        else:
            return self.predecir_muestra(muestra, nodo.derecha)

    # Método para predecir las clases de un conjunto de muestras
    def predecir(self, X):
        return np.array([self.predecir_muestra(muestra) for muestra in X])

# Ejemplo de uso:
# Datos de ejemplo
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([0, 1, 1, 0])

# Construir y entrenar la lista de decisión K-DL
lista_decision_kd = ListaDecisionKD(k=1)
lista_decision_kd.entrenar(X, y)
