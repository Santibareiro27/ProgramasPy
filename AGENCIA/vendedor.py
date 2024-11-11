from persona import Persona
from operacion import Operacion

class Vendedor(Persona):
    id = 1
    def __init__(self, dni: int, apellido: str, nombres: str) -> None:
        super().__init__(dni, apellido, nombres)
        self.id = Vendedor.id
        Vendedor.id += 1
        self.operaciones = {} # key = id de operacion, value = Operacion
        
    def AgregarOperacion(self, descripcion:str, movil):
        operacion = Operacion(descripcion,movil)
        self.operaciones[operacion.id] = operacion
        
    def __eq__(self, value: object) -> bool:
        if isinstance(value,Vendedor):
            return self.id == value.id