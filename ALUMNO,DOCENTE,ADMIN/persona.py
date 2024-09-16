class Persona:
    def __init__(self, apellido: str, nombre: str, dni: str) -> None:
        self.__apellido = apellido
        self.__nombre = nombre
        self.__dni = dni
        
    @property
    def apellido(self):
        return self.__apellido
        
    @property
    def nombre(self):
        return self.__nombre
        
    @property
    def dni(self):
        return self.__dni