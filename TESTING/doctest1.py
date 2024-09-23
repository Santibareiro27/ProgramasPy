def potencia(base,exp):
    """
    Calcula una potencia con una
    base y un exponente dado
    
    >>> potencia(2,4)
    16
    
    >>> potencia(5,0)
    1
    
    """
    
    if exp == 0:
        result = 1
    else:
        result = base
        for i in range(1,exp):
            result *= base
    return result

if __name__ == "__main__":
    import doctest
    doctest.testmod()