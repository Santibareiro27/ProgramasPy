from tesorero import Tesorero
from banco import Banco
from noalphaerror import NoAlphaError
from nonumerror import NoNumError

t1 = Tesorero("Santiago","Daniel","12345678",108000)

print(t1)

ban = True

while ban:
    try:
        nombre = input("Nombre del banco: ")
        print(type(nombre))
        if nombre.isalpha():
            banco = Banco(nombre)
            ban = False
        else:
            raise NoAlphaError("El nombre debe ser alfabetico")
    except NoAlphaError as err:
        print(err)

nombre = input("Ingrese el nombre: ")
apellido = input("Ingrese el apellido: ")
try:
    dni = input("Ingrese el dni: ")
    if isinstance(dni,int) or (isinstance(dni,str) and dni.isnumeric()):
        dni = int(dni)
    else:
        raise NoNumError
    saldo = input("Ingrese el saldo: ")
    if isinstance(saldo, float):
        banco.NuevoEmpleado(apellido,nombre,dni,saldo)
    else:
        raise Exception
except NoNumError:
    print("El dni ingresado no es valido")
except Exception:
    print("El saldo ingresado no es valido")