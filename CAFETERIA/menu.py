from producto import Producto

class Menu():
    def __init__(self) -> None:
        self.productos = []
        
    def AgregarProducto(self, nombre: str, precio: float):
        for prod in self.productos:
            if nombre == prod.nombre:
                return False
        self.productos.append(Producto(nombre, precio))
        return True