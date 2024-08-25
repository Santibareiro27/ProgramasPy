from cuenta import Cuenta

class Banco:
    def __init__(self, name) -> None:
        self.name = name
        self.cuentas = []
        
    def NuevaCuenta(self, cbu:str):
        if isinstance(cbu,str) and len(cbu) == 8 and cbu.isdigit():
            self.cuentas.append(Cuenta(cbu))
        else:
            raise ValueError()