from datetime import datetime

#id es una variable de clase, self.id es una variable de instancia

class Cliente:
    id = 1 #id autoincremental
    def __init__(self) -> None:
        self.id = Cliente.id
        Cliente.id += 1
        self.fechaDesde = datetime.now()