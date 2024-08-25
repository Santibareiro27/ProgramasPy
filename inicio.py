from movimiento import Movimiento
from cuenta import Cuenta
from banco import Banco
from datetime import date

def menu():
    print('''
          MENU
          1) Nuevo Movimiento
          2) Ver CBU
          ''')

banco1 = Banco('BancoMacro')
banco1.NuevaCuenta('12345678')
banco1.cuentas[0].nuevo_movimiento(-12034.5)
print(banco1.cuentas[0].movimientos[0].monto)