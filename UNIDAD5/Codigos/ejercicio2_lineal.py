from interpolacion_lineal import interpolacion_lineal

print("=" * 60)
print("   EJERCICIO 2: INTERPOLACION LINEAL")
print("   Temperatura de un fluido")
print("=" * 60)

# Datos del problema
# t = 10s -> T = 22C,  t = 20s -> T = 35C
# Estimar temperatura en t = 16s

x0, y0 = 10.0, 22.0
x1, y1 = 20.0, 35.0
x_interpolar = 16.0

print(f"\nDatos dados:")
print(f"  (x0, y0) = ({x0}, {y0})")
print(f"  (x1, y1) = ({x1}, {y1})")
print(f"  Valor a interpolar: x = {x_interpolar}\n")

y_resultado = interpolacion_lineal(x0, y0, x1, y1, x_interpolar)

print(f"Aplicando la formula:")
print(f"  T = y0 + ((y1 - y0) / (x1 - x0)) * (x - x0)")
print(f"  T = {y0} + (({y1} - {y0}) / ({x1} - {x0})) * ({x_interpolar} - {x0})")
print(f"  T = {y0} + ({y1 - y0} / {x1 - x0}) * {x_interpolar - x0}")
print(f"  T = {y0} + {(y1 - y0)/(x1 - x0)} * {x_interpolar - x0}")
print(f"  T = {y0} + {((y1 - y0)/(x1 - x0)) * (x_interpolar - x0)}")
print(f"\nResultado: T({x_interpolar}) = {y_resultado}")
