import unittest
from localidad import Localidad
from producto import Producto
from administracion import Administracion
from excepciones import ProductoNoEncontradoError, LocalidadDuplicadaError, LocalidadNoEncontradaError

class TestLocalidad(unittest.TestCase):
    """
    Verificar que las localidades se crean correctamente.
    Verificar que la sobrecarga del método __eq__() funcione correctamente para comparar localidades.
    """

    def test_creacion_localidad(self):
        # Verificar que una localidad se crea correctamente
        localidad = Localidad("Deposito A", "Isla 1", 1, "Lado A", 1, 10)
        self.assertEqual(localidad.deposito, "Deposito A")
        self.assertEqual(localidad.isla, "Isla 1")
        self.assertEqual(localidad.modulo, 1)
        self.assertEqual(localidad.lado, "Lado A")
        self.assertEqual(localidad.estante, 1)
        self.assertEqual(localidad.cantidad, 10)

    def test_igualdad_localidades(self):
        # Verificar que dos localidades iguales (en términos de atributos) se consideren iguales
        localidad1 = Localidad("Deposito A", "Isla 1", 1, "Lado A", 1)
        localidad2 = Localidad("Deposito A", "Isla 1", 1, "Lado A", 1)
        localidad3 = Localidad("Deposito B", "Isla 2", 2, "Lado B", 2)
        self.assertEqual(localidad1, localidad2)  # Deben ser iguales
        self.assertNotEqual(localidad1, localidad3)  # No deben ser iguales


class TestProducto(unittest.TestCase):

    def setUp(self):
        # Reiniciar el ID autoincremental antes de cada test
        Producto.id = 1
    
    def test_creacion_producto(self):
        # Crear dos productos y verificar que los IDs son autoincrementales
        producto1 = Producto("Teclado")
        producto2 = Producto("Mouse")
        self.assertEqual(producto1.id, 1)
        self.assertEqual(producto2.id, 2)
        self.assertEqual(producto1.descripcion, "Teclado")
        self.assertEqual(producto2.descripcion, "Mouse")
    
    def test_stock_sin_localidades(self):
        # Un producto sin localidades debería tener stock 0
        producto = Producto("Monitor")
        self.assertEqual(producto.stock(), 0)
    
    def test_stock_con_localidades(self):
        # Verificar que el stock de un producto se calcule correctamente
        producto = Producto("Impresora")
        localidad1 = Localidad("Deposito A", "Isla 1", 1, "Lado A", 1, 50)
        localidad2 = Localidad("Deposito B", "Isla 2", 2, "Lado B", 2, 30)
        producto.localidades.append(localidad1)
        producto.localidades.append(localidad2)
        self.assertEqual(producto.stock(), 80)

    def test_posee_localidad(self):
        # Verificar que el método `poseeLocalidad()` funcione correctamente
        producto = Producto("Laptop")
        localidad = Localidad("Deposito A", "Isla 1", 1, "Lado A", 1)
        self.assertFalse(producto.poseeLocalidad(localidad))  # No debe poseer esta localidad
        producto.localidades.append(localidad)
        self.assertTrue(producto.poseeLocalidad(localidad))  # Ahora debe poseer la localidad


class TestAdministracion(unittest.TestCase):

    def setUp(self):
        # Reiniciar el ID autoincremental antes de cada test
        Producto.id = 1
        # Configuración inicial para los tests
        self.admin = Administracion()
        self.admin.agregarProducto("Teclado")
        self.admin.agregarProducto("Mouse")

    def test_agregar_producto(self):
        # Verificar que los productos se agregan correctamente
        self.assertEqual(len(self.admin.productos), 2)
        self.assertEqual(self.admin.productos[1].descripcion, "Teclado")
        self.assertEqual(self.admin.productos[2].descripcion, "Mouse")
    
    def test_agregar_localidad(self):
        # Verificar que se puede agregar una localidad a un producto
        self.admin.agregarLocalidad(1, "Deposito A", "Isla 1", 1, "Lado A", 1)
        self.assertEqual(len(self.admin.productos[1].localidades), 1)
    
    def test_agregar_localidad_duplicada(self):
        # Verificar que se lanza una excepción al agregar una localidad duplicada
        self.admin.agregarLocalidad(1, "Deposito A", "Isla 1", 1, "Lado A", 1)
        with self.assertRaises(LocalidadDuplicadaError):
            self.admin.agregarLocalidad(1, "Deposito A", "Isla 1", 1, "Lado A", 1)
    
    def test_agregar_localidad_producto_inexistente(self):
        # Verificar que se lanza una excepción al agregar una localidad a un producto inexistente
        with self.assertRaises(ProductoNoEncontradoError):
            self.admin.agregarLocalidad(99, "Deposito A", "Isla 1", 1, "Lado A", 1)

    def test_cargar_stock(self):
        # Verificar que se puede cargar stock en una localidad existente
        self.admin.agregarLocalidad(1, "Deposito A", "Isla 1", 1, "Lado A", 1)
        self.admin.cargarStock(1, 100, "Deposito A", "Isla 1", 1, "Lado A", 1)
        self.assertEqual(self.admin.productos[1].stock(), 100)

    def test_cargar_stock_localidad_inexistente(self):
        # Verificar que se lanza una excepción si se intenta cargar stock en una localidad inexistente
        with self.assertRaises(LocalidadNoEncontradaError):
            self.admin.cargarStock(1, 100, "Deposito A", "Isla 1", 1, "Lado A", 1)

    def test_consultar_stock(self):
        # Verificar que se puede consultar el stock total de un producto
        self.admin.agregarLocalidad(1, "Deposito A", "Isla 1", 1, "Lado A", 1)
        self.admin.cargarStock(1, 100, "Deposito A", "Isla 1", 1, "Lado A", 1)
        stock_total = self.admin.stock(1)
        self.assertEqual(stock_total, 100)
    
    def test_consultar_stock_producto_inexistente(self):
        # Verificar que se lanza una excepción al consultar el stock de un producto inexistente
        with self.assertRaises(ProductoNoEncontradoError):
            self.admin.stock(99)

if __name__ == '__main__':
    unittest.main()