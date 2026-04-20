import numpy as np

# ══════════════════════════════════════════════════════════
#  FUNCIONES PRINCIPALES
# ══════════════════════════════════════════════════════════

def eliminacion_gaussiana(A, b):
    """
    Resuelve el sistema Ax = b usando Eliminación Gaussiana con Pivoteo Parcial.
    """
    n = len(b)
    M = np.array([[float(A[i][j]) for j in range(n)] + [float(b[i])] for i in range(n)])

    print("\n" + "=" * 55)
    print("       ELIMINACIÓN GAUSSIANA CON PIVOTEO PARCIAL")
    print("=" * 55)
    print("\n Matriz aumentada inicial [A|b]:")
    imprimir_matriz(M, n)

    # ── ELIMINACIÓN HACIA ADELANTE ──
    for col in range(n):

        # Pivoteo parcial
        max_fila = col
        for fila in range(col + 1, n):
            if abs(M[fila][col]) > abs(M[max_fila][col]):
                max_fila = fila

        if max_fila != col:
            M[[col, max_fila]] = M[[max_fila, col]]
            print(f"\n Pivoteo: intercambiamos F{col+1} con F{max_fila+1}")
            imprimir_matriz(M, n)

        # Pivote cero
        if abs(M[col][col]) < 1e-12:
            for fila in range(col, n):
                if abs(M[fila][n]) > 1e-12:
                    print("\n SISTEMA INCOMPATIBLE")
                    print(f"   Fila {fila+1}: 0 = {M[fila][n]:.4f} -> Contradiccion")
                    return None
            print("\n SISTEMA INDETERMINADO (infinitas soluciones)")
            return None

        # Eliminar debajo del pivote
        print(f"\n Pivote en columna {col+1}: {M[col][col]:.4f}")
        for fila in range(col + 1, n):
            if abs(M[fila][col]) > 1e-12:
                m = M[fila][col] / M[col][col]
                M[fila] = M[fila] - m * M[col]
                print(f"   m{fila+1}{col+1} = {m:.4f}  ->  F{fila+1} = F{fila+1} - ({m:.4f}) x F{col+1}")

        print(f"\n Despues de eliminar columna {col+1}:")
        imprimir_matriz(M, n)

    # ── SUSTITUCIÓN HACIA ATRÁS ──
    print("\n Sustitucion hacia atras:")
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        suma = sum(M[i][j] * x[j] for j in range(i + 1, n))
        x[i] = (M[i][n] - suma) / M[i][i]
        print(f"   x{i+1} = ({M[i][n]:.4f} - {suma:.4f}) / {M[i][i]:.4f} = {x[i]:.4f}")

    return x


def imprimir_matriz(M, n):
    for fila in M:
        coefs = "  ".join(f"{v:8.4f}" for v in fila[:n])
        ind   = f"{fila[n]:8.4f}"
        print(f"  [ {coefs}  |  {ind} ]")


def verificar_solucion(A, b, x):
    print("\n Verificacion:")
    for i in range(len(b)):
        resultado = sum(A[i][j] * x[j] for j in range(len(x)))
        ok = "OK" if abs(resultado - b[i]) < 1e-8 else "ERROR"
        print(f"   Ecuacion {i+1}: {resultado:.4f} = {b[i]}  [{ok}]")


# ══════════════════════════════════════════════════════════
#  INTERFAZ INTERACTIVA
# ══════════════════════════════════════════════════════════

def ingresar_sistema():
    print("\n" + "=" * 55)
    print("       INGRESA TU PROPIO SISTEMA")
    print("=" * 55)

    while True:
        try:
            n = int(input("\n cuantas ecuaciones tiene tu sistema? (ej: 2, 3, 4): "))
            if n < 2:
                print("   Minimo 2 ecuaciones.")
                continue
            break
        except ValueError:
            print("   Ingresa un numero entero valido.")

    variables = ['x', 'y', 'z', 'w'] if n <= 4 else [f"x{i+1}" for i in range(n)]

    print(f"\n Ingresa los coeficientes separados por espacios.")
    print(f"   Ejemplo: para  2x + y - z = 8  escribe:  2 1 -1\n")

    A = []
    for i in range(n):
        while True:
            try:
                vars_str = ", ".join(variables)
                entrada = input(f"   Ecuacion {i+1} - coeficientes [{vars_str}]: ")
                coefs = list(map(float, entrada.strip().split()))
                if len(coefs) != n:
                    print(f"   Necesitas exactamente {n} coeficientes.")
                    continue
                A.append(coefs)
                break
            except ValueError:
                print("   Solo numeros separados por espacios.")

    print(f"\n Ahora los terminos independientes (lado derecho del =).\n")
    while True:
        try:
            entrada = input(f"   Terminos independientes [{n} valores]: ")
            b = list(map(float, entrada.strip().split()))
            if len(b) != n:
                print(f"   Necesitas exactamente {n} valores.")
                continue
            break
        except ValueError:
            print("   Solo numeros separados por espacios.")

    print("\n Sistema ingresado:")
    for i in range(n):
        terminos = " + ".join(
            f"({int(A[i][j]) if float(A[i][j]).is_integer() else A[i][j]}){variables[j]}"
            for j in range(n)
        )
        bi = int(b[i]) if float(b[i]).is_integer() else b[i]
        print(f"   {terminos} = {bi}")

    return A, b, variables


def menu_principal():
    print("\n" + "=" * 55)
    print("   ELIMINACION GAUSSIANA — MENU PRINCIPAL")
    print("=" * 55)

    while True:
        print("\n  Que quieres hacer?")
        print("  [1] Ejemplo 1 — Sistema 3x3 (solucion unica)")
        print("  [2] Ejemplo 2 — Sistema 2x2 (incompatible)")
        print("  [3] Ingresar mi propio sistema")
        print("  [0] Salir")

        opcion = input("\n  Opcion: ").strip()

        if opcion == "1":
            A = [[ 2,  1, -1], [-3, -1,  2], [-2,  1,  2]]
            b = [8, -11, -3]
            sol = eliminacion_gaussiana(A, b)
            if sol is not None:
                print("\n SOLUCION:")
                for var, val in zip(['x', 'y', 'z'], sol):
                    print(f"   {var} = {val:.4f}")
                verificar_solucion(A, b, sol)

        elif opcion == "2":
            A = [[1, 1], [2, 2]]
            b = [2, 5]
            sol = eliminacion_gaussiana(A, b)
            if sol is None:
                print("\n   El sistema no tiene solucion.")

        elif opcion == "3":
            A, b, variables = ingresar_sistema()
            sol = eliminacion_gaussiana(A, b)
            if sol is not None:
                print("\n SOLUCION:")
                for var, val in zip(variables, sol):
                    print(f"   {var} = {val:.4f}")
                verificar_solucion(A, b, sol)

        elif opcion == "0":
            print("\n Hasta luego!\n")
            break
        else:
            print("   Opcion no valida, intenta de nuevo.")

        input("\n  Presiona Enter para continuar...")


if __name__ == "__main__":
    menu_principal()