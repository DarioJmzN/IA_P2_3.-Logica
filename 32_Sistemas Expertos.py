#Pablo Dario Jimenez Nu*o 21310143

class Regla:
    def __init__(self, antecedentes, consecuente):
        self.antecedentes = antecedentes  # Lista de antecedentes de la regla
        self.consecuente = consecuente    # Consecuente de la regla

class MotorInferencia:
    def __init__(self, base_reglas):
        self.base_reglas = base_reglas  # Base de reglas del motor

    def inferir(self, hechos):
        # Iterar sobre cada regla en la base de reglas
        for regla in self.base_reglas:
            # Verificar si todos los antecedentes de la regla están presentes en los hechos observados
            antecedentes_verdaderos = all(hecho in hechos for hecho in regla.antecedentes)
            if antecedentes_verdaderos:
                return regla.consecuente  # Si se cumplen los antecedentes, devolver el consecuente
        return None  # Si no se pudo inferir ningún consecuente, devolver None

# Definir la base de reglas
base_reglas = [
    Regla(["tiene_plumas", "pone_huevos"], "es_un_ave"),          # Regla 1: si tiene plumas y pone huevos, es un ave
    Regla(["tiene_patas", "no_vuela"], "es_un_mamifero"),         # Regla 2: si tiene patas y no vuela, es un mamífero
    Regla(["tiene_alas", "pone_huevos"], "es_un_ave"),            # Regla 3: si tiene alas y pone huevos, es un ave
    Regla(["tiene_plumas", "vuela"], "es_un_ave"),                # Regla 4: si tiene plumas y vuela, es un ave
]

# Crear el motor de inferencia con la base de reglas
motor = MotorInferencia(base_reglas)

# Definir los hechos observados
hechos_observados = ["tiene_plumas", "pone_huevos"]  # Ejemplo de hechos observados

# Inferir el tipo de animal
tipo_animal = motor.inferir(hechos_observados)

# Imprimir el resultado
if tipo_animal:
    print("El animal es:", tipo_animal)  # Imprimir el tipo de animal inferido
else:
    print("No se puede determinar el tipo de animal.")  # Imprimir un mensaje si no se puede inferir ningún tipo


















