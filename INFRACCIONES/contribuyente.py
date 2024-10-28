class Contribuyente():
    def __init__(self, documento:str, apellido:str, nombres:str, direccion:str, celular:str) -> None:
        self.documento = documento
        self.apellido = apellido
        self.nombres = nombres
        self.direccion = direccion
        self.celular = celular