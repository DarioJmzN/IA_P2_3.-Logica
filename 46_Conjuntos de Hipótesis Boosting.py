#Pablo Dario Jimenez Nu*o 21310143

from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Generamos datos sintéticos
X, y = make_classification(n_samples=1000, n_features=20, n_classes=2, random_state=42)

# Dividimos los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Creamos un clasificador base (en este caso, un árbol de decisión)
base_clf = DecisionTreeClassifier(max_depth=1)

# Creamos el clasificador AdaBoost
adaboost_clf = AdaBoostClassifier(base_estimator=base_clf, n_estimators=50, random_state=42)

# Entrenamos el clasificador AdaBoost
adaboost_clf.fit(X_train, y_train)

# Realizamos predicciones en el conjunto de prueba
y_pred = adaboost_clf.predict(X_test)

# Calculamos la precisión del clasificador AdaBoost
accuracy = accuracy_score(y_test, y_pred)
print("Precisión del clasificador AdaBoost:", accuracy)
