#Pablo Dario Jimenez Nu*o 21310143

import numpy as np

class FOIL:
    def __init__(self):
        self.regla = None

    def entrenar(self, X, y):
        n_muestras, n_caracteristicas = X.shape
        regla = []
        for i in range(n_caracteristicas):
            valores_unicos = np.unique(X[:, i])
            for valor in valores_unicos:
                positivos = np.sum(y[X[:, i] == valor])
                negativos = np.sum(~y[X[:, i] == valor])
                total_positivos = np.sum(y)
                total_negativos = n_muestras - total_positivos
                ganancia = (positivos / total_positivos) / (positivos / total_positivos + negativos / total_negativos)
                regla.append((i, valor, ganancia))
        mejor_regla = max(regla, key=lambda x: x[2])
        self.regla = mejor_regla

    def predecir_muestra(self, muestra):
        if self.regla[1] == muestra[self.regla[0]]:
            return 1
        else:
            return 0

    def predecir(self, X):
        return np.array([self.predecir_muestra(muestra) for muestra in X])

# Ejemplo de uso:
# Datos de ejemplo
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([0, 1, 1, 0])

# Construir y entrenar el modelo FOIL
foil = FOIL()
foil.entrenar(X, y)
