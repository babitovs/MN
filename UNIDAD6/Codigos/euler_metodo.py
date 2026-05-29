def euler(f, x0, y0, h, x_final):
    """
    Método de Euler para resolver EDOs de primer orden.
    
    Parámetros:
        f       : función f(x, y) que define la EDO dy/dx = f(x, y)
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
        y = y + h * f(x, y)
        x = x + h
        x_vals.append(round(x, 10))
        y_vals.append(y)
    
    return x_vals, y_vals


if __name__ == "__main__":
    
    print("=" * 70)
    print("       METODO DE EULER - Ley de Enfriamiento de Newton")
    print("=" * 70)
    
    # ── Definir el problema ──
    # EDO: dT/dt = -0.1(T - 20)
    # T(0) = 80 C  (temperatura inicial)
    # Temperatura ambiente = 20 C
    # h = 0.5 minutos
    # Encontrar T(1.5)
    
    def f(t, T):
        return -0.1 * (T - 20)
    
    t0 = 0
    T0 = 80
    h = 0.5
    t_final = 1.5
    
    print(f"\nEDO: dT/dt = -0.1(T - 20)")
    print(f"Condicion inicial: T({t0}) = {T0} C")
    print(f"Temperatura ambiente: 20 C")
    print(f"Tamano de paso: h = {h} min")
    print(f"Evaluar hasta: t = {t_final} min\n")
    
    # ── Resolver ──
    t_vals, T_vals = euler(f, t0, T0, h, t_final)
    
    # ── Imprimir tabla de resultados con pendiente ──
    print(f"{'Paso':<6} {'t_i':<10} {'T_i':<16} {'f(t_i,T_i)':<16}")
    print("-" * 48)
    
    for i in range(len(t_vals)):
        pendiente = f(t_vals[i], T_vals[i])
        print(f"{i:<6} {t_vals[i]:<10.4f} {T_vals[i]:<16.6f} {pendiente:<16.6f}")
    
    print("-" * 48)
    print(f"\nResultado: T({t_final}) = {T_vals[-1]:.6f} C")
    
    # ── Comparar con h mas pequeno ──
    print("\n" + "=" * 70)
    print("  COMPARACION: Ingresa un h mas pequeno para mejorar la precision")
    print("=" * 70)
    
    try:
        h_nuevo = float(input("\nIngresa el nuevo valor de h (ej: 0.1, 0.05): "))
        
        t_vals2, T_vals2 = euler(f, t0, T0, h_nuevo, t_final)
        
        print(f"\n--- Resultados con h = {h_nuevo} ---\n")
        print(f"{'Paso':<6} {'t_i':<10} {'T_i':<16} {'f(t_i,T_i)':<16}")
        print("-" * 48)
        
        for i in range(len(t_vals2)):
            pendiente = f(t_vals2[i], T_vals2[i])
            print(f"{i:<6} {t_vals2[i]:<10.4f} {T_vals2[i]:<16.6f} {pendiente:<16.6f}")
        
        print("-" * 48)
        print(f"\nResultado con h = {h}: T({t_final}) = {T_vals[-1]:.6f} C")
        print(f"Resultado con h = {h_nuevo}: T({t_final}) = {T_vals2[-1]:.6f} C")
        print(f"Diferencia: {abs(T_vals[-1] - T_vals2[-1]):.6f} C")
    except:
        print("No se ingreso un valor. Fin del programa.")
