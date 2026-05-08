def interpolacion_lineal(x0, y0, x1, y1, x):
    return y0 + ((y1 - y0) / (x1 - x0)) * (x - x0)

def interpolacion_segmentada(puntos, x):
    """
    Calcula la interpolación lineal segmentada para un punto x dado un arreglo de puntos.
    puntos: lista de tuplas [(x0, y0), (x1, y1), ..., (xn, yn)] ordenadas por x.
    """
    if x < puntos[0][0] or x > puntos[-1][0]:
        raise ValueError("El valor de x está fuera del rango de los puntos dados.")
    
    for i in range(len(puntos) - 1):
        x0, y0 = puntos[i]
        x1, y1 = puntos[i+1]
        if x0 <= x <= x1:
            y = interpolacion_lineal(x0, y0, x1, y1, x)
            return y, (x0, y0), (x1, y1)

if __name__ == "__main__":
    print("="*60)
    print("         MÉTODO DE INTERPOLACIÓN SEGMENTADA")
    print("="*60)
    
    # Puntos de la primera tablita de la imagen 1
    puntos = [(1.0, 2.0), (1.5, 0.0), (2.0, 3.0)]
    print(f"Puntos disponibles: {puntos}")
    
    x_seg = 1.8
    y_seg, pt0, pt1 = interpolacion_segmentada(puntos, x_seg)
    
    print(f"\nInterpolación Segmentada en x = {x_seg}")
    print(f"El valor x cae en el segmento entre {pt0} y {pt1}")
    print(f"Resultado de la interpolación lineal en ese segmento:")
    print(f"y = {y_seg}")
