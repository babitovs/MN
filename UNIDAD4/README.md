# Unidad 4: Diferenciación e Integración Numérica

En esta cuarta unidad abordamos las técnicas para aproximar la derivada y la integral definida de funciones matemáticas utilizando métodos numéricos. Esto es muy útil cuando se trabaja con datos tabulados o con funciones complejas.

---

##  Conceptos Teóricos: Diferenciación Numérica

Se basa en aproximar la pendiente (derivada) utilizando diferencias finitas.

### 1. Diferencias Hacia Adelante y Hacia Atrás

#### Conceptos Teóricos

Aproximan la derivada evaluando la función en el punto actual y un punto posterior (hacia adelante) o anterior (hacia atrás). La idea geométrica es calcular la pendiente de una recta secante que pasa por dos puntos cercanos de la función, como una aproximación de la pendiente de la tangente.

- **Diferencia hacia adelante:** Usa el punto actual y el siguiente.
- **Diferencia hacia atrás:** Usa el punto actual y el anterior.

#### Fórmulas

**Fórmula (Hacia Adelante):**

<p align="center">
  <img src="https://latex.codecogs.com/svg.latex?%5Ccolor%7Bwhite%7Df%27(x_i)%20%5Capprox%20%5Cfrac%7Bf(x_%7Bi%2B1%7D)%20-%20f(x_i)%7D%7Bh%7D" alt="Hacia Adelante"/>
</p>

**Fórmula (Hacia Atrás):**

<p align="center">
  <img src="https://latex.codecogs.com/svg.latex?%5Ccolor%7Bwhite%7Df%27(x_i)%20%5Capprox%20%5Cfrac%7Bf(x_i)%20-%20f(x_%7Bi-1%7D)%7D%7Bh%7D" alt="Hacia Atrás"/>
</p>

#### Análisis de Error

- **Error de truncamiento:** O(h) para ambas fórmulas. El error proviene de truncar la serie de Taylor después del primer término:

<p align="center">
  <img src="https://latex.codecogs.com/svg.latex?%5Ccolor%7Bwhite%7DE_t%20%3D%20-%5Cfrac%7Bh%7D%7B2%7Df%27%27(%5Cxi)" alt="Error adelante/atrás"/>
</p>

- Al reducir h a la mitad, el error se reduce aproximadamente a la mitad.
- Un h demasiado pequeño puede introducir errores de redondeo significativos (cancelación catastrófica en el numerador).

#### Condiciones de Aplicación

- **Cuándo usarlos:** Son los más simples de implementar. La diferencia hacia adelante es útil cuando solo se tienen datos a la derecha del punto; la diferencia hacia atrás, cuando solo se tienen datos a la izquierda.
- **Limitaciones:** Precisión limitada (orden 1). No son simétricas respecto al punto de evaluación, lo que introduce un sesgo en la aproximación.
- **Comparación:** Menos precisas que la diferencia centrada (O(h²)) y que las fórmulas de 3 puntos.

#### Ejemplo Numérico

Dada **f(x) = x²**, calcular **f'(2)** con **h = 0.1** (valor exacto: f'(2) = 4).

**Hacia Adelante:**
- f'(2) ≈ [f(2.1) - f(2)] / 0.1 = [4.41 - 4] / 0.1 = 0.41 / 0.1 = **4.1**
- Error: |4.1 - 4| = 0.1

**Hacia Atrás:**
- f'(2) ≈ [f(2) - f(1.9)] / 0.1 = [4 - 3.61] / 0.1 = 0.39 / 0.1 = **3.9**
- Error: |3.9 - 4| = 0.1

| Método | Aproximación | Error absoluto |
|---|---|---|
| Hacia Adelante | 4.1 | 0.1 |
| Hacia Atrás | 3.9 | 0.1 |
| Valor exacto | 4.0 | — |

**Códigos:** [`hacia_adelante.py`](Codigos/hacia_adelante.py), [`hacia_atras.py`](Codigos/hacia_atras.py)

---

### 2. Diferencias Centradas

#### Conceptos Teóricos

Equilibra el error utilizando un punto anterior y uno posterior para mayor precisión. Geométricamente, se calcula la pendiente de la recta secante que pasa por los dos puntos vecinos, lo cual da una mejor aproximación de la tangente al ser simétrica respecto al punto central.

