from error import ComisionInexistenteError, ComisionExistenteError
from comision import Comision

class Asignatura():
    def __init__(self, nombre) -> None:
       self.nombre = nombre
       self.__comisiones = []
       
    def AgregarComision(self, nombre, cupo = 10):
        comision = Comision(nombre, cupo)
        if comision not in self.__comisiones:
            self.__comisiones.append(comision)
        else:
            raise ComisionExistenteError
        
    def EliminarComision(self, nombre):
        if nombre in self.__comisiones:
            self.__comisiones.remove(nombre)
        else:
            raise ComisionInexistenteError
        
    def Comision(self, nombre):
        for com in self.__comisiones:
            if com == nombre:
                return com
        raise ComisionInexistenteError