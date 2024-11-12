class Producto():
    def __init__(self, id:int, descripcion:str, palletizado:int) -> None:
        self.id = id
        self.descripcion = descripcion
        self.palletizado = palletizado #Cuantas unidades puede contener un pallet