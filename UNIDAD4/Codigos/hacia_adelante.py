def diferencia_hacia_adelante(f, x, h):
    """
    Aproxima la primera derivada de f en el punto x 
    usando diferencia hacia adelante.
    """
    derivada = (f(x + h) - f(x)) / h
    return derivada
import time
# Caso de prueba
def funcion(t):
    return 10 / (t + 1)

t = 2
h = 0.5
inicio = time.perf_counter()
resultado = diferencia_hacia_adelante(funcion, t, h)
fin = time.perf_counter()
tiempo_ejecucion = fin - inicio
print(f"La aceleracion aproximada (hacia adelante) es: {resultado}")
print(f"Tiempo de ejecución: {tiempo_ejecucion:.8f} segundos")  