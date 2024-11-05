from personal import Personal
from datetime import datetime

class Profesional(Personal):
    def __init__(self, dni: int, apellido: str, nombres: str, nacimiento: datetime.date, matricula: str, especialidad: str) -> None:
        super().__init__(dni, apellido, nombres, nacimiento)
        self.matricula = matricula
        self.especialidad = especialidad