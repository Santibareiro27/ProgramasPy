from datetime import datetime
from personal import Personal

class Visita():
    id = 1
    def __init__(self, descripcion: str, personal: Personal, descartables: list) -> None:
        self.id = Visita.id
        self.descripcion = descripcion
        self.personal = personal
        self.descartables = descartables
        self.fechahora = datetime.now()
        Visita.id += 1