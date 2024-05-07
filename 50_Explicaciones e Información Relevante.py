#Pablo Dario Jimenez Nu*o 21310143
import numpy as np

class ExplicacionesInformacionRelevante:
    def __init__(self):
        self.explicacion = None

    def entrenar(self, X, y):
        n_muestras, n_caracteristicas = X.shape
        self.explicacion = [None] * n_caracteristicas  # Inicializar la explicación como una lista de None
        for i in range(n_caracteristicas):
            valores_unicos = np.unique(X[:, i])
            # Si solo hay un valor único en la característica, la explicación es ese valor
            if len(valores_unicos) == 1:
                self.explicacion[i] = valores_unicos[0]
            else:
                # Si hay más de un valor único, la explicación es la frecuencia de cada valor
                conteo_valores = np.bincount(X[:, i])
                self.explicacion[i] = {valor: conteo for valor, conteo in enumerate(conteo_valores) if conteo > 0}

    def predecir(self, X):
        return np.array([self.explicacion[i] for i in range(len(self.explicacion))])

# Ejemplo de uso:
# Datos de ejemplo
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])

# Construir y entrenar el modelo de Explicaciones e Información Relevante
expl_info_relevante = ExplicacionesInformacionRelevante()
expl_info_relevante.entrenar(X, y)
