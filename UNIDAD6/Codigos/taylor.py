import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# 1. Definir la EDO, su derivada y parámetros
def f(t, y):
    return y - t**2 + 1

# Segunda derivada (y'') necesaria para Taylor de Orden 2
def df_dt(t, y): 
    return y - t**2 - 2*t + 1

t0, y0 = 0, 0.5
t_final = 4
h = 0.2

# 2. Generar arreglos numéricos
t_values = np.arange(t0, t_final + h, h)
y_values = np.zeros(len(t_values))
y_values[0] = y0

# Calcular Método de Taylor de Orden 2
for i in range(len(t_values) - 1):
    y_prime = f(t_values[i], y_values[i])
    y_double_prime = df_dt(t_values[i], y_values[i])
    
    # Aplicamos la fórmula de Taylor truncada
    y_values[i+1] = y_values[i] + h * y_prime + (h**2 / 2) * y_double_prime

# 3. Configurar figura
fig, ax = plt.subplots()
ax.set_xlim(t0, t_final)
ax.set_ylim(0, max(y_values) + 1)
ax.set_title("Método de Taylor (Orden 2) Animado")
ax.grid(True)

# Usamos un cuadrado (marker='s') y color naranja
linea_taylor, = ax.plot([], [], marker='s', color='orange', label='Taylor Ord 2')
ax.legend()

# 4. Funciones de animación
def init():
    linea_taylor.set_data([], [])
    return linea_taylor,

def update(frame):
    linea_taylor.set_data(t_values[:frame+2], y_values[:frame+2])
    return linea_taylor,

ani = FuncAnimation(fig, update, frames=len(t_values), init_func=init, blit=True, interval=500)

# Descomenta la siguiente línea para exportar el video (requiere FFmpeg)
# ani.save('animacion_taylor.mp4', fps=2)

plt.show()