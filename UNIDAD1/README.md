# Unidad 1: Teoría de Errores y Fundamentos Numéricos

En esta primera unidad se abordan los conceptos fundamentales de los métodos numéricos, analizando principalmente las limitaciones computacionales y los tipos de errores que surgen al realizar aproximaciones matemáticas mediante programación.

---

##  Conceptos Teóricos: Tipos de Errores

### 1. División por Cero (Búsqueda de Raíces)

#### Conceptos Teóricos
Este error se da en métodos abiertos como Newton-Raphson. Ocurre cuando la derivada de la función se vuelve cero (o muy cercana a cero), provocando una división por cero en la fórmula iterativa. El origen del problema está en que la tangente a la curva se vuelve horizontal, por lo que no intersecta al eje X en ningún punto finito.

#### Fórmulas

**Fórmula de iteración (Newton-Raphson):**

<p align="center">
  <img src="https://latex.codecogs.com/svg.latex?%5Ccolor%7Bwhite%7Dx_{i%2B1}%20%3D%20x_i%20-%20%5Cfrac%7Bf(x_i)%7D%7Bf%27(x_i)%7D" alt="Newton-Raphson"/>
</p>

Si **f'(xᵢ) = 0**, la operación falla.

#### Análisis de Error

Cuando **f'(xᵢ)** se aproxima a cero, el cociente tiende a infinito y el error se vuelve incontrolable. En aritmética de punto flotante, esto puede manifestarse como:
- Un valor `inf` o `nan` que detiene el cálculo.
- Un salto enorme que aleja la aproximación de la raíz real.

El error en este caso no se mide como truncamiento o redondeo, sino como un **error de singularidad** inherente al método cuando la derivada se anula.

#### Condiciones de Aplicación

