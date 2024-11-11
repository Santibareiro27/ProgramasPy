from persona import Persona

class Responsable(Persona):
    def __init__(self, dni:int, apellido:str, nombres:str) -> None:
        super().__init__(dni, apellido, nombres)