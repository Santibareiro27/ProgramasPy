from detalle import Detalle

class Pedido():
    id = 1
    def __init__(self) -> None:
        self.id = Pedido.id
        Pedido.id += 1
        self.cargado = False
        self.detalles = []
        
    def AgregarProducto(self, producto, cantidad:int):
        detalle = self.BuscarProducto(producto.id)
        if detalle == None:
            self.detalles.append(Detalle(producto,cantidad))
        else:
            detalle.cantidad += cantidad
    
    def CantidadDePallets(self) -> int:
        pallets = 0
        for detalle in self.detalles:
            pallets += detalle.cantidad/20
        if pallets % 1 == 0:
            return int(pallets)
        else:
            return int(pallets) + 1
    
    def BuscarProducto(self, producto_id:int) -> Detalle|None:
        for detalle in self.detalles:
            if producto_id == detalle.producto.id:
                return detalle
        return None