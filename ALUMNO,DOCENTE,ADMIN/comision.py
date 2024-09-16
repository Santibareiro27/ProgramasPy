from alumno import Alumno
from docente import Docente

class Comision:
    def __init__(self, codigo: str, materia: str, nombre: str, aula: str) -> None:
        self.codigo = codigo
        self.materia = materia
        self.nombre = nombre
        self.aula = aula
        self.docentes = {}
        self.alumnos = {}
        
    def NuevoDocente(self, apellido: str, nombre: str, rol: str, dni: str, matricula: str, sueldo: float):
        self.docentes[matricula] = Docente(apellido.capitalize(), nombre.capitalize(), rol, dni, matricula, sueldo)
        
    def NuevoAlumno(self, apellido: str, nombre: str, dni: str, legajo: str):
        self.alumnos[legajo] = Alumno(apellido, nombre, dni, legajo)
    
    def EliminarDocente(self, matricula:str):
        if matricula in self.docentes:
            self.docentes.pop(matricula)
        else:
            print(f"ERROR: No se encontro el docente con matricula: {matricula}")
    
    def EliminarAlumno(self, legajo:str):
        if legajo in self.alumnos:
            self.alumnos.pop(legajo)
        else:
            print(f"ERROR: No se encontro el alumno con nro de legajo: {legajo}")
    
    def ListarIntegrantes(self):
        print("\nDocentes:")
        for doce in self.docentes.values():
            print(f"{doce.apellido} {doce.nombre}, matricula: {doce.matricula}, rol: {doce.rol}")
        print("Alumnos:")
        for alu in self.alumnos.values():
            print(f"{alu.apellido} {alu.nombre}, nro de legajo: {alu.legajo}")
            
    def MostrarAlumno(self, legajo:str):
        if legajo in self.alumnos:
            print(f"Alumno encontrado: {self.alumnos[legajo].apellido} {self.alumnos[legajo].nombre}, dni: {self.alumnos[legajo].dni}")
        else:
            print(f"No se encontro el alumno con legajo {legajo}")