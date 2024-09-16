from docente import Docente
from administrativo import Administrativo
from alumno import Alumno
from comision import Comision

comisionx = Comision("F12","Fisica I","Comision 1","D1")
comisionx.NuevoDocente("Telleria","Juan", "responsable","12345678","123",150000)
comisionx.NuevoDocente("Molina","Jorge", "adjunto","12345670","124",100000)

comisionx.NuevoAlumno("Bareiro","Santiago Daniel","87654321","101")

comisionx.ListarIntegrantes()

legajoBuscado = input("\nIngrese el legajo del alumno que desea buscar: ")
comisionx.MostrarAlumno(legajoBuscado)

legajoBuscado = input("\nIngrese la matricula del docente que desea eliminar: ")

comisionx.EliminarDocente(legajoBuscado)

comisionx.ListarIntegrantes()