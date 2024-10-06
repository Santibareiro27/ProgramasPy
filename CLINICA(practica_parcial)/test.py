import unittest
from datetime import datetime

from persona import Persona
from persona import Paciente
from persona import Profesional
from turno import Turno
from clinica import Clinica


class TestPersona(unittest.TestCase):

    def test_constructor_persona(self):
        # Probar que se inicialicen correctamente las propiedades
        persona = Persona(1234, 'Juan', 111222333)

        self.assertEqual(persona.documento, 1234)
        self.assertEqual(persona.nombre, 'Juan')
        self.assertEqual(persona.celular, 111222333)

    def test_constructor_sin_celular(self):
        # Probar que se pueda construir sin celular
        persona = Persona(5678, 'Maria')

        self.assertEqual(persona.documento, 5678)
        self.assertEqual(persona.nombre, 'Maria')
        self.assertIsNone(persona.celular)

    def test_cambiar_celular(self):
        # Probar que se pueda cambiar el celular
        persona = Persona(1234, 'Juan')

        persona.celular = 111222333
        self.assertEqual(persona.celular, 111222333)

        persona.celular = None
        self.assertIsNone(persona.celular)


class TestPaciente(unittest.TestCase):

    def test_constructor_paciente(self):
        # Probar que herede bien de Persona
        paciente = Paciente(1234, 'Juan', 111222333)

        self.assertEqual(paciente.documento, 1234)
        self.assertEqual(paciente.nombre, 'Juan')
        self.assertEqual(paciente.celular, 111222333)

    def test_cantidad_turnos_inicializado(self):
        # Probar que la cantidad de turnos se inicialice en Cero (valor entero)
        paciente = Paciente(1234, 'Juan', 112223333)
        self.assertEqual(paciente.cantidad_turnos, 0)

    def test_contador_turnos(self):
        # Probar el contador de turnos
        paciente = Paciente(1234, 'Juan', 111222333)
        self.assertEqual(paciente.cantidad_turnos, 0)
        
        paciente.cantidad_turnos += 1
        self.assertEqual(paciente.cantidad_turnos, 1)

        paciente.cantidad_turnos += 2 
        self.assertEqual(paciente.cantidad_turnos, 3)

    def test_herencia_persona(self):
        # Probar que se comporte también como Persona
        paciente = Paciente(1234, 'Juan', 111222333)
        persona = Persona(1234, 'Juan', 111222333)

        self.assertEqual(paciente.documento, persona.documento)
        self.assertEqual(paciente.nombre, persona.nombre)
        self.assertEqual(paciente.celular, persona.celular)


class TestProfesional(unittest.TestCase):

    def test_constructor_profesional(self):
        # Probar inicialización correcta
        p = Profesional(1234, 'Juan', 1, 'Medicina', 111222333)
        
        self.assertEqual(p.documento, 1234)
        self.assertEqual(p.nombre, 'Juan')
        self.assertEqual(p.celular, 111222333)
        self.assertEqual(p.matricula, 1)
        self.assertEqual(p.especialidad, 'Medicina')

    def test_matricula_numerica(self):
        # Probar que matrícula sea numérica
        self.assertRaises(TypeError, Profesional, 1234, 'Juan', 'A123', 'Medicina', 111222333)
    
    def test_especialidad_text(self):
        # Probar que la especialidad sea texto
        self.assertRaises(TypeError, Profesional, 1234, 'Juan', 1, 777, 111222333)

    def test_herencia_persona(self):
        # Probar que se comporte también como Persona
        p = Profesional(1234, 'Juan', 1, 'Medicina', 111222333)
        per = Persona(1234, 'Juan', 111222333)
        
        self.assertEqual(p.documento, per.documento)
        self.assertEqual(p.nombre, per.nombre)
        self.assertEqual(p.celular, per.celular)


class TestTurno(unittest.TestCase):

    def test_constructor_turno(self):
        # Probar que se inicialicen correctamente las propiedades
        paciente = Paciente(1234, 'Juan') 
        profesional = Profesional(4567, 'Pedro', 1, 'Medicina', 111222)
        fecha = datetime(2023, 5, 1, 10, 30)
        turno = Turno(paciente, profesional, fecha)
        
        self.assertEqual(turno.paciente, paciente)
        self.assertEqual(turno.profesional, profesional)
        self.assertEqual(turno.diahora, fecha)


