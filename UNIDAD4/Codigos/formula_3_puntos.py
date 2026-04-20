import math
import time

def tres_puntos_adelante(f, x, h):
    return (1 / (2 * h)) * (-3 * f(x) + 4 * f(x + h) - f(x + 2 * h))

def tres_puntos_atras(f, x, h):
    return (1 / (2 * h)) * (3 * f(x) - 4 * f(x - h) + f(x - 2 * h))

def tres_puntos_centrada(f, x, h):
    return (1 / (2 * h)) * (f(x + h) - f(x - h))

# ==========================================
# PRUEBA 1: Hacia Adelante (Vehículo Autónomo)
# ==========================================
funcion_v = lambda t: 10 / (t + 1)
t_val = 2
h_val = 0.5

inicio = time.perf_counter()
res_adelante = tres_puntos_adelante(funcion_v, t_val, h_val)
fin = time.perf_counter()

print("--- FÓRMULA 3 PUNTOS HACIA ADELANTE ---")
print(f"Resultado: {res_adelante:.4f} m/s^2")
print(f"Tiempo: {fin - inicio:.8f} seg\n")

# ==========================================
# PRUEBA 2: Hacia Atrás (Servidor)
# ==========================================
funcion_r = lambda t: -2*t**3 + 12*t**2
t_val2 = 3
h_val2 = 0.5

inicio = time.perf_counter()
res_atras = tres_puntos_atras(funcion_r, t_val2, h_val2)
fin = time.perf_counter()

print("--- FÓRMULA 3 PUNTOS HACIA ATRÁS ---")
print(f"Resultado: {res_atras:.4f} Mbps/min")
print(f"Tiempo: {fin - inicio:.8f} seg\n")

# ==========================================
# PRUEBA 3: Centrada (Placa Térmica)
# ==========================================
def funcion_t(x):
    return math.log(x)

x_val = 2
h_val3 = 0.1

inicio = time.perf_counter()
res_centrada = tres_puntos_centrada(funcion_t, x_val, h_val3)
fin = time.perf_counter()

print("--- FÓRMULA 3 PUNTOS CENTRADA ---")
print(f"Resultado: {res_centrada:.4f}")
print(f"Tiempo: {fin - inicio:.8f} seg")