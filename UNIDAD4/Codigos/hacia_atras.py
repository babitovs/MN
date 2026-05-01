def diferencia_hacia_atras(f, x, h):
    """
    Aproxima la primera derivada de f en el punto x 
    usando diferencia hacia atras.
    """
    derivada = (f(x) - f(x - h)) / h
    return derivada

import time
# Caso de prueba
funcion = lambda x: x**3 - 2*x**2 + 5*x

x = 1
h = 0.2
inicio = time.perf_counter()

resultado = diferencia_hacia_atras(funcion, x, h)
fin = time.perf_counter()
tiempo_ejecucion = fin - inicio
print(f"La tasa de cambio de fuerza (hacia atras) es: {resultado}")
print(f"Tiempo de ejecución: {tiempo_ejecucion:.8f} segundos")