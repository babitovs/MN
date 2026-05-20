# Unidad 3: Sistemas de Ecuaciones Lineales

En esta tercera unidad abordamos la resolución de sistemas de ecuaciones lineales algebraicas. Nos centramos en el método exacto de Eliminación Gaussiana y en el análisis de los diferentes tipos de soluciones que pueden presentarse.

---

##  Conceptos Teóricos: Resolución de Sistemas Lineales

### 1. Eliminación Gaussiana

#### Conceptos Teóricos

Es un algoritmo fundamental en álgebra lineal para determinar las soluciones de un sistema de ecuaciones lineales **Ax = b**. Consiste en aplicar operaciones elementales por filas para transformar la matriz aumentada en una matriz triangular superior, seguida de sustitución hacia atrás.

El proceso se divide en dos fases:
1. **Eliminación hacia adelante:** Se eliminan los coeficientes por debajo de la diagonal principal mediante combinaciones lineales de filas, obteniendo una matriz triangular superior.
2. **Sustitución hacia atrás:** Se resuelven las variables de abajo hacia arriba, comenzando por la última ecuación (que tiene una sola incógnita).

#### Fórmulas

**Factor de eliminación (multiplicador):**

<p align="center">
  <img src="https://latex.codecogs.com/svg.latex?%5Ccolor%7Bwhite%7Dm_%7Bik%7D%20%3D%20%5Cfrac%7Ba_%7Bik%7D%7D%7Ba_%7Bkk%7D%7D" alt="Multiplicador"/>
</p>

**Operación de eliminación:**

<p align="center">
  <img src="https://latex.codecogs.com/svg.latex?%5Ccolor%7Bwhite%7Da_%7Bij%7D%5E%7B(new)%7D%20%3D%20a_%7Bij%7D%20-%20m_%7Bik%7D%20%5Ccdot%20a_%7Bkj%7D" alt="Eliminación"/>
</p>

**Fórmula de Sustitución hacia Atrás:**

<p align="center">
  <img src="https://latex.codecogs.com/svg.latex?%5Ccolor%7Bwhite%7Dx_i%20%3D%20%5Cfrac%7Bb_i%20-%20%5Csum_%7Bj%3Di%2B1%7D%5E%7Bn%7D%20a_%7Bij%7Dx_j%7D%7Ba_%7Bii%7D%7D" alt="Sustitución hacia atrás"/>
</p>

#### Análisis de Error

- **Complejidad:** O(n³/3) operaciones para la fase de eliminación y O(n²) para la sustitución hacia atrás.
- **Errores de redondeo:** Se acumulan durante las operaciones de eliminación, especialmente cuando los pivotes (elementos diagonales) son cercanos a cero.
- **Pivoteo parcial:** Se recomienda intercambiar filas para colocar el elemento de mayor valor absoluto como pivote, reduciendo los errores de redondeo.
- **Número de condición:** Si la matriz A está mal condicionada (κ(A) >> 1), pequeños errores en los datos producen grandes errores en la solución. El error relativo satisface:

<p align="center">
  <img src="https://latex.codecogs.com/svg.latex?%5Ccolor%7Bwhite%7D%5Cfrac%7B%5C%7C%5CDelta%20x%5C%7C%7D%7B%5C%7Cx%5C%7C%7D%20%5Cleq%20%5Ckappa(A)%20%5Ccdot%20%5Cfrac%7B%5C%7C%5CDelta%20b%5C%7C%7D%7B%5C%7Cb%5C%7C%7D" alt="Número de condición"/>
</p>

#### Condiciones de Aplicación

- **Cuándo usarlo:** Es el método estándar para resolver sistemas lineales de tamaño moderado. Es la base de muchos otros algoritmos (factorización LU, cálculo de determinantes, inversión de matrices).
- **Limitaciones:** No es eficiente para sistemas muy grandes y dispersos (se prefieren métodos iterativos como Gauss-Seidel o Jacobi). Si un pivote es cero y no se puede intercambiar filas, el método falla.
- **Comparación:** Más eficiente que la Regla de Cramer para n > 3. Más robusto con pivoteo parcial. Para sistemas muy grandes, los métodos iterativos pueden ser más apropiados.

#### Ejemplo Numérico