class TestClinica(unittest.TestCase):

    def setUp(self):
        self.clinica = Clinica('Clínica Mayo')

    def test_constructor_clinica(self):
        # Verificar inicialización
        self.assertEqual(self.clinica.nombre, 'Clínica Mayo')
        self.assertDictEqual(self.clinica.pacientes, {})
        self.assertDictEqual(self.clinica.profesionales, {})
        self.assertDictEqual(self.clinica.turnos, {})

    def test_agregar_paciente(self):
        # Probar agregar paciente
        p = Paciente(1234, 'Juan', 111222333)
        self.clinica.AgregarPaciente(1234, 'Juan', 111222333)
        self.assertEqual(self.clinica.pacientes[1234], p)

    def test_agregar_profesional(self):
        # Probar agregar profesional
        pr = Profesional(4567, 'Pedro', 1, 'Medicina', 444555666)
        self.clinica.AgregarProfesional(4567, 'Pedro', 1, 'Medicina', 444555666)
        self.assertEqual(self.clinica.profesionales[1], pr)

    def test_buscar_profesional_existente(self):
        pr = Profesional(4567, 'Pedro', 1, 'Medicina', 444555666)
        self.clinica.profesionales[1] = pr
        encontrado = self.clinica.BuscarProfesional(1)
        self.assertEqual(encontrado, pr)
    
    def test_buscar_profesional_no_existe(self):
        # Prueba para verificar el retorno de None al buscar un profesional inexistente
        encontrado = self.clinica.BuscarProfesional(1)
        self.assertIsNone(encontrado)

    def test_buscar_paciente_existente(self):
        # Buscar un paciente existente
        p = Paciente(1234, 'Juan', 1112222333)
        self.clinica.pacientes[1234] = p
        encontrado = self.clinica.BuscarPaciente(1234)
        self.assertEqual(encontrado, p)

    def test_buscar_paciente_no_existe(self):
        # Prueba para buscar un paciente que no existe, debe retornar None
        encontrado = self.clinica.BuscarPaciente(12345)
        self.assertIsNone(encontrado)

    def test_asignar_turno_paciente_no_existe(self):
        # Prueba para verificar excepción al intentar asignar un turno a un paciente inexistente
        with self.assertRaises(Exception):
            self.clinica.AsignarTurno(1234, 1, 1, 5, 2023, 10, 30)
    
    def test_asignar_turno_profesional_no_existe(self):
        # Prueba para verificar excepción al intentar asignar un turno con un profesional inexistente
        p = Paciente(1234, 'Juan', 111222333)
        self.clinica.AgregarPaciente(1234, 'Juan', 111222333)
        with self.assertRaises(Exception):
            self.clinica.AsignarTurno(1234, 111, 1, 5, 2023, 10, 30)

    def test_asignar_turno(self):
        # Prueba de asignar un turno
        self.clinica.AgregarPaciente(1234, 'Juan', 111222333)
        self.clinica.AgregarProfesional(4567, 'Pedro', 1, 'Medicina', 444555666)         
        self.clinica.AsignarTurno(1234, 1, 1, 5, 2023, 10, 30)
    
    def test_asignar_turno_repetido(self):
        # Prueba para evitar asignar un turno repetido
        self.clinica.AgregarPaciente(1234, 'Juan', 111222333)
        self.clinica.AgregarProfesional(4567, 'Pedro', 1, 'Medicina', 444555666)

        self.clinica.AsignarTurno(1234, 1, 1, 5, 2023, 10, 30)
        
        with self.assertRaises(Exception):
            self.clinica.AsignarTurno(1234, 1, 1, 5, 2023, 10, 30)

    def test_obtener_pacientes_fecha(self):
        # Prueba para obtener los pacientes de un profesional para una fecha dada
        p1 = Paciente(1234, 'Juan', 111222333)
        p2 = Paciente(5678, 'Maria', 444555666)
        pr = Profesional(9101, 'Laura', 1, 'Pediatría')
        
        self.clinica.AgregarPaciente(1234, 'Juan', 111222333)
        self.clinica.AgregarPaciente(5678, 'Maria', 444555666)
        self.clinica.AgregarProfesional(9101, 'Laura', 1, 'Pediatría')
        
        fecha = datetime(2023, 5, 1, 10, 30)        
        self.clinica.AsignarTurno(1234, 1, 1, 5, 2023, 10, 30)
        self.clinica.AsignarTurno(5678, 1, 1, 5, 2023, 10, 40)
        
        pacientes = self.clinica.PacientesDeUnaFechaParaUnProfesional(fecha, pr)
        self.assertEqual(pacientes[0].cantidad_turnos, 1)
        self.assertEqual(len(pacientes), 2)
        self.assertIn(p1, pacientes)
        self.assertIn(p2, pacientes)

    def test_obtener_fecha_paciente_profesional(self):
        # Prueba para obtener la fecha del turno de un paciente, para un profesional y día determinado
        p1 = Paciente(1234, 'Juan', 111222333)
        p2 = Paciente(5678, 'Maria', 444555666)
        pr = Profesional(9101, 'Laura', 1, 'Pediatría')
        
        self.clinica.AgregarPaciente(1234, 'Juan', 111222333)
        self.clinica.AgregarPaciente(5678, 'Maria', 444555666)
        self.clinica.AgregarProfesional(9101, 'Laura', 1, 'Pediatría')
        
        fecha = datetime(2023, 5, 1, 10, 30)
        self.clinica.AsignarTurno(1234, 1, 1, 5, 2023, 10, 30)
        self.clinica.AsignarTurno(5678, 1, 1, 5, 2023, 10, 40)
        
        fecha_turno = self.clinica.TurnoDeUnPacienteEnUnaFechaParaUnProfesional(p1, fecha, pr)
        self.assertEqual(len(fecha_turno), 1)
        self.assertIn(fecha, fecha_turno)


if __name__ == '__main__':
    unittest.main()