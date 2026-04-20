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
    x2 = a+2*h
    x3 =b
    integral = (3* h / 8) * (f(x0) + 3 * f(x1) + 3 * f(x2) + f(x3))
    return integral

import math
import time

def funcion(x):
    return 5*x + 2*x**3

a = 1
b = 4
n = 3
inicio = time.perf_counter()
resultado = simpson3_8(funcion,a,b)
fin = time.perf_counter()
tiempo_ejecucion = fin - inicio
print(f"El resultado de la integral por el metodo de Simpson 3/8 aproximada es: {resultado}")
print(f"Tiempo de ejecución: {tiempo_ejecucion:.8f} segundos")