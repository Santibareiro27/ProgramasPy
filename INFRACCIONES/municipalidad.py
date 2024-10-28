from infraccion import Infraccion
from movil import Movil
from contribuyente import Contribuyente

class Municipalidad():
    def __init__(self, municipio:str) -> None:
        self.municipio = municipio
        self.infracciones = {}
        self.moviles = {}
        self.contribuyentes = {}
        
    def Registrar_infraccion(self, descripcion:str, patente:str):
        if patente in self.moviles:
            infraccion = Infraccion(descripcion,self.moviles[patente])
            self.infracciones[infraccion.id] = infraccion
            
    def Agregar_movil(self, patente:str, dni_titular:str):
        if patente not in self.moviles and dni_titular in self.contribuyentes:
            self.moviles[patente] = Movil(patente, self.contribuyentes[dni_titular])
            
    def Agregar_contribuyente(self, dni:str, apellido:str, nombres:str, direccion:str, celular:str):
        if dni not in self.contribuyentes:
            self.contribuyentes[dni] = Contribuyente(dni, apellido, nombres, direccion, celular)

    def Infracciones_de_contribuyente(self, dni:str) -> list:
        if dni in self.contribuyentes:
            return [infraccion for infraccion in self.infracciones.values() if infraccion.movil.Propietario().documento == dni]
        raise Exception("El contribuyente no existe")

    def Infracciones_de_movil(self, patente:str) -> list:
        if patente in self.moviles:
            return [infraccion for infraccion in self.infracciones.values() if infraccion.movil.patente == patente]
        raise Exception("El movil no existe")
        
    def Contribuyentes_sin_infracciones(self) -> list:
        return [con for con in self.contribuyentes.values() if self.Infracciones_de_contribuyente(con.documento) == []]



if __name__ == "__main__":
    muni = Municipalidad("Obera")
    
    muni.Agregar_contribuyente("12345678", "Bareiro", "Santiago Daniel", "Sarmiento 365", "3755-294382")
    muni.Agregar_movil("AA123BB", "12345678")
    muni.Agregar_movil("AA123CC", "12345678")
    muni.Registrar_infraccion("Alta velocidad","AA123BB")
    muni.Registrar_infraccion("Luz roja","AA123CC")
    
    for inf in  muni.Infracciones_de_contribuyente("12345678"):
        print(inf.descripcion)