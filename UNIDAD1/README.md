# Unidad 1: Teoría de Errores y Fundamentos Numéricos

En esta primera unidad se abordan los conceptos fundamentales de los métodos numéricos, analizando principalmente las limitaciones computacionales y los tipos de errores que surgen al realizar aproximaciones matemáticas mediante programación.

---

## 🧠 Conceptos Teóricos: Tipos de Errores

### 1. División por Cero (Búsqueda de Raíces)
Este error se da en métodos abiertos como Newton-Raphson. Ocurre cuando la derivada de la función se vuelve cero (o muy cercana a cero), provocando una división por cero en la fórmula iterativa.

**Fórmula de iteración (Newton-Raphson):**
$$ x_{i+1} = x_i - \frac{f(x_i)}{f'(x_i)} $$
Si $f'(x_i) = 0$, la operación falla.

**Código:** [`Div_por_0.py`](Codigos/Div_por_0.py)

---

### 2. Error de Truncamiento (Ecuaciones Diferenciales)
Se ilustra clásicamente con métodos numéricos como Euler. Si el tamaño del paso ($h$) al discretizar un proceso continuo es demasiado grande, el error se acumula iteración tras iteración al truncar los términos de series de orden superior.

**Fórmula del método de Euler:**
$$ y_{i+1} = y_i + f(x_i, y_i)h $$

**Código:** [`Error_trunca.py`](Codigos/Error_trunca.py)

---

### 3. Subdesbordamiento Aritmético (Underflow)
Este error sucede cuando una operación genera un número tan minúsculo que la computadora pierde la capacidad de representarlo y lo redondea a `0.0`. Si ese valor luego se usa como divisor, causará una falla fatal en la ejecución del programa.

**Código:** [`underflow.py`](Codigos/underflow.py)

---

### 4. Falla de la Propiedad Asociativa en Coma Flotante
Demuestra que en programación, el orden en que se suman números de punto flotante de diferentes magnitudes altera el resultado. Sumar de una forma u otra provoca pérdidas significativas de precisión.

**Demostración:**
$$ (a + b) + c \neq a + (b + c) $$ 
(en precisión finita de coma flotante).

**Código:** [`falla_asosiativa.py`](Codigos/falla_asosiativa.py)

---

## 💻 Prácticas Adicionales (Python)

* 🐍 [`cramer.py`](./Codigos/cramer.py): Implementación de la Regla de Cramer para resolución de sistemas.

---

## 📝 Problemario de la Unidad

Aquí se encuentran los ejercicios prácticos resueltos a mano/documento sobre los temas de esta unidad:

👉 [Clic aquí para ver el Problemario de la Unidad 1](https://drive.google.com/file/d/1hkU41Ss2quZtRJRcbKP0robxbN_3qKiQ/view?usp=drive_link)