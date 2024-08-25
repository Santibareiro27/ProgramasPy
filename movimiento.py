import datetime as dt

class Movimiento:
    def __init__(self, monto: float) -> None:
        self.monto = monto
        self.fechahora = dt.datetime.now()
