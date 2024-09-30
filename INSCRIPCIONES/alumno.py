class Alumno():
    def __init__(self, matricula: int) -> None:
        self.matricula = matricula
        
    def __eq__(self, __value: object) -> bool:
        if isinstance(__value, Alumno):
            return self.matricula == __value.matricula
        return False