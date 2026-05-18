import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# 1. Definir la EDO y parámetros
def f(t, y):
    return y - t**2 + 1

t0, y0 = 0, 0.5
t_final = 4
h = 0.2

# 2. Generar arreglos numéricos
t_values = np.arange(t0, t_final + h, h)
y_values = np.zeros(len(t_values))
y_values[0] = y0

# Calcular Método de Runge-Kutta 4 (RK4)
for i in range(len(t_values) - 1):
    t_i = t_values[i]
    y_i = y_values[i]
    
    # Cálculo de las 4 pendientes
    k1 = f(t_i, y_i)
    k2 = f(t_i + h/2, y_i + (h/2)*k1)
    k3 = f(t_i + h/2, y_i + (h/2)*k2)
    k4 = f(t_i + h, y_i + h*k3)
    
    # Promedio ponderado para calcular el siguiente punto
    y_values[i+1] = y_i + (h / 6) * (k1 + 2*k2 + 2*k3 + k4)

# 3. Configurar figura
fig, ax = plt.subplots()
ax.set_xlim(t0, t_final)
ax.set_ylim(0, max(y_values) + 1)
ax.set_title("Método de Runge-Kutta 4 Animado")
ax.grid(True)

# Usamos un triángulo (marker='^') y color verde
linea_rk4, = ax.plot([], [], marker='^', color='green', label='RK4')
ax.legend()

# 4. Funciones de animación
def init():
    linea_rk4.set_data([], [])
    return linea_rk4,

def update(frame):
    linea_rk4.set_data(t_values[:frame+1], y_values[:frame+1])
    return linea_rk4,

ani = FuncAnimation(fig, update, frames=len(t_values), init_func=init, blit=True, interval=500)

# Descomenta la siguiente línea para exportar el video (requiere FFmpeg)
# ani.save('animacion_rk4.mp4', fps=2)

plt.show()