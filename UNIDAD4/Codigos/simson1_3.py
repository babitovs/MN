import numpy as np

def simpson13(f,a,b,n):
    """
    implementacion del metodo de simpson 1/3.
    f: funcion a integrar
    a: limite inferior
    b: limite superior
    n: numero de intervalos (debe ser par)
    """

    if n % 2 != 0:
        raise ValueError("el numero de intervalos 'n' debe ser par.")
    h= (b-a) / n
    x= np.linspace(a,b,n+1)
    y= f(x)

    suma = y[0] + y[-1]

    for i in range(1,n):
        if i % 2 ==0:
            suma+= 2 * y[i]
        else:
            suma+= 4 * y[i]

    integral = (h/3) * suma
    return integral

funcion = lambda x: x**2
a = 0
b = 1
n = 4
resultado= simpson13(funcion,a,b,n)
print(f"EL resultado de la integral : {resultado}")
