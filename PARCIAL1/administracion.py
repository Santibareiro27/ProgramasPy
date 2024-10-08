from excepciones import ProductoNoEncontradoError, LocalidadDuplicadaError, LocalidadNoEncontradaError
from producto import Producto
from localidad import Localidad

class Administracion():
    def __init__(self) -> None:
        self.productos = {} #key: id de producto, value: producto
        
    def agregarProducto(self, descripcion: str):
        producto = Producto(descripcion) #primero crea el producto para que genere la id
        self.productos[producto.id] = producto
        
    def agregarLocalidad(self, id: int, deposito: str, isla: str, modulo: int, lado: str, estante: int, cantidad: int = 0):
        if id not in self.productos:
            raise ProductoNoEncontradoError
        localidad = Localidad(deposito, isla, modulo, lado, estante, cantidad)
        if self.productos[id].poseeLocalidad(localidad) == False: #se uso el metodo de Producto anteriormente creado
            self.productos[id].localidades.append(localidad)
        else:
            raise LocalidadDuplicadaError
        
    def cargarStock(self, id: int, stock_a_sumar: int, deposito: str, isla: str, modulo: int, lado: str, estante: int):
        if id not in self.productos:
            raise ProductoNoEncontradoError
        localidad = Localidad(deposito, isla, modulo, lado, estante)
        for loc in self.productos[id].localidades:
            if loc == localidad:
                loc.cantidad += stock_a_sumar
                break #si ubo coincidencia se ejecuta el break
        else: #si el bucle no encuentra break, finaliza de manera normal y se levanta el error
            raise LocalidadNoEncontradaError
        
    def stock(self, id: int):
        if id not in self.productos:
            raise ProductoNoEncontradoError
        return self.productos[id].stock()