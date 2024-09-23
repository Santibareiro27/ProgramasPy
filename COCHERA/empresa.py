from galpon import Galpon

class Empresa:
    def __init__(self, razonSocial: str, cuit: str) -> None:
        self.razonSocial = razonSocial
        self.cuit = cuit
        self.galpones = {} #key: id,value: Galpon
        self.id_actaul = 1
    
    def AgregarGalpon(self, ubi: str, capacidad: int, nombre: str):
        self.galpones[self.id_actaul] = Galpon(self.id_actaul, ubi, capacidad, nombre)
        self.id_actaul += 1
        
    def EliminarGalpon(self, id: int):
        if id in self.galpones:
            self.galpones.pop(id)
            return True
        else:
            return False