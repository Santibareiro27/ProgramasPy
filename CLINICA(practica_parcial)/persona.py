class Persona():
    def __init__(self, documento: int, nombre: int, celular: int = None) -> None:
        self.documento = documento
        self.nombre = nombre
        self.celular = celular
        
class Paciente(Persona):
    def __init__(self, documento: int, nombre: int, celular: int = None) -> None:
        super().__init__(documento, nombre, celular)
        self.cantidad_turnos = 0
        
    def __eq__(self, value: object) -> bool:
        if isinstance(value, Paciente):
            return self.documento == value.documento
        return False
        
class Profesional(Persona):
    def __init__(self, documento: int, nombre: int, matricula: int, especialidad: str, celular: int = None) -> None:
        super().__init__(documento, nombre, celular)
        if not isinstance(matricula, int): raise TypeError
        if not isinstance(especialidad, str): raise TypeError
        self.matricula = matricula
        self.especialidad = especialidad
        
    def __eq__(self, value: object) -> bool:
        if isinstance(value, Profesional):
            return self.matricula == value.matricula
        return False
    
    def __hash__(self) -> int:
        return self.matricula