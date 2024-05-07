#Pablo Dario Jimenez Nu*o 21310143
import numpy as np

class EspacioVersionesAQ:
    def __init__(self):
        self.version = None

    def entrenar(self, X, y):
        n_muestras, n_caracteristicas = X.shape
        self.version = [None] * n_caracteristicas  # Inicializar la versión como una lista de None
        for i in range(n_caracteristicas):
            valores_unicos = np.unique(X[:, i])
            # Si solo hay un valor único en la característica, la versión es ese valor
            if len(valores_unicos) == 1:
                self.version[i] = valores_unicos[0]
            else:
                # Si hay más de un valor único, la versión es '?'
                self.version[i] = '?'

    def predecir(self, X):
        return np.array([self.version[i] for i in range(len(self.version))])

# Ejemplo de uso:
# Datos de ejemplo
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([0, 1, 1, 0])

# Construir y entrenar el Espacio de Versiones con AQ
espacio_versiones = EspacioVersionesAQ()
espacio_versiones.entrenar(X, y)