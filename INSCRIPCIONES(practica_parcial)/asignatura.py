from comision import Comision
from error import ComisionInexistenteError, ComisionExistenteError

class Asignatura():
    def __init__(self, nombre) -> None:
        self.nombre = nombre
        self.comisiones = []
        
    def AgregarComision(self, nombre: str, cupo = 10):
        comision = Comision(nombre, cupo)
        if comision not in self.comisiones:
            self.comisiones.append(comision)
        else:
            raise ComisionExistenteError
    
    def EliminarComision(self, nombre: str):
        self.comisiones.remove(self.Comision(nombre))
        
    def Comision(self, nombre: str):
        for com in self.comisiones:
            if com.nombre == nombre:
                return com
        else:
            raise ComisionInexistenteError