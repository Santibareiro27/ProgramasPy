class Localidad():
    def __init__(self, deposito: str, isla: str, modulo: int, lado: str, estante: int, cantidad: int = 0) -> None:
        self.deposito = deposito
        self.isla = isla
        self.modulo = modulo
        self.lado = lado
        self.estante = estante
        self.cantidad = cantidad
        
    def __eq__(self, value: object) -> bool:
        if isinstance(value, Localidad):
            return self.deposito==value.deposito and self.isla==value.isla and self.modulo==value.modulo and self.lado==value.lado and self.estante==value.estante
        return False