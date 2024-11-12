class Pallet():
    id = 1
    def __init__(self) -> None:
        self.id = Pallet.id
        Pallet.id += 1
        self.productos = {}
        self.capacidad = 20
        self.utilizado = 0