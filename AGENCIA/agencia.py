from sucursal import Sucursal
from responsable import Responsable
from vendedor import Vendedor

class Agencia():
    def __init__(self, nombre:str, cuit:str) -> None:
        self.nombre = nombre
        self.cuit = cuit
        self.sucursales = {} # key = nombre, value = Sucursal
        self.responsables = {} # key = dni, value = responsable
        self.vendedores = {} # key = dni, value = vendedor
        
    def NuevaSucursal(self, nombre:str, responsable:int):
        if nombre in self.sucursales:
            raise Exception()
        if responsable not in self.responsables:
            raise Exception()
        self.sucursales[nombre] = Sucursal(nombre)
        self.sucursales[nombre].AgregarResponsable(self.responsables[responsable])
        
    def NuevoResponsable(self, dni:int, apellido:str, nombres:str):
        if dni in self.responsables:
            raise Exception()
        self.responsables[dni] = Responsable(dni,apellido,nombres)
        
    def NuevoVendedor(self, dni:int, apellido:str, nombres:str):
        if dni in self.vendedores:
            raise Exception()
        self.vendedores[dni] = Vendedor(dni,apellido,nombres)
        
    def AgregarResponsableSucursal(self, responsable:int, sucursal:str):
        if sucursal not in self.sucursales:
            raise Exception()
        if responsable not in self.responsables:
            raise Exception()
        self.sucursales[sucursal].AgregarResponsable(self.responsables[responsable])
        
    def AgregarVendedorSucursal(self, vendedor:int, sucursal:str):
        if sucursal not in self.sucursales:
            raise Exception()
        if vendedor not in self.vendedores:
            raise Exception()
        self.sucursales[sucursal].AgregarVendedor(self.vendedores[vendedor])
        
    def Operaciones(self, sucursal:str = None, vendedor:int = None) -> list :
        lista = []
        if sucursal == None:
            for sucur in self.sucursales:
                lista += self.sucursales[sucur].Operaciones(vendedor)
        elif sucursal in self.sucursales:
                lista = self.sucursales[sucursal].Operaciones(vendedor)
        else:
            raise Exception()
        return lista
    
    def MovilesVendidos(self, sucursal:str = None) -> list:
        if sucursal not in self.sucursales:
            raise Exception()
        return [operacion.movil for operacion in self.Operaciones(sucursal)]