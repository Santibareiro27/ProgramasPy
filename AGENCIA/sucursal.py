from datetime import datetime
from movil import Movil

class Sucursal():
    def __init__(self, nombre:str) -> None:
        self.nombre = nombre
        self.responsables = {} # key = datetime.now(), value = responsable
        self.vendedores = {} # key = id de vendedor, value = vendedor
        self.moviles = {} # key = patente, value = movil
        
    def AgregarResponsable(self, responsable):
        self.responsables[datetime.now()] = responsable
        
    def AgregarVendedor(self, vendedor):
        self.vendedores[vendedor.id] = vendedor
        
    def AgregarOperacion(self, vendedor:int, descripcion:str, movil:str):
        if vendedor not in self.vendedores:
            raise Exception()
        self.vendedores[vendedor].AgregarOperacion(descripcion,self.moviles[movil])
        
    def ResponsableActual(self):
        return self.responsables[max(self.responsables)]
    
    def Operaciones(self, vendedor = None) -> list:
        if vendedor == None:
            return [operacion for ven in self.vendedores.values() for operacion in ven.operaciones.values()]
        elif vendedor in self.vendedores:
            return list(self.vendedores[vendedor.id].operaciones.values())
        else:
            raise Exception()
        
    def AgregarMovil(self, marca:str, color:str, modelo:str, año:int, patente:str):
        if patente not in self.moviles:
            self.moviles[patente] = Movil(marca, color, modelo, año, patente)
        else:
            raise Exception()