Resolver el sistema:
- 2x₁ + x₂ - x₃ = 8
- -3x₁ - x₂ + 2x₃ = -11
- -2x₁ + x₂ + 2x₃ = -3

**Matriz aumentada inicial:**

| | x₁ | x₂ | x₃ | b |
|---|---|---|---|---|
| F1 | 2 | 1 | -1 | 8 |
| F2 | -3 | -1 | 2 | -11 |
| F3 | -2 | 1 | 2 | -3 |

**Paso 1 — Eliminación (columna 1):**
- m₂₁ = -3/2 = -1.5 → F2 = F2 - (-1.5)F1 = F2 + 1.5·F1
  - F2: [0, 0.5, 0.5, 1]
- m₃₁ = -2/2 = -1 → F3 = F3 - (-1)F1 = F3 + F1
  - F3: [0, 2, 1, 5]

**Paso 2 — Eliminación (columna 2):**
- m₃₂ = 2/0.5 = 4 → F3 = F3 - 4·F2
  - F3: [0, 0, -1, 1]

**Matriz triangular superior:**

| | x₁ | x₂ | x₃ | b |
|---|---|---|---|---|
| F1 | 2 | 1 | -1 | 8 |
| F2 | 0 | 0.5 | 0.5 | 1 |
| F3 | 0 | 0 | -1 | 1 |

**Sustitución hacia atrás:**
- x₃ = 1/(-1) = **-1**
- x₂ = (1 - 0.5(-1))/0.5 = 1.5/0.5 = **3**
- x₁ = (8 - 1(3) - (-1)(-1))/2 = (8 - 3 - 1)/2 = 4/2 = **2**

**Solución: x₁ = 2, x₂ = 3, x₃ = -1**

**Verificación:** 2(2) + 3 - (-1) = 4 + 3 + 1 = 8 ✓

**Código Base:** [`EliminacionGaussiana.py`](Codigos/EliminacionGaussiana.py)
**Ejemplo Paso a Paso:** [`EjemploGaussiana.py`](Codigos/EjemploGaussiana.py)

---

### 2. Sistema Compatible Determinado

#### Conceptos Teóricos

El sistema tiene una **única solución**. Geométricamente (en 2D), representa líneas que se cruzan en un solo punto. En 3D, representa tres planos que se intersectan en un único punto. El método de Gauss procede sin problemas hasta encontrar los valores de cada variable.

#### Fórmulas

Un sistema es compatible determinado cuando el **rango de la matriz de coeficientes** es igual al **rango de la matriz aumentada** y ambos son iguales al **número de incógnitas**:

<p align="center">
  <img src="https://latex.codecogs.com/svg.latex?%5Ccolor%7Bwhite%7Drango(A)%20%3D%20rango(A%7Cb)%20%3D%20n" alt="Compatible determinado"/>
</p>

#### Análisis de Error

- En este caso, el determinante de A es **distinto de cero**: det(A) ≠ 0.
- La precisión de la solución depende del número de condición de la matriz: κ(A) = ||A|| · ||A⁻¹||.
- Si κ(A) es cercano a 1, el sistema está bien condicionado y la solución es fiable.

#### Condiciones de Aplicación

- **Cuándo ocurre:** Cuando todas las ecuaciones son linealmente independientes y el sistema tiene exactamente n ecuaciones con n incógnitas.
- **Verificación:** Se comprueba que det(A) ≠ 0, o equivalentemente, que tras la eliminación gaussiana no aparecen pivotes nulos.

#### Ejemplo Numérico

El sistema del ejemplo anterior es compatible determinado:
- 3 ecuaciones, 3 incógnitas
- det(A) ≠ 0
- Solución única: x₁ = 2, x₂ = 3, x₃ = -1

---

### 3. Sistema Compatible Indeterminado

#### Conceptos Teóricos

Ocurre cuando el sistema tiene **infinitas soluciones**. En el proceso de Gauss, una fila de la matriz aumentada se anula por completo (**0 = 0**), indicando que hay ecuaciones linealmente dependientes o redundantes. Geométricamente, en 2D esto significa líneas coincidentes; en 3D, planos que se intersectan en una recta o coinciden.

#### Fórmulas

La condición para un sistema indeterminado es:

<p align="center">
  <img src="https://latex.codecogs.com/svg.latex?%5Ccolor%7Bwhite%7Drango(A)%20%3D%20rango(A%7Cb)%20%3C%20n" alt="Compatible indeterminado"/>
