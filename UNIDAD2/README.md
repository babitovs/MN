# Unidad 2: Métodos de Búsqueda de Raíces (Ecuaciones No Lineales)

En esta segunda unidad nos enfocamos en la resolución de ecuaciones algebraicas y trascendentes. El objetivo principal es encontrar las raíces de una función matemática mediante aproximaciones numéricas, utilizando tanto métodos cerrados (con intervalos) como métodos abiertos.

---

##  Conceptos Teóricos: Métodos Numéricos

### 1. Método de Bisección (Cerrado)

#### Conceptos Teóricos

Es un método robusto pero lento. Se basa en el teorema del valor intermedio, dividiendo repetidamente a la mitad un intervalo [xᵢ, xₛ] que contiene la raíz. Si f(xᵢ)·f(xₛ) < 0, entonces existe al menos una raíz en dicho intervalo. En cada iteración se evalúa el punto medio y se determina en cuál mitad permanece la raíz.

#### Fórmulas

<p align="center">
  <img src="https://latex.codecogs.com/svg.latex?%5Ccolor%7Bwhite%7Dx_r%20%3D%20%5Cfrac%7Bx_i%20%2B%20x_s%7D%7B2%7D" alt="Bisección"/>
</p>

**Criterio de selección del nuevo intervalo:**
- Si f(xᵢ)·f(xᵣ) < 0 → la raíz está en [xᵢ, xᵣ], se hace xₛ = xᵣ.
- Si f(xᵢ)·f(xᵣ) > 0 → la raíz está en [xᵣ, xₛ], se hace xᵢ = xᵣ.

#### Análisis de Error

- **Error máximo en la iteración n:**

<p align="center">
  <img src="https://latex.codecogs.com/svg.latex?%5Ccolor%7Bwhite%7DE_n%20%3D%20%5Cfrac%7Bx_s%20-%20x_i%7D%7B2%5En%7D" alt="Error bisección"/>
</p>

- **Convergencia:** Lineal (orden 1). El error se reduce a la mitad en cada iteración.
- **Número de iteraciones necesarias** para alcanzar una tolerancia ε:

<p align="center">
  <img src="https://latex.codecogs.com/svg.latex?%5Ccolor%7Bwhite%7Dn%20%3D%20%5Clceil%20%5Clog_2%20%5Cleft(%20%5Cfrac%7Bx_s%20-%20x_i%7D%7B%5Cvarepsilon%7D%20%5Cright)%20%5Crceil" alt="Iteraciones bisección"/>
</p>

#### Condiciones de Aplicación

- **Cuándo usarlo:** Cuando se necesita **garantía de convergencia** y se conoce un intervalo que contiene la raíz (cambio de signo). Es ideal como método de respaldo.
- **Limitaciones:** Es el más lento de los cuatro métodos presentados. No puede encontrar raíces donde la función solo toca el eje X sin cruzarlo (raíces de multiplicidad par). No funciona si no se tiene un intervalo con cambio de signo.
- **Comparación:** Más lento que Falsa Posición, Newton-Raphson y Secante, pero es el único que **siempre converge** si el intervalo contiene una raíz.

#### Ejemplo Numérico

Encontrar la raíz de **f(x) = x³ - x - 2** en el intervalo **[1, 2]**.

f(1) = 1 - 1 - 2 = -2 (negativo)
f(2) = 8 - 2 - 2 = 4 (positivo) → hay cambio de signo.

**Iteración 1:**
- xᵣ = (1 + 2) / 2 = **1.5**
- f(1.5) = 3.375 - 1.5 - 2 = -0.125 (negativo)
- f(1)·f(1.5) > 0 → la raíz está en [1.5, 2]

**Iteración 2:**
- xᵣ = (1.5 + 2) / 2 = **1.75**
- f(1.75) = 5.3594 - 1.75 - 2 = 1.6094 (positivo)
- f(1.5)·f(1.75) < 0 → la raíz está en [1.5, 1.75]

**Iteración 3:**
- xᵣ = (1.5 + 1.75) / 2 = **1.625**
- f(1.625) = 4.2910 - 1.625 - 2 = 0.6660 (positivo)
- f(1.5)·f(1.625) < 0 → la raíz está en [1.5, 1.625]

| Iteración | xᵢ | xₛ | xᵣ | f(xᵣ) |
|---|---|---|---|---|
| 1 | 1.0 | 2.0 | 1.5 | -0.125 |
| 2 | 1.5 | 2.0 | 1.75 | 1.6094 |
| 3 | 1.5 | 1.75 | 1.625 | 0.6660 |

La raíz real es x ≈ 1.5214.

**Código:** [`Biseccion.py`](Codigos/Biseccion.py)

---

### 2. Método de la Falsa Posición / Regula Falsi (Cerrado)

#### Conceptos Teóricos

Similar a la bisección, pero en lugar de tomar el punto medio, une los puntos extremos del intervalo con una línea recta y usa la intersección con el eje X como la nueva aproximación. Converge más rápido que la bisección porque la posición del nuevo punto está influenciada por los valores de la función en los extremos.

