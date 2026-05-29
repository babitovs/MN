from interpolacion_cuadratica import interpolacion_cuadratica_lagrange

print("=" * 60)
print("   EJERCICIO 4: INTERPOLACION CUADRATICA (LAGRANGE)")
print("   Aproximar ln(2)")
print("=" * 60)

# Datos del problema
# f(x) = ln(x)
# Puntos: (1, 0), (4, 1.38629), (6, 1.79176)
# Interpolar en x = 2
# Resultado esperado: ~0.56583

x0, y0 = 1.0, 0.0
x1, y1 = 4.0, 1.38629
x2, y2 = 6.0, 1.79176
x_interpolar = 2.0

print(f"\nDatos dados:")
print(f"  (x0, y0) = ({x0}, {y0})")
print(f"  (x1, y1) = ({x1}, {y1})")
print(f"  (x2, y2) = ({x2}, {y2})")
print(f"  Valor a interpolar: x = {x_interpolar}\n")

y_resultado, l0, l1, l2 = interpolacion_cuadratica_lagrange(x0, y0, x1, y1, x2, y2, x_interpolar)

print(f"Calculo de los polinomios de Lagrange:")
print(f"  L0({x_interpolar}) = ({x_interpolar}-{x1})({x_interpolar}-{x2}) / ({x0}-{x1})({x0}-{x2}) = {l0:.6f}")
print(f"  L1({x_interpolar}) = ({x_interpolar}-{x0})({x_interpolar}-{x2}) / ({x1}-{x0})({x1}-{x2}) = {l1:.6f}")
print(f"  L2({x_interpolar}) = ({x_interpolar}-{x0})({x_interpolar}-{x1}) / ({x2}-{x0})({x2}-{x1}) = {l2:.6f}")
print(f"\nSustituyendo en la formula de Lagrange:")
print(f"  y = {y0}({l0:.6f}) + {y1}({l1:.6f}) + {y2}({l2:.6f})")
print(f"  y = {y0*l0:.6f} + {y1*l1:.6f} + {y2*l2:.6f}")
print(f"\nResultado: y({x_interpolar}) = {y_resultado:.5f}")
print(f"Valor real de ln(2) = 0.69315")
