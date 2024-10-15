from pedido import Pedido
from producto import Producto

class Administracion():
    def __init__(self) -> None:
        self.pedidos = {} #key: id pedido, value: instancias de Pedido
        self.productos = {} #key: id producto, value: instancias de Producto
        
    def Crear_pedido(self):
        pedido = Pedido()
        self.pedidos[pedido.id] = pedido
        
    def Agregar_producto(self, descripcion: str):
        producto = Producto(descripcion)
        self.productos[producto.id] = producto
        
    def Agregar_producto_al_pedido(self, pedido_id: int, producto_id: int, cantidad: int):
        pedido = self.pedidos[pedido_id]
        if cantidad > 0 and producto_id in self.productos:
            for detalle in pedido.detalles:
                if detalle.producto_id == producto_id:
                    detalle.cantidad += cantidad
            else:
                pedido.Agregar_producto(producto_id, cantidad)
                
    def Productos_de_pedido(self, pedido_id) -> list:
        return [detalle.producto_id for detalle in self.pedidos[pedido_id].detalles]
    
    def Productos_pedidos(self) -> dict:
        productos_pedidos = {}
        for producto_id in self.productos:
            productos_pedidos[producto_id] = 0
        for key in self.pedidos:
            for detalle in self.pedidos[key].detalles:
                productos_pedidos[detalle.producto_id] += detalle.cantidad
        return productos_pedidos

if __name__ == "__main__":
    admin = Administracion()
    admin.Agregar_producto("teclado")
    admin.Agregar_producto("mouse")
    admin.Agregar_producto("auricular")
    admin.Agregar_producto("monitor")
    admin.Crear_pedido() #pedido 1
    admin.Crear_pedido() #pedido 2
    
    admin.Agregar_producto_al_pedido(1,1,3) #agrega al pedido 1 3 teclados
    admin.Agregar_producto_al_pedido(1,2,2) #agrega al pedido 1 2 mouses
    admin.Agregar_producto_al_pedido(2,2,3) #agrega al pedido 2 3 mouses
    admin.Agregar_producto_al_pedido(2,3,1) #agrega al pedido 2 1 auricular
    
    print(admin.Productos_de_pedido(1))
    print(admin.Productos_de_pedido(2))
    
    producto_cantidad = admin.Productos_pedidos()
    print(producto_cantidad)