class Alumno():
    def __init__(self, matricula: int) -> None:
        self.matricula = matricula
        
    def __eq__(self, value: object) -> bool:
        if isinstance(value,Alumno):
            return self.matricula == value.matricula
        else:
            return False