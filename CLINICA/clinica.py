from persona import Paciente, Profesional
from turno import Turno
from datetime import datetime, date

class Clinica():
    def __init__(self, nombre: str) -> None:
        self.nombre = nombre
        self.pacientes = {} #key: documento
        self.profesionales = {} #key: matricula
        self.turnos = {} #key: profesional, value: diccionario de dias de turnos -> (key: date, value: lista de turnos en un dia)
        
    def AgregarPaciente(self, documento: int, nombre: str, celular: int = None):
        if documento not in self.pacientes:
            self.pacientes[documento] = Paciente(documento, nombre, celular)
        
    def AgregarProfesional(self, documento: int, nombre: str, matricula: int, especialidad: str, celular: int = None):
        if matricula not in self.profesionales:
            self.profesionales[matricula] = Profesional(documento, nombre, matricula, especialidad, celular)
        
    def BuscarPaciente(self, dni: int):
        if dni in self.pacientes:
            return self.pacientes[dni]
        return None
        
    def BuscarProfesional(self, matricula: int):
        if matricula in self.profesionales:
            return self.profesionales[matricula]
        return None
    
    def AsignarTurno(self, dni: int, mat: int, dia, mes, año, hora, minuto):
        paci = self.BuscarPaciente(dni)
        prof = self.BuscarProfesional(mat)
        if not isinstance(paci,Paciente):
            raise ValueError("No se encontro el paciente")
        if not isinstance(prof,Profesional):
            raise ValueError("No se encontro el profesional")

        diaturno = date(año, mes, dia) #key para el diccionario de un profesional
        diahoraturno = datetime(año, mes, dia, hora, minuto) #horario para el turno
        
        if prof not in self.turnos: #si hay un nuevo profesional crea su diccionario
            self.turnos[prof] = {}
        if diaturno not in self.turnos[prof]: #si ese dia no tiene turnos, crea la lista de turnos de ese dia
            self.turnos[prof][diaturno] = []
        turnosdia = self.turnos[prof][diaturno]
        turno = Turno(paci,prof,diahoraturno)
        if turno not in turnosdia:
            turnosdia.append(turno)
            paci.cantidad_turnos += 1
        else:
            raise TypeError("Turno ocupado")
            
    def PacientesDeUnaFechaParaUnProfesional(self, fecha: datetime, prof: Profesional):
        return [t.paciente for t in self.turnos[prof][fecha.date()]]
    
    def TurnoDeUnPacienteEnUnaFechaParaUnProfesional(self, paci: Paciente, fecha: datetime, prof: Profesional):
        return [t.diahora for t in self.turnos[prof][fecha.date()] if t.paciente == paci]