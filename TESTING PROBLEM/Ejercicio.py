'''
PROBLEMA:

Crear una función que, dado un String como parámetro, imprima una frase 
describiendo la letra que más se repite y la cantidad de repeticiones, 
de la forma mas eficiente posible.

Ejemplo:
    Entrada: "Hola, mi nombre es Ariel, soy una sirena, vivo bajo el mar"
    Salida: "La letra que más se repite es la A con 6 repeticiones"
'''

def analizaString(cadena: str):
    '''
    Codificar en esta función la solución al problema.
    Pueden utilizarse las funciones auxiliares que se deseen.
    
    INPUT:
        cadena es un String con la frase a analizar.
        
    OUTPUT:
        un String formateado según la consigna. "áéíóúÁÉÍÓÚ"
    '''
    
    ###############
    abc = {}
    cantidad = 0
    for i in cadena:
        if i.isalpha():
            j = i.lower()
            match j:
                case 'á': j = 'a'
                case 'é': j = 'e'
                case 'í': j = 'i'
                case 'ó': j = 'o'
                case 'ú': j = 'u'
            if j not in abc:
                abc[j] = 1
            else:
                abc[j] += 1
    for i in abc:
        if abc[i] > cantidad:
            cantidad = abc[i]
            letra = i
    ###############
    
    
    # Ejemplo para el formateo del String de salida
    return "La letra que más se repite es la {} con {} repeticiones".format(letra.upper(), cantidad)



if __name__ == '__main__':
    '''
    Permite ejecutar este contenido únicamente si el módulo no se inicia desde
    una declaración de importación.
    
    Ref.: https://docs.python.org/3/library/__main__.html
    '''
    
    cadena = "Hola, mi nombre es Ariel, soy una sirena, vivo bajo el mar"
    print(analizaString(cadena))