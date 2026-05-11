# Unidad 4: Diferenciación e Integración Numérica

En esta cuarta unidad abordamos las técnicas para aproximar la derivada y la integral definida de funciones matemáticas utilizando métodos numéricos. Esto es muy útil cuando se trabaja con datos tabulados o con funciones complejas.

---

## 🧠 Conceptos Teóricos: Diferenciación Numérica

Se basa en aproximar la pendiente (derivada) utilizando diferencias finitas.

### 1. Diferencias Hacia Adelante y Hacia Atrás
Aproximan la derivada evaluando la función en el punto actual y un punto posterior o anterior.

**Fórmula (Hacia Adelante):**

<p align="center">
  <img src="https://latex.codecogs.com/svg.latex?%5Ccolor%7Bwhite%7Df%27(x_i)%20%5Capprox%20%5Cfrac%7Bf(x_%7Bi%2B1%7D)%20-%20f(x_i)%7D%7Bh%7D" alt="Hacia Adelante"/>
</p>

**Fórmula (Hacia Atrás):**

<p align="center">
  <img src="https://latex.codecogs.com/svg.latex?%5Ccolor%7Bwhite%7Df%27(x_i)%20%5Capprox%20%5Cfrac%7Bf(x_i)%20-%20f(x_%7Bi-1%7D)%7D%7Bh%7D" alt="Hacia Atrás"/>
</p>

**Códigos:** [`hacia_adelante.py`](Codigos/hacia_adelante.py), [`hacia_atras.py`](Codigos/hacia_atras.py)

---

### 2. Diferencias Centradas
Equilibra el error utilizando un punto anterior y uno posterior para mayor precisión.

**Fórmula:**

<p align="center">
  <img src="https://latex.codecogs.com/svg.latex?%5Ccolor%7Bwhite%7Df%27(x_i)%20%5Capprox%20%5Cfrac%7Bf(x_%7Bi%2B1%7D)%20-%20f(x_%7Bi-1%7D)%7D%7B2h%7D" alt="Centrada"/>
</p>

**Código:** [`centrada.py`](Codigos/centrada.py)

---

### 3. Fórmulas de 3 Puntos
Utilizan tres puntos de evaluación para minimizar aún más el error de truncamiento.

**Fórmula (3 Puntos Hacia Adelante):**

<p align="center">
  <img src="https://latex.codecogs.com/svg.latex?%5Ccolor%7Bwhite%7Df%27(x_i)%20%5Capprox%20%5Cfrac%7B-3f(x_i)%20%2B%204f(x_%7Bi%2B1%7D)%20-%20f(x_%7Bi%2B2%7D)%7D%7B2h%7D" alt="3 Puntos"/>
</p>

**Código:** [`formula_3_puntos.py`](Codigos/formula_3_puntos.py)

---

## 🧠 Conceptos Teóricos: Integración Numérica (Newton-Cotes)

Métodos para aproximar el área bajo la curva de una función.

### 4. Regla del Trapecio
Aproxima el área bajo la curva uniendo los puntos con líneas rectas, formando trapecios. Es el más básico.

**Fórmula:**

<p align="center">
  <img src="https://latex.codecogs.com/svg.latex?%5Ccolor%7Bwhite%7D%5Cint_a%5Eb%20f(x)%20%5C%2C%20dx%20%5Capprox%20(b-a)%20%5Cfrac%7Bf(a)%20%2B%20f(b)%7D%7B2%7D" alt="Trapecio"/>
</p>

**Código:** [`trapecio.py`](Codigos/trapecio.py)

---

### 5. Regla de Simpson 1/3
Utiliza polinomios de segundo grado (parábolas) para conectar series de tres puntos. Altamente precisa, pero requiere un número par de intervalos.

**Fórmula:**

<p align="center">
  <img src="https://latex.codecogs.com/svg.latex?%5Ccolor%7Bwhite%7D%5Cint_%7Bx_0%7D%5E%7Bx_2%7D%20f(x)%20%5C%2C%20dx%20%5Capprox%20%5Cfrac%7Bh%7D%7B3%7D%20%5Bf(x_0)%20%2B%204f(x_1)%20%2B%20f(x_2)%5D" alt="Simpson 1/3"/>
</p>

**Código:** [`simson1_3.py`](Codigos/simson1_3.py)

---

### 6. Regla de Simpson 3/8
Utiliza polinomios de tercer grado (cúbicos). Se aplica típicamente cuando la cantidad de segmentos evaluados es múltiplo de 3.

**Fórmula:**

<p align="center">
  <img src="https://latex.codecogs.com/svg.latex?%5Ccolor%7Bwhite%7D%5Cint_%7Bx_0%7D%5E%7Bx_3%7D%20f(x)%20%5C%2C%20dx%20%5Capprox%20%5Cfrac%7B3h%7D%7B8%7D%20%5Bf(x_0)%20%2B%203f(x_1)%20%2B%203f(x_2)%20%2B%20f(x_3)%5D" alt="Simpson 3/8"/>
</p>

**Código:** [`simpson38.py`](Codigos/simpson38.py)

---

## 📝 Problemario de la Unidad

Aquí se encuentran los ejercicios prácticos resueltos a mano o en documento:

👉 [Enlace al Problemario de la Unidad 4](https://drive.google.com/file/d/1Mc7tDKgipwPgc0xZjn1tuNDzN3_1NgIl/view?usp=sharing)