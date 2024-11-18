from pallet import Pallet

class Carga():
    id = 1
    def __init__(self, pedido:int) -> None:
        self.id = Carga.id
        Carga.id += 1
        self.capacidad = 20
        self.pedido = pedido #id del pedido
        self.pallets = {}
        
    def Productos(self) -> set:
        productos = set()
        for pallet in self.pallets.values():
            for producto in pallet.productos.values():
                productos.add(producto)
        return productos
    
    def AgregarProducto(self, producto:int, cantidad:int):
        pass
    
    def AgregarPallet(self, cantidad:int = 1):
        if len(self.pallets) + cantidad > self.capacidad:
            raise Exception()
        for i in range(cantidad):
            pallet = Pallet()
            self.pallets[pallet.id] = pallet