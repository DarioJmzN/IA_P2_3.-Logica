#Pablo Dario Jimenez Nu*o 21310143
import re

class AnalizadorLexico:
    def __init__(self):
        self.expresiones = []  # Lista para almacenar las expresiones regulares y sus tipos asociados

    def agregar_token(self, patron, tipo):
        """
        Agrega un nuevo token con su patrón y tipo asociado a la lista de expresiones.
        :param patron: El patrón de expresión regular para reconocer el token.
        :param tipo: El tipo asociado al token.
        """
        self.expresiones.append((re.compile(patron), tipo))

    def analizar(self, texto):
        """
        Analiza el texto dado y devuelve una lista de tokens encontrados.
        :param texto: El texto a analizar.
        :return: Una lista de tuplas (tipo, valor) representando los tokens encontrados.
        """
        tokens = []  # Lista para almacenar los tokens encontrados
        while texto:
            texto = texto.strip()  # Elimina los espacios en blanco al principio y al final del texto
            emparejado = False  # Bandera para indicar si se ha emparejado un token
            for patron, tipo in self.expresiones:
                match = patron.match(texto)  # Intenta hacer coincidir el patrón con el inicio del texto
                if match:
                    valor = match.group(0)  # Obtiene el valor coincidente
                    tokens.append((tipo, valor))  # Agrega el token a la lista de tokens
                    texto = texto[len(valor):]  # Actualiza el texto restante para analizar
                    emparejado = True  # Indica que se ha emparejado un token
                    break
            if not emparejado:
                raise ValueError("Caracter no reconocido: {}".format(texto[0]))  # Si no se encuentra ninguna coincidencia, levanta un error
        return tokens  # Devuelve la lista de tokens encontrados

# Ejemplo de uso:
analizador = AnalizadorLexico()

# Agrega los tokens con sus patrones correspondientes
analizador.agregar_token(r'\d+', 'ENTERO')  # Reconoce números enteros
analizador.agregar_token(r'\+', 'SUMA')      # Reconoce el operador suma
analizador.agregar_token(r'-', 'RESTA')      # Reconoce el operador resta
analizador.agregar_token(r'\*', 'MULTIPLICACION')  # Reconoce el operador multiplicación
analizador.agregar_token(r'/', 'DIVISION')  # Reconoce el operador división
analizador.agregar_token(r'\s+', 'ESPACIO') # Reconoce espacios en blanco

texto = "3 + 4 * 5 - 6 / 2"
tokens = analizador.analizar(texto)
print(tokens)


