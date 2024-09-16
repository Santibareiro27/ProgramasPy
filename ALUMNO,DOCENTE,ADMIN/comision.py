from alumno import Alumno
from docente import Docente

class Comision:
    def __init__(self, materia: str, nombre: str, aula: str) -> None:
        self.materia = materia
        self.nombre = nombre
        self.aula = aula
        self.docentes = {}
        self.alumnos = {}
    
    def NuevoIntegrante(self, integrante):
        value = 1
        if isinstance(integrante,Docente):
            self.docentes[integrante.matricula] = integrante
        elif isinstance(integrante,Alumno):
            self.alumnos[integrante.legajo] = integrante
        else:
            value = -1
            print(f"El valor {integrante} no es valido como argumento")
        return value
    
    def EliminarIntegrante(self, id:str, rol:str):
        value = 1
        if rol == 'D':
            if id in self.docentes:
                self.docentes.pop(id)
            else:
                value = 0
        elif rol == 'A':
            if id in self.alumnos:
                self.alumnos.pop(id)
            else:
                value = 0
        else:
            value = -1
            print(f"El valor {rol} no es valido como argumento")
        return value
    
    def ListarIntegrantes(self):
        print("\nDocentes:")
        for doce in self.docentes.values():
            print(f"{doce.titulo} {doce.apellido} {doce.nombre}, matricula: {doce.matricula}")
        print("Alumnos:")
        for alu in self.alumnos.values():
            print(f"{alu.apellido} {alu.nombre}, nro de legajo: {alu.legajo}")
            
    def BuscarIntegrante(self, id:str, rol:str):
        if rol == 'D':
            if id in self.docentes:
                return self.docentes[id]
        elif rol == 'A':
            if id in self.alumnos:
                return self.alumnos[id]
        else:
            print(f"El valor {rol} no es valido como argumento")
            return -1
        return 0