class Movil():
    def __init__(self, patente:str, titular) -> None:
        self.patente = patente
        self.titular = titular #debe ser de la instancia Contribuyente
        
    def Propietario(self):
        return self.titular