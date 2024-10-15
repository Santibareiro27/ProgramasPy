from detalle import Detalle

class Pedido():
    id = 1
    def __init__(self) -> None:
        self.id = Pedido.id
        Pedido.id += 1
        self.detalles = []
        
    def Agregar_producto(self, producto_id: int, cantidad: int):
        self.detalles.append(Detalle(producto_id, cantidad))