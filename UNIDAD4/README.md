# Unidad 4: Diferenciación e Integración Numérica

En esta cuarta unidad abordamos las técnicas para aproximar la derivada y la integral definida de funciones matemáticas utilizando métodos numéricos. Esto es muy útil cuando se trabaja con datos tabulados o con funciones complejas.

---

## 🧠 Conceptos Teóricos: Diferenciación Numérica

Se basa en aproximar la pendiente (derivada) utilizando diferencias finitas.

### 1. Diferencias Hacia Adelante y Hacia Atrás
Aproximan la derivada evaluando la función en el punto actual y un punto posterior o anterior.

**Fórmula (Hacia Adelante):**
$$ f'(x_i) \approx \frac{f(x_{i+1}) - f(x_i)}{h} $$

**Fórmula (Hacia Atrás):**
$$ f'(x_i) \approx \frac{f(x_i) - f(x_{i-1})}{h} $$

**Códigos:** [`hacia_adelante.py`](Codigos/hacia_adelante.py), [`hacia_atras.py`](Codigos/hacia_atras.py)

---

### 2. Diferencias Centradas
Equilibra el error utilizando un punto anterior y uno posterior para mayor precisión.

**Fórmula:**
$$ f'(x_i) \approx \frac{f(x_{i+1}) - f(x_{i-1})}{2h} $$

**Código:** [`centrada.py`](Codigos/centrada.py)

---

### 3. Fórmulas de 3 Puntos
Utilizan tres puntos de evaluación para minimizar aún más el error de truncamiento.

**Fórmulas (Adelante/Atrás 3 puntos):**
$$ f'(x_i) \approx \frac{-3f(x_i) + 4f(x_{i+1}) - f(x_{i+2})}{2h} $$

**Código:** [`formula_3_puntos.py`](Codigos/formula_3_puntos.py)

---

## 🧠 Conceptos Teóricos: Integración Numérica (Newton-Cotes)

Métodos para aproximar el área bajo la curva de una función.

### 4. Regla del Trapecio
Aproxima el área bajo la curva uniendo los puntos con líneas rectas, formando trapecios. Es el más básico.

**Fórmula:**
$$ \int_a^b f(x) \, dx \approx (b - a) \frac{f(a) + f(b)}{2} $$

**Código:** [`trapecio.py`](Codigos/trapecio.py)

---

### 5. Regla de Simpson 1/3
Utiliza polinomios de segundo grado (parábolas) para conectar series de tres puntos. Altamente precisa, pero requiere un número par de intervalos.

**Fórmula (para un intervalo simple de 3 puntos):**
$$ \int_{x_0}^{x_2} f(x) \, dx \approx \frac{h}{3} [f(x_0) + 4f(x_1) + f(x_2)] $$

**Código:** [`simson1_3.py`](Codigos/simson1_3.py)

---

### 6. Regla de Simpson 3/8
Utiliza polinomios de tercer grado (cúbicos). Se aplica típicamente cuando la cantidad de segmentos evaluados es múltiplo de 3.

**Fórmula (para un intervalo simple de 4 puntos):**
$$ \int_{x_0}^{x_3} f(x) \, dx \approx \frac{3h}{8} [f(x_0) + 3f(x_1) + 3f(x_2) + f(x_3)] $$

**Código:** [`simpson38.py`](Codigos/simpson38.py)

---

## 📝 Problemario de la Unidad

Aquí se encuentran los ejercicios prácticos resueltos a mano o en documento:

👉 [Enlace al Problemario de la Unidad 4](https://drive.google.com/file/d/1Mc7tDKgipwPgc0xZjn1tuNDzN3_1NgIl/view?usp=sharing)