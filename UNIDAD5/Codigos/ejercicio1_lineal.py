from interpolacion_lineal import interpolacion_lineal

print("=" * 60)
print("   EJERCICIO 1: INTERPOLACION LINEAL")
print("   Deformacion de un resorte")
print("=" * 60)

# Datos del problema
# x = Fuerza (N), y = Deformacion (mm)
# (x0, y0) = (2, 4)  y  (x1, y1) = (5, 10)
# Interpolar en x = 3

x0, y0 = 2.0, 4.0
x1, y1 = 5.0, 10.0
x_interpolar = 3.0

print(f"\nDatos dados:")
print(f"  (x0, y0) = ({x0}, {y0})")
print(f"  (x1, y1) = ({x1}, {y1})")
print(f"  Valor a interpolar: x = {x_interpolar}\n")

y_resultado = interpolacion_lineal(x0, y0, x1, y1, x_interpolar)

print(f"Aplicando la formula:")
print(f"  y = y0 + ((y1 - y0) / (x1 - x0)) * (x - x0)")
print(f"  y = {y0} + (({y1} - {y0}) / ({x1} - {x0})) * ({x_interpolar} - {x0})")
print(f"  y = {y0} + ({y1 - y0} / {x1 - x0}) * {x_interpolar - x0}")
print(f"  y = {y0} + {(y1 - y0)/(x1 - x0)} * {x_interpolar - x0}")
print(f"  y = {y0} + {((y1 - y0)/(x1 - x0)) * (x_interpolar - x0)}")
print(f"\nResultado: y({x_interpolar}) = {y_resultado}")
