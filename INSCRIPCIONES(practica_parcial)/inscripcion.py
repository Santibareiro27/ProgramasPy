from alumno import Alumno
from datetime import datetime

class Inscripcion():
    def __init__(self, alumno: Alumno) -> None:
        self.alumno = alumno
        self.alta = datetime.now()
        self.baja = None
        
    def __eq__(self, value: object) -> bool:
        if isinstance(value,Inscripcion):
            return self.alumno == value.alumno
        elif isinstance(value,Alumno):
            return self.alumno == value
        else:
            return False