# Unidad 5: Métodos de Interpolación

En esta unidad exploramos distintos métodos numéricos para estimar valores intermedios entre datos conocidos, utilizando técnicas de interpolación polinómica y segmentada. A continuación se describe cada método implementado en la carpeta de `Codigos`.

---

## 1. Interpolación Lineal

#### Conceptos Teóricos

La interpolación lineal es el método más básico y consiste en unir dos puntos mediante una línea recta. Se utiliza cuando se asume que la variación entre los puntos es constante (comportamiento lineal). Geométricamente, se traza un segmento de recta entre dos puntos conocidos y se evalúa la recta en el punto deseado.

Es el caso más simple de interpolación polinómica: se ajusta un polinomio de grado 1 a los datos.

#### Fórmulas

Dados dos puntos **(x₀, y₀)** y **(x₁, y₁)**, el valor de **y** para un punto **x** intermedio se calcula como:

<p align="center">
  <img src="https://latex.codecogs.com/svg.latex?%5Ccolor%7Bwhite%7Dy%20%3D%20y_0%20%2B%20%5Cfrac%7By_1%20-%20y_0%7D%7Bx_1%20-%20x_0%7D%20(x%20-%20x_0)" alt="Interpolación Lineal"/>
</p>

Esto es equivalente a:

<p align="center">
  <img src="https://latex.codecogs.com/svg.latex?%5Ccolor%7Bwhite%7Dy%20%3D%20%5Cfrac%7B(x%20-%20x_1)%7D%7B(x_0%20-%20x_1)%7D%20y_0%20%2B%20%5Cfrac%7B(x%20-%20x_0)%7D%7B(x_1%20-%20x_0)%7D%20y_1" alt="Lineal Lagrange"/>
</p>

#### Análisis de Error

- **Error de truncamiento:**

<p align="center">
  <img src="https://latex.codecogs.com/svg.latex?%5Ccolor%7Bwhite%7DE_t%20%3D%20%5Cfrac%7B(x%20-%20x_0)(x%20-%20x_1)%7D%7B2!%7D%20f%27%27(%5Cxi)" alt="Error lineal"/>
</p>

- **Orden:** O(h²) donde h = x₁ - x₀. El error depende de la segunda derivada de la función real (su curvatura).
- Para funciones **lineales**, el error es cero (interpolación exacta).
- Para funciones con alta curvatura (f'' grande), la interpolación lineal puede ser muy imprecisa.

#### Condiciones de Aplicación

- **Cuándo usarla:** Cuando se tienen solo dos puntos, cuando la función es aproximadamente lineal en el intervalo, o cuando se necesita una estimación rápida y sencilla.
- **Limitaciones:** No captura curvatura. Para funciones con comportamiento no lineal, el error puede ser significativo. Solo usa 2 puntos de datos.
- **Comparación:** Menos precisa que la interpolación cuadrática (Lagrange) y que la segmentada con muchos puntos. Es la más rápida y simple de todas.

#### Ejemplo Numérico

Dados los puntos **(1, 1)** y **(3, 9)** (de f(x) = x²), estimar **f(2)** (valor exacto: 4).

y = 1 + [(9 - 1) / (3 - 1)] × (2 - 1)
y = 1 + [8 / 2] × 1
y = 1 + 4 = **5**

Error: |5 - 4| = 1 (la interpolación lineal sobrestima porque ignora la curvatura).

| x | y (lineal) | y exacto (x²) | Error |
|---|---|---|---|
| 1.5 | 3.0 | 2.25 | 0.75 |
| 2.0 | 5.0 | 4.00 | 1.00 |
| 2.5 | 7.0 | 6.25 | 0.75 |

**Código:** [`interpolacion_lineal.py`](Codigos/interpolacion_lineal.py)

---

## 2. Interpolación Cuadrática (Método de Lagrange)

#### Conceptos Teóricos

La interpolación cuadrática aproxima los datos utilizando un polinomio de grado 2 (una parábola). El método de Lagrange nos proporciona una forma estructurada de encontrar este polinomio utilizando tres puntos conocidos: **(x₀, y₀)**, **(x₁, y₁)** y **(x₂, y₂)**.

