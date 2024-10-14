class Deposito():
    def __init__(self, nombre: str, direccion: str) -> None:
        self.nombre = nombre
        self.direccion = direccion
        self.frutas = {} #key: nombre de fruta, value: cantidad de frutas
        self.descartes = {} #key: nombre de fruta, value: cantidad de frutas descartadas
        self.enuso = True
        
    def Total(self, fruta: str) -> int:
        return self.frutas[fruta]
        
    def TotalDescarte(self, fruta: str) -> int:
        return self.descartes[fruta]
    
    def Agregar(self, fruta: str, cantidad: int):
        if not self.Contiene(fruta):
            self.frutas[fruta] = 0
            self.descartes[fruta] = 0
        self.frutas[fruta] += cantidad
        
    def Extraer(self, fruta: str, cantidad: int):
        if self.Contiene(fruta):
            if self.frutas[fruta] >= cantidad:
                self.frutas[fruta] -= cantidad
                return True
        return False
                
    def DescartarFruta(self, fruta: str, cantidad: str):
        if self.Contiene(fruta):
            if self.frutas[fruta] >= cantidad:
                self.frutas[fruta] -= cantidad
                self.descartes[fruta] += cantidad
                
    def Contiene(self, fruta: str) -> bool:
        if fruta in self.frutas:
            return True
        return False