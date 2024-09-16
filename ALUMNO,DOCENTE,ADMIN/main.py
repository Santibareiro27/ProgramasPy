from docente import Docente
from administrativo import Administrativo
from alumno import Alumno
from comision import Comision

comisionx = Comision("Fisica I","Comision 1","D1")
docente1 = Docente("Jorge","Telleria", "Ingeniero","12345678","123",100000)
comisionx.NuevoIntegrante(docente1)
alumno1 = Alumno("Bareiro","Santiago Daniel","87654321","101")
comisionx.NuevoIntegrante(alumno1)

comisionx.ListarIntegrantes()

legajoBuscado = input("\nIngrese el legajo del alumno que desea buscar: ")
alumnoBuscado = comisionx.BuscarIntegrante(legajoBuscado,'A')
if isinstance(alumnoBuscado,Alumno):
    print("Alumno encontrado: ",alumnoBuscado.apellido,alumnoBuscado.nombre,"dni:",alumnoBuscado.dni)
elif alumnoBuscado == 0:
    print("No se encontro el alumno buscado")

legajoBuscado = input("\nIngrese el legajo del alumno que desea eliminar: ")
match (comisionx.EliminarIntegrante(legajoBuscado,'A')):
    case 1:
        print("Eliminacion exitosa")
    case 0:
        print("No se encontro el alumno buscado")
    
comisionx.ListarIntegrantes()