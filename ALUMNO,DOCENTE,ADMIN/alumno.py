from persona import Persona

class Alumno(Persona):
    def __init__(self, apellido: str, nombre: str, dni: str, legajo: str) -> None:
        super().__init__(apellido, nombre, dni)
        self.__legajo = legajo
        
    @property
    def legajo(self):
        return self.__legajo