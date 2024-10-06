class Producto():
    def __init__(self, nombre: str, precio: float) -> None:
        self.nombre = nombre
        self.precio = precio
        
    def __str__(self) -> str:
        return f"Nombre del producto: {self.nombre}\nPrecio actual: {self.precio}"
    
    def __eq__(self, value: object) -> bool:
        if isinstance(value, Producto):
            return self.nombre == value.nombre
        return False