A diferencia de la interpolación lineal, este método captura la **curvatura** de la función al usar un punto más, lo que generalmente resulta en una aproximación significativamente mejor.

#### Fórmulas

El polinomio de interpolación de Lagrange de grado 2 está dado por:

<p align="center">
  <img src="https://latex.codecogs.com/svg.latex?%5Ccolor%7Bwhite%7Dy%20%3D%20y_0%20%5Ccdot%20L_0(x)%20%2B%20y_1%20%5Ccdot%20L_1(x)%20%2B%20y_2%20%5Ccdot%20L_2(x)" alt="Lagrange"/>
</p>

Donde los polinomios base se calculan como:

<p align="center">
  <img src="https://latex.codecogs.com/svg.latex?%5Ccolor%7Bwhite%7DL_0(x)%20%3D%20%5Cfrac%7B(x%20-%20x_1)(x%20-%20x_2)%7D%7B(x_0%20-%20x_1)(x_0%20-%20x_2)%7D" alt="L0"/>
</p>

<p align="center">
  <img src="https://latex.codecogs.com/svg.latex?%5Ccolor%7Bwhite%7DL_1(x)%20%3D%20%5Cfrac%7B(x%20-%20x_0)(x%20-%20x_2)%7D%7B(x_1%20-%20x_0)(x_1%20-%20x_2)%7D" alt="L1"/>
</p>

<p align="center">
  <img src="https://latex.codecogs.com/svg.latex?%5Ccolor%7Bwhite%7DL_2(x)%20%3D%20%5Cfrac%7B(x%20-%20x_0)(x%20-%20x_1)%7D%7B(x_2%20-%20x_0)(x_2%20-%20x_1)%7D" alt="L2"/>
</p>

#### Análisis de Error

- **Error de truncamiento:**

<p align="center">
  <img src="https://latex.codecogs.com/svg.latex?%5Ccolor%7Bwhite%7DE_t%20%3D%20%5Cfrac%7B(x%20-%20x_0)(x%20-%20x_1)(x%20-%20x_2)%7D%7B3!%7D%20f%27%27%27(%5Cxi)" alt="Error cuadrática"/>
</p>

