#Pablo Dario Jimenez Nu*o 21310143

import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Definir las variables de entrada y salida difusas
temperatura = ctrl.Antecedent(np.arange(0, 101, 1), 'temperatura')
velocidad = ctrl.Antecedent(np.arange(0, 101, 1), 'velocidad')
flujo_aire = ctrl.Consequent(np.arange(0, 101, 1), 'flujo_aire')

# Definir las funciones de membresía para cada variable
temperatura['fria'] = fuzz.trimf(temperatura.universe, [0, 0, 50])
temperatura['templada'] = fuzz.trimf(temperatura.universe, [25, 50, 75])
temperatura['calida'] = fuzz.trimf(temperatura.universe, [50, 100, 100])

velocidad['lenta'] = fuzz.trimf(velocidad.universe, [0, 0, 50])
velocidad['media'] = fuzz.trimf(velocidad.universe, [25, 50, 75])
velocidad['rapida'] = fuzz.trimf(velocidad.universe, [50, 100, 100])

flujo_aire['bajo'] = fuzz.trimf(flujo_aire.universe, [0, 0, 50])
flujo_aire['medio'] = fuzz.trimf(flujo_aire.universe, [25, 50, 75])
flujo_aire['alto'] = fuzz.trimf(flujo_aire.universe, [50, 100, 100])

# Definir reglas difusas
regla1 = ctrl.Rule(temperatura['fria'] & velocidad['lenta'], flujo_aire['bajo'])
regla2 = ctrl.Rule(temperatura['templada'] & velocidad['media'], flujo_aire['medio'])
regla3 = ctrl.Rule(temperatura['calida'] & velocidad['rapida'], flujo_aire['alto'])

# Crear el sistema de control difuso
sistema_control = ctrl.ControlSystem([regla1, regla2, regla3])
sistema = ctrl.ControlSystemSimulation(sistema_control)

# Asignar valores de entrada al sistema de control difuso
sistema.input['temperatura'] = 35
sistema.input['velocidad'] = 75

# Evaluar el sistema de control difuso
sistema.compute()

# Obtener el resultado
print("Flujo de aire:", sistema.output['flujo_aire'])














