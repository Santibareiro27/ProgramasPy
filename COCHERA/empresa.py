from galpon import Galpon

class Empresa:
    def __init__(self, razonSocial: str) -> None:
        self.razonSocial = razonSocial
        self.galpones = {} #key: id,value: Galpon
    
    def AgregarGalpon(self, id: int, ubi: str, capacidad: int, nombre: str):
        self.galpones[id] = Galpon(id, ubi, capacidad, nombre)
        
    def EliminarGalpon(self, id: int):
        self.galpones.pop(id)