- **Cuándo ocurre:** Al aplicar Newton-Raphson cerca de puntos donde la función tiene máximos, mínimos locales o puntos de inflexión (f'(x) = 0).
- **Cómo prevenirlo:** Verificar que |f'(xᵢ)| > ε (un umbral mínimo) antes de calcular la siguiente iteración, o utilizar un método alternativo como bisección en zonas conflictivas.
- **Limitaciones:** Ningún método abierto está libre de este riesgo; se debe validar siempre la derivada.

#### Ejemplo Numérico

Consideremos la función **f(x) = x³ - 2x + 2**, cuya derivada es **f'(x) = 3x² - 2**.

Si iniciamos con **x₀ = 0**:
- f(0) = 0 - 0 + 2 = 2
- f'(0) = 0 - 2 = -2
- x₁ = 0 - (2 / -2) = **1.0**

Si iniciamos con **x₀ = 0.8165** (cerca de donde f'(x) ≈ 0):
- f(0.8165) ≈ 0.9098
- f'(0.8165) = 3(0.8165)² - 2 ≈ **0.0003** (casi cero)
- x₁ = 0.8165 - (0.9098 / 0.0003) ≈ **-3032** → ¡divergencia total!

Esto demuestra que la cercanía de la derivada a cero genera una **falla catastrófica** del método.

**Código:** [`Div_por_0.py`](Codigos/Div_por_0.py)

---

### 2. Error de Truncamiento (Ecuaciones Diferenciales)

#### Conceptos Teóricos
Se ilustra clásicamente con métodos numéricos como Euler. Si el tamaño del paso (**h**) al discretizar un proceso continuo es demasiado grande, el error se acumula iteración tras iteración al truncar los términos de series de orden superior. Es la diferencia entre la solución exacta y la aproximación numérica obtenida al usar una cantidad finita de términos.

#### Fórmulas

**Fórmula del método de Euler:**

<p align="center">
  <img src="https://latex.codecogs.com/svg.latex?%5Ccolor%7Bwhite%7Dy_{i%2B1}%20%3D%20y_i%20%2B%20f(x_i%2C%20y_i)%20%5Ccdot%20h" alt="Euler"/>
</p>

**Error de truncamiento local (serie de Taylor):**

<p align="center">
  <img src="https://latex.codecogs.com/svg.latex?%5Ccolor%7Bwhite%7DE_t%20%3D%20%5Cfrac%7Bh%5E2%7D%7B2%7D%20y%27%27(%5Cxi)" alt="Error truncamiento"/>
</p>

#### Análisis de Error

- **Error local de truncamiento:** O(h²) — proviene de ignorar los términos de orden 2 y superiores en la serie de Taylor.
- **Error global acumulado:** O(h) — se acumula a lo largo de N = (b-a)/h pasos.
- Un paso **h** más pequeño reduce el error, pero aumenta el número de operaciones y puede introducir más error de redondeo.

#### Condiciones de Aplicación

- **Cuándo ocurre:** En cualquier método numérico que aproxime un proceso continuo mediante pasos discretos (Euler, RK, diferencias finitas, etc.).
- **Cómo minimizarlo:** Reducir el tamaño del paso h o usar métodos de orden superior (Taylor orden 2, RK4).
- **Limitaciones:** Reducir h indefinidamente no siempre mejora la precisión debido a la acumulación de errores de redondeo.

#### Ejemplo Numérico

Resolvamos **dy/dx = -y**, con **y(0) = 1**, solución exacta: **y(x) = e⁻ˣ**.

**Con h = 0.5:**
- y₁ = 1 + 0.5(-1) = **0.5** | Exacto: e⁻⁰·⁵ ≈ 0.6065 | Error: 0.1065
- y₂ = 0.5 + 0.5(-0.5) = **0.25** | Exacto: e⁻¹ ≈ 0.3679 | Error: 0.1179

**Con h = 0.1:**
- y₁ = 1 + 0.1(-1) = **0.9** | Exacto: e⁻⁰·¹ ≈ 0.9048 | Error: 0.0048
- y₂ = 0.9 + 0.1(-0.9) = **0.81** | Exacto: e⁻⁰·² ≈ 0.8187 | Error: 0.0087

Se observa que al reducir h de 0.5 a 0.1, el error se reduce significativamente.

**Código:** [`Error_trunca.py`](Codigos/Error_trunca.py)

---

### 3. Subdesbordamiento Aritmético (Underflow)

#### Conceptos Teóricos
Este error sucede cuando una operación genera un número tan minúsculo que la computadora pierde la capacidad de representarlo y lo redondea a `0.0`. Si ese valor luego se usa como divisor, causará una falla fatal en la ejecución del programa. Está directamente relacionado con los límites del estándar IEEE 754 para punto flotante.

#### Fórmulas

El número positivo más pequeño representable en punto flotante de doble precisión (64 bits) es:

<p align="center">
  <img src="https://latex.codecogs.com/svg.latex?%5Ccolor%7Bwhite%7Dx_%7Bmin%7D%20%5Capprox%202.225%20%5Ctimes%2010%5E%7B-308%7D" alt="Mínimo representable"/>
</p>

Cualquier valor menor que este será redondeado a 0.0 (underflow gradual o abrupto según la implementación).

#### Análisis de Error

- **Tipo de error:** Error de representación (underflow).
- No se trata de un error de truncamiento ni de redondeo clásico, sino de una **limitación del hardware** para representar números extremadamente pequeños.
- La magnitud del error puede ser del 100% cuando un valor no nulo se convierte en 0.0.
- Si el valor afectado se usa como divisor, produce una **división por cero** secundaria.

#### Condiciones de Aplicación

- **Cuándo ocurre:** En cálculos con exponenciales negativas muy grandes, factoriales, o productos de muchos números pequeños.
- **Cómo prevenirlo:** Trabajar en escala logarítmica cuando se manejan cantidades muy pequeñas; verificar que los denominadores no sean cero antes de dividir.
- **Limitaciones:** Es un problema inherente a la representación finita de números en cualquier lenguaje de programación.

#### Ejemplo Numérico

En Python (doble precisión):

```
x = 1e-300
y = x * 1e-10   # y = 1e-310 → representable (subnormal)
z = x * 1e-20   # z = 1e-320 → ¡UNDERFLOW! → z = 0.0

# Si luego dividimos:
resultado = 1.0 / z  # ZeroDivisionError: float division by zero
```

| Operación | Resultado | ¿Underflow? |
|---|---|---|
| 1e-300 × 1e-5 | 1e-305 | No |
| 1e-300 × 1e-10 | 1e-310 | No (subnormal) |
| 1e-300 × 1e-20 | 0.0 | **Sí** |

**Código:** [`underflow.py`](Codigos/underflow.py)

---

### 4. Falla de la Propiedad Asociativa en Coma Flotante

#### Conceptos Teóricos
Demuestra que en programación, el orden en que se suman números de punto flotante de diferentes magnitudes altera el resultado. Sumar de una forma u otra provoca pérdidas significativas de precisión. Esto ocurre porque al sumar un número muy grande con uno muy pequeño, el número pequeño puede "desaparecer" por la limitada cantidad de dígitos significativos disponibles.

#### Fórmulas

**Demostración:**

<p align="center">
  <img src="https://latex.codecogs.com/svg.latex?%5Ccolor%7Bwhite%7D(a%20%2B%20b)%20%2B%20c%20%5Cneq%20a%20%2B%20(b%20%2B%20c)" alt="Asociativa"/>
</p>

(en precisión finita de coma flotante).

Esto se debe a que en punto flotante de precisión finita, la suma no es asociativa cuando las magnitudes de los operandos difieren significativamente.

#### Análisis de Error

- **Tipo de error:** Error de redondeo por pérdida de dígitos significativos.
- **Magnitud:** El error relativo puede alcanzar valores de hasta ε_maq (épsilon de máquina, ≈ 2.22 × 10⁻¹⁶ en doble precisión) por cada operación que involucre cancelación catastrófica.
- La pérdida de asociatividad es mayor cuando |a| >> |b| o viceversa.

#### Condiciones de Aplicación

- **Cuándo ocurre:** Al sumar series largas de números con magnitudes muy diferentes, como en sumatorias de series de Taylor, cálculos financieros con montos dispares, o en productos punto de vectores.
- **Cómo minimizarlo:** Ordenar los sumandos de menor a mayor magnitud antes de sumar; usar aritmética de precisión arbitraria (como el módulo `decimal` en Python); emplear algoritmos de suma compensada (como la suma de Kahan).
- **Limitaciones:** Es un problema fundamental de la aritmética IEEE 754; no puede eliminarse completamente, solo mitigarse.

#### Ejemplo Numérico

Tomemos a = 1.0, b = 1e-16, c = 1e-16 en Python (doble precisión):

```
a = 1.0
b = 1e-16
c = 1e-16

resultado1 = (a + b) + c
# a + b = 1.0 (b se pierde por redondeo)
# resultado1 = 1.0 + 1e-16 = 1.0

resultado2 = a + (b + c)
# b + c = 2e-16
# resultado2 = 1.0 + 2e-16 = 1.0000000000000002

print(resultado1 == resultado2)  # False
```

| Agrupación | Resultado | ¿Preciso? |
|---|---|---|
| (a + b) + c | 1.0000000000000000 | No — se perdió b |
| a + (b + c) | 1.0000000000000002 | Más preciso |

**Código:** [`falla_asosiativa.py`](Codigos/falla_asosiativa.py)

---

### 5. Regla de Cramer (Resolución de Sistemas de Ecuaciones)

#### Conceptos Teóricos
La Regla de Cramer es un método algebraico para resolver sistemas de ecuaciones lineales de **n × n** que utiliza determinantes. Permite calcular cada variable del sistema como el cociente de dos determinantes: uno modificado (sustituyendo una columna por el vector de términos independientes) y el determinante del sistema original.

#### Fórmulas

Para un sistema **Ax = b**, cada variable se calcula como:

<p align="center">
  <img src="https://latex.codecogs.com/svg.latex?%5Ccolor%7Bwhite%7Dx_i%20%3D%20%5Cfrac%7B%5Cdet(A_i)%7D%7B%5Cdet(A)%7D" alt="Cramer"/>
</p>

Donde **Aᵢ** es la matriz A con la columna **i** reemplazada por el vector **b**.

Para un sistema 2×2:

<p align="center">
  <img src="https://latex.codecogs.com/svg.latex?%5Ccolor%7Bwhite%7Dx%20%3D%20%5Cfrac%7B%5Cbegin%7Bvmatrix%7D%20b_1%20%26%20a_%7B12%7D%20%5C%5C%20b_2%20%26%20a_%7B22%7D%20%5Cend%7Bvmatrix%7D%7D%7B%5Cbegin%7Bvmatrix%7D%20a_%7B11%7D%20%26%20a_%7B12%7D%20%5C%5C%20a_%7B21%7D%20%26%20a_%7B22%7D%20%5Cend%7Bvmatrix%7D%7D%2C%20%5Cquad%20y%20%3D%20%5Cfrac%7B%5Cbegin%7Bvmatrix%7D%20a_%7B11%7D%20%26%20b_1%20%5C%5C%20a_%7B21%7D%20%26%20b_2%20%5Cend%7Bvmatrix%7D%7D%7B%5Cbegin%7Bvmatrix%7D%20a_%7B11%7D%20%26%20a_%7B12%7D%20%5C%5C%20a_%7B21%7D%20%26%20a_%7B22%7D%20%5Cend%7Bvmatrix%7D%7D" alt="Cramer 2x2"/>
</p>

#### Análisis de Error

- **Error numérico:** Cramer depende del cálculo de determinantes, que puede sufrir de **cancelación catastrófica** para matrices mal condicionadas.
- **Complejidad:** Para un sistema n×n, se requieren (n+1) determinantes de tamaño n×n, lo que da una complejidad de O(n! · n) si se calcula por cofactores, o O(n³) usando métodos optimizados.
- El método es **numéricamente inestable** para sistemas grandes o con número de condición alto.

#### Condiciones de Aplicación

- **Cuándo usarlo:** Es ideal para sistemas pequeños (2×2 o 3×3) donde la solución analítica es práctica y rápida.
- **Limitaciones:** No debe usarse para sistemas grandes (n > 4) por su elevado costo computacional y su inestabilidad numérica. Para esos casos, se prefiere Eliminación Gaussiana o factorización LU.
- **Requisito obligatorio:** det(A) ≠ 0 (el sistema debe ser compatible determinado).

#### Ejemplo Numérico

Resolvamos el sistema:
- 2x + y = 5
- 3x - 2y = 4

**Paso 1:** Calcular det(A):
- det(A) = (2)(-2) - (1)(3) = -4 - 3 = **-7**

**Paso 2:** Calcular x:
- det(A₁) = (5)(-2) - (1)(4) = -10 - 4 = **-14**
- x = -14 / -7 = **2**

**Paso 3:** Calcular y:
- det(A₂) = (2)(4) - (5)(3) = 8 - 15 = **-7**
- y = -7 / -7 = **1**

**Verificación:** 2(2) + 1 = 5 ✓ | 3(2) - 2(1) = 4 ✓

**Código:** [`cramer.py`](Codigos/cramer.py)

---

## 📝 Problemario de la Unidad

Aquí se encuentran los ejercicios prácticos resueltos a mano/documento sobre los temas de esta unidad:

👉 [Clic aquí para ver el Problemario de la Unidad 1](https://drive.google.com/file/d/1hkU41Ss2quZtRJRcbKP0robxbN_3qKiQ/view?usp=drive_link)