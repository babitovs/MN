import numpy as np

def eliminacion_gaussiana(A, b):
    """
    Resuelve el sistema Ax = b usando Eliminación Gaussiana con Pivoteo Parcial.
    
    Parámetros:
        A : matriz de coeficientes (lista de listas o numpy array)
        b : vector de términos independientes
    
    Retorna:
        x : vector solución, o mensaje si el sistema es incompatible/indeterminado
    """
    n = len(b)
    
    # Construir matriz aumentada [A|b]
    M = np.array([[float(A[i][j]) for j in range(n)] + [float(b[i])] for i in range(n)])
    
    print("=" * 55)
    print("       ELIMINACIÓN GAUSSIANA CON PIVOTEO PARCIAL")
    print("=" * 55)
    print("\n📋 Matriz aumentada inicial [A|b]:")
    imprimir_matriz(M, n)

    # ── ELIMINACIÓN HACIA ADELANTE ──────────────────────────
    for col in range(n):
        
        # Pivoteo parcial: buscar el mayor |valor| en la columna
        max_fila = col
        for fila in range(col + 1, n):
            if abs(M[fila][col]) > abs(M[max_fila][col]):
                max_fila = fila
        
        # Intercambiar filas si es necesario
        if max_fila != col:
            M[[col, max_fila]] = M[[max_fila, col]]
            print(f"\n🔄 Pivoteo: intercambiamos F{col+1} ↔ F{max_fila+1}")
            imprimir_matriz(M, n)
        
        # Verificar si el pivote es cero (sistema sin solución única)
        if abs(M[col][col]) < 1e-12:
            # Revisar si es incompatible o indeterminado
            for fila in range(col, n):
                if abs(M[fila][n]) > 1e-12:
                    print("\n❌ SISTEMA INCOMPATIBLE")
                    print(f"   Fila {fila+1}: 0 = {M[fila][n]:.4f} → Contradicción")
                    return None
            print("\n⚠️  SISTEMA INDETERMINADO (infinitas soluciones)")
            return None
        
        # Eliminación: hacer ceros debajo del pivote
        print(f"\n📌 Pivote en columna {col+1}: {M[col][col]:.4f}")
        for fila in range(col + 1, n):
            if abs(M[fila][col]) > 1e-12:
                m = M[fila][col] / M[col][col]
                M[fila] = M[fila] - m * M[col]
                print(f"   m{fila+1}{col+1} = {m:.4f}  →  F{fila+1} ← F{fila+1} - ({m:.4f}) × F{col+1}")
        
        print(f"\n✅ Después de eliminar columna {col+1}:")
        imprimir_matriz(M, n)

    # ── SUSTITUCIÓN HACIA ATRÁS ─────────────────────────────
    print("\n🔁 Sustitución hacia atrás:")
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        suma = sum(M[i][j] * x[j] for j in range(i + 1, n))
        x[i] = (M[i][n] - suma) / M[i][i]
        print(f"   x{i+1} = ({M[i][n]:.4f} - {suma:.4f}) / {M[i][i]:.4f} = {x[i]:.4f}")

    return x


def imprimir_matriz(M, n):
    """Imprime la matriz aumentada de forma legible."""
    for fila in M:
        coefs = "  ".join(f"{v:8.4f}" for v in fila[:n])
        ind   = f"{fila[n]:8.4f}"
        print(f"  [ {coefs}  |  {ind} ]")


def verificar_solucion(A, b, x):
    """Verifica sustituyendo la solución en el sistema original."""
    print("\n🔍 Verificación:")
    for i in range(len(b)):
        resultado = sum(A[i][j] * x[j] for j in range(len(x)))
        ok = "✓" if abs(resultado - b[i]) < 1e-8 else "✗"
        print(f"   Ecuación {i+1}: {resultado:.4f} = {b[i]} {ok}")


# ══════════════════════════════════════════════════════════
#  EJEMPLO 1 — Sistema compatible con solución única
# ══════════════════════════════════════════════════════════
print("\n" + "🟢 " * 20)
print("EJEMPLO 1: Sistema 3x3 con solución única")
print("🟢 " * 20)

A1 = [
    [ 2,  1, -1],
    [-3, -1,  2],
    [-2,  1,  2]
]
b1 = [8, -11, -3]

solucion1 = eliminacion_gaussiana(A1, b1)

if solucion1 is not None:
    print("\n🎯 SOLUCIÓN:")
    variables = ['x', 'y', 'z']
    for i, val in enumerate(solucion1):
        print(f"   {variables[i]} = {val:.4f}")
    verificar_solucion(A1, b1, solucion1)


# ══════════════════════════════════════════════════════════
#  EJEMPLO 2 — Sistema incompatible (sin solución)
# ══════════════════════════════════════════════════════════
print("\n\n" + "🔴 " * 20)
print("EJEMPLO 2: Sistema incompatible (sin solución)")
print("🔴 " * 20)

A2 = [
    [1, 1],
    [2, 2]
]
b2 = [2, 5]

solucion2 = eliminacion_gaussiana(A2, b2)

if solucion2 is None:
    print("\n   El sistema no tiene solución.")


# ══════════════════════════════════════════════════════════
#  FUNCIÓN GENÉRICA — Úsala con cualquier sistema
# ══════════════════════════════════════════════════════════
print("\n\n" + "=" * 55)
print("  ¿CÓMO USAR CON TU PROPIO SISTEMA?")
print("=" * 55)
print("""
  A = [
      [a11, a12, a13],   # coeficientes ecuación 1
      [a21, a22, a23],   # coeficientes ecuación 2
      [a31, a32, a33],   # coeficientes ecuación 3
  ]
  b = [b1, b2, b3]       # términos independientes

  solucion = eliminacion_gaussiana(A, b)
""")