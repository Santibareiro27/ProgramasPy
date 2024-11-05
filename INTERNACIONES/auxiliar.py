from personal import Personal
from datetime import datetime

class Auxiliar(Personal):
    def __init__(self, dni: int, apellido: str, nombres: str, nacimiento: datetime.date, descripcion: str) -> None:
        super().__init__(dni, apellido, nombres, nacimiento)
        self.descripcion = descripcion