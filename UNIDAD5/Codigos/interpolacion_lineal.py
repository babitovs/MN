def interpolacion_lineal(x0, y0, x1, y1, x):
    """
    Calcula la interpolación lineal para un punto x dados dos puntos (x0, y0) y (x1, y1).
    """
    y = y0 + ((y1 - y0) / (x1 - x0)) * (x - x0)
    return y

if __name__ == "__main__":
    print("="*60)
    print("           MÉTODO DE INTERPOLACIÓN LINEAL")
    print("="*60)
    
    # Ejemplo con datos de la primera tabla del Ejercicio 1
    x0, y0 = 1.0, 2.0
    x1, y1 = 1.5, 0.0
    x_val = 1.25
    
    print(f"Datos dados:")
    print(f"(x0, y0) = ({x0}, {y0})")
    print(f"(x1, y1) = ({x1}, {y1})")
    print(f"Valor a interpolar: x = {x_val}\n")
    
    y_res = interpolacion_lineal(x0, y0, x1, y1, x_val)
    
    print(f"Resultado de la interpolación lineal en x = {x_val}:")
    print(f"y = {y_res}")
