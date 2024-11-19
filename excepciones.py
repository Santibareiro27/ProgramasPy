class NumeroNegativoError(Exception):
    def __init__(self):
        super().__init__("El resultado no puede ser negativo")
        
class NumeroCeroError(Exception):
    def __init__(self):
        super().__init__("El resultado no puede ser 0")


a = input("Valor a: ")
b = input("Valor b: ")
try:
    c = int(a) + int(b)
    if c < 0: raise NumeroNegativoError
    if c == 0: raise NumeroCeroError
except NumeroNegativoError:
    raise NumeroNegativoError()
except NumeroCeroError:
    print("esto se imprime si el resultado es 0")
finally:
    print("esto se imprime siempre")