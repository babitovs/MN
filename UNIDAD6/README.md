# Unidad 6: Solución de Ecuaciones Diferenciales Ordinarias (EDOs)

En esta sexta unidad abordamos los métodos numéricos para resolver ecuaciones diferenciales ordinarias (EDOs) de primer orden con condiciones iniciales. Se estudian tres enfoques fundamentales: el Método de Euler, el Método de Runge-Kutta de orden 4 (RK4) y la Serie de Taylor de orden 2, cada uno con diferente nivel de precisión y complejidad computacional.

📄 **Documento de ejercicios resueltos:** [Ver en Google Docs](https://docs.google.com/document/d/1lAJiOekYKJGTKZc3jBedKOxqVlFyG8dfG4qKHUtQwt4/edit?usp=sharing)

---

## 📐 Conceptos Teóricos: Métodos para EDOs

Todos los métodos de esta unidad resuelven problemas de valor inicial (PVI) de la forma:

<p align="center">
  <img src="https://latex.codecogs.com/svg.latex?%5Ccolor%7Bwhite%7D%5Cfrac%7Bdy%7D%7Bdx%7D%20%3D%20f(x%2C%20y)%2C%20%5Cquad%20y(x_0)%20%3D%20y_0" alt="PVI"/>
</p>

La idea general es avanzar paso a paso desde la condición inicial, calculando valores aproximados de **y** en puntos sucesivos separados por un tamaño de paso **h**.

---

### 1. Método de Euler

#### Conceptos Teóricos

El Método de Euler es el esquema numérico más sencillo para resolver EDOs. Se basa en la idea geométrica de seguir la **recta tangente** a la curva solución en cada punto conocido para estimar el siguiente valor. Es decir, se aproxima la curva por una sucesión de segmentos rectos cuya pendiente está dada por la función **f(x, y)**.

Es un método de **un solo paso** y **explícito**: para calcular el nuevo valor solo se necesita información del punto actual.

#### Fórmulas

La fórmula iterativa del Método de Euler es:

<p align="center">
  <img src="https://latex.codecogs.com/svg.latex?%5Ccolor%7Bwhite%7Dy_%7Bi%2B1%7D%20%3D%20y_i%20%2B%20h%20%5Ccdot%20f(x_i%2C%20y_i)" alt="Euler"/>
</p>

Donde:
- **yᵢ** es el valor aproximado en el paso actual.
- **h** es el tamaño del paso.
- **f(xᵢ, yᵢ)** es la pendiente evaluada en el punto actual.

#### Análisis de Error

| Tipo de error | Orden |
|---|---|
| Error local de truncamiento | O(h²) |
| Error global acumulado | O(h) |

El método de Euler es de **primer orden**. El error global crece linealmente conforme se avanza en la solución. Para mejorar la precisión es necesario **reducir el tamaño del paso h**, pero esto incrementa el número de evaluaciones de la función y puede amplificar los errores de redondeo.

#### Condiciones de Aplicación

- **Cuándo usarlo:** Es ideal para una primera aproximación rápida, para fines didácticos, o cuando la función es muy suave y el intervalo de integración es corto.
- **Limitaciones:** Es el método menos preciso de los tres presentados. Con pasos grandes, la solución puede divergir significativamente de la solución real.
- **Comparación:** Mucho más simple pero menos preciso que RK4. Requiere menos cálculos por paso que Taylor de orden 2 (no necesita derivadas adicionales).

#### Ejemplo Numérico

Resolvamos la EDO:  **dy/dx = -2y**, con **y(0) = 1**, usando **h = 0.1**.

La solución analítica exacta es:

<p align="center">
  <img src="https://latex.codecogs.com/svg.latex?%5Ccolor%7Bwhite%7Dy(x)%20%3D%20e%5E%7B-2x%7D" alt="Solución exacta"/>
</p>

**Iteración 1** (i = 0):
- x₀ = 0, y₀ = 1
- f(x₀, y₀) = -2(1) = -2
- y₁ = 1 + 0.1 × (-2) = **0.8**
- Valor exacto: y(0.1) = e⁻⁰·² ≈ 0.8187

**Iteración 2** (i = 1):
- x₁ = 0.1, y₁ = 0.8
- f(x₁, y₁) = -2(0.8) = -1.6
- y₂ = 0.8 + 0.1 × (-1.6) = **0.64**
- Valor exacto: y(0.2) = e⁻⁰·⁴ ≈ 0.6703

| Paso | xᵢ | yᵢ (Euler) | y exacta | Error absoluto |
|---|---|---|---|---|
| 0 | 0.0 | 1.0000 | 1.0000 | 0.0000 |
| 1 | 0.1 | 0.8000 | 0.8187 | 0.0187 |
| 2 | 0.2 | 0.6400 | 0.6703 | 0.0303 |

**Código (animación):** [`euler.py`](Codigos/euler.py)

**Código (método puro):** [`euler_metodo.py`](Codigos/euler_metodo.py)

---

### 2. Método de Runge-Kutta de Orden 4 (RK4)

#### Conceptos Teóricos

El Método de Runge-Kutta de cuarto orden (RK4) es uno de los métodos más utilizados en la práctica para resolver EDOs. A diferencia de Euler, que evalúa la pendiente en un solo punto, RK4 calcula **cuatro estimaciones de pendiente** dentro de cada subintervalo y las combina en un **promedio ponderado** para obtener una aproximación mucho más precisa.

Geométricamente, es como tomar muestras de la pendiente al inicio, dos veces en el punto medio y una vez al final del intervalo, logrando capturar mejor la curvatura de la solución real.

#### Fórmulas

Las cuatro pendientes se calculan como:

<p align="center">
  <img src="https://latex.codecogs.com/svg.latex?%5Ccolor%7Bwhite%7Dk_1%20%3D%20f(x_i%2C%20y_i)" alt="k1"/>
</p>

<p align="center">
  <img src="https://latex.codecogs.com/svg.latex?%5Ccolor%7Bwhite%7Dk_2%20%3D%20f%5Cleft(x_i%20%2B%20%5Cfrac%7Bh%7D%7B2%7D%2C%20%5C%3B%20y_i%20%2B%20%5Cfrac%7Bh%7D%7B2%7Dk_1%5Cright)" alt="k2"/>
</p>

<p align="center">
  <img src="https://latex.codecogs.com/svg.latex?%5Ccolor%7Bwhite%7Dk_3%20%3D%20f%5Cleft(x_i%20%2B%20%5Cfrac%7Bh%7D%7B2%7D%2C%20%5C%3B%20y_i%20%2B%20%5Cfrac%7Bh%7D%7B2%7Dk_2%5Cright)" alt="k3"/>
</p>

<p align="center">
  <img src="https://latex.codecogs.com/svg.latex?%5Ccolor%7Bwhite%7Dk_4%20%3D%20f(x_i%20%2B%20h%2C%20%5C%3B%20y_i%20%2B%20h%20%5Ccdot%20k_3)" alt="k4"/>
</p>

Y la fórmula de actualización es:

<p align="center">
  <img src="https://latex.codecogs.com/svg.latex?%5Ccolor%7Bwhite%7Dy_%7Bi%2B1%7D%20%3D%20y_i%20%2B%20%5Cfrac%7Bh%7D%7B6%7D%20%5Cleft(%20k_1%20%2B%202k_2%20%2B%202k_3%20%2B%20k_4%20%5Cright)" alt="RK4"/>
</p>

#### Análisis de Error

| Tipo de error | Orden |
|---|---|
| Error local de truncamiento | O(h⁵) |
| Error global acumulado | O(h⁴) |

RK4 es un método de **cuarto orden**, lo que significa que al reducir el paso a la mitad, el error global se reduce aproximadamente por un factor de 16. Es significativamente más preciso que Euler y Taylor de orden 2 para un mismo tamaño de paso.

#### Condiciones de Aplicación

- **Cuándo usarlo:** Es el método de elección cuando se necesita alta precisión sin recurrir a métodos adaptativos o implícitos. Funciona excelentemente para la mayoría de EDOs no rígidas.
- **Limitaciones:** Requiere **cuatro evaluaciones** de la función f por paso, lo cual lo hace más costoso computacionalmente que Euler o Taylor de orden 2. No es adecuado para ecuaciones rígidas (*stiff*).
- **Comparación:** Es mucho más preciso que Euler (orden 4 vs. orden 1) y que Taylor de orden 2, sin necesitar el cálculo explícito de derivadas parciales.

#### Ejemplo Numérico

Resolvamos la misma EDO: **dy/dx = -2y**, con **y(0) = 1**, usando **h = 0.1**.

**Iteración 1** (i = 0):
- x₀ = 0, y₀ = 1
- k₁ = f(0, 1) = -2(1) = -2
- k₂ = f(0.05, 1 + 0.05(-2)) = f(0.05, 0.9) = -2(0.9) = -1.8
- k₃ = f(0.05, 1 + 0.05(-1.8)) = f(0.05, 0.91) = -2(0.91) = -1.82
- k₄ = f(0.1, 1 + 0.1(-1.82)) = f(0.1, 0.818) = -2(0.818) = -1.636
- y₁ = 1 + (0.1/6)(-2 + 2(-1.8) + 2(-1.82) + (-1.636))
- y₁ = 1 + (0.1/6)(-2 - 3.6 - 3.64 - 1.636)
- y₁ = 1 + (0.1/6)(-10.876)
- y₁ = 1 - 0.18127 = **0.81873**
- Valor exacto: y(0.1) = e⁻⁰·² ≈ 0.81873

**Iteración 2** (i = 1):
- x₁ = 0.1, y₁ = 0.81873
- k₁ = -2(0.81873) = -1.63746
- k₂ = f(0.15, 0.81873 + 0.05(-1.63746)) = -2(0.73686) = -1.47371
- k₃ = f(0.15, 0.81873 + 0.05(-1.47371)) = -2(0.74504) = -1.49009
- k₄ = f(0.2, 0.81873 + 0.1(-1.49009)) = -2(0.66972) = -1.33944
- y₂ = 0.81873 + (0.1/6)(-1.63746 + 2(-1.47371) + 2(-1.49009) + (-1.33944))
- y₂ = 0.81873 + (0.1/6)(-8.90450)
- y₂ = 0.81873 - 0.14841 = **0.67032**
- Valor exacto: y(0.2) = e⁻⁰·⁴ ≈ 0.67032

| Paso | xᵢ | yᵢ (RK4) | y exacta | Error absoluto |
|---|---|---|---|---|
| 0 | 0.0 | 1.00000 | 1.00000 | 0.00000 |
| 1 | 0.1 | 0.81873 | 0.81873 | ≈ 0.00000 |
| 2 | 0.2 | 0.67032 | 0.67032 | ≈ 0.00000 |

Como se observa, RK4 reproduce la solución exacta con una precisión excepcional incluso con h = 0.1.

**Código (animación):** [`RK4.py`](Codigos/RK4.py)

**Código (método puro):** [`RK4_metodo.py`](Codigos/RK4_metodo.py)

---

### 3. Serie de Taylor de Orden 2

#### Conceptos Teóricos

El Método de Taylor de orden 2 se basa en la **expansión en serie de Taylor** de la función solución alrededor del punto actual. En lugar de usar solo la primera derivada (como Euler), incluye también el término de la **segunda derivada**, lo que permite capturar mejor la curvatura de la solución.

La idea matemática es aproximar la solución y(x) mediante los dos primeros términos de su serie de Taylor:

<p align="center">
  <img src="https://latex.codecogs.com/svg.latex?%5Ccolor%7Bwhite%7Dy(x%2Bh)%20%5Capprox%20y(x)%20%2B%20h%20%5Ccdot%20y%27(x)%20%2B%20%5Cfrac%7Bh%5E2%7D%7B2%7D%20%5Ccdot%20y%27%27(x)" alt="Taylor expansión"/>
</p>

Donde **y'(x) = f(x, y)** y **y''(x) = f'(x, y)** se obtiene derivando la función f respecto a x (aplicando la regla de la cadena).

#### Fórmulas

La fórmula iterativa del Método de Taylor de orden 2 es:

<p align="center">
  <img src="https://latex.codecogs.com/svg.latex?%5Ccolor%7Bwhite%7Dy_%7Bi%2B1%7D%20%3D%20y_i%20%2B%20h%20%5Ccdot%20f(x_i%2C%20y_i)%20%2B%20%5Cfrac%7Bh%5E2%7D%7B2%7D%20%5Ccdot%20f%27(x_i%2C%20y_i)" alt="Taylor Orden 2"/>
</p>

Donde la derivada total de f se calcula como:

<p align="center">
  <img src="https://latex.codecogs.com/svg.latex?%5Ccolor%7Bwhite%7Df%27(x%2C%20y)%20%3D%20%5Cfrac%7B%5Cpartial%20f%7D%7B%5Cpartial%20x%7D%20%2B%20%5Cfrac%7B%5Cpartial%20f%7D%7B%5Cpartial%20y%7D%20%5Ccdot%20f(x%2C%20y)" alt="Derivada total"/>
</p>

#### Análisis de Error

| Tipo de error | Orden |
|---|---|
| Error local de truncamiento | O(h³) |
| Error global acumulado | O(h²) |

Taylor de orden 2 es un método de **segundo orden**, lo que significa que al reducir el paso a la mitad, el error global se reduce aproximadamente por un factor de 4. Representa un punto intermedio de precisión entre Euler y RK4.

#### Condiciones de Aplicación

- **Cuándo usarlo:** Es útil cuando se puede calcular fácilmente la derivada total de f(x, y) y se necesita mayor precisión que Euler sin el costo computacional de RK4.
- **Limitaciones:** Requiere conocer y poder calcular analíticamente las **derivadas parciales** de f(x, y), lo cual puede ser complicado o inviable para funciones complejas.
- **Comparación:** Más preciso que Euler (orden 2 vs. orden 1) pero menos que RK4 (orden 2 vs. orden 4). La principal desventaja frente a RK4 es la necesidad de calcular derivadas explícitamente.

#### Ejemplo Numérico

Resolvamos la misma EDO: **dy/dx = -2y**, con **y(0) = 1**, usando **h = 0.1**.

Para esta EDO: f(x, y) = -2y, y la derivada total es:
- ∂f/∂x = 0
- ∂f/∂y = -2
- f'(x, y) = 0 + (-2)(-2y) = 4y

**Iteración 1** (i = 0):
- x₀ = 0, y₀ = 1
- f(x₀, y₀) = -2(1) = -2
- f'(x₀, y₀) = 4(1) = 4
- y₁ = 1 + 0.1(-2) + (0.01/2)(4)
- y₁ = 1 - 0.2 + 0.02 = **0.82**
- Valor exacto: y(0.1) = e⁻⁰·² ≈ 0.8187

**Iteración 2** (i = 1):
- x₁ = 0.1, y₁ = 0.82
- f(x₁, y₁) = -2(0.82) = -1.64
- f'(x₁, y₁) = 4(0.82) = 3.28
- y₂ = 0.82 + 0.1(-1.64) + (0.01/2)(3.28)
- y₂ = 0.82 - 0.164 + 0.0164 = **0.6724**
- Valor exacto: y(0.2) = e⁻⁰·⁴ ≈ 0.6703

| Paso | xᵢ | yᵢ (Taylor 2) | y exacta | Error absoluto |
|---|---|---|---|---|
| 0 | 0.0 | 1.0000 | 1.0000 | 0.0000 |
| 1 | 0.1 | 0.8200 | 0.8187 | 0.0013 |
| 2 | 0.2 | 0.6724 | 0.6703 | 0.0021 |

Se observa que la precisión es notablemente mejor que Euler, aunque inferior a RK4.

**Código (animación):** [`taylor.py`](Codigos/taylor.py)

**Código (método puro):** [`taylor_metodo.py`](Codigos/taylor_metodo.py)

---

##  Comparación General de los Métodos

| Característica | Euler | Taylor Orden 2 | RK4 |
|---|---|---|---|
| Orden de precisión global | O(h) | O(h²) | O(h⁴) |
| Evaluaciones de f por paso | 1 | 1 (+ derivadas) | 4 |
| Requiere derivadas de f | No | Sí | No |
| Facilidad de implementación | Muy fácil | Moderada | Moderada |
| Precisión | Baja | Media | Alta |
| Uso recomendado | Didáctico / aprox. rápida | Funciones con derivadas simples | Uso general / alta precisión |
