def simpson3_8(f,a,b):
    """
    Implementacion del metodo simpson 3/8
    f = funcion a integrar
    a = limite inferior
    b = limite superior
    """
    h = (b-a) / 3
    x0 = a
    x1 = a + h
    x2 = a+2+h
    x3 =b
    integral = (3* h / 8) * (f(x0) + 3 * f(x1) + 3 * f(x2) + f(x3))
    return integral

import math

def funcion(x):
    return math.sin(x)

a = 0
b = math.pi
resultado = simpson3_8(funcion,a,b)
print(f"El resultado de la integral por el metodo de Simpson 3/8 aproximada es: {resultado}")