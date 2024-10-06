from menu import Menu

class Sucursal():
    def __init__(self, ubicacion: str) -> None:
        self.ubicacion = ubicacion
        self.menu = Menu()
        
    def MostrarMenu(self):
        for prod in self.menu.productos:
            print(prod)