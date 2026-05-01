import math
print("--- Demostración de Underflow ---")
try:
    # Exponencial de un número negativo muy grande
    resultado = math.exp(-1000)
    print(f"El resultado exacto es mayor a cero, pero Python muestra: {resultado}")
    
    # Si usamos esto en una fórmula posterior:
    division = 1.0 / resultado
except ZeroDivisionError:
    print("\nERROR CRÍTICO: El subdesbordamiento convirtió el valor a 0.0, provocando una división por cero.")