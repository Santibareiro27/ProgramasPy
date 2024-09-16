from persona import Persona

class Movil:
    def __init__(self, patente: str, color: str, marca: str, modelo: str, duenio: Persona) -> None:
        self.patente = patente
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.duenio = duenio