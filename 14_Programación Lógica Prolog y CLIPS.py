#Pablo Dario Jimenez Nu*o 21310143

#PROLOG

from pyswip import Prolog

# Inicializar el intérprete de Prolog
prolog = Prolog()

# Definir hechos y reglas
prolog.assertz("padre(juan, maria)")
prolog.assertz("padre(pedro, juan)")

# Consultar relaciones
for solucion in prolog.query("padre(X, Y)"):
    print(f"{solucion['X']} es padre de {solucion['Y']}")

#CLIPS

import clips

# Crear un entorno CLIPS
env = clips.Environment()

# Cargar reglas y hechos
env.build("""
    (deffacts hechos-iniciales
        (padre juan maria)
        (padre pedro juan)
    )

    (defrule regla1
        (padre ?x ?y)
        =>
        (printout t ?x " es padre de " ?y crlf)
    )
""")

# Ejecutar el sistema experto
env.run()

# Cerrar el entorno CLIPS
env.reset()









