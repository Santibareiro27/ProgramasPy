from empleado import Empleado

class Tesorero(Empleado):
    def __init__(self, nombre, apellido, dni, saldo) -> None:
        super.__init__(self, nombre, apellido, dni, saldo)