#### Fórmulas

<p align="center">
  <img src="https://latex.codecogs.com/svg.latex?%5Ccolor%7Bwhite%7Df%27(x_i)%20%5Capprox%20%5Cfrac%7Bf(x_%7Bi%2B1%7D)%20-%20f(x_%7Bi-1%7D)%7D%7B2h%7D" alt="Centrada"/>
</p>

#### Análisis de Error

- **Error de truncamiento:** O(h²). Es un orden completo más precisa que las diferencias hacia adelante y hacia atrás:

<p align="center">
  <img src="https://latex.codecogs.com/svg.latex?%5Ccolor%7Bwhite%7DE_t%20%3D%20-%5Cfrac%7Bh%5E2%7D%7B6%7Df%27%27%27(%5Cxi)" alt="Error centrada"/>
</p>

- Al reducir h a la mitad, el error se reduce aproximadamente por un factor de 4.

#### Condiciones de Aplicación

- **Cuándo usarlo:** Siempre que se disponga de datos a ambos lados del punto de evaluación. Es la opción predeterminada recomendada para diferenciación numérica.
- **Limitaciones:** No puede aplicarse en los extremos de un conjunto de datos tabulados (no hay punto anterior o posterior disponible).
- **Comparación:** Más precisa que adelante/atrás (O(h²) vs. O(h)), pero menos que las fórmulas de 3 puntos con extremo incluido. Requiere dos evaluaciones de f por punto.

#### Ejemplo Numérico

Dada **f(x) = x²**, calcular **f'(2)** con **h = 0.1** (valor exacto: 4).

- f'(2) ≈ [f(2.1) - f(1.9)] / (2 × 0.1)
- f'(2) ≈ [4.41 - 3.61] / 0.2 = 0.80 / 0.2 = **4.0**
- Error: |4.0 - 4| = **0.0** (exacto para polinomios de grado ≤ 2)

Para f(x) = x³, f'(2) exacto = 12, con h = 0.1:
- f'(2) ≈ [f(2.1) - f(1.9)] / 0.2 = [9.261 - 6.859] / 0.2 = 2.402 / 0.2 = **12.01**
- Error: |12.01 - 12| = 0.01

**Código:** [`centrada.py`](Codigos/centrada.py)

---

### 3. Fórmulas de 3 Puntos

#### Conceptos Teóricos

Utilizan tres puntos de evaluación para minimizar aún más el error de truncamiento. Estas fórmulas se derivan de ajustar un polinomio de grado 2 a tres puntos y derivarlo. Son especialmente útiles en los **extremos** de una tabla de datos donde no se puede usar la fórmula centrada.

#### Fórmulas

**Fórmula (3 Puntos Hacia Adelante — extremo izquierdo):**

<p align="center">
  <img src="https://latex.codecogs.com/svg.latex?%5Ccolor%7Bwhite%7Df%27(x_i)%20%5Capprox%20%5Cfrac%7B-3f(x_i)%20%2B%204f(x_%7Bi%2B1%7D)%20-%20f(x_%7Bi%2B2%7D)%7D%7B2h%7D" alt="3 Puntos"/>
</p>

**Fórmula (3 Puntos Hacia Atrás — extremo derecho):**

<p align="center">
  <img src="https://latex.codecogs.com/svg.latex?%5Ccolor%7Bwhite%7Df%27(x_i)%20%5Capprox%20%5Cfrac%7Bf(x_%7Bi-2%7D)%20-%204f(x_%7Bi-1%7D)%20%2B%203f(x_i)%7D%7B2h%7D" alt="3 Puntos atrás"/>
</p>

#### Análisis de Error

- **Error de truncamiento:** O(h²), igual que la centrada, pero aplicable en los extremos.

<p align="center">
  <img src="https://latex.codecogs.com/svg.latex?%5Ccolor%7Bwhite%7DE_t%20%3D%20%5Cfrac%7Bh%5E2%7D%7B3%7Df%27%27%27(%5Cxi)" alt="Error 3 puntos"/>
</p>

- Estas fórmulas sacrifican la simetría para poder evaluarse en los bordes de la tabla de datos.

