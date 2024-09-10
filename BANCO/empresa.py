from cliente import Cliente

class Empresa(Cliente):
    def __init__(self, cuit:str, razonSocial:str) -> None:
        super().__init__()
        self.cuit = cuit
        self.razonSocial = razonSocial