from persona import Persona
from datetime import datetime

class Personal(Persona):
    legajo = 1
    def __init__(self, dni: int, apellido: str, nombres: str, nacimiento: datetime.date) -> None:
        super().__init__(dni, apellido, nombres, nacimiento)
        self.legajo = Personal.legajo
        Personal.legajo += 1