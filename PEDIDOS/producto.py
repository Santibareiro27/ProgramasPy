class Producto():
    id = 1
    def __init__(self, descripcion: str) -> None:
        self.id = Producto.id
        Producto.id += 1
        self.descripcion = descripcion