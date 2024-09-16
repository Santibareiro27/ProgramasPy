from movil import Movil

class Galpon:
    def __init__(self, id: int, ubi: str, capacidad: int, nombre: str) -> None:
        self.id = id
        self.ubi = ubi
        self.capacidad = capacidad
        self.nombre = nombre
        self.moviles = {}
        
    def AgregarMovil(self, movil: Movil):
        if len(self.moviles) < self.capacidad and movil.patente not in self.moviles:
            self.moviles[movil.patente] = movil
        else:
            print("Error: capacidad maxima de moviles alcanzada")
        
    def EliminarMovil(self, patente):
        self.moviles.pop(patente)