from datetime import datetime

class Operacion():
    id = 1
    def __init__(self, descripcion:str, movil) -> None:
        self.id = Operacion.id
        Operacion.id += 1
        self.descripcion = descripcion
        self.fecha_hora = datetime.now()
        self.movil = movil