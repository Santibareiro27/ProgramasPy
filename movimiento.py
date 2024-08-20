import datetime as dt

class Movimiento:
    def __init__(self, monto: float, fechahora = dt.datetime.timestamp(), tipo = 'C') -> None:
        self.monto = monto
        self.fechahora = fechahora
        self.tipo = tipo
