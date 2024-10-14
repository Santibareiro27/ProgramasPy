from deposito import Deposito

class Administracion():
    def __init__(self) -> None:
        self.__depositos = {} #key: nombre de deposito, value: deposito
        
    def AgregarDeposito(self, nombre: str, direccion: str):
        self.__depositos[nombre] = Deposito(nombre, direccion)
    
    def DepositoEnUso(self) -> int:
        depositos_en_uso = 0
        for dep in self.__depositos.values():
            if dep.enuso == True:
                depositos_en_uso += 1
        return depositos_en_uso
    
    def Total(self, fruta: str) -> int:
        total = 0
        for dep in self.__depositos.values():
            if dep.Contiene(fruta):
                total += dep.Total[fruta]
        return total
    
    def TotalDeposito(self, fruta: str, deposito: str) -> int:
        if deposito in self.__depositos:
            return self.__depositos[deposito].Total(fruta)
        else:
            raise Exception("depósito inexistente")
        
    def TotalDescartes(self, fruta: str) -> int:
        total = 0
        for dep in self.__depositos.values():
            if dep.Contiene(fruta):
                total += dep.TotalDescarte[fruta]
        return total
    
    def TotalDeposito(self, fruta: str, deposito: str) -> int:
        if deposito in self.__depositos:
            return self.__depositos[deposito].TotalDescarte(fruta)
        else:
            return 0
    
    def MoverFrutas(self, fruta: str, cantidad: str, desde: str, hacia: str):
        if desde in self.__depositos and hacia in self.__depositos:
            desde = self.__depositos[desde]
            hacia = self.__depositos[hacia]
            if desde.Extraer(fruta,cantidad):
                hacia.Agregar(fruta,cantidad)
        else:
            raise Exception("depósito inexistente")
    
if __name__ == "__main__":
    admin = Administracion()
    admin.AgregarDeposito("depo1","Sarmiento 325")
    admin.AgregarDeposito("depo2","9 de Julio 174")
    