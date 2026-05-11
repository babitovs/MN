# Unidad 5: Métodos de Interpolación

En esta unidad exploramos distintos métodos numéricos para estimar valores intermedios entre datos conocidos, utilizando técnicas de interpolación polinómica y segmentada. A continuación se describe cada método implementado en la carpeta de `Codigos`.

## 1. Interpolación Lineal

La interpolación lineal es el método más básico y consiste en unir dos puntos mediante una línea recta. Se utiliza cuando se asume que la variación entre los puntos es constante (comportamiento lineal).

**Fórmula:**
Dados dos puntos **(x₀, y₀)** y **(x₁, y₁)**, el valor de **y** para un punto **x** intermedio se calcula como:

<p align="center">
  <img src="https://latex.codecogs.com/svg.latex?y%20%3D%20y_0%20%2B%20%5Cfrac%7By_1%20-%20y_0%7D%7Bx_1%20-%20x_0%7D%20(x%20-%20x_0)" alt="Interpolación Lineal"/>
</p>

**Código:** [`interpolacion_lineal.py`](Codigos/interpolacion_lineal.py)

---

## 2. Interpolación Cuadrática (Método de Lagrange)

La interpolación cuadrática aproxima los datos utilizando un polinomio de grado 2 (una parábola). El método de Lagrange nos proporciona una forma estructurada de encontrar este polinomio utilizando tres puntos conocidos: **(x₀, y₀)**, **(x₁, y₁)** y **(x₂, y₂)**.

**Fórmulas:**
El polinomio de interpolación de Lagrange de grado 2 está dado por:

<p align="center">
  <img src="https://latex.codecogs.com/svg.latex?y%20%3D%20y_0%20%5Ccdot%20L_0(x)%20%2B%20y_1%20%5Ccdot%20L_1(x)%20%2B%20y_2%20%5Ccdot%20L_2(x)" alt="Lagrange"/>
</p>

Donde los polinomios base se calculan como:

<p align="center">
  <img src="https://latex.codecogs.com/svg.latex?L_0(x)%20%3D%20%5Cfrac%7B(x%20-%20x_1)(x%20-%20x_2)%7D%7B(x_0%20-%20x_1)(x_0%20-%20x_2)%7D" alt="L0"/>
</p>

<p align="center">
  <img src="https://latex.codecogs.com/svg.latex?L_1(x)%20%3D%20%5Cfrac%7B(x%20-%20x_0)(x%20-%20x_2)%7D%7B(x_1%20-%20x_0)(x_1%20-%20x_2)%7D" alt="L1"/>
</p>

<p align="center">
  <img src="https://latex.codecogs.com/svg.latex?L_2(x)%20%3D%20%5Cfrac%7B(x%20-%20x_0)(x%20-%20x_1)%7D%7B(x_2%20-%20x_0)(x_2%20-%20x_1)%7D" alt="L2"/>
</p>

**Código:** [`interpolacion_cuadratica.py`](Codigos/interpolacion_cuadratica.py) (Incluye la resolución paso a paso de los ejercicios).

---

## 3. Interpolación Segmentada

La interpolación segmentada consiste en dividir el conjunto de datos en pequeños intervalos y aplicar interpolación de bajo grado (generalmente lineal o cuadrática) en cada uno de estos segmentos, en lugar de intentar ajustar un polinomio de grado alto a todos los puntos a la vez.

**Ventajas:** 
* Evita el fenómeno de oscilación (como el fenómeno de Runge) que ocurre al usar polinomios de grado alto con muchos puntos.
* Es más estable para conjuntos de datos grandes.

En nuestra implementación, aplicamos **interpolación lineal por segmentos**: primero iteramos para encontrar en qué intervalo **[xᵢ, xᵢ₊₁]** se encuentra nuestro valor **x**, y luego aplicamos la fórmula de interpolación lineal únicamente sobre ese segmento.

**Código:** [`interpolacion_segmentada.py`](Codigos/interpolacion_segmentada.py)
