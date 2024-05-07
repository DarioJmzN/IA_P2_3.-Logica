#Pablo Dario Jimenez Nu*o 21310143

class MejorHipotesisActual:
    def __init__(self):
        self.hipotesis = None

    def entrenar(self, X, y):
        n_muestras, n_caracteristicas = X.shape
        self.hipotesis = [None] * n_caracteristicas  # Inicializar la hipótesis como una lista de None
        for i in range(n_caracteristicas):
            valores_unicos = np.unique(X[:, i])
            # Si solo hay un valor único en la característica, la hipótesis es ese valor
            if len(valores_unicos) == 1:
                self.hipotesis[i] = valores_unicos[0]
            else:
                # Si hay más de un valor único, la hipótesis es el valor más frecuente en y para esa característica
                self.hipotesis[i] = np.bincount(y[np.where(X[:, i] == valores_unicos)].flatten()).argmax()

    def predecir(self, X):
        return np.array([self.hipotesis[i] for i in range(len(self.hipotesis))])

# Ejemplo de uso:
# Datos de ejemplo
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([0, 1, 1, 0])

# Construir y entrenar la Mejor Hipótesis Actual
mejor_hipotesis = MejorHipotesisActual()
mejor_hipotesis.entrenar(X, y)
