from persona import Persona

class Empleado(Persona):
    def __init__(self, apellido: str, nombre: str, dni: str, matricula: str, sueldo: float) -> None:
        super().__init__(apellido, nombre, dni)
        self.__matricula = matricula
        self.sueldo = sueldo
        
    @property
    def matricula(self):
        return self.__matricula