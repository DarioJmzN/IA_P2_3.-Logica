#Pablo Dario Jimenez Nu*o 21310143

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import numpy as np

# Generamos datos sintéticos.
np.random.seed(0)
X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)

# Dividimos los datos en conjuntos de entrenamiento y prueba.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entrenamos el modelo de regresión lineal.
model = LinearRegression()
model.fit(X_train, y_train)

# Hacemos predicciones en el conjunto de prueba.
y_pred = model.predict(X_test)

# Calculamos el error cuadrático medio.
mse = mean_squared_error(y_test, y_pred)

# Mostramos los resultados.
print("Modelo de regresión lineal entrenado y evaluado.")
print("Coeficientes del modelo:", model.coef_)
print("Intercepto del modelo:", model.intercept_)
print("Error cuadrático medio:", mse)