#### Condiciones de Aplicación

- **Cuándo usarlas:** En los extremos de una tabla de datos donde la diferencia centrada no es aplicable. La versión "hacia adelante" se usa al inicio de la tabla y la versión "hacia atrás" al final.
- **Limitaciones:** Aunque tienen error O(h²) como la centrada, la constante del error puede ser mayor, haciéndolas ligeramente menos precisas para puntos interiores.
- **Comparación:** Misma precisión asintótica que la centrada, pero diseñadas para puntos extremos. Más precisas que las fórmulas de 1er orden (adelante/atrás simples).

#### Ejemplo Numérico

Dada **f(x) = eˣ**, calcular **f'(0)** con **h = 0.1** (valor exacto: f'(0) = e⁰ = 1).

Usando la fórmula de 3 puntos hacia adelante con x₀ = 0:
- f(0) = 1.0000
- f(0.1) = e⁰·¹ = 1.10517
- f(0.2) = e⁰·² = 1.22140

f'(0) ≈ [-3(1.0000) + 4(1.10517) - 1.22140] / (2 × 0.1)
f'(0) ≈ [-3.0000 + 4.42068 - 1.22140] / 0.2
f'(0) ≈ 0.19928 / 0.2 = **0.9964**

| Método | Aproximación | Error absoluto |
|---|---|---|
| Hacia adelante (O(h)) | 1.0517 | 0.0517 |
| 3 puntos (O(h²)) | 0.9964 | 0.0036 |
| Valor exacto | 1.0000 | — |

La fórmula de 3 puntos reduce el error en más de un orden de magnitud.

**Código:** [`formula_3_puntos.py`](Codigos/formula_3_puntos.py)

---

##  Conceptos Teóricos: Integración Numérica (Newton-Cotes)

Métodos para aproximar el área bajo la curva de una función.

### 4. Regla del Trapecio

#### Conceptos Teóricos

Aproxima el área bajo la curva uniendo los puntos con líneas rectas, formando trapecios. Es el más básico de los métodos de integración numérica. La idea es reemplazar la función curva por una línea recta entre los límites de integración y calcular el área del trapecio resultante.

#### Fórmulas

**Fórmula simple (un solo trapecio):**

<p align="center">
  <img src="https://latex.codecogs.com/svg.latex?%5Ccolor%7Bwhite%7D%5Cint_a%5Eb%20f(x)%20%5C%2C%20dx%20%5Capprox%20(b-a)%20%5Cfrac%7Bf(a)%20%2B%20f(b)%7D%7B2%7D" alt="Trapecio"/>
</p>

**Fórmula compuesta (n subintervalos):**

<p align="center">
  <img src="https://latex.codecogs.com/svg.latex?%5Ccolor%7Bwhite%7D%5Cint_a%5Eb%20f(x)%20%5C%2C%20dx%20%5Capprox%20%5Cfrac%7Bh%7D%7B2%7D%20%5Cleft%5B%20f(x_0)%20%2B%202%5Csum_%7Bi%3D1%7D%5E%7Bn-1%7D%20f(x_i)%20%2B%20f(x_n)%20%5Cright%5D" alt="Trapecio compuesto"/>
</p>

#### Análisis de Error

- **Error de truncamiento (fórmula simple):**

<p align="center">
  <img src="https://latex.codecogs.com/svg.latex?%5Ccolor%7Bwhite%7DE_t%20%3D%20-%5Cfrac%7B(b-a)%5E3%7D%7B12%7Df%27%27(%5Cxi)" alt="Error trapecio"/>
</p>

- **Error de la fórmula compuesta:** O(h²). Al duplicar el número de subintervalos, el error se reduce por un factor de 4.
- Es **exacta** para polinomios de grado ≤ 1 (funciones lineales).

#### Condiciones de Aplicación

- **Cuándo usarlo:** Cuando se necesita una aproximación rápida y sencilla, o cuando los datos vienen tabulados con pocos puntos. Es la base conceptual de métodos más avanzados.
- **Limitaciones:** Precisión baja para funciones con mucha curvatura. Requiere muchos subintervalos para obtener buena precisión en funciones no lineales.
- **Comparación:** Menos preciso que Simpson 1/3 y 3/8. No requiere número par de intervalos (ventaja sobre Simpson 1/3).

