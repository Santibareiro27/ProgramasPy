from datetime import datetime
from alumno import Alumno

class Inscripcion():
    def __init__(self, alumno: Alumno) -> None:
        self.alumno = alumno
        self.alta = datetime.now()
        self.baja = None
        
    def __eq__(self, __value: object) -> bool:
        if isinstance(__value, Inscripcion):
            return self.alumno == __value.alumno
        elif isinstance(__value, Alumno):
            return self.alumno == __value
        return False