# Unidad 4: Diferenciación e Integración Numérica

En esta cuarta unidad abordamos las técnicas para aproximar la derivada y la integral definida de funciones matemáticas utilizando métodos numéricos. Esto es especialmente útil cuando se trabaja con datos tabulados (puntos discretos) o con funciones cuya integración o derivación analítica es muy compleja o imposible.

---

## 🧠 Conceptos Teóricos: Métodos Numéricos

### Diferenciación Numérica
Se basa en aproximar la pendiente (derivada) de una función utilizando diferencias finitas.
1. **Diferencias Hacia Adelante / Atrás**: Aproximan la derivada evaluando la función en el punto actual y un punto posterior (hacia adelante) o en un punto anterior (hacia atrás).
2. **Diferencias Centradas**: Aproximan la derivada utilizando un punto anterior y uno posterior. Esto equilibra el error y ofrece generalmente una mayor precisión.
3. **Fórmulas de 3 Puntos**: Fórmulas que utilizan más puntos de evaluación (tres en lugar de dos) para minimizar el error de truncamiento y obtener un cálculo más exacto.

### Integración Numérica (Cuadratura de Newton-Cotes)
Métodos para aproximar el área bajo la curva de una función definida en un intervalo.
4. **Regla del Trapecio**: Aproxima el área bajo la curva uniendo los puntos con líneas rectas, formando trapecios. Es el método más básico pero menos preciso.
5. **Regla de Simpson 1/3**: Utiliza polinomios de segundo grado (parábolas) para conectar series de tres puntos y aproximar la integral. Es considerablemente más precisa que el trapecio.
6. **Regla de Simpson 3/8**: Utiliza polinomios de tercer grado (cúbicos) para conectar puntos. Se aplica cuando se necesita otra variante en el número de intervalos evaluados.

---

## 💻 Prácticas y Código (Python)

A continuación, se presentan los scripts desarrollados para aplicar las fórmulas numéricas:

**Diferenciación Numérica:**
* 🐍 [`hacia_adelante.py`](./Codigos/hacia_adelante.py): Diferencias finitas hacia adelante.
* 🐍 [`hacia_atras.py`](./Codigos/hacia_atras.py): Diferencias finitas hacia atrás.
* 🐍 [`centrada.py`](./Codigos/centrada.py): Diferencias finitas centradas.
* 🐍 [`formula_3_puntos.py`](./Codigos/formula_3_puntos.py): Implementación de las fórmulas de derivación de 3 puntos.

**Integración Numérica:**
* 🐍 [`trapecio.py`](./Codigos/trapecio.py): Implementación de la Regla del Trapecio.
* 🐍 [`simson1_3.py`](./Codigos/simson1_3.py): Implementación de la Regla de Simpson 1/3.
* 🐍 [`simpson38.py`](./Codigos/simpson38.py): Implementación de la Regla de Simpson 3/8.

---

## 📝 Problemario de la Unidad

Aquí se encuentran los ejercicios prácticos resueltos a mano o en documento sobre la aplicación de las diferentes fórmulas de derivación e integración:

👉 [Enlace pendiente al Problemario de la Unidad 4](#)