#### Fórmulas

<p align="center">
  <img src="https://latex.codecogs.com/svg.latex?%5Ccolor%7Bwhite%7Dx_r%20%3D%20x_s%20-%20%5Cfrac%7Bf(x_s)(x_i%20-%20x_s)%7D%7Bf(x_i)%20-%20f(x_s)%7D" alt="Falsa Posición"/>
</p>

#### Análisis de Error

- **Convergencia:** Superlineal en la mayoría de los casos, pero puede degradarse a lineal si un extremo del intervalo permanece fijo (el método se "estanca" de un lado).
- **Error:** No tiene una fórmula cerrada simple para el error como bisección, pero generalmente converge más rápido.
- **Orden:** Aproximadamente 1.618 (razón áurea) en condiciones ideales.

#### Condiciones de Aplicación

- **Cuándo usarlo:** Cuando se tiene un intervalo con cambio de signo y se desea una convergencia más rápida que bisección, especialmente si la función es aproximadamente lineal en el intervalo.
- **Limitaciones:** Puede ser más lento que bisección si la función es muy curva en el intervalo y un extremo se mantiene fijo durante muchas iteraciones.
- **Comparación:** Más rápido que bisección en la mayoría de los casos, pero sin la garantía de reducción uniforme del intervalo. Más lento que Newton-Raphson y Secante, pero no requiere derivadas.

#### Ejemplo Numérico

Encontrar la raíz de **f(x) = x³ - x - 2** en el intervalo **[1, 2]**.

f(1) = -2, f(2) = 4.

**Iteración 1:**
- xᵣ = 2 - [4(1 - 2)] / [-2 - 4] = 2 - [-4] / [-6] = 2 - 0.6667 = **1.3333**
- f(1.3333) = 2.3704 - 1.3333 - 2 = -0.9630 (negativo)
- f(1.3333)·f(2) < 0 → intervalo [1.3333, 2]

**Iteración 2:**
- xᵣ = 2 - [4(1.3333 - 2)] / [-0.9630 - 4] = 2 - [4(-0.6667)] / [-4.9630] = 2 - 0.5374 = **1.4626**
- f(1.4626) = 3.1283 - 1.4626 - 2 = -0.3343 (negativo)
- f(1.4626)·f(2) < 0 → intervalo [1.4626, 2]

| Iteración | xᵢ | xₛ | xᵣ | f(xᵣ) |
|---|---|---|---|---|
| 1 | 1.0 | 2.0 | 1.3333 | -0.9630 |
| 2 | 1.3333 | 2.0 | 1.4626 | -0.3343 |

**Código:** [`Falsa_posicion.py`](Codigos/Falsa_posicion.py)

---

### 3. Método de Newton-Raphson (Abierto)

#### Conceptos Teóricos

Uno de los métodos más rápidos y utilizados. A partir de una estimación inicial, utiliza la derivada de la función para proyectar una intersección en el eje X. Geométricamente, se traza la recta tangente a la curva en el punto actual y se toma su intersección con el eje X como la siguiente aproximación.

Es un método **abierto**: no requiere un intervalo con cambio de signo, pero la convergencia depende fuertemente de la elección del punto inicial.

#### Fórmulas

<p align="center">
  <img src="https://latex.codecogs.com/svg.latex?%5Ccolor%7Bwhite%7Dx_{i%2B1}%20%3D%20x_i%20-%20%5Cfrac%7Bf(x_i)%7D%7Bf%27(x_i)%7D" alt="Newton-Raphson"/>
</p>

#### Análisis de Error

- **Convergencia:** Cuadrática (orden 2) cerca de la raíz. Esto significa que el número de dígitos correctos se **duplica** en cada iteración.
- **Error en la iteración i+1:**

<p align="center">
  <img src="https://latex.codecogs.com/svg.latex?%5Ccolor%7Bwhite%7De_%7Bi%2B1%7D%20%5Capprox%20%5Cfrac%7Bf%27%27(%5Cxi)%7D%7B2f%27(%5Cxi)%7D%20e_i%5E2" alt="Error Newton"/>
</p>

- Si la raíz tiene multiplicidad > 1, la convergencia se degrada a lineal.

#### Condiciones de Aplicación

