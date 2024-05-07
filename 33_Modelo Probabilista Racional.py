#Pablo Dario Jimenez Nu*o 21310143

from collections import defaultdict

class ModeloProbabilisticoRacional:
    def __init__(self):
        self.distribucion = defaultdict(float)  # Diccionario para almacenar la distribución de probabilidad

    def aprender(self, datos):
        total = len(datos)
        for dato in datos:
            self.distribucion[dato] += 1 / total  # Calcula la probabilidad de cada dato

    def predecir(self, dato):
        return self.distribucion[dato] if dato in self.distribucion else 0  # Devuelve la probabilidad del dato

# Crear un modelo probabilístico racional
modelo = ModeloProbabilisticoRacional()

# Datos de entrenamiento
datos_entrenamiento = ["A", "B", "A", "C", "A", "B", "C", "D", "B", "C"]

# Aprender del conjunto de datos de entrenamiento
modelo.aprender(datos_entrenamiento)

# Realizar predicciones
print("Predicción para el dato 'A':", modelo.predecir("A"))
print("Predicción para el dato 'E':", modelo.predecir("E"))



















