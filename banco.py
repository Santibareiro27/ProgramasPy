from cuenta import Cuenta

class Banco:
    def __init__(self, name) -> None:
        self.name = name
        self.__cuentas = []
        
    def NuevaCuenta(self, cbu:str):
        if len(cbu) == 8 and cbu.isdigit():
            self.__cuentas[cbu] = Cuenta(cbu)
        else:
            raise ValueError()
        
    def CuentasSegunEstado(self):
        contador_AC = 0
        contador_DE = 0
        contador_CE = 0
        for cuenta in self.cuentas:
            match(cuenta.estado):
                case 'AC':
                    contador_AC += 1
                case 'DE':
                    contador_DE += 1
                case 'CE':
                    contador_CE += 1