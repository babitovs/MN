# Unidad 1: Teoría de Errores y Fundamentos Numéricos

En esta primera unidad se abordan los conceptos fundamentales de los métodos numéricos, analizando principalmente las limitaciones computacionales y los tipos de errores que surgen al realizar aproximaciones matemáticas mediante programación.

---

## 🧠 Conceptos Teóricos: Tipos de Errores

1. **División por Cero (Búsqueda de Raíces)**
   Este error se da en métodos abiertos como Newton-Raphson. Ocurre cuando la derivada de la función se vuelve cero (o muy cercana a cero), provocando una división por cero en la fórmula iterativa.

2. **Error de Truncamiento (Ecuaciones Diferenciales)**
   Se ilustra clásicamente con el método de Euler. Si el tamaño del paso (`h`) al discretizar un proceso continuo es demasiado grande, el error se acumula iteración tras iteración, alejando la simulación del resultado real matemático.

3. **Subdesbordamiento Aritmético (Underflow)**
   Este error sucede cuando una operación genera un número tan minúsculo que la computadora pierde la capacidad de representarlo y lo redondea a `0.0`. Si ese valor luego se usa como divisor, causará una falla fatal en la ejecución del programa.

4. **Falla de la Propiedad Asociativa en Coma Flotante**
   Demuestra que en programación, el orden en que se suman números de punto flotante de diferentes magnitudes altera el resultado. Sumar de una forma u otra provoca pérdidas significativas de precisión.

---

## 💻 Prácticas y Código (Python)

A continuación, se presentan los scripts desarrollados para demostrar y calcular los errores mencionados, además de implementaciones adicionales:

* 🐍 [`Div_por_0.py`](./Codigos/Div_por_0.py): Simulación del error de división por cero.
* 🐍 [`Error_trunca.py`](./Codigos/Error_trunca.py): Demostración de acumulación de error por truncamiento.
* 🐍 [`underflow.py`](./Codigos/underflow.py): Ejemplo de subdesbordamiento aritmético en la memoria.
* 🐍 [`falla_asosiativa.py`](./Codigos/falla_asosiativa.py): Comprobación de la pérdida de precisión al alterar el orden de suma.
* 🐍 [`cramer.py`](./Codigos/cramer.py): Implementación de la Regla de Cramer para resolución de sistemas.

---

## 📝 Problemario de la Unidad

Aquí se encuentran los ejercicios prácticos resueltos a mano/documento sobre los temas de esta unidad:

👉 [Clic aquí para ver el Problemario de la Unidad 1](#) *(Sustituye el "#" por tu link de Drive/OneDrive)*