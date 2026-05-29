def taylor_orden2(f, df, x0, y0, h, x_final):
    """
    Método de Taylor de Orden 2 para resolver EDOs de primer orden.
    
    Parámetros:
        f       : función f(x, y) que define la EDO dy/dx = f(x, y)
        df      : derivada total de f, es decir f'(x,y) = ∂f/∂x + (∂f/∂y)·f(x,y)
        x0      : valor inicial de x
        y0      : valor inicial de y (condición inicial)
        h       : tamaño del paso
        x_final : valor final de x
    
    Retorna:
        x_vals : lista con los valores de x
        y_vals : lista con los valores aproximados de y
    """
    x_vals = [x0]
    y_vals = [y0]
    
    x = x0
    y = y0
    
    while x < x_final - 1e-10:
        y_prima = f(x, y)
        y_doble_prima = df(x, y)
        
        # Fórmula de Taylor de orden 2
        y = y + h * y_prima + (h**2 / 2) * y_doble_prima
        x = x + h
        x_vals.append(round(x, 10))
        y_vals.append(y)
    
    return x_vals, y_vals


if __name__ == "__main__":
    import math
    
    print("=" * 65)
    print("      MÉTODO DE TAYLOR DE ORDEN 2 - Solución de EDOs")
    print("=" * 65)
    
    # ── Definir el problema ──
    # EDO: dy/dx = -2y,  y(0) = 1
    # Solución exacta: y(x) = e^(-2x)
    #
    # f(x, y) = -2y
    # Derivada total: f'(x, y) = ∂f/∂x + (∂f/∂y)·f(x,y)
    #                           = 0 + (-2)·(-2y) = 4y
    
    def f(x, y):
        return -2 * y
    
    def df(x, y):
        return 4 * y
    
    def solucion_exacta(x):
        return math.exp(-2 * x)
    
    x0 = 0
    y0 = 1
    h = 0.1
    x_final = 1.0
    
    print(f"\nEDO: dy/dx = -2y")
    print(f"Condición inicial: y({x0}) = {y0}")
    print(f"Tamaño de paso h = {h}")
    print(f"Intervalo: [{x0}, {x_final}]")
    print(f"\nf(x, y) = -2y")
    print(f"f'(x, y) = 4y  (derivada total)\n")
    
    # ── Resolver ──
    x_vals, y_vals = taylor_orden2(f, df, x0, y0, h, x_final)
    
    # ── Imprimir tabla de resultados ──
    print(f"{'Paso':<6} {'x':<10} {'y (Taylor 2)':<16} {'y (exacta)':<16} {'Error abs.':<14}")
    print("-" * 62)
    
    for i in range(len(x_vals)):
        y_exact = solucion_exacta(x_vals[i])
        error = abs(y_vals[i] - y_exact)
        print(f"{i:<6} {x_vals[i]:<10.4f} {y_vals[i]:<16.10f} {y_exact:<16.10f} {error:<14.10f}")
    
    print("-" * 62)
    print(f"\nValor aproximado final: y({x_final}) ~= {y_vals[-1]:.10f}")
    print(f"Valor exacto:          y({x_final}) = {solucion_exacta(x_final):.10f}")
    print(f"Error absoluto final:  {abs(y_vals[-1] - solucion_exacta(x_final)):.10f}")
