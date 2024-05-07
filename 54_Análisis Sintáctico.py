#Pablo Dario Jimenez Nu*o 21310143
class AnalizadorSintactico:
    def __init__(self, tokens):
        self.tokens = tokens
        self.posicion = 0

    def obtener_token_actual(self):
        """
        Retorna el token actual.
        """
        if self.posicion < len(self.tokens):
            return self.tokens[self.posicion]
        else:
            return None

    def avanzar(self):
        """
        Avanza a la siguiente posición de token.
        """
        self.posicion += 1

    def expresion(self):
        """
        Regla de producción para la expresión.
        """
        valor = self.termino()

        while self.obtener_token_actual() is not None and self.obtener_token_actual()[0] in ('SUMA', 'RESTA'):
            tipo, valor_operador = self.obtener_token_actual()
            self.avanzar()

            if tipo == 'SUMA':
                valor += self.termino()
            elif tipo == 'RESTA':
                valor -= self.termino()

        return valor

    def termino(self):
        """
        Regla de producción para el término.
        """
        valor = self.factor()

        while self.obtener_token_actual() is not None and self.obtener_token_actual()[0] in ('MULTIPLICACION', 'DIVISION'):
            tipo, valor_operador = self.obtener_token_actual()
            self.avanzar()

            if tipo == 'MULTIPLICACION':
                valor *= self.factor()
            elif tipo == 'DIVISION':
                valor /= self.factor()

        return valor

    def factor(self):
        """
        Regla de producción para el factor.
        """
        tipo, valor = self.obtener_token_actual()
        self.avanzar()

        if tipo == 'ENTERO':
            return int(valor)
        elif tipo == 'PARENTESIS_IZQUIERDO':
            resultado = self.expresion()
            if self.obtener_token_actual()[0] != 'PARENTESIS_DERECHO':
                raise SyntaxError("Se esperaba un paréntesis derecho")
            self.avanzar()
            return resultado
        else:
            raise SyntaxError("Factor inválido")

    def parse(self):
        """
        Inicia el análisis sintáctico.
        """
        resultado = self.expresion()
        if self.obtener_token_actual() is not None:
            raise SyntaxError("Token inesperado")
        return resultado

# Ejemplo de uso:
tokens = [('ENTERO', '3'), ('SUMA', '+'), ('ENTERO', '4'), ('MULTIPLICACION', '*'), ('ENTERO', '5'), ('RESTA', '-'), ('ENTERO', '6'), ('DIVISION', '/'), ('ENTERO', '2')]
parser = AnalizadorSintactico(tokens)
resultado = parser.parse()
print("Resultado:", resultado)


