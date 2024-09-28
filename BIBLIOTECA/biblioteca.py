class Libro():
    def __init__(self, titulo: str, autor: str, ejemplares_disponibles: int) -> None:
        self.titulo = titulo
        self.autor = autor
        if ejemplares_disponibles < 0:
            raise ValueError("La cantidad de libros disponibles no puede ser negativa")
        self.ejemplares_disponibles = ejemplares_disponibles
        
    def actualizar_ejemplares(self, nueva_cantidad: int): #toma la nueva cantidad y la reemplaza
        if nueva_cantidad >= 0:
            self.ejemplares_disponibles = nueva_cantidad
        else:
            raise ValueError("La cantidad de libros disponibles no puede ser negativa")
        
    def __str__(self) -> str: #representacion un un print
        return self.titulo
    
    def __repr__(self) -> str: #representacion en una lista
        return f"{self.titulo} de {self.autor} - stock: {self.ejemplares_disponibles}"

class Usuario():
    def __init__(self, nombre) -> None:
        self.nombre = nombre #nombre del ususario
        self.libros_prestados = [] #libros que la biblioteca le presto al usuario
        
    def agregar_libro_prestado(self, libro: Libro): #agrega un libro a la lista
        if isinstance(libro,Libro):
            self.libros_prestados.append(libro)
        else:
            raise TypeError(f"Se esperaba un libro, pero llego un dato del tipo: {type(libro)}")
        
    def devolver_libro_prestado(self, libro: Libro): #devuelve un libro a la biblioteca
        if isinstance(libro,Libro):
            self.libros_prestados.remove(libro)
        else:
            raise TypeError(f"Se esperaba un libro, pero llego un dato del tipo: {type(libro)}")
        
class Biblioteca():
    def __init__(self) -> None:
        self.libros = []

    def agregar_libro(self, libro: Libro): #agrega un libro nuevo a la biblioteca
        if isinstance(libro,Libro):
            self.libros.append(libro)
        else:
            raise TypeError(f"Se esperaba un libro, pero llego un dato del tipo: {type(libro)}")
        
    def prestar_libro(self, libro: Libro, usuario: Usuario): #presta un libro al usuario
        if libro in self.mostrar_libros_disponibles() and libro.ejemplares_disponibles > 0:
            libro.ejemplares_disponibles -= 1
            usuario.agregar_libro_prestado(libro)
            return True
        else:
            return False
        
    def devolver_libro(self, libro: Libro, usuario: Usuario): #un usuario devuelve un libro
        if libro in self.mostrar_libros_disponibles() and libro in usuario.libros_prestados:
            libro.ejemplares_disponibles += 1
            usuario.devolver_libro_prestado(libro)
            return True
        return False
                
    def mostrar_libros_disponibles(self):
        return [libro for libro in self.libros if libro.ejemplares_disponibles > 0]
    
    def libros_prestados_usuario(self, usuario: Usuario):
        return usuario.libros_prestados
        
if __name__ == "__main__":
    libro1 = Libro("Octubre un crimen", "Isabelle Allende", 3)
    libro2 = Libro("Las cronicas de Narnia: el leon, la bruja y el ropero", "C. S. Lewis", 4)
    user27 = Usuario("Bareiro, Santiago Daniel")
    bib = Biblioteca()
    bib.agregar_libro(libro1)
    bib.agregar_libro(libro2)
    bib.prestar_libro(libro1,user27)
    print(bib.libros_prestados_usuario(user27))