#### Ejemplo Numérico

Calcular la integral de **f(x) = x²** de 0 a 1 (valor exacto: 1/3 ≈ 0.3333).

**Con 1 trapecio (n = 1, h = 1):**
- I ≈ (1-0) × [f(0) + f(1)] / 2 = 1 × [0 + 1] / 2 = **0.5**
- Error: |0.5 - 0.3333| = 0.1667

**Con 2 trapecios (n = 2, h = 0.5):**
- I ≈ (0.5/2) × [f(0) + 2f(0.5) + f(1)] = 0.25 × [0 + 2(0.25) + 1] = 0.25 × 1.5 = **0.375**
- Error: |0.375 - 0.3333| = 0.0417

| n (subintervalos) | h | Aproximación | Error |
|---|---|---|---|
| 1 | 1.0 | 0.5000 | 0.1667 |
| 2 | 0.5 | 0.3750 | 0.0417 |
| 4 | 0.25 | 0.3438 | 0.0104 |

**Código:** [`trapecio.py`](Codigos/trapecio.py)

---

### 5. Regla de Simpson 1/3

#### Conceptos Teóricos

Utiliza polinomios de segundo grado (parábolas) para conectar series de tres puntos. En lugar de aproximar la curva con una línea recta (como el trapecio), se ajusta una parábola que pasa por tres puntos consecutivos y se calcula el área bajo esa parábola. Esto resulta en una aproximación mucho más precisa.

#### Fórmulas

**Fórmula simple:**

<p align="center">
  <img src="https://latex.codecogs.com/svg.latex?%5Ccolor%7Bwhite%7D%5Cint_%7Bx_0%7D%5E%7Bx_2%7D%20f(x)%20%5C%2C%20dx%20%5Capprox%20%5Cfrac%7Bh%7D%7B3%7D%20%5Bf(x_0)%20%2B%204f(x_1)%20%2B%20f(x_2)%5D" alt="Simpson 1/3"/>
</p>

**Fórmula compuesta (n subintervalos, n par):**

<p align="center">
  <img src="https://latex.codecogs.com/svg.latex?%5Ccolor%7Bwhite%7D%5Cint_a%5Eb%20f(x)%20%5C%2C%20dx%20%5Capprox%20%5Cfrac%7Bh%7D%7B3%7D%20%5Cleft%5B%20f(x_0)%20%2B%204%5Csum_%7Bi%3Dimpar%7D%20f(x_i)%20%2B%202%5Csum_%7Bi%3Dpar%7D%20f(x_i)%20%2B%20f(x_n)%20%5Cright%5D" alt="Simpson 1/3 compuesto"/>
</p>

#### Análisis de Error

- **Error de truncamiento (fórmula simple):**

<p align="center">
  <img src="https://latex.codecogs.com/svg.latex?%5Ccolor%7Bwhite%7DE_t%20%3D%20-%5Cfrac%7Bh%5E5%7D%7B90%7Df%5E%7B(4)%7D(%5Cxi)" alt="Error Simpson 1/3"/>
</p>

- **Error de la fórmula compuesta:** O(h⁴). Es dos órdenes más precisa que el trapecio.
- Es **exacta** para polinomios de grado ≤ 3 (a pesar de usar parábolas de grado 2).

#### Condiciones de Aplicación

- **Cuándo usarla:** Es la regla de integración numérica más utilizada por su excelente relación precisión/costo. Es ideal para funciones suaves.
- **Limitaciones:** Requiere un **número par de subintervalos** (n par). Si n es impar, se debe combinar con la regla de Simpson 3/8 o usar trapecio para un segmento.
- **Comparación:** Mucho más precisa que el trapecio (O(h⁴) vs. O(h²)). Ligeramente más precisa que Simpson 3/8 en general. Es el método de integración numérica preferido para uso general.

#### Ejemplo Numérico

Calcular la integral de **f(x) = x²** de 0 a 1 con **n = 2** (h = 0.5). Valor exacto: 1/3 ≈ 0.3333.

- x₀ = 0, x₁ = 0.5, x₂ = 1
- f(0) = 0, f(0.5) = 0.25, f(1) = 1

