from empleado import Empleado

class Administrativo(Empleado):
    def __init__(self, apellido: str, nombre: str, dni: str, matricula: str, sueldo: float) -> None:
        super().__init__(apellido, nombre, dni, matricula, sueldo)