class Persona():
    def __init__(self, documento: int, nombre: str, celular: int = None) -> None:
        self.documento = documento
        self.nombre = nombre
        self.celular = celular

class Paciente(Persona):
    def __init__(self, documento: int, nombre: str, celular: int = None) -> None:
        super().__init__(documento, nombre, celular)
        self.cantidad_turnos = 0
        
    def __eq__(self, value: object) -> bool:
        if isinstance(value, Paciente):
            return self.documento == value.documento
        return False

class Profesional(Persona):
    def __init__(self, documento: int, nombre: str, matricula: int, especialidad: str, celular: int = None) -> None:
        super().__init__(documento, nombre, celular)
        self.matricula = matricula
        self.especialidad = especialidad
        if not isinstance(matricula, int):
            raise TypeError("La matricula debe ser numerica entera")
        if not isinstance(especialidad, str):
            raise TypeError("La especialidad debe ser texto")
    
    def __eq__(self, value: object) -> bool:
        if isinstance(value, Profesional):
            return self.matricula == value.matricula
        return False
    
    def __hash__(self) -> int:
        return hash(self.matricula)