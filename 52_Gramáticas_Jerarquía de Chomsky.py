#Pablo Dario Jimenez Nu*o 21310143
class GramaticaChomsky:
    def __init__(self):
        self.terminales = set()
        self.no_terminales = set()
        self.producciones = []

    def agregar_produccion(self, produccion):
        if len(produccion) == 2:
            izquierda, derecha = produccion
            if izquierda.isupper():
                self.no_terminales.add(izquierda)
            else:
                raise ValueError("El lado izquierdo de la producción debe ser un no-terminal.")
            if all(simbolo.isupper() for simbolo in derecha) or all(simbolo.islower() for simbolo in derecha):
                self.producciones.append(produccion)
                self.terminales.update(derecha)
            else:
                raise ValueError("El lado derecho de la producción debe contener solo terminales o no-terminales.")
        else:
            raise ValueError("La producción debe tener exactamente dos símbolos.")

    def es_regular(self):
        for izquierda, derecha in self.producciones:
            if len(derecha) == 1 and derecha[0].islower():
                continue
            elif len(derecha) == 2 and derecha[0].islower() and derecha[1].isupper():
                continue
            else:
                return False
        return True

# Ejemplo de uso:
gramatica = GramaticaChomsky()
gramatica.agregar_produccion(('S', 'AB'))
gramatica.agregar_produccion(('A', 'a'))
gramatica.agregar_produccion(('B', 'b'))
print("Es regular:", gramatica.es_regular())

