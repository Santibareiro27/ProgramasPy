import unittest
from biblioteca import Libro, Biblioteca, Usuario

class TestLibro(unittest.TestCase):

    def test_creacion_libro(self):
        libro = Libro("El gran Gatsby", "F. Scott Fitzgerald", 5)
        self.assertEqual(libro.titulo, "El gran Gatsby")
        self.assertEqual(libro.autor, "F. Scott Fitzgerald")
        self.assertEqual(libro.ejemplares_disponibles, 5)

    def test_actualizar_ejemplares(self):
        libro = Libro("El gran Gatsby", "F. Scott Fitzgerald", 5)
        libro.actualizar_ejemplares(3)
        self.assertEqual(libro.ejemplares_disponibles, 3)
    
    def test_no_pueden_existe_ejemplares_negativos(self):
        libro = Libro("Algoritmos Genéticos con Python: Un enfoque práctico para resolver problemas de ingeniería", "Daniel Gutiérrez Reina", 10) 
        with self.assertRaises(ValueError):
            libro.actualizar_ejemplares(-3)


class TestBiblioteca(unittest.TestCase):

    def setUp(self):
        self.biblioteca = Biblioteca()
        self.libro1 = Libro("El gran Gatsby", "F. Scott Fitzgerald", 5)
        self.libro2 = Libro("Cien años de soledad", "Gabriel García Márquez", 3)
        self.usuario = Usuario("Alice")

    def test_agregar_libro(self):
        self.biblioteca.agregar_libro(self.libro1)
        self.assertEqual(len(self.biblioteca.libros), 1)
        self.assertIn(self.libro1, self.biblioteca.libros)

    def test_prestar_devolver_libros(self):
        self.biblioteca.agregar_libro(self.libro1)
        self.biblioteca.agregar_libro(self.libro2)

        self.assertTrue(self.biblioteca.prestar_libro(self.libro1, self.usuario))
        self.assertTrue(self.libro1 in self.usuario.libros_prestados)

        self.assertTrue(self.biblioteca.devolver_libro(self.libro1, self.usuario))
        self.assertTrue(self.libro1 not in self.usuario.libros_prestados)

    def test_mostrar_libros_disponibles(self):
        self.biblioteca.agregar_libro(self.libro1)
        self.biblioteca.agregar_libro(self.libro2)
        
        libros_disponibles = self.biblioteca.mostrar_libros_disponibles()
        self.assertIn(self.libro1, libros_disponibles)
        self.assertIn(self.libro2, libros_disponibles)


class TestUsuario(unittest.TestCase):

    def setUp(self):
        self.usuario = Usuario("Alice")
        self.libro = Libro("El gran Gatsby", "F. Scott Fitzgerald", 5)

    def test_agregar_libro_prestado(self):
        self.usuario.agregar_libro_prestado(self.libro)
        self.assertEqual(len(self.usuario.libros_prestados), 1)
        self.assertIn(self.libro, self.usuario.libros_prestados)

    def test_devolver_libro_prestado(self):
        self.usuario.agregar_libro_prestado(self.libro)
        self.usuario.devolver_libro_prestado(self.libro)
        self.assertEqual(len(self.usuario.libros_prestados), 0)
        self.assertNotIn(self.libro, self.usuario.libros_prestados)

if __name__ == '__main__':
    unittest.main()