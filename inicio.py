from movimiento import Movimiento
from persona import Persona
from cuenta import Cuenta
from banco import Banco
from datetime import date

def menu():
    print("""
          1. Aniadir movimiento
          S. Salir
          """)
    opc = input("Opcion: ")
    match(opc.upper()):
        case '1':
            pass
        case 's':
            return 0
    return 1

banco = Banco("Banco Macro")

nuevocbu = input("Ingrese cbu para la nueva cuenta: ")
banco.NuevaCuenta(nuevocbu)

while(menu()):
    pass

monto = input("Ingrese el monto de el movimiento")