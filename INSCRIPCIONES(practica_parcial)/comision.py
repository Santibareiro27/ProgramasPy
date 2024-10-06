from error import ComisionLlenaError, AlumnoInscriptoError, InscripcionInexistenteError
from inscripcion import Inscripcion

class Comision():
    def __init__(self, nombre: str, cupo: int) -> None:
        self.nombre = nombre
        self.cupo = cupo
        self.inscripciones = []
        
    def Agregar(self, alumno):
        if len(self.Alumnos_activos()) >= self.cupo:
            raise ComisionLlenaError
        if alumno not in self.inscripciones:
            self.inscripciones.append(Inscripcion(alumno))
        else:
            raise AlumnoInscriptoError
        
    def Eliminar(self, alumno):
        if alumno in self.Alumnos_activos():
            self.inscripciones.remove(alumno)
        else:
            raise InscripcionInexistenteError
        
    def Alumnos_activos(self):
        return [ins.alumno for ins in self.inscripciones if ins.baja == None]
    
    def __eq__(self, value: object) -> bool:
        if isinstance(value,Comision):
            return self.nombre == value.nombre
        else:
            return False