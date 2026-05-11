# Unidad 2: Métodos de Búsqueda de Raíces (Ecuaciones No Lineales)

En esta segunda unidad nos enfocamos en la resolución de ecuaciones algebraicas y trascendentes. El objetivo principal es encontrar las raíces de una función matemática mediante aproximaciones numéricas, utilizando tanto métodos cerrados (con intervalos) como métodos abiertos.

---

## 🧠 Conceptos Teóricos: Métodos Numéricos

### 1. Método de Bisección (Cerrado)
Es un método robusto pero lento. Se basa en el teorema del valor intermedio, dividiendo repetidamente a la mitad un intervalo $[x_i, x_s]$ que contiene la raíz.

**Fórmula:**
$$ x_r = \frac{x_i + x_s}{2} $$

**Código:** [`Biseccion.py`](Codigos/Biseccion.py)

---

### 2. Método de la Falsa Posición / Regula Falsi (Cerrado)
Similar a la bisección, pero une los puntos extremos del intervalo con una línea recta y usa la intersección con el eje X como la nueva aproximación. Converge más rápido que la bisección.

**Fórmula:**
$$ x_r = x_s - \frac{f(x_s)(x_i - x_s)}{f(x_i) - f(x_s)} $$

**Código:** [`Falsa_posicion.py`](Codigos/Falsa_posicion.py)

---

### 3. Método de Newton-Raphson (Abierto)
Uno de los métodos más rápidos y utilizados. A partir de una estimación inicial, utiliza la derivada de la función para proyectar una intersección en el eje X.

**Fórmula:**
$$ x_{i+1} = x_i - \frac{f(x_i)}{f'(x_i)} $$

**Código:** [`newton_r.py`](Codigos/newton_r.py)

---

### 4. Método de la Secante (Abierto)
Es una alternativa a Newton-Raphson que aproxima la derivada utilizando una línea secante que pasa por dos puntos iniciales, $x_{i-1}$ y $x_i$.

**Fórmula:**
$$ x_{i+1} = x_i - \frac{f(x_i)(x_{i-1} - x_i)}{f(x_{i-1}) - f(x_i)} $$

**Código:** [`secante.py`](Codigos/secante.py)

---

## 📝 Problemario de la Unidad

Aquí se encuentran los ejercicios prácticos resueltos sobre la aplicación manual y comprobación de estos métodos:

👉 [Clic aquí para ver el Problemario de la Unidad 2](https://docs.google.com/spreadsheets/d/1U-aCeb3EvohoChZQm3W79aWKl9u6HLWw/edit?usp=sharing&ouid=102675729823874484334&rtpof=true&sd=true)