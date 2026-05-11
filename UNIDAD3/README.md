# Unidad 3: Sistemas de Ecuaciones Lineales

En esta tercera unidad abordamos la resolución de sistemas de ecuaciones lineales algebraicas. Nos centramos en el método exacto de Eliminación Gaussiana y en el análisis de los diferentes tipos de soluciones que pueden presentarse.

---

## 🧠 Conceptos Teóricos: Resolución de Sistemas Lineales

### 1. Eliminación Gaussiana
Es un algoritmo fundamental en álgebra lineal para determinar las soluciones de un sistema de ecuaciones lineales **Ax = b**. Consiste en aplicar operaciones elementales por filas para transformar la matriz aumentada en una matriz triangular superior, seguida de sustitución hacia atrás.

**Fórmula de Sustitución hacia Atrás:**

<p align="center">
  <img src="https://latex.codecogs.com/svg.latex?x_i%20%3D%20%5Cfrac%7Bb_i%20-%20%5Csum_%7Bj%3Di%2B1%7D%5E%7Bn%7D%20a_%7Bij%7Dx_j%7D%7Ba_%7Bii%7D%7D" alt="Sustitución hacia atrás"/>
</p>

**Código Base:** [`EliminacionGaussiana.py`](Codigos/EliminacionGaussiana.py)
**Ejemplo Paso a Paso:** [`EjemploGaussiana.py`](Codigos/EjemploGaussiana.py)

---

### 2. Sistema Compatible Determinado
El sistema tiene una **única solución**. Geométricamente (en 2D), representa líneas que se cruzan en un solo punto. El método de Gauss procede sin problemas hasta encontrar los valores de cada variable.

---

### 3. Sistema Compatible Indeterminado
Ocurre cuando el sistema tiene **infinitas soluciones**. En el proceso de Gauss, una fila de la matriz aumentada se anula por completo (**0 = 0**), indicando que hay ecuaciones linealmente dependientes o redundantes.

**Código:** [`sistema_indeterminado.py`](Codigos/sistema_indeterminado.py)

---

### 4. Sistema Incompatible
Se da cuando el sistema **no tiene solución** (ecuaciones contradictorias). Al aplicar Gauss, se llega a una situación absurda (por ejemplo, **0 = c**, donde **c ≠ 0**), lo que geométricamente significa líneas paralelas que nunca se cruzan.

**Código:** [`sistema_incompatible.py`](Codigos/sistema_incompatible.py)

---

## 💻 Prácticas Adicionales (Python)

* 🐍 [`gaussiana.py`](./Codigos/gaussiana.py) (y variaciones como `eliminacion_gaussiana.py`): Implementaciones y mejoras adicionales del método de eliminación.

---

## 📝 Problemario de la Unidad

Aquí se encuentran los ejercicios prácticos resueltos sobre la aplicación manual de este método en diversos sistemas de ecuaciones:

👉 [Enlace al Problemario de la Unidad 3](https://drive.google.com/file/d/1QAKz5zaOGzR5Itj0MmPUoBxKQ__QZQ0_/view?usp=sharing)
