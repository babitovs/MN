from RK4_metodo import runge_kutta_4

print("=" * 60)
print("   EJERCICIO 9: METODO DE RUNGE-KUTTA 4 (RK4)")
print("   dy/dx = x + y,  y(0) = 1,  h = 0.1")
print("=" * 60)

# EDO: dy/dx = x + y
def f(x, y):
    return x + y

x0 = 0
y0 = 1
h = 0.1
x_final = 0.1

print(f"\nDatos del problema:")
print(f"  f(x, y) = x + y")
print(f"  Condicion inicial: y({x0}) = {y0}")
print(f"  Tamano de paso: h = {h}")
print(f"  Evaluar hasta: x = {x_final}\n")

x_vals, y_vals = runge_kutta_4(f, x0, y0, h, x_final)

# Mostrar detalles de las pendientes k1, k2, k3, k4 para el paso 1
print("Detalle del calculo (Paso 1):")
y_i = y0
x_i = x0
k1 = f(x_i, y_i)
k2 = f(x_i + h/2, y_i + (h/2)*k1)
k3 = f(x_i + h/2, y_i + (h/2)*k2)
k4 = f(x_i + h, y_i + h*k3)
print(f"  k1 = f({x_i}, {y_i}) = {k1}")
print(f"  k2 = f({x_i + h/2}, {y_i + (h/2)*k1}) = {k2}")
print(f"  k3 = f({x_i + h/2}, {y_i + (h/2)*k2}) = {k3}")
print(f"  k4 = f({x_i + h}, {y_i + h*k3}) = {k4}")
print(f"  y1 = {y_i} + ({h}/6)({k1} + 2({k2}) + 2({k3}) + {k4})")
print(f"  y1 = {y_i} + ({h}/6)({k1 + 2*k2 + 2*k3 + k4})")

print(f"\n{'Paso':<6} {'x':<10} {'y (RK4)':<16}")
print("-" * 32)
for i in range(len(x_vals)):
    print(f"{i:<6} {x_vals[i]:<10.4f} {y_vals[i]:<16.10f}")

print("-" * 32)
print(f"\nResultado: y({x_final}) = {y_vals[-1]:.5f}")
