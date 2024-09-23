class Movil:
    def __init__(self, patente: str, color: str, marca: str, modelo: str) -> None:
        self.patente = patente
        self.color = color
        self.marca = marca
        self.modelo = modelo
    
    def __str__(self) -> str:
        return f"""
    {self.marca} {self.modelo}
    Color: {self.color}
    Patente: {self.patente}
    """
    
    def __eq__(self, value: object) -> bool:
        if isinstance(value,Movil):
            return self.patente == value.patente
        elif isinstance(value, str):
            return self.patente == value
        else:
            return False