I ≈ (0.5/3) × [f(0) + 4f(0.5) + f(1)]
I ≈ (0.5/3) × [0 + 4(0.25) + 1]
I ≈ (0.1667) × [0 + 1 + 1]
I ≈ 0.1667 × 2 = **0.3333**

| Método | n | Aproximación | Error |
|---|---|---|---|
| Trapecio | 2 | 0.3750 | 0.0417 |
| Simpson 1/3 | 2 | 0.3333 | **0.0000** |

Simpson 1/3 da resultado **exacto** para este polinomio de grado 2.

**Código:** [`simson1_3.py`](Codigos/simson1_3.py)

---

### 6. Regla de Simpson 3/8

#### Conceptos Teóricos

Utiliza polinomios de tercer grado (cúbicos) para conectar series de cuatro puntos. Se aplica típicamente cuando la cantidad de segmentos evaluados es múltiplo de 3. Es una variante de la regla de Simpson que utiliza un punto más por segmento, logrando una precisión comparable pero con mayor flexibilidad en el número de intervalos.

#### Fórmulas

**Fórmula simple:**

<p align="center">
  <img src="https://latex.codecogs.com/svg.latex?%5Ccolor%7Bwhite%7D%5Cint_%7Bx_0%7D%5E%7Bx_3%7D%20f(x)%20%5C%2C%20dx%20%5Capprox%20%5Cfrac%7B3h%7D%7B8%7D%20%5Bf(x_0)%20%2B%203f(x_1)%20%2B%203f(x_2)%20%2B%20f(x_3)%5D" alt="Simpson 3/8"/>
</p>

#### Análisis de Error

- **Error de truncamiento (fórmula simple):**

<p align="center">
  <img src="https://latex.codecogs.com/svg.latex?%5Ccolor%7Bwhite%7DE_t%20%3D%20-%5Cfrac%7B3h%5E5%7D%7B80%7Df%5E%7B(4)%7D(%5Cxi)" alt="Error Simpson 3/8"/>
</p>

- **Error de la fórmula compuesta:** O(h⁴), mismo orden que Simpson 1/3.
- Es **exacta** para polinomios de grado ≤ 3.

#### Condiciones de Aplicación

- **Cuándo usarla:** Cuando el número de subintervalos es **múltiplo de 3** (n = 3, 6, 9, ...). También se usa como complemento de Simpson 1/3 cuando n es impar: se aplica Simpson 3/8 a los últimos 3 segmentos y Simpson 1/3 al resto.
- **Limitaciones:** Ligeramente menos precisa que Simpson 1/3 para el mismo h (la constante del error es mayor). Requiere una evaluación más de la función por aplicación.
- **Comparación:** Mismo orden de precisión que Simpson 1/3 (O(h⁴)). Más precisa que el trapecio. Su principal ventaja es la flexibilidad con números impares de intervalos.

#### Ejemplo Numérico

Calcular la integral de **f(x) = x³** de 0 a 3 con **n = 3** (h = 1). Valor exacto: 3⁴/4 = 81/4 = 20.25.

- x₀ = 0, x₁ = 1, x₂ = 2, x₃ = 3
- f(0) = 0, f(1) = 1, f(2) = 8, f(3) = 27

I ≈ (3 × 1/8) × [f(0) + 3f(1) + 3f(2) + f(3)]
I ≈ (3/8) × [0 + 3(1) + 3(8) + 27]
I ≈ 0.375 × [0 + 3 + 24 + 27]
I ≈ 0.375 × 54 = **20.25**

| Método | Aproximación | Error |
|---|---|---|
| Trapecio (n=3) | 20.25 | variable |
| Simpson 3/8 | 20.25 | **0.0000** |

Simpson 3/8 da resultado **exacto** para este polinomio de grado 3.

**Código:** [`simpson38.py`](Codigos/simpson38.py)

---

##  Problemario de la Unidad

Aquí se encuentran los ejercicios prácticos resueltos a mano o en documento:

👉 [Enlace al Problemario de la Unidad 4](https://drive.google.com/file/d/1Mc7tDKgipwPgc0xZjn1tuNDzN3_1NgIl/view?usp=sharing)