from empleado import Empleado

class Tesorero(Empleado):
    def __init__(self, apellido, nombre, dni, sueldo) -> None:
        super().__init__(apellido, nombre, dni, sueldo)
        self.__fallos = 0