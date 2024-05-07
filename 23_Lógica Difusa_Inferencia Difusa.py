#Pablo Dario Jimenez Nu*o 21310143

import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Definir las variables de entrada y salida difusas
calidad_comida = ctrl.Antecedent(np.arange(0, 11, 1), 'calidad_comida')
servicio = ctrl.Antecedent(np.arange(0, 11, 1), 'servicio')
propina = ctrl.Consequent(np.arange(0, 26, 1), 'propina')

# Definir las funciones de membresía para cada variable
calidad_comida.automf(3)  # Definir automáticamente 3 funciones de membresía para la calidad de la comida
servicio.automf(3)  # Definir automáticamente 3 funciones de membresía para el servicio
propina['baja'] = fuzz.trimf(propina.universe, [0, 0, 13])  # Función de membresía triangular para propina baja
propina['media'] = fuzz.trimf(propina.universe, [0, 13, 25])  # Función de membresía triangular para propina media
propina['alta'] = fuzz.trimf(propina.universe, [13, 25, 25])  # Función de membresía triangular para propina alta

# Visualización de las funciones de membresía
calidad_comida.view()
servicio.view()
propina.view()

# Definir reglas difusas
regla1 = ctrl.Rule(calidad_comida['poor'] | servicio['poor'], propina['baja'])
regla2 = ctrl.Rule(servicio['average'], propina['media'])
regla3 = ctrl.Rule(servicio['good'] | calidad_comida['good'], propina['alta'])

# Crear el sistema de control difuso
sistema_control = ctrl.ControlSystem([regla1, regla2, regla3])
sistema = ctrl.ControlSystemSimulation(sistema_control)

# Asignar valores de entrada al sistema de control difuso
sistema.input['calidad_comida'] = 6.5
sistema.input['servicio'] = 9.8

# Evaluar el sistema de control difuso
sistema.compute()

# Obtener el resultado de la propina
print("Propina sugerida:", sistema.output['propina'])















