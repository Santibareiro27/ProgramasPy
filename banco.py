from cuenta import Cuenta
from cajero import Cajero
from gerente import Gerente
from tesorero import Tesorero

class Banco:
    def __init__(self, name) -> None:
        self.name = name
        self.__cuentas = {}
        self.__empleados = {}
        
    def NuevaCuenta(self, cbu:str):
        cuenta = Cuenta(cbu)
        self.__cuentas[cbu] = cuenta
        return cuenta
        
    def CuentasSegunEstado(self):
        contador = 0
        for cuenta in self.__cuentas.values():
            if cuenta.estado == 'AC':
                contador += 1
        return contador
    
    def NuevoEmpleado(self, apellido:str, nombre:str, dni:str, rol:str):
        match rol:
            case 'C':
                empleado = Cajero(apellido, nombre, dni, 1000)
                self.__empleados[dni] = empleado
                return empleado
            case 'G':
                empleado = Gerente(apellido, nombre, dni, 3000)
                self.__empleados[dni] = empleado
                return empleado
            case 'T':
                empleado = Tesorero(apellido, nombre, dni, 2000)
                self.__empleados[dni] = empleado
                return empleado
            case _:
                pass
            
    def BusarCuenta(self, cbu:str) -> Cuenta:
        if cbu in self.__cuentas:
            return self.__cuentas[cbu]