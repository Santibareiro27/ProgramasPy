class ProductoNoEncontradoError(Exception):
    def __init__(self) -> None:
        super().__init__("No se encontro el producto buscado")

class LocalidadDuplicadaError(Exception):
    def __init__(self) -> None:
        super().__init__("La localidad esta duplicada")

class LocalidadNoEncontradaError(Exception):
    def __init__(self) -> None:
        super().__init__("No se encontro la localidad buscada")