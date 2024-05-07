#Pablo Dario Jimenez Nu*o 21310143

class BaseConocimiento:
    def __init__(self):
        self.hechos = set()  # Inicializamos un conjunto para almacenar los hechos conocidos

    def agregar_hecho(self, hecho):
        self.hechos.add(hecho)  # Método para agregar un hecho a la base de conocimiento

    def verificar_hecho(self, hecho):
        return hecho in self.hechos  # Método para verificar si un hecho está en la base de conocimiento

class MotorInferencia:
    def __init__(self, base_conocimiento):
        self.base_conocimiento = base_conocimiento  # Inicializamos el motor de inferencia con una base de conocimiento dada

    def inferir(self, hecho):
        if self.base_conocimiento.verificar_hecho(hecho):
            return True  # Si el hecho está en la base de conocimiento, lo consideramos verdadero
        else:
            # Si el hecho no está en la base de conocimiento, asumimos que es verdadero por defecto
            return True

# Crear una base de conocimiento
base = BaseConocimiento()
base.agregar_hecho("pájaros_vuelan")  # Agregamos un hecho a la base de conocimiento

# Crear un motor de inferencia con la base de conocimiento
motor = MotorInferencia(base)

# Verificar si un hecho está en la base de conocimiento e inferir su verdad
print("¿Los pájaros vuelan?", motor.inferir("pájaros_vuelan"))  # Verificar si "pájaros_vuelan" es verdadero
print("¿Los peces vuelan?", motor.inferir("peces_vuelan"))  # Verificar si "peces_vuelan" es verdadero (por defecto)


















