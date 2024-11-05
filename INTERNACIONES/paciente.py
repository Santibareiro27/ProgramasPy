from persona import Persona
from datetime import datetime

class Paciente(Persona):
    id = 1
    def __init__(self, dni: int, apellido: str, nombres: str, nacimiento: datetime, obra_social: str) -> None:
        super().__init__(dni, apellido, nombres, nacimiento)
        self.id = Paciente.id
        self.obra_social = obra_social
        self.desde = datetime.now()
        Paciente.id += 1