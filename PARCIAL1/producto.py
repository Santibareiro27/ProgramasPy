class Producto():
    id = 1
    def __init__(self, descripcion: str) -> None:
        self.id = Producto.id
        self.descripcion = descripcion
        self.localidades = []
        Producto.id += 1
        
    def stock(self):
        stock = 0
        for loc in self.localidades:
            stock += loc.cantidad
        return stock
    
    def poseeLocalidad(self, localidad):
        if localidad in self.localidades:
            return True
        else:
            return False