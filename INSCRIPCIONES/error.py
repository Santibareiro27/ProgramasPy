class ComisionInexistenteError(Exception):
    def __init__(self) -> None:
        super().__init__("La comisión no existe")

class ComisionExistenteError(Exception):
    def __init__(self) -> None:
        super().__init__("La comisión ya existe")

class ComisionLlenaError(Exception):
    def __init__(self) -> None:
        super().__init__("La comisión está llena")

class AlumnoInscriptoError(Exception):
    def __init__(self) -> None:
        super().__init__("El alumno ya está inscripto")
        
class InscripcionInexistenteError(Exception):
    def __init__(self) -> None:
        super().__init__("No existe inscripción para este alumno")
    pass

if __name__ == "__main__":
    pass