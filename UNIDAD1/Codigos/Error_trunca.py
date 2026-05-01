import math

print("--- Método de Euler con paso grande ---")

# Ecuación diferencial simple: dy/dt = y, y(0)=1 (La solución real es e^t)
t = 0.0
y = 1.0
paso_grande = 0.5  # Un h demasiado grande

for i in range(4):
    print(f"t={t}, y calculado ={y}, y real = {math.exp(t)}")
    
    # y_{n+1} = y_n + h*f(t_n, y_n)
    y = y + paso_grande * y 
    t += paso_grande

# Tras pocas iteraciones, el 'y calculado' se aleja drásticamente del 'y real'