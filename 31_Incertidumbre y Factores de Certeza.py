#Pablo Dario Jimenez Nu*o 21310143

class Hecho:
    def __init__(self, nombre, certeza):
        self.nombre = nombre
        self.certeza = certeza  # Certidumbre del hecho (un valor entre 0 y 1)

class BaseConocimiento:
    def __init__(self):
        self.hechos = {}

    def agregar_hecho(self, hecho):
        self.hechos[hecho.nombre] = hecho

class MotorInferencia:
    def __init__(self, base_conocimiento):
        self.base_conocimiento = base_conocimiento

    def obtener_certeza_hecho(self, nombre_hecho):
        if nombre_hecho in self.base_conocimiento.hechos:
            return self.base_conocimiento.hechos[nombre_hecho].certeza
        else:
            return None  # Retornar None si el hecho no está en la base de conocimiento

# Crear una base de conocimiento
base = BaseConocimiento()
base.agregar_hecho(Hecho("pájaros_vuelan", 0.8))  # Agregamos un hecho con certeza del 80%
base.agregar_hecho(Hecho("peces_vuelan", 0.2))  # Agregamos otro hecho con certeza del 20%

# Crear un motor de inferencia con la base de conocimiento
motor = MotorInferencia(base)

# Obtener la certeza de un hecho
certeza_pajaros_vuelan = motor.obtener_certeza_hecho("pájaros_vuelan")
certeza_peces_vuelan = motor.obtener_certeza_hecho("peces_vuelan")

print("Certeza de que los pájaros vuelan:", certeza_pajaros_vuelan)
print("Certeza de que los peces vuelan:", certeza_peces_vuelan)



















