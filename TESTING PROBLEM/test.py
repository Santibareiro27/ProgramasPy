import unittest
from Ejercicio import analizaString


class TestFuncion(unittest.TestCase):
    '''
    Un par de tests automáticos para auto-evaluar la implementación de la
    solución al problema planteado.
    Simplemente ejecutar (ambos .py deben estar en el mismo directorio)
    '''

    def test_ejemplo_consigna_1(self):
        entrada = "Hola, mi nombre es Ariel, soy una sirena, vivo bajo el mar"
        salida = "La letra que más se repite es la A con 6 repeticiones"
        self.assertEqual(analizaString(entrada), salida)
    
    def test_ejemplo_consigna_2(self):
        entrada = "Guau. Ojalá yo hablara cetáceo."
        salida = "La letra que más se repite es la A con 7 repeticiones"
        self.assertEqual(analizaString(entrada), salida)
    
    def test_ejemplo_consigna_3(self):
        entrada = "Construimos demasiados muros y no suficientes puentes (Isaac Newton)."
        salida = "La letra que más se repite es la S con 9 repeticiones"
        self.assertEqual(analizaString(entrada), salida)
    
    def test_ejemplo_consigna_4(self):
        entrada = "Es sencillo hacer que las cosas sean complicadas, pero es difícil hacer que sean sencillas (Friedrich Nietzsche)."
        salida = "La letra que más se repite es la E con 14 repeticiones"
        self.assertEqual(analizaString(entrada), salida)


if __name__ == '__main__':
    unittest.main()