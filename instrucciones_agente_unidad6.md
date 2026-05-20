# Instrucciones para el Agente — Actualización README Unidad 6

## Contexto del Repositorio

Estás trabajando en el repositorio `Portafolio_MN`. El repositorio tiene la siguiente estructura general (que ya existe y debes respetar):

```
Portafolio_MN/
├── UNIDAD1/
│   ├── Codigos/
│   ├── img/
│   └── README.md
├── UNIDAD2/
│   ├── Codigos/
│   ├── img/
│   └── README.md
├── UNIDAD3/
│   ├── Codigos/
│   ├── animations.md
│   └── README.md
├── UNIDAD4/
│   ├── algotimos/
│   ├── Codigos/
│   ├── Problemario/
│   └── README.md
├── UNIDAD5/
│   ├── Codigos/
│   ├── img_recursos/
│   └── README.md
└── UNIDAD6/
    ├── Codigos/
    │   ├── euler.py
    │   ├── RK4.py
    │   └── taylor.py
    └── README.md   ← este es el archivo que debes modificar
```

---

## Tu Tarea

Modifica el archivo `UNIDAD6/README.md` para que siga la **misma estructura visual y de contenido** que tienen los README de las demás unidades del portafolio.

Antes de escribir, **lee primero los README de las otras unidades** para extraer el estilo, formato, jerarquía de encabezados y convenciones visuales que usan, y luego replica ese mismo estilo en el README de la Unidad 6.

---

## Contenido que debe tener el README de la Unidad 6

La Unidad 6 pertenece a la materia de **Métodos Numéricos** y cubre el tema de **Solución de Ecuaciones Diferenciales Ordinarias (EDOs)**. Los tres métodos que se deben documentar son:

1. **Método de Euler**
2. **Método de Runge-Kutta de orden 4 (RK4)**
3. **Serie de Taylor de orden 2**

---

## Estructura requerida para cada método

Cada uno de los tres métodos debe contener las siguientes secciones, en este orden:

### 1. Conceptos Teóricos
- Explicar en qué consiste el método.
- Describir la idea geométrica o matemática detrás de él.
- Indicar qué tipo de problema resuelve (EDO de la forma `dy/dx = f(x, y)` con condición inicial).

### 2. Fórmulas
- Presentar las fórmulas matemáticas principales del método usando notación LaTeX en Markdown (bloques `$$...$$`).
- Para **Euler**: fórmula iterativa `y_{i+1} = y_i + h * f(x_i, y_i)`.
- Para **RK4**: las cuatro pendientes k1, k2, k3, k4 y la fórmula de actualización.
- Para **Taylor orden 2**: la fórmula con primera y segunda derivada `y_{i+1} = y_i + h*f + (h²/2)*f'`.

### 3. Análisis de Error
- Explicar el tipo de error local y global del método.
- Indicar el orden de truncamiento:
  - Euler: O(h) global, O(h²) local.
  - RK4: O(h⁴) global, O(h⁵) local.
  - Taylor orden 2: O(h²) global, O(h³) local.
- Mencionar brevemente cómo afecta el tamaño del paso `h` a la precisión.

### 4. Condiciones de Aplicación
- Indicar cuándo es apropiado usar el método.
- Mencionar limitaciones o desventajas.
- Comparar brevemente con los otros métodos si aplica (por ejemplo: Euler es simple pero menos preciso; RK4 es más costoso pero más exacto).

### 5. Ejemplo Numérico
- Incluir un ejemplo concreto resuelto paso a paso.
- Usar una EDO sencilla, por ejemplo: `dy/dx = -2y`, `y(0) = 1`, con `h = 0.1`, calculando al menos 2 iteraciones.
- Mostrar los valores numéricos de cada paso del método.
- Comparar (si es posible) con la solución analítica exacta.

### 6. Código
- Al final de cada sección de método, agregar un enlace al archivo de código correspondiente dentro de `Codigos/`:
  - Euler → `Codigos/euler.py`
  - RK4 → `Codigos/RK4.py`
  - Taylor → `Codigos/taylor.py`
- Usar el mismo formato de enlace que usan los otros README del portafolio.

---

## Restricciones importantes

- **No modifiques** ningún archivo fuera de `UNIDAD6/README.md`.
- **No modifiques** los archivos `.py` dentro de `Codigos/`.
- Respeta el estilo de los otros README: si usan HTML dentro del Markdown, emojis, badges, tablas, o algún componente visual específico, replícalo en el README de la Unidad 6.
- El idioma de todo el contenido debe ser **español**.
- Asegúrate de que el archivo quede bien formateado y que los bloques LaTeX se rendericen correctamente en GitHub Markdown.

---

## Resumen de lo que debe quedar al terminar

El archivo `UNIDAD6/README.md` debe:
- Tener la misma apariencia y estructura que los README de las demás unidades.
- Documentar los tres métodos: Euler, RK4 y Taylor orden 2.
- Incluir para cada uno: conceptos teóricos, fórmulas LaTeX, análisis de error, condiciones de aplicación, ejemplo numérico resuelto y enlace al código.
- Estar escrito completamente en español.
