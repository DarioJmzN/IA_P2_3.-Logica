#Pablo Dario Jimenez Nu*o 21310143

class Robot:
    def __init__(self, nombre, posicion_actual, objetivo):
        self.nombre = nombre
        self.posicion_actual = posicion_actual
        self.objetivo = objetivo

    def mover(self, nueva_posicion):
        print(f"{self.nombre} se mueve de {self.posicion_actual} a {nueva_posicion}.")
        self.posicion_actual = nueva_posicion

class SistemaVigilancia:
    def __init__(self, robot):
        self.robot = robot

    def monitorear_ejecucion(self):
        print("Monitoreando ejecución...")
        if self.obstaculo_en_camino():
            print("¡Obstáculo encontrado!")
            self.replanificar_ruta()

    def obstaculo_en_camino(self):
        # Simulemos que el robot encuentra un obstáculo aleatoriamente
        import random
        return random.choice([True, False])

    def replanificar_ruta(self):
        # Simplemente movamos al robot a una posición aleatoria para evitar el obstáculo
        nueva_posicion = f"Posición aleatoria {random.randint(1, 10)}"
        print(f"Replanificando ruta para evitar el obstáculo. Nueva posición: {nueva_posicion}")
        self.robot.mover(nueva_posicion)


# Definir el robot y su objetivo
robot = Robot("Robot1", "Inicio", "Destino")

# Crear instancia del sistema de vigilancia
sistema_vigilancia = SistemaVigilancia(robot)

# Simular la ejecución del robot y monitorear continuamente
while robot.posicion_actual != robot.objetivo:
    sistema_vigilancia.monitorear_ejecucion()
    # Simulemos el movimiento del robot
    nueva_posicion = f"Posición aleatoria {random.randint(1, 10)}"
    robot.mover(nueva_posicion)

print("¡Objetivo alcanzado!")


