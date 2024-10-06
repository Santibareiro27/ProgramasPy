from datetime import datetime

class Turno():
    def __init__(self, paciente, profesional, diahora) -> None:
        self.paciente = paciente
        self.profesional = profesional
        self.diahora = diahora
        
    def __eq__(self, value: object) -> bool:
        if isinstance(value, Turno):
            return self.diahora == value.diahora
        return False