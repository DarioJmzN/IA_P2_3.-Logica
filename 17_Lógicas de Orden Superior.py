#Pablo Dario Jimenez Nu*o 21310143

# Función de orden superior que toma una función como argumento
def aplicar_funcion(funcion, valor):
    return funcion(valor)

# Funciones de orden superior
def duplicar(numero):
    return numero * 2

def triplicar(numero):
    return numero * 3

# Usando funciones de orden superior
resultado1 = aplicar_funcion(duplicar, 5)
print("Resultado de duplicar:", resultado1)

resultado2 = aplicar_funcion(triplicar, 7)
print("Resultado de triplicar:", resultado2)










