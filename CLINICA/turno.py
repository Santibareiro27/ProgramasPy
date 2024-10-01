from persona import Paciente, Profesional
from datetime import datetime

class Turno():
    def __init__(self, paciente: Paciente, profesional: Profesional, diahora: datetime) -> None:
        self.paciente = paciente
        self.profesional = profesional
        self.diahora = diahora
        
    def __eq__(self, value) -> bool:
        return self.diahora == value.diahora