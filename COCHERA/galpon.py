from movil import Movil

class Galpon:
    def __init__(self, id: int, ubi: str, capacidad: int, nombre: str) -> None:
        self.id = id
        self.ubi = ubi
        self.capacidad = capacidad #capacidad maxima
        self.nombre = nombre
        self.moviles = {} #key: patente, value: Movil
        
    def __eq__(self, value: object) -> bool:
        if isinstance(value,Galpon):
            return self.id == value.id
        else:
            return False
        
    def __str__(self) -> str:
        return f""" {self.nombre} id: {self.id}
    Ubicacion: {self.ubi}
    Cantidad de moviles: {len(self.moviles)}/{self.capacidad}
        """
        
    def AgregarMovil(self, patente: str, color: str, marca: str, modelo: str):
        if len(self.moviles) < self.capacidad:
            if patente not in self.moviles:
                movil = Movil(patente, color, marca, modelo)
                self.moviles[patente] = movil
                return movil
            else:
                return -2 #hay una patente igual
        return -1 #capacidad insuficiente
            
    def EliminarMovil(self, patente):
        if patente in self.moviles:
            self.moviles.pop(patente)
            return True
        else:
            return False #no se encontro
            
    def BuscarMovil(self, patente):
        if isinstance(patente,Movil):
            patente = patente.patente
        if isinstance(patente,str):
            if patente in self.moviles:
                return self.moviles[patente] #se encontro
            else:
                return False #no se encontro
        else:
            return patente #error de tipo de dato