import math

def diferencia_centrada(f, x, h):
    """
    Aproxima la primera derivada de f en el punto x 
    usando diferencia centrada.
    """
    derivada = (f(x + h) - f(x - h)) / (2 * h)
    return derivada

# Caso de prueba
import time
def funcion(x):
    return math.log(x)

x = 2
h = 0.1
inicio = time.perf_counter()
resultado = diferencia_centrada(funcion, x, h)
fin = time.perf_counter()
tiempo_ejecucion = fin - inicio
print(f"El gradiente de temperatura (diferencia centrada) es: {resultado}")
print(f"Tiempo de ejecución: {tiempo_ejecucion:.8f} segundos")