class ComisionInexistenteError(Exception):
    def __init__(self) -> None:
        super().__init__("La comisión no existe")

class ComisionExistenteError(Exception):
    def __init__(self) -> None:
        super().__init__("La comisión ya existe")

class AlumnoInscriptoError(Exception):
    def __init__(self) -> None:
        super().__init__("El alumno ya está inscripto")

class ComisionLlenaError(Exception):
    def __init__(self) -> None:
        super().__init__("La comisión está llena")

class InscripcionInexistenteError(Exception):
    def __init__(self) -> None:
        super().__init__("No existe inscripción para este alumno")