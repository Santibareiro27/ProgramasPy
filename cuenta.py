import datetime as dt
from movimiento import Movimiento

class Cuenta:
    def __init__(self, cbu:str) -> None:
        self.cbu = cbu
        self.fechacreacion = dt.date.today()
        self.movimientos = []
        
    def nuevo_movimiento(self, monto:float):
        if isinstance(monto,float) and (monto < 1000000):
            self.movimientos.append(Movimiento(monto))
        else:
            raise ValueError()