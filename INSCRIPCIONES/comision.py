from error import ComisionLlenaError, AlumnoInscriptoError, InscripcionInexistenteError
from inscripcion import Inscripcion
from alumno import Alumno
from datetime import datetime

class Comision():
    def __init__(self, nombre: str, cupo: int = 20) -> None:
        self.nombre = nombre
        self.cupo = cupo
        self.__inscripciones = []
        
    def Agregar(self, alumno: Alumno):
        if len(self.Alumnos_activos()) < self.cupo:
            inscripcion = Inscripcion(alumno)
            if inscripcion not in self.__inscripciones:
                self.__inscripciones.append(inscripcion)
            else:
                raise AlumnoInscriptoError
        else:
            raise ComisionLlenaError
        
    def Eliminar(self, alumno: Alumno):
        if alumno in self.Alumnos_activos():
            for inscripcion_alumno in self.__inscripciones:
                if inscripcion_alumno == alumno:
                    inscripcion_alumno.baja = datetime.now()
        else:
            raise InscripcionInexistenteError
        
    def Alumnos_activos(self):
        return [ins.alumno for ins in self.__inscripciones if ins.baja == None]
    
    def __eq__(self, __value: object) -> bool:
        if isinstance(__value, Comision):
            return self.nombre.lower() == __value.nombre
        elif isinstance(__value,str):
            return self.nombre.lower() == __value
        return False
    
    def __str__(self) -> str:
        return self.nombre.title()
    
    def __repr__(self) -> str:
        return self.nombre.upper()
    
if __name__ == "__main__":
    print(Alumno(123) == Alumno(123))