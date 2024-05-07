#Pablo Dario Jimenez Nu*o 21310143

import clips

# Crear un nuevo ambiente CLIPS
env = clips.Environment()

# Cargar la extensión FuzzyCLIPS
env.load("fuzzyclips")

# Definir las funciones de membresía
env.build("(deffuz-function triangular (parametros) (triangle (cadr parametros) (car parametros) (caddr parametros)))")

# Definir una variable difusa
env.build("(deffuzzy-variable x -10 10 (triangular -5 0 5))")

# Definir un conjunto difuso
env.build("(deffuzzy-set y x (triangular -8 -3 2))")

# Imprimir la definición del conjunto difuso
print(env.eval("(ppdefrule rule1)"))

# Cerrar el ambiente CLIPS
env.destroy()
















