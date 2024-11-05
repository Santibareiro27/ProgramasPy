from datetime import datetime

class Persona():
    def __init__(self, dni: int, apellido: str, nombres: str, nacimiento: datetime) -> None:
        self.dni = dni
        self.apellido = apellido
        self.nombres = nombres
        self.nacimiento = nacimiento
        
    def edad(self):
        return datetime.now() - self.nacimiento
    
    def __eq__(self, value: object) -> bool:
        return self.dni == value.dni