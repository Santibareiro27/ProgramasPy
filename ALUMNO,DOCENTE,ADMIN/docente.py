from empleado import Empleado

class Docente(Empleado):
    def __init__(self, apellido: str, nombre: str, titulo: str, dni: str, matricula: str, sueldo: float) -> None:
        super().__init__(apellido, nombre, dni, matricula, sueldo)
        self.titulo = titulo