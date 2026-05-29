from euler_metodo import euler

print("=" * 60)
print("   EJERCICIO 7: METODO DE EULER (2 iteraciones)")
print("   dy/dx = x + y,  y(0) = 1,  h = 0.1")
print("=" * 60)

# EDO: dy/dx = x + y
def f(x, y):
    return x + y

x0 = 0
y0 = 1
h = 0.1
x_final = 0.2

print(f"\nDatos del problema:")
print(f"  f(x, y) = x + y")
print(f"  Condicion inicial: y({x0}) = {y0}")
print(f"  Tamano de paso: h = {h}")
print(f"  Evaluar hasta: x = {x_final}\n")

x_vals, y_vals = euler(f, x0, y0, h, x_final)

print(f"{'Paso':<6} {'x':<10} {'y (Euler)':<16}")
print("-" * 32)
for i in range(len(x_vals)):
    print(f"{i:<6} {x_vals[i]:<10.4f} {y_vals[i]:<16.10f}")

print("-" * 32)
print(f"\nResultado: y({x_final}) = {y_vals[-1]}")