- **Orden:** O(h³) donde h es el espaciado entre puntos. El error depende de la tercera derivada de la función.
- Para funciones **cuadráticas** (f''' = 0), la interpolación es exacta.
- Aumentar el número de puntos no siempre mejora la precisión (fenómeno de Runge con puntos equiespaciados).

#### Condiciones de Aplicación

- **Cuándo usarla:** Cuando se tienen al menos 3 puntos de datos y la función muestra curvatura. Es el método más común para interpolación de precisión moderada.
- **Limitaciones:** Con 3 puntos fijos, solo puede capturar comportamiento parabólico. Para funciones con formas más complejas, se necesitan polinomios de mayor grado o interpolación segmentada.
- **Comparación:** Más precisa que la lineal (O(h³) vs. O(h²)). Para muchos puntos, los polinomios de grado alto pueden oscilar (fenómeno de Runge), por lo que la interpolación segmentada es preferible.

#### Ejemplo Numérico

Dados los puntos **(1, 1)**, **(2, 4)** y **(3, 9)** (de f(x) = x²), estimar **f(1.5)** (valor exacto: 2.25).

**Paso 1:** Calcular los polinomios base en x = 1.5:

L₀(1.5) = (1.5 - 2)(1.5 - 3) / [(1 - 2)(1 - 3)] = (-0.5)(-1.5) / [(-1)(-2)] = 0.75 / 2 = **0.375**

L₁(1.5) = (1.5 - 1)(1.5 - 3) / [(2 - 1)(2 - 3)] = (0.5)(-1.5) / [(1)(-1)] = -0.75 / -1 = **0.75**

L₂(1.5) = (1.5 - 1)(1.5 - 2) / [(3 - 1)(3 - 2)] = (0.5)(-0.5) / [(2)(1)] = -0.25 / 2 = **-0.125**

**Paso 2:** Calcular el valor interpolado:

y = 1(0.375) + 4(0.75) + 9(-0.125)
y = 0.375 + 3.0 - 1.125 = **2.25**

Error: |2.25 - 2.25| = **0.0** (exacto, ya que f(x) = x² es un polinomio de grado 2).

| x | y (lineal) | y (cuadrática) | y exacto | Error lineal | Error cuadrático |
|---|---|---|---|---|---|
| 1.5 | 2.5 | 2.25 | 2.25 | 0.25 | 0.00 |

**Código:** [`interpolacion_cuadratica.py`](Codigos/interpolacion_cuadratica.py) (Incluye la resolución paso a paso de los ejercicios).

---

## 3. Interpolación Segmentada

#### Conceptos Teóricos

La interpolación segmentada consiste en dividir el conjunto de datos en pequeños intervalos y aplicar interpolación de bajo grado (generalmente lineal o cuadrática) en cada uno de estos segmentos, en lugar de intentar ajustar un polinomio de grado alto a todos los puntos a la vez.

**Ventajas:**
* Evita el fenómeno de oscilación (como el fenómeno de Runge) que ocurre al usar polinomios de grado alto con muchos puntos.
* Es más estable para conjuntos de datos grandes.

En nuestra implementación, aplicamos **interpolación lineal por segmentos**: primero iteramos para encontrar en qué intervalo **[xᵢ, xᵢ₊₁]** se encuentra nuestro valor **x**, y luego aplicamos la fórmula de interpolación lineal únicamente sobre ese segmento.

#### Fórmulas

Para cada segmento [xᵢ, xᵢ₊₁], se aplica la interpolación lineal local:

<p align="center">
  <img src="https://latex.codecogs.com/svg.latex?%5Ccolor%7Bwhite%7Dy%20%3D%20y_i%20%2B%20%5Cfrac%7By_%7Bi%2B1%7D%20-%20y_i%7D%7Bx_%7Bi%2B1%7D%20-%20x_i%7D%20(x%20-%20x_i)%2C%20%5Cquad%20x%20%5Cin%20%5Bx_i%2C%20x_%7Bi%2B1%7D%5D" alt="Segmentada"/>
</p>

La función interpolante global es **continua** pero no necesariamente diferenciable en los puntos de unión (nodos).

#### Análisis de Error

- **Error por segmento:** O(hᵢ²) donde hᵢ = xᵢ₊₁ - xᵢ es el ancho del segmento i.
- **Error global:** O(h²) donde h = máx(hᵢ), es decir, el ancho del segmento más grande.
- A diferencia de un polinomio global de grado alto, el error **no crece** descontroladamente al aumentar el número de puntos.
- La **continuidad** está garantizada (la función es continua en los nodos), pero la **suavidad** no (puede haber "esquinas" en los puntos de unión).

#### Condiciones de Aplicación

- **Cuándo usarla:** Para conjuntos de datos grandes donde la interpolación polinómica global oscilaría. Es la estrategia preferida en la mayoría de aplicaciones prácticas (gráficos por computadora, CAD, análisis de datos experimentales).
- **Limitaciones:** La interpolación lineal por segmentos no es suave (C⁰ pero no C¹). Para suavidad, se requieren splines cúbicos (segmentada de grado 3).
- **Comparación:** Mucho más estable que la interpolación polinómica global para muchos puntos. Menos precisa localmente que Lagrange con los mismos datos, pero más robusta globalmente.

#### Ejemplo Numérico

Datos tabulados:

| x | 0 | 1 | 2 | 4 |
|---|---|---|---|---|
| y | 1 | 3 | 2 | 5 |

Estimar **f(1.5)** y **f(3)**.

**Para x = 1.5:** Pertenece al segmento [1, 2]
- y = 3 + [(2 - 3) / (2 - 1)] × (1.5 - 1)
- y = 3 + (-1)(0.5) = 3 - 0.5 = **2.5**

**Para x = 3:** Pertenece al segmento [2, 4]
- y = 2 + [(5 - 2) / (4 - 2)] × (3 - 2)
- y = 2 + (1.5)(1) = 2 + 1.5 = **3.5**

| x evaluado | Segmento | Valor interpolado |
|---|---|---|
| 0.5 | [0, 1] | 2.0 |
| 1.5 | [1, 2] | 2.5 |
| 3.0 | [2, 4] | 3.5 |

**Código:** [`interpolacion_segmentada.py`](Codigos/interpolacion_segmentada.py)
