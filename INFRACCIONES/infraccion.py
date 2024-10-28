class Infraccion():
    id = 1
    def __init__(self, descripcion:str, movil) -> None:
        self.id = Infraccion.id
        self.descripcion = descripcion
        self.movil = movil
        Infraccion.id += 1