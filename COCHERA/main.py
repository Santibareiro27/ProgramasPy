from empresa import Empresa
from galpon import Galpon
from movil import Movil

empresa = Empresa("EldorisInc","30123456789")
empresa.AgregarGalpon("9 de Julio 1293",4,"Galpon centro")

galpon = empresa.galpones[1] #por comodidad, uso galpon como puntero

if isinstance(galpon,Galpon): #si no ejecuto este if, no se autocompletan los metodos
    print(galpon.AgregarMovil("AA123BB","azul","Toyota","Corola"))
    print(galpon.AgregarMovil("AA123BC","azul","Ford","Focus"))
    print(galpon.AgregarMovil("AA123BD","azul","Ford","Focus"))
    print(galpon.AgregarMovil("AA123BD","azul","Ford","Focus")) #no se agrega porque se repite patente, devuelve -2
    print(galpon.AgregarMovil("AA123BE","azul","Ford","Focus"))
    print(galpon.AgregarMovil("AA123BF","azul","Ford","Focus")) #no se agrega porque se alcanzo la capacidad maxima, devuelve -1
    
    print(galpon.BuscarMovil("AA123BB"))
    
    print(galpon.EliminarMovil("AA123BE"))
    
    print(galpon.BuscarMovil("AA123BE"))


