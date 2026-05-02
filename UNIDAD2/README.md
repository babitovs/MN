# Unidad 2: Métodos de Búsqueda de Raíces (Ecuaciones No Lineales)

En esta segunda unidad nos enfocamos en la resolución de ecuaciones algebraicas y trascendentes. El objetivo principal es encontrar las raíces de una función matemática mediante aproximaciones numéricas, utilizando tanto métodos cerrados (con intervalos) como métodos abiertos.

---

## 🧠 Conceptos Teóricos: Métodos Numéricos

1. **Método de Bisección (Cerrado)**
   Es un método robusto pero lento. Se basa en el teorema del valor intermedio, dividiendo repetidamente a la mitad un intervalo que contiene la raíz hasta acotar el error a una tolerancia deseada.

2. **Método de la Falsa Posición / Regula Falsi (Cerrado)**
   Similar a la bisección, pero en lugar de dividir el intervalo a la mitad, une los puntos extremos del intervalo con una línea recta y usa la intersección con el eje X como la nueva aproximación. Suele converger más rápido que la bisección.

3. **Método de Newton-Raphson (Abierto)**
   Uno de los métodos más rápidos y utilizados. A partir de una estimación inicial (un solo punto), utiliza la derivada de la función (la pendiente de la recta tangente) para proyectar una intersección en el eje X, acercándose rápidamente a la raíz. 

4. **Método de la Secante (Abierto)**
   Es una alternativa a Newton-Raphson que no requiere calcular la derivada analítica de la función (lo cual a veces es muy difícil). En su lugar, aproxima la derivada utilizando una línea secante que pasa por dos puntos iniciales.

---

## 💻 Prácticas y Código (Python)

A continuación, se presentan los scripts desarrollados para automatizar la búsqueda de raíces con cada uno de los métodos estudiados:

* 🐍 [`Biseccion.py`](./Codigos/Biseccion.py): Implementación del método de Bisección buscando el cambio de signo.
* 🐍 [`Falsa_posicion.py`](./Codigos/Falsa_posicion.py): Código para el método de la Falsa Posición.
* 🐍 [`newton_r.py`](./Codigos/newton_r.py): Implementación de Newton-Raphson usando la función y su derivada.
* 🐍 [`secante.py`](./Codigos/secante.py): Código del método de la Secante usando dos aproximaciones iniciales.

---

## 📝 Problemario de la Unidad

Aquí se encuentran los ejercicios prácticos resueltos sobre la aplicación manual y comprobación de estos métodos:

👉 [Clic aquí para ver el Problemario de la Unidad 2](https://docs.google.com/spreadsheets/d/1U-aCeb3EvohoChZQm3W79aWKl9u6HLWw/edit?usp=sharing&ouid=102675729823874484334&rtpof=true&sd=true) 