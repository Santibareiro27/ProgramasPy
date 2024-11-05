from datetime import datetime
from paciente import Paciente
from personal import Personal
from profesional import Profesional
from auxiliar import Auxiliar
from visita import Visita

class Internacion():
    id = 1
    def __init__(self, paciente: Paciente, solicitante: Profesional, diagnostico: str, ) -> None:
        self.fechahora = datetime.now()
        self.paciente = paciente
        self.solicitante = solicitante
        self.diagnostico = diagnostico
        self.visitas = []
        self.alta = None
        
    def ObraSocial(self) -> str:
        return self.paciente.obra_social
    
    def AgregarVisita(self, descripcion: str, personal: Personal, descartables: list = None):
        self.visitas.append(Visita(descripcion,personal,descartables))
        
    def CantidadDeVisitas(self):
        return len(self.visitas)
    
    def AuxiliaresAsistieron(self) -> set:
        return set([visita.personal for visita in self.visitas if isinstance(visita.personal,Auxiliar)])