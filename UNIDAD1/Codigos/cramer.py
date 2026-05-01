def resolver_sistema_2x2(a1, b1, c1, a2, b2, c2):
    """
    Resuelve un sistema de la forma:
    a1*x + b1*y = c1
    a2*x + b2*y = c2
    Usando la Regla de Cramer (determinantes) para hacerlo manual sin librerías.
    """
    determinante_principal = (a1 * b2) - (b1 * a2)
    if determinante_principal == 0:
        return "El sistema no tiene solución única (líneas paralelas)"
    
    # Calculamos x e y usando determinantes
    x = ((c1 * b2) - (b1 * c2)) / determinante_principal
    y = ((a1 * c2) - (c1 * a2)) / determinante_principal
    return x, y

print("--- Sistema Mal Condicionado (Sin Numpy) ---")
#Ecuación 1: 1.0x + 1.0y = 2.0
#Ecuación 2: 1.0x + 1.0001y = 2.0001
#Matemáticamente, la respuesta exacta es x=1, y=1
x1, y1 = resolver_sistema_2x2(1.0, 1.0, 2.0, 1.0, 1.0001, 2.0001)
print(f"Caso 1 (Original): x={x1}, y={y1}")

#AHORA EL ERROR:
#Cambiamos el resultado de la segunda ecuación por una nada (0.0001 de diferencia)
#Ecuación 2 modificada: 1.0x + 1.0001y = 2.0002
x2, y2 = resolver_sistema_2x2(1.0, 1.0, 2.0, 1.0, 1.0001, 2.0002)
print(f"Caso 2 (Pequeño cambio): x={x2}, y={y2}")
print("\nConclusión: Cambiar el dato de entrada en 0.0001 duplicó el valor de Y y anuló X.")