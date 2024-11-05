from datetime import datetime
from paciente import Paciente
from profesional import Profesional
from auxiliar import Auxiliar
from descartable import Descartable
from internacion import Internacion
from datetime import *
from error import *

class Clinica():
    def __init__(self, nombre: str) -> None:
        self.nombre = nombre
        self.internaciones = {} #key = id de internacion, value = Internacion
        self.personal = {} #key = dni, value = Personal
        self.pacientes = {} #key = dni, value = Paciente
        self.descartables = {} #key = descripcion, value = Descartable
        
    def AgregarInternacion(self, paciente: int, solicitante: str, diagnostico: str):
        if paciente not in self.pacientes:
            raise PacienteInexistenteError
        if self.ExisteProfesional(solicitante) == False:
            raise ProfesionalInexistenteError
        paciente = self.pacientes[paciente]
        if paciente.id in self.internaciones:
            if self.internaciones[paciente.id].alta == None:
                raise PacienteInternadoError
        profesional = self.BuscarProfesional(solicitante)
        internacion = Internacion(paciente, profesional, diagnostico)
        self.internaciones[internacion.id] = internacion
        
    def AgregarPaciente(self, dni: int, apellido: str, nombres: str, nacimiento: datetime.date, obra_social: str):
        if dni in self.pacientes:
            raise PacienteExistenteError()
        else:
            paciente = Paciente(dni, apellido, nombres, nacimiento, obra_social)
            self.pacientes[paciente.dni] = paciente
            
    def AgregarDescartable(self, descripcion: str, precio_unitario: float, cantidad: int = 0):
        if descripcion in self.descartables:
            self.descartables[descripcion].precio = precio_unitario
            self.descartables[descripcion].cantidad = cantidad
        else:
            self.descartables[descripcion] = Descartable(descripcion, precio_unitario, cantidad)
            
    def AgregarPersonal(self, dni: int, apellido: str, nombres: str, nacimiento: datetime.date, **args):
        if args["dni"] in self.personal:
            raise PersonalExistenteError()
        if "matricula" and "especialidad" in args:
            self.personal[args["dni"]] = Profesional(dni, apellido, nombres, nacimiento, args["matricula"], args["especialidad"])
        elif "descripcion" in args:
            self.personal[args["dni"]] = Profesional(dni, apellido, nombres, nacimiento, args["descripcion"])
        else:
            raise ValueError()
        
    def ExisteProfesional(self, matricula: int) -> bool:
        for personal in self.personal.values():
            if isinstance(personal, Profesional):
                if matricula == personal.matricula:
                    return True
        return False
    
    def BuscarProfesional(self, matricula: int) -> bool:
        for personal in self.personal.values():
            if isinstance(personal, Profesional):
                if matricula == personal.matricula:
                    return personal
        return None
    
    def MesMasInternacionesAnio(self, año: int):
        InterMesMayor = 0
        MesMayor = 0
        for mes in range(1,13):
            InterMesActual = 0
            for internacion in self.internaciones.values():
                if internacion.fechahora.year == año and internacion.fechahora.month == mes:
                    InterMesActual += 1
            if InterMesActual > InterMesMayor:
                InterMesMayor = InterMesActual
                MesMayor = mes
        match MesMayor:
            case 1:
                MesMayor = "Enero"
            case 2:
                MesMayor = "Febrero"
            case 3:
                MesMayor = "Marzo"
            case 4:
                MesMayor = "Abril"
            case 5:
                MesMayor = "Mayo"
            case 6:
                MesMayor = "Junio"
            case 7:
                MesMayor = "Julio"
            case 8:
                MesMayor = "Agosto"
            case 9:
                MesMayor = "Septiembre"
            case 10:
                MesMayor = "Octubre"
            case 11:
                MesMayor = "Noviembre"
            case 12:
                MesMayor = "Diciembre"
        return MesMayor

    def InternacionConMasVisitas(self) -> list:
        lista = []
        vmax = 0
        for internacion in self.internaciones.values():
            if len(internacion.visitas) == vmax:
                lista.append(internacion)
            elif len(internacion.visitas) > vmax:
                vmax = len(internacion.visitas)
                lista.clear()
                lista.append(internacion)
        return lista

    def PersonalDeCumpleaniosEsteMes(self) -> list:
        mes_actual = datetime.now().month
        return[persona for persona in self.personal.values() if persona.nacimiento.month == mes_actual]

    def PacientesConMasDeXInternaciones(self, cantidad: int) -> list:
        lista = []
        for paciente in self.pacientes.values():
            internaciones_paciente = 0
            for internacion in self.internaciones.values():
                if internacion.paciente == paciente:
                    internaciones_paciente += 1
            if internaciones_paciente > cantidad:
                lista.append(paciente)
        return lista

    def VisitasPersonalFecha(self, personal: int, fecha: datetime.date) -> list:
        lista = []
        fecha = fecha.date()
        if personal not in self.personal:
            raise Exception()
        personal = self.personal[personal]
        for internacion in self.internaciones.values():
            for visita in internacion.visitas:
                if visita.personal.dni == personal.dni and visita.fechahora.date() == fecha:
                    lista.append(visita)
        return lista
                    
                    
if __name__ == "__main__":
    clinica = Clinica("La Clinica")
    