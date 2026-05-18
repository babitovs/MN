import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# 1. Definir la EDO y parámetros
def f(t, y):
    return y - t**2 + 1

t0, y0 = 0, 0.5
t_final = 4
h = 0.2

# 2. Generar los arreglos de numpy para los datos
t_values = np.arange(t0, t_final + h, h)
y_values = np.zeros(len(t_values))
y_values[0] = y0

# Calcular el método (Ejemplo: Euler)
for i in range(len(t_values) - 1):
    y_values[i+1] = y_values[i] + h * f(t_values[i], y_values[i])

# 3. Configurar la figura de Matplotlib
fig, ax = plt.subplots()
ax.set_xlim(t0, t_final)
ax.set_ylim(0, max(y_values) + 1)
ax.set_title("Método de Euler Animado")
ax.grid(True)

# Crear un objeto de línea vacío que se actualizará
linea_euler, = ax.plot([], [], marker='o', label='Aproximación Numérica')
ax.legend()

# 4. Función de inicialización para la animación
def init():
    linea_euler.set_data([], [])
    return linea_euler,

# 5. Función que dibuja cada fotograma (frame)
def update(frame):
    # Toma los datos hasta el frame actual
    t_frame = t_values[:frame+1]
    y_frame = y_values[:frame+1]
    
    linea_euler.set_data(t_frame, y_frame)
    return linea_euler,

# 6. Ejecutar la animación
# frames = len(t_values) asegura que haya un frame por cada punto calculado
ani = FuncAnimation(fig, update, frames=len(t_values),
                    init_func=init, blit=True, interval=500) # interval=500ms por paso

# Para guardar la animación como MP4 (requiere ffmpeg instalado en tu entorno)
# ani.save('animacion_euler.mp4', fps=2)

plt.show()