from taylor_metodo import taylor_orden2

print("=" * 60)
print("   EJERCICIO 8: METODO DE TAYLOR DE ORDEN 2")
print("   y' = y - x,  y(0) = 2,  h = 0.1")
print("=" * 60)

# EDO: y' = y - x
# f(x, y) = y - x
# Derivada total: f'(x,y) = df/dx + (df/dy)*f(x,y)
#   df/dx = -1
#   df/dy = 1
#   f'(x,y) = -1 + 1*(y - x) = y - x - 1

def f(x, y):
    return y - x

def df(x, y):
    return y - x - 1

x0 = 0
y0 = 2
h = 0.1
x_final = 0.1

print(f"\nDatos del problema:")
print(f"  f(x, y) = y - x")
print(f"  f'(x, y) = y - x - 1  (derivada total)")
print(f"  Condicion inicial: y({x0}) = {y0}")
print(f"  Tamano de paso: h = {h}")
print(f"  Evaluar hasta: x = {x_final}\n")

x_vals, y_vals = taylor_orden2(f, df, x0, y0, h, x_final)

print(f"{'Paso':<6} {'x':<10} {'y (Taylor 2)':<16}")
print("-" * 32)
for i in range(len(x_vals)):
    print(f"{i:<6} {x_vals[i]:<10.4f} {y_vals[i]:<16.10f}")

print("-" * 32)
print(f"\nResultado: y({x_final}) = {y_vals[-1]}")
