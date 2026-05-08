def interpolacion_cuadratica_lagrange(x0, y0, x1, y1, x2, y2, x):
    """
    Calcula la interpolación cuadrática utilizando el método de Lagrange
    para un punto x dados tres puntos (x0, y0), (x1, y1) y (x2, y2).
    """
    # L0(x)
    l0 = ((x - x1) * (x - x2)) / ((x0 - x1) * (x0 - x2))
    # L1(x)
    l1 = ((x - x0) * (x - x2)) / ((x1 - x0) * (x1 - x2))
    # L2(x)
    l2 = ((x - x0) * (x - x1)) / ((x2 - x0) * (x2 - x1))
    
    y = (y0 * l0) + (y1 * l1) + (y2 * l2)
    return y, l0, l1, l2

if __name__ == "__main__":
    print("="*60)
    print("   MÉTODO DE INTERPOLACIÓN CUADRÁTICA (LAGRANGE)")
    print("="*60)
    
    # --- EJERCICIO 1 ---
    print("\n--- EJERCICIO 1 ---")
    x0, y0 = 1.0, 5.0
    x1, y1 = 2.0, 12.0
    x2, y2 = 3.0, 23.0
    x_val = 2.5
    
    print(f"Datos dados:")
    print(f"(x0, y0) = ({x0}, {y0})")
    print(f"(x1, y1) = ({x1}, {y1})")
    print(f"(x2, y2) = ({x2}, {y2})")
    print(f"Valor a interpolar: x = {x_val}\n")
    
    y_res, l0, l1, l2 = interpolacion_cuadratica_lagrange(x0, y0, x1, y1, x2, y2, x_val)
    
    print("Cálculo de los polinomios de Lagrange (L0, L1, L2):")
    print(f"L0({x_val}) = {l0}")
    print(f"L1({x_val}) = {l1}")
    print(f"L2({x_val}) = {l2}")
    print(f"\nSustituyendo en la fórmula de Lagrange:")
    print(f"y = {y0}({l0}) + {y1}({l1}) + {y2}({l2})")
    print(f"y = {y_res}")
    print(f"Nueva (x, y) = ({x_val}, {y_res})")

    # --- EJERCICIO 2 ---
    print("\n--- EJERCICIO 2 ---")
    x0_2, y0_2 = 1.0, 3.0
    x1_2, y1_2 = 4.0, 24.0
    x2_2, y2_2 = 7.0, 67.0
    x_val_2 = 5.0
    
    print(f"Datos dados:")
    print(f"(x0, y0) = ({x0_2}, {y0_2})")
    print(f"(x1, y1) = ({x1_2}, {y1_2})")
    print(f"(x2, y2) = ({x2_2}, {y2_2})")
    print(f"Valor a interpolar: x = {x_val_2}\n")
    
    y_res_2, l0_2, l1_2, l2_2 = interpolacion_cuadratica_lagrange(x0_2, y0_2, x1_2, y1_2, x2_2, y2_2, x_val_2)
    
    print("Cálculo de los polinomios de Lagrange (L0, L1, L2):")
    print(f"L0({x_val_2}) = {l0_2} (aprox -1/9)")
    print(f"L1({x_val_2}) = {l1_2} (aprox 8/9)")
    print(f"L2({x_val_2}) = {l2_2} (aprox 2/9)")
    print(f"\nSustituyendo en la fórmula de Lagrange:")
    print(f"y = {y0_2}({l0_2:.4f}) + {y1_2}({l1_2:.4f}) + {y2_2}({l2_2:.4f})")
    print(f"y = {y_res_2:.4f}")
    print(f"Resultado final aproximado: 35.8889")
