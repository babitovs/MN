def funcion(x):
    return x**2 - 2

def derivada(x):
    return 2*x

#Método de Newton-Raphson
def newton_raphson(x_inicial):
    x = x_inicial
    # Simulamos un punto de inicio donde la derivada es exactamente cero
    if derivada(x) == 0:
        print("Error: La derivada es cero. División por cero inminente.")
        # x = x - (funcion(x) / derivada(x)) -> ZeroDivisionError
    else:
        print("Calculando...")

print("--- Falla en Newton-Raphson ---")
newton_raphson (0.0) # El minimo de la parábola tiene pendiente cero