import unittest 
from alumno import Alumno
from asignatura import Asignatura
from comision import Comision
from inscripcion import Inscripcion
from error import *


class TestAlumno(unittest.TestCase):

    def test_crear_alumno(self):
        alumno = Alumno(12345)
        self.assertEqual(alumno.matricula, 12345)


class TestErrores(unittest.TestCase):

    def test_comision_inexistente_error(self):
        error = ComisionInexistenteError()
        self.assertEqual(str(error), "La comisión no existe")
    
    def test_comision_existente_error(self):
        error = ComisionExistenteError()
        self.assertEqual(str(error), "La comisión ya existe")
    
    def test_alumno_inscripto_error(self):
        error = AlumnoInscriptoError()
        self.assertEqual(str(error), "El alumno ya está inscripto")
    
    def test_comision_llena_error(self):
        error = ComisionLlenaError()
        self.assertEqual(str(error), "La comisión está llena")

    def test_inscripcion_inexistente_error(self):
        error = InscripcionInexistenteError()
        self.assertEqual(str(error), "No existe inscripción para este alumno")

class TestInscripcion(unittest.TestCase):

    def test_crear_inscripcion(self):
        alumno = Alumno(12345)
        inscripcion = Inscripcion(alumno)
        self.assertEqual(inscripcion.alumno, alumno)
        self.assertIsNone(inscripcion.baja)
    
    def test_comparar_inscripciones_iguales(self):
        alumno = Alumno(1)
        inscripcion1 = Inscripcion(alumno)
        inscripcion2 = Inscripcion(alumno)
        self.assertEqual(inscripcion1, inscripcion2)
    
    def test_comparar_inscripciones_distintos(self):
        alumno1 = Alumno(1)
        alumno2 = Alumno(2)
        inscripcion1 = Inscripcion(alumno1)
        inscripcion2 = Inscripcion(alumno2)
        self.assertNotEqual(inscripcion1, inscripcion2)


class TestAsignatura(unittest.TestCase):

    def setUp(self):
        self.asignatura = Asignatura("Matemática")
    
    def test_agregar_comision_ok(self):
        comision_cmp = Comision("101", 10)
        self.asignatura.AgregarComision("101")
        self.assertEqual(self.asignatura.Comision("101"), comision_cmp)
    
    def test_agregar_comision_repetida(self):
        self.asignatura.AgregarComision("101")
        with self.assertRaises(ComisionExistenteError):
            self.asignatura.AgregarComision("101")
    
    def test_eliminar_comision_ok(self):
        comision_cmp = Comision("101", 10)
        self.asignatura.AgregarComision("101")
        self.assertEqual(self.asignatura.Comision("101"), comision_cmp)
        self.asignatura.EliminarComision("101")
        with self.assertRaises(ComisionInexistenteError):
            self.assertNotEqual(self.asignatura.Comision("101"), comision_cmp) 

    def test_eliminar_comision_no_existe(self):
        with self.assertRaises(ComisionInexistenteError):
            self.asignatura.EliminarComision("101")
    
    def test_obtener_comision(self):
        comision = Comision("101", 10) 
        self.asignatura.AgregarComision("101")
        self.assertEqual(self.asignatura.Comision("101"), comision)


class TestComision(unittest.TestCase):

    def setUp(self):
        self.comision = Comision("101", 10)

    def test_agregar_alumno_ok(self):
        alumno = Alumno(1)
        self.comision.Agregar(alumno)
        self.assertEqual(len(self.comision.Alumnos_activos()), 1)
        self.assertIn(alumno, self.comision.Alumnos_activos())
    
    def test_agregar_alumno_repetido(self):
        alumno = Alumno(1)
        self.comision.Agregar(alumno)
        with self.assertRaises(AlumnoInscriptoError):
            self.comision.Agregar(alumno)
    
    def test_agregar_alumno_comision_llena(self):
        for i in range(10):
            self.comision.Agregar(Alumno(i))
        alumno = Alumno(11)
        with self.assertRaises(ComisionLlenaError):
            self.comision.Agregar(alumno)
    
    def test_eliminar_alumno_ok(self):
        alumno = Alumno(1)
        self.comision.Agregar(alumno)
        self.comision.Eliminar(alumno)
        self.assertEqual(len(self.comision.Alumnos_activos()), 0)

    def test_eliminar_alumno_no_inscripto(self):
        alumno = Alumno(1)
        with self.assertRaises(InscripcionInexistenteError):
            self.comision.Eliminar(alumno)

if __name__ == '__main__':
    unittest.main()