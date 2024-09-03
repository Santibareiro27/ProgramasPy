from datetime import date

class Persona:
    '''
    tu vieja
    '''
    def __init__(self, apellido: str, nombre: str, nacimiento: date) -> None:
        self.__apellido = apellido
        self.__nombre = nombre
        self.__nacimiento = nacimiento
    
    @property #Decorador property (para lectura)
    def apellido(self):
        return self.__apellido
    
    @apellido.setter #Decorador setter (para escritura)
    def apellido(self,nuevo):
        self.__apellido = nuevo
    
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self,nuevo):
        self.__nombre = nuevo