import datetime as dt
from movimiento import Movimiento

class Cuenta:
    def __init__(self, cbu:str, saldo) -> None:
        self.cbu = cbu
        self.__saldo = 0
        self.fechacreacion = dt.date.today()
        self.__movimientos = []
        self.cerrada = None
        self.estado = 'AC'
    
    def nuevo_movimiento(self, monto:float):
        if self.estado == 'AC' and self.__saldo + monto >= 0:
            self.__movimientos.append(Movimiento(monto))
            self.__saldo += monto
    
    @property
    def Saldo(self):
        return self.__saldo