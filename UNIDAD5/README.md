# Unidad 5: Métodos de Interpolación

En esta unidad exploramos distintos métodos numéricos para estimar valores intermedios entre datos conocidos, utilizando técnicas de interpolación polinómica y segmentada. A continuación se describe cada método implementado en la carpeta de `Codigos`.

## 1. Interpolación Lineal

La interpolación lineal es el método más básico y consiste en unir dos puntos mediante una línea recta. Se utiliza cuando se asume que la variación entre los puntos es constante (comportamiento lineal).

**Fórmula:**
Dados dos puntos $(x_0, y_0)$ y $(x_1, y_1)$, el valor de $y$ para un punto $x$ intermedio se calcula como:

$$ y = y_0 + \frac{y_1 - y_0}{x_1 - x_0} (x - x_0) $$

**Código:** [`interpolacion_lineal.py`](Codigos/interpolacion_lineal.py)

---

## 2. Interpolación Cuadrática (Método de Lagrange)

La interpolación cuadrática aproxima los datos utilizando un polinomio de grado 2 (una parábola). El método de Lagrange nos proporciona una forma estructurada de encontrar este polinomio utilizando tres puntos conocidos: $(x_0, y_0)$, $(x_1, y_1)$ y $(x_2, y_2)$.

**Fórmulas:**
El polinomio de interpolación de Lagrange de grado 2 está dado por:

$$ y = y_0 \cdot L_0(x) + y_1 \cdot L_1(x) + y_2 \cdot L_2(x) $$

Donde los polinomios base $L_i(x)$ se calculan como:

$$ L_0(x) = \frac{(x - x_1)(x - x_2)}{(x_0 - x_1)(x_0 - x_2)} $$

$$ L_1(x) = \frac{(x - x_0)(x - x_2)}{(x_1 - x_0)(x_1 - x_2)} $$

$$ L_2(x) = \frac{(x - x_0)(x - x_1)}{(x_2 - x_0)(x_2 - x_1)} $$

**Código:** [`interpolacion_cuadratica.py`](Codigos/interpolacion_cuadratica.py) (Incluye la resolución paso a paso de los ejercicios).

---

## 3. Interpolación Segmentada

La interpolación segmentada consiste en dividir el conjunto de datos en pequeños intervalos y aplicar interpolación de bajo grado (generalmente lineal o cuadrática) en cada uno de estos segmentos, en lugar de intentar ajustar un polinomio de grado alto a todos los puntos a la vez.

**Ventajas:** 
* Evita el fenómeno de oscilación (como el fenómeno de Runge) que ocurre al usar polinomios de grado alto con muchos puntos.
* Es más estable para conjuntos de datos grandes.

En nuestra implementación, aplicamos **interpolación lineal por segmentos**: primero iteramos para encontrar en qué intervalo $[x_i, x_{i+1}]$ se encuentra nuestro valor $x$, y luego aplicamos la fórmula de interpolación lineal únicamente sobre ese segmento.

**Código:** [`interpolacion_segmentada.py`](Codigos/interpolacion_segmentada.py)
