from sucursal import Sucursal

sucursal = Sucursal("9 de Julio 1162")
sucursal.menu.AgregarProducto("hamburguesa simple", 300)
sucursal.menu.AgregarProducto("hamburguesa doble", 500)
sucursal.menu.AgregarProducto("hamburguesa veggie", 350)
sucursal.MostrarMenu()