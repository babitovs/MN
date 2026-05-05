# Unidad 3: Sistemas de Ecuaciones Lineales

En esta tercera unidad abordamos la resolución de sistemas de ecuaciones lineales algebraicas. El objetivo principal es encontrar los valores de las incógnitas que satisfacen múltiples ecuaciones simultáneamente, centrándonos en el método exacto de Eliminación Gaussiana y analizando los diferentes tipos de soluciones que pueden presentarse.

---

## 🧠 Conceptos Teóricos: Resolución de Sistemas Lineales

1. **Eliminación Gaussiana**
   Es un algoritmo fundamental en álgebra lineal para determinar las soluciones de un sistema de ecuaciones lineales. Consiste en aplicar operaciones elementales por filas para transformar la matriz aumentada del sistema en una matriz triangular superior, lo que permite resolver las incógnitas mediante sustitución hacia atrás.

2. **Sistema Compatible Determinado**
   Es aquel sistema de ecuaciones que tiene una única solución. Geométricamente, en un sistema de dos variables, representa líneas que se intersecan en un solo punto. El método de eliminación de Gauss procede sin problemas hasta encontrar los valores de cada variable.

3. **Sistema Compatible Indeterminado**
   Ocurre cuando el sistema tiene infinitas soluciones. En el proceso de eliminación gaussiana, esto se detecta cuando una fila de la matriz aumentada se anula por completo (se vuelve toda de ceros), indicando que hay ecuaciones redundantes o linealmente dependientes.

4. **Sistema Incompatible**
   Se da cuando el sistema de ecuaciones no tiene ninguna solución (las ecuaciones son contradictorias). Al aplicar Gauss, se llega a una situación absurda (por ejemplo, `0 = constante no nula`), lo que geométricamente significa que las líneas o planos nunca se cruzan.

---

## 💻 Prácticas y Código (Python)

A continuación, se presentan los scripts desarrollados para resolver sistemas de ecuaciones lineales y demostrar los diferentes casos que se pueden presentar:

* 🐍 [`EliminacionGaussiana.py`](./Codigos/EliminacionGaussiana.py): Implementación del algoritmo base de Eliminación Gaussiana.
* 🐍 [`EjemploGaussiana.py`](./Codigos/EjemploGaussiana.py): Ejemplo práctico de resolución de un sistema paso a paso.
* 🐍 [`sistema_indeterminado.py`](./Codigos/sistema_indeterminado.py): Demostración de un sistema con infinitas soluciones (filas redundantes).
* 🐍 [`sistema_incompatible.py`](./Codigos/sistema_incompatible.py): Demostración de un sistema sin solución (ecuaciones contradictorias).
* 🐍 [`gaussiana.py`](./Codigos/gaussiana.py) (y variaciones): Implementaciones adicionales y mejoras del método de eliminación.

---

## 📝 Problemario de la Unidad

Aquí se encuentran los ejercicios prácticos resueltos sobre la aplicación manual de este método en diversos sistemas de ecuaciones:

👉 [Enlace pendiente al Problemario de la Unidad 3](https://drive.google.com/file/d/1QAKz5zaOGzR5Itj0MmPUoBxKQ__QZQ0_/view?usp=sharing) 