</p>

Las variables libres (n - rango(A)) pueden tomar cualquier valor y las demás se expresan en función de ellas.

#### Análisis de Error

- det(A) = 0, lo que indica que la matriz es **singular**.
- No hay una solución única, por lo que no tiene sentido hablar de error de la solución en el sentido tradicional.
- El algoritmo de Gauss detecta esta situación cuando un pivote se anula y la fila correspondiente de la matriz aumentada es completamente nula.

#### Condiciones de Aplicación

- **Cuándo ocurre:** Cuando una o más ecuaciones son combinaciones lineales de otras. Hay más incógnitas que ecuaciones independientes.
- **Cómo se detecta:** Durante la eliminación gaussiana, al menos una fila se convierte en [0 0 ... 0 | 0].
- **Solución:** Se parametrizan las variables libres y se expresan las demás en función de ellas.

#### Ejemplo Numérico

Sistema:
- x + y + z = 6
- 2x + 2y + 2z = 12
- x + y + 2z = 8

**Eliminación:**
- F2 = F2 - 2·F1: [0, 0, 0 | 0] → fila nula (F2 es múltiplo de F1)
- F3 = F3 - F1: [0, 0, 1 | 2]

**Resultado:**
- z = 2
- x + y = 6 - 2 = 4 → x = 4 - t, y = t (para cualquier t ∈ ℝ)

**Solución general:** (4 - t, t, 2) con t libre. Infinitas soluciones.

**Código:** [`sistema_indeterminado.py`](Codigos/sistema_indeterminado.py)

---

### 4. Sistema Incompatible

#### Conceptos Teóricos

Se da cuando el sistema **no tiene solución** (ecuaciones contradictorias). Al aplicar Gauss, se llega a una situación absurda (por ejemplo, **0 = c**, donde **c ≠ 0**), lo que geométricamente significa líneas paralelas que nunca se cruzan (en 2D) o planos que no se intersectan en un punto común (en 3D).

#### Fórmulas

La condición para un sistema incompatible es:

<p align="center">
  <img src="https://latex.codecogs.com/svg.latex?%5Ccolor%7Bwhite%7Drango(A)%20%5Cneq%20rango(A%7Cb)" alt="Incompatible"/>
</p>

Esto ocurre porque la matriz aumentada tiene una fila de la forma [0 0 ... 0 | c] con c ≠ 0.

#### Análisis de Error

- No existe solución, por lo que no se puede calcular error.
- El sistema debe rechazarse o reformularse.
- En la práctica, esto se detecta automáticamente durante la eliminación gaussiana cuando se encuentra una fila contradictoria.

#### Condiciones de Aplicación

- **Cuándo ocurre:** Cuando las ecuaciones representan restricciones geométricas contradictorias (líneas paralelas, planos paralelos sin intersección).
- **Cómo se detecta:** Una fila de la forma [0 0 ... 0 | c] con c ≠ 0 durante la eliminación.
- **Acción recomendada:** Revisar la formulación del problema. En aplicaciones de ajuste de datos, usar mínimos cuadrados como alternativa.

#### Ejemplo Numérico

Sistema:
- x + y = 3
- 2x + 2y = 8

**Eliminación:**
- F2 = F2 - 2·F1: [0, 0 | 2]

Obtenemos: **0 = 2** → ¡Contradicción!

Geométricamente: la primera ecuación es la recta y = 3 - x, la segunda es y = 4 - x. Son rectas **paralelas** (misma pendiente, distinto intercepto). No se cruzan.

**El sistema no tiene solución.**

**Código:** [`sistema_incompatible.py`](Codigos/sistema_incompatible.py)

---

##  Prácticas Adicionales (Python)

* 🐍 [`gaussiana.py`](./Codigos/gaussiana.py) (y variaciones como `eliminacion_gaussiana.py`): Implementaciones y mejoras adicionales del método de eliminación.

---

##  Problemario de la Unidad

Aquí se encuentran los ejercicios prácticos resueltos sobre la aplicación manual de este método en diversos sistemas de ecuaciones:

👉 [Enlace al Problemario de la Unidad 3](https://drive.google.com/file/d/1QAKz5zaOGzR5Itj0MmPUoBxKQ__QZQ0_/view?usp=sharing)
