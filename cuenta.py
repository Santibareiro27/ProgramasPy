import datetime as dt
from movimiento import Movimiento

class Cuenta:
    def __init__(self, nro: int, fecha = dt.date.today()) -> None:
        self.nro = nro
        self.fecha = fecha
        self.movimientos = []
        
    def nuevo_movimiento(self, monto, tipo = 'C', fechahora = dt.datetime.timestamp()):
        if tipo in ('C','D','c','d'):
            m = Movimiento(monto, tipo, fechahora)
        