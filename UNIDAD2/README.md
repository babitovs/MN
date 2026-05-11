# Unidad 2: Métodos de Búsqueda de Raíces (Ecuaciones No Lineales)

En esta segunda unidad nos enfocamos en la resolución de ecuaciones algebraicas y trascendentes. El objetivo principal es encontrar las raíces de una función matemática mediante aproximaciones numéricas, utilizando tanto métodos cerrados (con intervalos) como métodos abiertos.

---

## 🧠 Conceptos Teóricos: Métodos Numéricos

### 1. Método de Bisección (Cerrado)
Es un método robusto pero lento. Se basa en el teorema del valor intermedio, dividiendo repetidamente a la mitad un intervalo [xᵢ, xₛ] que contiene la raíz.

**Fórmula:**

<p align="center">
  <img src="https://latex.codecogs.com/svg.latex?x_r%20%3D%20%5Cfrac%7Bx_i%20%2B%20x_s%7D%7B2%7D" alt="Bisección"/>
</p>

**Código:** [`Biseccion.py`](Codigos/Biseccion.py)

---

### 2. Método de la Falsa Posición / Regula Falsi (Cerrado)
Similar a la bisección, pero une los puntos extremos del intervalo con una línea recta y usa la intersección con el eje X como la nueva aproximación. Converge más rápido que la bisección.

**Fórmula:**

<p align="center">
  <img src="https://latex.codecogs.com/svg.latex?x_r%20%3D%20x_s%20-%20%5Cfrac%7Bf(x_s)(x_i%20-%20x_s)%7D%7Bf(x_i)%20-%20f(x_s)%7D" alt="Falsa Posición"/>
</p>

**Código:** [`Falsa_posicion.py`](Codigos/Falsa_posicion.py)

---

### 3. Método de Newton-Raphson (Abierto)
Uno de los métodos más rápidos y utilizados. A partir de una estimación inicial, utiliza la derivada de la función para proyectar una intersección en el eje X.

**Fórmula:**

<p align="center">
  <img src="https://latex.codecogs.com/svg.latex?x_{i%2B1}%20%3D%20x_i%20-%20%5Cfrac%7Bf(x_i)%7D%7Bf%27(x_i)%7D" alt="Newton-Raphson"/>
</p>

**Código:** [`newton_r.py`](Codigos/newton_r.py)

---

### 4. Método de la Secante (Abierto)
Es una alternativa a Newton-Raphson que aproxima la derivada utilizando una línea secante que pasa por dos puntos iniciales.

**Fórmula:**

<p align="center">
  <img src="https://latex.codecogs.com/svg.latex?x_{i%2B1}%20%3D%20x_i%20-%20%5Cfrac%7Bf(x_i)(x_{i-1}%20-%20x_i)%7D%7Bf(x_{i-1})%20-%20f(x_i)%7D" alt="Secante"/>
</p>

**Código:** [`secante.py`](Codigos/secante.py)

---

## 📝 Problemario de la Unidad

Aquí se encuentran los ejercicios prácticos resueltos sobre la aplicación manual y comprobación de estos métodos:

👉 [Clic aquí para ver el Problemario de la Unidad 2](https://docs.google.com/spreadsheets/d/1U-aCeb3EvohoChZQm3W79aWKl9u6HLWw/edit?usp=sharing&ouid=102675729823874484334&rtpof=true&sd=true)