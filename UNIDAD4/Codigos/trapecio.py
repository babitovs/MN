def metodo_del_trapecio(f,a,b,n):
    """
    Aproxima la integral de f desde a hasta b usando la regla 
    del trapecio compuesta
    """
    h = (b-a) / n
    suma = f(a) + f(b)

    for i in range(1,n):
        suma += 2 * f(a + i * h)

    integral = (h / 2) * suma
    return integral

import math

def funcion(x):
    return x**2

a=0
b=1
n=100
resultado = metodo_del_trapecio(funcion,a,b,n)
print(f"El resultado aproximado es: {resultado}")

