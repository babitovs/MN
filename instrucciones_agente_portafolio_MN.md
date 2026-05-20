# Instrucciones para el Agente — Estandarización de READMEs del Portafolio de Métodos Numéricos

## Contexto del Repositorio

Estás trabajando en el repositorio `Portafolio_MN`. El repositorio tiene la siguiente estructura (ya existente, no la modifiques):

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
    └── README.md
```

---

## Tu Tarea General

Tu objetivo es **estandarizar los README de todas las unidades (UNIDAD1 a UNIDAD6)** para que todas sigan la misma estructura de contenido definida más abajo.

### Proceso que debes seguir para cada unidad:

1. **Lee el README actual** de la unidad.
2. **Identifica los métodos o temas** que ya están documentados en él.
3. **Detecta qué secciones faltan** comparando contra la estructura requerida.
4. **Lista los archivos de código** disponibles dentro de su carpeta `Codigos/` para saber qué enlaces agregar.
5. **Aplica solo los cambios necesarios**: si una sección ya existe y está bien, consérvala tal como está; si falta, agrégala; si está incompleta, complétala.
6. **No reescribas contenido que ya esté correcto** — el objetivo es completar, no reemplazar.

Trabaja unidad por unidad en orden: UNIDAD1, UNIDAD2, UNIDAD3, UNIDAD4, UNIDAD5, UNIDAD6.

---

## Estructura Estándar Requerida para cada README

Cada README debe tener las siguientes secciones **por cada método o tema que cubra la unidad**:

### Sección por método — en este orden:

#### 1. Conceptos Teóricos
- Explicar en qué consiste el método.
- Describir la idea matemática o geométrica detrás de él.
- Indicar qué tipo de problema resuelve.

#### 2. Fórmulas
- Presentar las fórmulas matemáticas principales usando notación LaTeX en bloques `$$...$$`.
- Incluir todas las expresiones relevantes del método (fórmula iterativa, coeficientes auxiliares, etc.).

#### 3. Análisis de Error
- Explicar el error de truncamiento local y global del método.
- Indicar el orden del método (O(hⁿ)).
- Mencionar cómo afecta el tamaño del paso a la precisión y estabilidad.

#### 4. Condiciones de Aplicación
- Indicar cuándo es apropiado usar el método.
- Mencionar sus limitaciones o desventajas.
- Comparar brevemente con otros métodos de la misma unidad si aplica.

#### 5. Ejemplo Numérico
- Incluir un ejemplo concreto resuelto paso a paso con valores numéricos reales.
- Mostrar al menos 2 iteraciones del proceso.
- Comparar con la solución exacta o analítica cuando sea posible.

#### 6. Código
- Agregar al final de la sección un enlace relativo al archivo `.py` correspondiente dentro de `Codigos/`.
- Usar el mismo formato de enlace que ya existe en el README (si ya hay un estilo definido, respétalo).

---

## Contenido específico por unidad

A continuación se detalla qué métodos cubre cada unidad y los datos clave para documentarlos correctamente.

### UNIDAD 6 — Solución de Ecuaciones Diferenciales Ordinarias (EDOs)

Métodos a documentar:

**Método de Euler**
- Fórmula: `y_{i+1} = y_i + h · f(x_i, y_i)`
- Error local: O(h²) — Error global: O(h)
- Código: `Codigos/euler.py`

**Runge-Kutta de orden 4 (RK4)**
- Fórmulas: k1, k2, k3, k4 y la actualización ponderada
- Error local: O(h⁵) — Error global: O(h⁴)
- Código: `Codigos/RK4.py`

**Serie de Taylor de orden 2**
- Fórmula: `y_{i+1} = y_i + h·f + (h²/2)·f'`
- Error local: O(h³) — Error global: O(h²)
- Código: `Codigos/taylor.py`

Ejemplo numérico sugerido para los tres métodos: `dy/dx = -2y`, `y(0) = 1`, `h = 0.1` (solución exacta: `y = e^{-2x}`).

---

**Para UNIDAD1 a UNIDAD5:** Lee el README existente de cada unidad para identificar los métodos que cubre, y aplica la estructura estándar a cada uno. No se te proporciona el contenido de esas unidades aquí porque ya está en el repositorio — debes leerlo directamente.

---

## Restricciones importantes

- **Solo modifica archivos README.md** dentro de cada carpeta de unidad. No toques ningún archivo `.py`, `.md` que no sea README, ni ninguna otra carpeta.
- **Conserva el estilo visual existente** de cada README: si usan HTML, emojis, badges, tablas o cualquier componente visual, mantenlo y extiéndelo con el mismo estilo.
- **No elimines contenido existente** que ya sea correcto — solo agrega o completa lo que falte.
- Todo el contenido nuevo debe estar en **español**.
- Las fórmulas deben usar bloques LaTeX `$$...$$` compatibles con GitHub Markdown.
- Los enlaces a código deben ser **rutas relativas** desde el README de cada unidad.

---

## Resumen de criterios de éxito

Al terminar, cada README de UNIDAD1 a UNIDAD6 debe:

- [ ] Documentar todos los métodos o temas que cubre esa unidad.
- [ ] Tener para cada método las 6 secciones: conceptos teóricos, fórmulas, análisis de error, condiciones de aplicación, ejemplo numérico y enlace al código.
- [ ] Seguir el mismo estilo visual que ya tenía el README original de esa unidad.
- [ ] Estar escrito completamente en español.
- [ ] Tener fórmulas LaTeX bien formadas y enlaces de código funcionales.
