from persona import Paciente, Profesional
from datetime import date, datetime
from turno import Turno

class Clinica():
    def __init__(self, nombre: str) -> None:
        self.nombre = nombre
        self.pacientes = {}
        self.profesionales = {}
        self.turnos = {}
        
    def AgregarPaciente(self, documento: int, nombre: str, celular: int = None):
        if documento not in self.pacientes:
            self.pacientes[documento] = Paciente(documento, nombre, celular)
    
    def AgregarProfesional(self, documento: int, nombre: str, matricula: int, especialidad: str, celular: int = None):
        if matricula not in self.profesionales:
            self.profesionales[matricula] = Profesional(documento, nombre, matricula, especialidad, celular)
    
    def BuscarPaciente(self, documento: int):
        if documento in self.pacientes:
            return self.pacientes[documento]
        else:
            return None
    
    def BuscarProfesional(self, matricula: int):
        if matricula in self.profesionales:
            return self.profesionales[matricula]
        else:
            return None
        
    def AsignarTurno(self, documento: int, matricula: int, dia: int, mes: int, año: int, hora: int, minuto: int):
        paciente = self.BuscarPaciente(documento)
        profesional = self.BuscarProfesional(matricula)
        if paciente == None or profesional == None:
            raise Exception
        if profesional not in self.turnos:
            self.turnos[profesional] = {}
        fecha = date(año, mes, dia)
        if fecha not in self.turnos[profesional]:
            self.turnos[profesional][fecha] = []
        turno = Turno(paciente,profesional,datetime(año, mes, dia, hora, minuto))
        if turno not in self.turnos[profesional][fecha]:
            self.turnos[profesional][fecha].append(turno)
            paciente.cantidad_turnos += 1
        else:
            raise Exception
        
    def PacientesDeUnaFechaParaUnProfesional(self, fecha: datetime, profesional: Profesional):
        return [turno.paciente for turno in self.turnos[profesional][fecha.date()]]
    
    def TurnoDeUnPacienteEnUnaFechaParaUnProfesional(self, paciente: Paciente, fecha: datetime, profesional: Profesional):
        return [turno.diahora for turno in self.turnos[profesional][fecha.date()] if turno.paciente == paciente]