- **Cuándo usarlo:** Cuando se conoce la derivada de la función (ya sea analíticamente o de forma simbólica) y se cuenta con una buena estimación inicial cercana a la raíz.
- **Limitaciones:** Puede **diverger** si el punto inicial está lejos de la raíz, si la función tiene inflexiones cercanas, o si la derivada se anula. Requiere calcular f'(x) en cada iteración.
- **Comparación:** Mucho más rápido que bisección y Falsa Posición, pero sin garantía de convergencia. Comparable en velocidad a la Secante, pero con mayor costo por iteración (requiere evaluar f y f').

#### Ejemplo Numérico

Encontrar la raíz de **f(x) = x³ - x - 2**, con **f'(x) = 3x² - 1**, partiendo de **x₀ = 2**.

**Iteración 1:**
- f(2) = 8 - 2 - 2 = 4
- f'(2) = 12 - 1 = 11
- x₁ = 2 - 4/11 = **1.6364**

**Iteración 2:**
- f(1.6364) = 4.3813 - 1.6364 - 2 = 0.7450
- f'(1.6364) = 3(1.6364)² - 1 = 7.0327 - 1 = 6.0327
- x₂ = 1.6364 - 0.7450/6.0327 = **1.5129**

| Iteración | xᵢ | f(xᵢ) | f'(xᵢ) | xᵢ₊₁ |
|---|---|---|---|---|
| 0 | 2.0000 | 4.0000 | 11.0000 | 1.6364 |
| 1 | 1.6364 | 0.7450 | 6.0327 | 1.5129 |

La raíz real es x ≈ 1.5214. Newton-Raphson converge mucho más rápido que bisección.

**Código:** [`newton_r.py`](Codigos/newton_r.py)

---

### 4. Método de la Secante (Abierto)

#### Conceptos Teóricos

Es una alternativa a Newton-Raphson que **no requiere conocer la derivada** de la función. En su lugar, aproxima la derivada utilizando una línea secante que pasa por dos puntos iniciales. Esto lo hace más práctico cuando la derivada es difícil o costosa de calcular.

#### Fórmulas

<p align="center">
  <img src="https://latex.codecogs.com/svg.latex?%5Ccolor%7Bwhite%7Dx_{i%2B1}%20%3D%20x_i%20-%20%5Cfrac%7Bf(x_i)(x_{i-1}%20-%20x_i)%7D%7Bf(x_{i-1})%20-%20f(x_i)%7D" alt="Secante"/>
</p>

Esto es equivalente a reemplazar f'(xᵢ) en Newton-Raphson por la aproximación:

<p align="center">
  <img src="https://latex.codecogs.com/svg.latex?%5Ccolor%7Bwhite%7Df%27(x_i)%20%5Capprox%20%5Cfrac%7Bf(x_i)%20-%20f(x_%7Bi-1%7D)%7D%7Bx_i%20-%20x_%7Bi-1%7D%7D" alt="Derivada aproximada"/>
</p>

#### Análisis de Error

- **Convergencia:** Superlineal, con orden aproximado de **1.618** (razón áurea φ).
- Es más lento que Newton-Raphson (orden 2) pero más rápido que bisección (orden 1).
- Sin embargo, requiere **una sola evaluación de f** por iteración (vs. dos en Newton-Raphson: f y f'), por lo que en términos de evaluaciones totales de función puede ser competitivo.

#### Condiciones de Aplicación

- **Cuándo usarlo:** Cuando no se dispone de la derivada analítica de la función o cuando su cálculo es muy costoso. Es una buena opción cuando se tienen dos puntos iniciales razonables.
- **Limitaciones:** Puede diverger si los puntos iniciales no son adecuados. Es un método abierto sin garantía de convergencia. Si f(xᵢ₋₁) ≈ f(xᵢ), la secante es casi horizontal y el método puede fallar.
- **Comparación:** No necesita derivadas (ventaja sobre Newton-Raphson). Convergencia más rápida que bisección y Falsa Posición, pero ligeramente más lenta que Newton-Raphson por iteración.

#### Ejemplo Numérico

Encontrar la raíz de **f(x) = x³ - x - 2**, con **x₋₁ = 1** y **x₀ = 2**.

f(1) = -2, f(2) = 4.

**Iteración 1:**
- x₁ = 2 - [4(1 - 2)] / [-2 - 4] = 2 - [-4]/[-6] = 2 - 0.6667 = **1.3333**
- f(1.3333) = -0.9630

**Iteración 2:**
- x₂ = 1.3333 - [-0.9630(2 - 1.3333)] / [4 - (-0.9630)]
- x₂ = 1.3333 - [-0.9630 × 0.6667] / [4.9630]
- x₂ = 1.3333 - [-0.6420] / [4.9630]
- x₂ = 1.3333 + 0.1294 = **1.4627**
- f(1.4627) ≈ -0.3335

| Iteración | xᵢ₋₁ | xᵢ | xᵢ₊₁ | f(xᵢ₊₁) |
|---|---|---|---|---|
| 1 | 1.0 | 2.0 | 1.3333 | -0.9630 |
| 2 | 2.0 | 1.3333 | 1.4627 | -0.3335 |

**Código:** [`secante.py`](Codigos/secante.py)

---

##  Problemario de la Unidad

Aquí se encuentran los ejercicios prácticos resueltos sobre la aplicación manual y comprobación de estos métodos:

 [Clic aquí para ver el Problemario de la Unidad 2](https://docs.google.com/spreadsheets/d/1U-aCeb3EvohoChZQm3W79aWKl9u6HLWw/edit?usp=sharing&ouid=102675729823874484334&rtpof=true&sd=true)