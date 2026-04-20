from manim import *

# ─────────────────────────────────────────────
#  COLORES
# ─────────────────────────────────────────────
PIVOT_COLOR     = YELLOW
ELIM_COLOR      = RED
RESULT_COLOR    = GREEN
HEADER_COLOR    = "#4EC9B0"
HIGHLIGHT_COLOR = ORANGE


# ═══════════════════════════════════════════════
# ESCENA 1 – Sistema de ecuaciones
# ═══════════════════════════════════════════════
class E1_Sistema(Scene):
    def construct(self):
        header = Text("Ejemplo: Sistema 3x3", font_size=44, color=BLUE, weight=BOLD)
        header.to_edge(UP, buff=0.4)
        self.play(Write(header))

        subtitulo = Text("Resolveremos el siguiente sistema con Eliminación Gaussiana:",
                         font_size=26, color=GRAY)
        subtitulo.next_to(header, DOWN, buff=0.3)
        self.play(FadeIn(subtitulo))

        eq1 = MathTex(r"2x + y - z = 8",      font_size=44, color=WHITE)
        eq2 = MathTex(r"-3x - y + 2z = -11",  font_size=44, color=WHITE)
        eq3 = MathTex(r"-2x + y + 2z = -3",   font_size=44, color=WHITE)
        sistema = VGroup(eq1, eq2, eq3).arrange(DOWN, buff=0.45)
        brace = Brace(sistema, LEFT, color=WHITE)
        sis_group = VGroup(brace, sistema).arrange(RIGHT, buff=0.2)
        sis_group.next_to(subtitulo, DOWN, buff=0.5)

        self.play(Create(brace))
        self.play(LaggedStart(Write(eq1), Write(eq2), Write(eq3), lag_ratio=0.35))
        self.wait(2)

        pregunta = Text("¿Cuáles son los valores de  x, y  y  z?", font_size=28, color=PIVOT_COLOR)
        pregunta.next_to(sis_group, DOWN, buff=0.45)
        self.play(FadeIn(pregunta))
        self.wait(2.5)
        self.play(FadeOut(VGroup(header, subtitulo, sis_group, pregunta)))


# ═══════════════════════════════════════════════
# ESCENA 2 – Matriz Aumentada
# ═══════════════════════════════════════════════
class E2_MatrizAumentada(Scene):
    def construct(self):
        header = Text("Paso 1: Construir la Matriz Aumentada", font_size=38, color=BLUE, weight=BOLD)
        header.to_edge(UP, buff=0.4)
        self.play(Write(header))

        nota = Text("Extraemos los coeficientes de cada ecuación:", font_size=26, color=GRAY)
        nota.next_to(header, DOWN, buff=0.3)
        self.play(FadeIn(nota))

        # Ecuaciones a la izquierda
        eq1 = MathTex(r"2x + y - z = 8",     font_size=34)
        eq2 = MathTex(r"-3x - y + 2z = -11", font_size=34)
        eq3 = MathTex(r"-2x + y + 2z = -3",  font_size=34)
        eqs = VGroup(eq1, eq2, eq3).arrange(DOWN, buff=0.35)
        brace = Brace(eqs, LEFT)
        sis = VGroup(brace, eqs).arrange(RIGHT, buff=0.15)
        sis.next_to(nota, DOWN, buff=0.4).shift(LEFT * 2.5)
        self.play(Create(brace), LaggedStart(Write(eq1), Write(eq2), Write(eq3), lag_ratio=0.3))
        self.wait(0.8)

        flecha = Arrow(LEFT * 0.2, RIGHT * 0.2, color=YELLOW, buff=0.1)
        flecha.next_to(sis, RIGHT, buff=0.3)
        self.play(GrowArrow(flecha))

        # Matriz aumentada
        mat = MathTex(
            r"\left[\begin{array}{ccc|c}"
            r"2 & 1 & -1 & 8 \\"
            r"-3 & -1 & 2 & -11 \\"
            r"-2 & 1 & 2 & -3"
            r"\end{array}\right]",
            font_size=38
        )
        mat.next_to(flecha, RIGHT, buff=0.3)
        self.play(Write(mat))
        self.wait(1)

        # Etiquetas de columnas
        labels = VGroup(
            Text("x", font_size=22, color=PIVOT_COLOR),
            Text("y", font_size=22, color=PIVOT_COLOR),
            Text("z", font_size=22, color=PIVOT_COLOR),
            Text("b", font_size=22, color=RESULT_COLOR),
        ).arrange(RIGHT, buff=0.52)
        labels.next_to(mat, UP, buff=0.15).shift(LEFT * 0.05)
        self.play(FadeIn(labels))

        conclusion = Text("Cada fila representa una ecuación, cada columna una variable.",
                          font_size=24, color=GRAY)
        conclusion.to_edge(DOWN, buff=0.5)
        self.play(FadeIn(conclusion))
        self.wait(2.5)
        self.play(FadeOut(VGroup(header, nota, sis, flecha, mat, labels, conclusion)))


# ═══════════════════════════════════════════════
# ESCENA 3 – Pivoteo Parcial
# ═══════════════════════════════════════════════
class E3_Pivoteo(Scene):
    def construct(self):
        header = Text("Paso 2: Pivoteo Parcial", font_size=40, color=BLUE, weight=BOLD)
        header.to_edge(UP, buff=0.4)
        self.play(Write(header))

        nota = Text("Buscamos el mayor |valor| en la columna 1 para usarlo como pivote.",
                    font_size=26, color=GRAY)
        nota.next_to(header, DOWN, buff=0.3)
        self.play(FadeIn(nota))

        mat = MathTex(
            r"\left[\begin{array}{ccc|c}"
            r"2 & 1 & -1 & 8 \\"
            r"-3 & -1 & 2 & -11 \\"
            r"-2 & 1 & 2 & -3"
            r"\end{array}\right]",
            font_size=40
        )
        mat.next_to(nota, DOWN, buff=0.45)
        self.play(Write(mat))
        self.wait(0.8)

        # Análisis columna 1
        c1 = Text("Columna 1:", font_size=26, color=HEADER_COLOR)
        v1 = MathTex(r"|2| = 2", font_size=30, color=WHITE)
        v2 = MathTex(r"|-3| = 3  \leftarrow  \text{MAYOR}", font_size=30, color=PIVOT_COLOR)
        v3 = MathTex(r"|-2| = 2", font_size=30, color=WHITE)
        analisis = VGroup(c1, v1, v2, v3).arrange(DOWN, buff=0.22, aligned_edge=LEFT)
        analisis.next_to(mat, DOWN, buff=0.4)

        self.play(Write(c1))
        self.play(Write(v1)); self.wait(0.4)
        self.play(Write(v2)); self.wait(0.4)
        self.play(Write(v3)); self.wait(0.8)

        swap = Text("→  Intercambiamos  F1  ↔  F2", font_size=28, color=ORANGE)
        swap.next_to(analisis, DOWN, buff=0.3)
        self.play(Write(swap))
        self.wait(1)

        self.play(FadeOut(VGroup(mat, analisis, swap)))

        mat2 = MathTex(
            r"\left[\begin{array}{ccc|c}"
            r"-3 & -1 & 2 & -11 \\"
            r"2 & 1 & -1 & 8 \\"
            r"-2 & 1 & 2 & -3"
            r"\end{array}\right]",
            font_size=40
        )
        mat2.next_to(nota, DOWN, buff=0.45)
        resultado = Text("Matriz con pivoteo aplicado:", font_size=26, color=RESULT_COLOR)
        resultado.next_to(nota, DOWN, buff=0.35)
        mat2.next_to(resultado, DOWN, buff=0.3)

        self.play(Write(resultado), Write(mat2))
        self.wait(2.5)
        self.play(FadeOut(VGroup(header, nota, resultado, mat2)))


# ═══════════════════════════════════════════════
# ESCENA 4 – Eliminación: Iteración 1
# ═══════════════════════════════════════════════
class E4_Elim_Iter1(Scene):
    def construct(self):
        header = Text("Paso 3: Eliminación — Iteración 1", font_size=38, color=BLUE, weight=BOLD)
        header.to_edge(UP, buff=0.3)
        self.play(Write(header))

        objetivo = Text("Objetivo: hacer ceros debajo del pivote en la columna 1",
                        font_size=25, color=GRAY)
        objetivo.next_to(header, DOWN, buff=0.25)
        self.play(FadeIn(objetivo))

        mat_ini = MathTex(
            r"\left[\begin{array}{ccc|c}"
            r"-3 & -1 & 2 & -11 \\"
            r"2 & 1 & -1 & 8 \\"
            r"-2 & 1 & 2 & -3"
            r"\end{array}\right]",
            font_size=36
        )
        pivote_label = Text("Pivote = -3  (F1, col 1)", font_size=24, color=PIVOT_COLOR)
        ini_group = VGroup(pivote_label, mat_ini).arrange(DOWN, buff=0.2)
        ini_group.next_to(objetivo, DOWN, buff=0.35)
        self.play(Write(pivote_label), Write(mat_ini))
        self.wait(0.8)

        # ── Multiplicador m21 ──
        sep = Line(LEFT*5.5, RIGHT*5.5, color=GRAY, stroke_width=1)
        sep.next_to(ini_group, DOWN, buff=0.3)
        self.play(Create(sep))

        t_m21 = Text("Multiplicador para eliminar F2:", font_size=24, color=HEADER_COLOR)
        f_m21 = MathTex(r"m_{21} = \frac{a_{21}}{a_{11}} = \frac{2}{-3} = -\frac{2}{3}",
                        font_size=32, color=ELIM_COLOR)
        g_m21 = VGroup(t_m21, f_m21).arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        g_m21.next_to(sep, DOWN, buff=0.25).shift(LEFT*1.5)
        self.play(Write(t_m21)); self.play(Write(f_m21)); self.wait(0.8)

        op21 = MathTex(r"F_2 \leftarrow F_2 - m_{21} \cdot F_1 = F_2 - \left(-\tfrac{2}{3}\right) F_1",
                       font_size=28, color=ORANGE)
        op21.next_to(g_m21, DOWN, buff=0.25)
        self.play(Write(op21)); self.wait(1)

        # Cálculo detallado F2
        calc21 = MathTex(
            r"F_2: \quad"
            r"\left[2-\left(-\tfrac{2}{3}\right)(-3),\ "
            r"1-\left(-\tfrac{2}{3}\right)(-1),\ "
            r"-1-\left(-\tfrac{2}{3}\right)(2),\ "
            r"8-\left(-\tfrac{2}{3}\right)(-11)\right]",
            font_size=24, color=WHITE
        )
        calc21.next_to(op21, DOWN, buff=0.2)
        self.play(Write(calc21)); self.wait(1)

        res21 = MathTex(r"F_2 \rightarrow \left[0,\ \tfrac{1}{3},\ \tfrac{1}{3},\ \tfrac{2}{3}\right]",
                        font_size=30, color=RESULT_COLOR)
        res21.next_to(calc21, DOWN, buff=0.2)
        self.play(Write(res21)); self.wait(1.5)

        self.play(FadeOut(VGroup(g_m21, op21, calc21, res21)))

        # ── Multiplicador m31 ──
        t_m31 = Text("Multiplicador para eliminar F3:", font_size=24, color=HEADER_COLOR)
        f_m31 = MathTex(r"m_{31} = \frac{a_{31}}{a_{11}} = \frac{-2}{-3} = \frac{2}{3}",
                        font_size=32, color=ELIM_COLOR)
        g_m31 = VGroup(t_m31, f_m31).arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        g_m31.next_to(sep, DOWN, buff=0.25).shift(LEFT*1.5)
        self.play(Write(t_m31)); self.play(Write(f_m31)); self.wait(0.8)

        op31 = MathTex(r"F_3 \leftarrow F_3 - m_{31} \cdot F_1 = F_3 - \tfrac{2}{3}\,F_1",
                       font_size=28, color=ORANGE)
        op31.next_to(g_m31, DOWN, buff=0.25)
        self.play(Write(op31)); self.wait(1)

        calc31 = MathTex(
            r"F_3: \quad"
            r"\left[-2-\tfrac{2}{3}(-3),\ "
            r"1-\tfrac{2}{3}(-1),\ "
            r"2-\tfrac{2}{3}(2),\ "
            r"-3-\tfrac{2}{3}(-11)\right]",
            font_size=24, color=WHITE
        )
        calc31.next_to(op31, DOWN, buff=0.2)
        self.play(Write(calc31)); self.wait(1)

        res31 = MathTex(r"F_3 \rightarrow \left[0,\ \tfrac{5}{3},\ \tfrac{2}{3},\ \tfrac{13}{3}\right]",
                        font_size=30, color=RESULT_COLOR)
        res31.next_to(calc31, DOWN, buff=0.2)
        self.play(Write(res31)); self.wait(1.5)

        self.play(FadeOut(VGroup(ini_group, sep, g_m31, op31, calc31, res31, objetivo)))

        # Resultado iteración 1
        header2 = Text("Resultado — Iteración 1", font_size=32, color=RESULT_COLOR)
        header2.next_to(header, DOWN, buff=0.3)
        mat_r1 = MathTex(
            r"\left[\begin{array}{ccc|c}"
            r"-3 & -1 & 2 & -11 \\"
            r"0 & \tfrac{1}{3} & \tfrac{1}{3} & \tfrac{2}{3} \\"
            r"0 & \tfrac{5}{3} & \tfrac{2}{3} & \tfrac{13}{3}"
            r"\end{array}\right]",
            font_size=40
        )
        mat_r1.next_to(header2, DOWN, buff=0.4)
        check = Text("✓ Columna 1 eliminada bajo el pivote", font_size=26, color=RESULT_COLOR)
        check.next_to(mat_r1, DOWN, buff=0.35)
        self.play(Write(header2), Write(mat_r1))
        self.play(FadeIn(check))
        self.wait(2.5)
        self.play(FadeOut(VGroup(header, header2, mat_r1, check)))


# ═══════════════════════════════════════════════
# ESCENA 5 – Eliminación: Iteración 2
# ═══════════════════════════════════════════════
class E5_Elim_Iter2(Scene):
    def construct(self):
        header = Text("Paso 3: Eliminación — Iteración 2", font_size=38, color=BLUE, weight=BOLD)
        header.to_edge(UP, buff=0.3)
        self.play(Write(header))

        objetivo = Text("Objetivo: hacer cero debajo del pivote en la columna 2",
                        font_size=25, color=GRAY)
        objetivo.next_to(header, DOWN, buff=0.25)
        self.play(FadeIn(objetivo))

        mat_ini = MathTex(
            r"\left[\begin{array}{ccc|c}"
            r"-3 & -1 & 2 & -11 \\"
            r"0 & \tfrac{1}{3} & \tfrac{1}{3} & \tfrac{2}{3} \\"
            r"0 & \tfrac{5}{3} & \tfrac{2}{3} & \tfrac{13}{3}"
            r"\end{array}\right]",
            font_size=36
        )
        pivote_label = Text("Pivote = 1/3  (F2, col 2)", font_size=24, color=PIVOT_COLOR)
        ini_group = VGroup(pivote_label, mat_ini).arrange(DOWN, buff=0.2)
        ini_group.next_to(objetivo, DOWN, buff=0.35)
        self.play(Write(pivote_label), Write(mat_ini))
        self.wait(0.8)

        sep = Line(LEFT*5.5, RIGHT*5.5, color=GRAY, stroke_width=1)
        sep.next_to(ini_group, DOWN, buff=0.3)
        self.play(Create(sep))

        # Multiplicador m32
        t_m32 = Text("Multiplicador para eliminar F3:", font_size=24, color=HEADER_COLOR)
        f_m32 = MathTex(r"m_{32} = \frac{a_{32}}{a_{22}} = \frac{5/3}{1/3} = 5",
                        font_size=32, color=ELIM_COLOR)
        g_m32 = VGroup(t_m32, f_m32).arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        g_m32.next_to(sep, DOWN, buff=0.25).shift(LEFT*1.5)
        self.play(Write(t_m32)); self.play(Write(f_m32)); self.wait(0.8)

        op32 = MathTex(r"F_3 \leftarrow F_3 - 5 \cdot F_2",
                       font_size=30, color=ORANGE)
        op32.next_to(g_m32, DOWN, buff=0.25)
        self.play(Write(op32)); self.wait(1)

        calc32 = MathTex(
            r"F_3: \quad"
            r"\left[0-5(0),\ "
            r"\tfrac{5}{3}-5\!\cdot\!\tfrac{1}{3},\ "
            r"\tfrac{2}{3}-5\!\cdot\!\tfrac{1}{3},\ "
            r"\tfrac{13}{3}-5\!\cdot\!\tfrac{2}{3}\right]",
            font_size=26, color=WHITE
        )
        calc32.next_to(op32, DOWN, buff=0.2)
        self.play(Write(calc32)); self.wait(1)

        res32 = MathTex(r"F_3 \rightarrow \left[0,\ 0,\ -\tfrac{1}{3},\ \tfrac{1}{3}\right]",
                        font_size=30, color=RESULT_COLOR)
        res32.next_to(calc32, DOWN, buff=0.2)
        self.play(Write(res32)); self.wait(1.5)

        self.play(FadeOut(VGroup(ini_group, sep, g_m32, op32, calc32, res32, objetivo)))

        # Resultado final triangular
        header2 = Text("Forma Triangular Superior  ✓", font_size=32, color=RESULT_COLOR)
        header2.next_to(header, DOWN, buff=0.35)
        mat_tri = MathTex(
            r"\left[\begin{array}{ccc|c}"
            r"-3 & -1 & 2 & -11 \\"
            r"0 & \tfrac{1}{3} & \tfrac{1}{3} & \tfrac{2}{3} \\"
            r"0 & 0 & -\tfrac{1}{3} & \tfrac{1}{3}"
            r"\end{array}\right]",
            font_size=42
        )
        mat_tri.next_to(header2, DOWN, buff=0.4)
        check = Text("La eliminación hacia adelante está completa.", font_size=26, color=GRAY)
        check.next_to(mat_tri, DOWN, buff=0.35)
        self.play(Write(header2), Write(mat_tri))
        self.play(FadeIn(check))
        self.wait(2.5)
        self.play(FadeOut(VGroup(header, header2, mat_tri, check)))


# ═══════════════════════════════════════════════
# ESCENA 6 – Sustitución hacia atrás
# ═══════════════════════════════════════════════
class E6_Sustitucion(Scene):
    def construct(self):
        header = Text("Paso 4: Sustitución hacia atrás", font_size=40, color=BLUE, weight=BOLD)
        header.to_edge(UP, buff=0.4)
        self.play(Write(header))

        nota = Text("Partimos de la última fila y subimos.", font_size=26, color=GRAY)
        nota.next_to(header, DOWN, buff=0.3)
        self.play(FadeIn(nota))

        mat = MathTex(
            r"\left[\begin{array}{ccc|c}"
            r"-3 & -1 & 2 & -11 \\"
            r"0 & \tfrac{1}{3} & \tfrac{1}{3} & \tfrac{2}{3} \\"
            r"0 & 0 & -\tfrac{1}{3} & \tfrac{1}{3}"
            r"\end{array}\right]",
            font_size=36
        )
        mat.next_to(nota, DOWN, buff=0.35).shift(LEFT*2)
        self.play(Write(mat))
        self.wait(0.8)

        # Paso z
        t_z = Text("Despejar z  (Fila 3):", font_size=26, color=HEADER_COLOR)
        f_z1 = MathTex(r"-\tfrac{1}{3}\,z = \tfrac{1}{3}", font_size=32)
        f_z2 = MathTex(r"z = \frac{1/3}{-1/3}", font_size=32)
        f_z3 = MathTex(r"\boxed{z = -1}", font_size=36, color=RESULT_COLOR)
        g_z = VGroup(t_z, f_z1, f_z2, f_z3).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        g_z.next_to(mat, RIGHT, buff=0.6).shift(UP*1)
        self.play(Write(t_z)); self.play(Write(f_z1)); self.wait(0.3)
        self.play(Write(f_z2)); self.wait(0.3)
        self.play(Write(f_z3)); self.wait(1)

        # Paso y
        t_y = Text("Despejar y  (Fila 2):", font_size=26, color=HEADER_COLOR)
        f_y1 = MathTex(r"\tfrac{1}{3}\,y + \tfrac{1}{3}(-1) = \tfrac{2}{3}", font_size=30)
        f_y2 = MathTex(r"\tfrac{1}{3}\,y = \tfrac{2}{3} + \tfrac{1}{3} = 1", font_size=30)
        f_y3 = MathTex(r"\boxed{y = 3}", font_size=36, color=RESULT_COLOR)
        g_y = VGroup(t_y, f_y1, f_y2, f_y3).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        g_y.next_to(g_z, DOWN, buff=0.35)
        self.play(Write(t_y)); self.play(Write(f_y1)); self.wait(0.3)
        self.play(Write(f_y2)); self.wait(0.3)
        self.play(Write(f_y3)); self.wait(1)

        # Paso x
        t_x = Text("Despejar x  (Fila 1):", font_size=26, color=HEADER_COLOR)
        f_x1 = MathTex(r"-3x - (3) + 2(-1) = -11", font_size=28)
        f_x2 = MathTex(r"-3x = -11 + 3 + 2 = -6", font_size=28)
        f_x3 = MathTex(r"\boxed{x = 2}", font_size=36, color=RESULT_COLOR)
        g_x = VGroup(t_x, f_x1, f_x2, f_x3).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        g_x.next_to(g_y, DOWN, buff=0.35)
        self.play(Write(t_x)); self.play(Write(f_x1)); self.wait(0.3)
        self.play(Write(f_x2)); self.wait(0.3)
        self.play(Write(f_x3)); self.wait(1.5)

        self.play(FadeOut(VGroup(header, nota, mat, g_z, g_y, g_x)))


# ═══════════════════════════════════════════════
# ESCENA 7 – Solución final y verificación
# ═══════════════════════════════════════════════
class E7_Solucion(Scene):
    def construct(self):
        header = Text("Solución Final", font_size=48, color=BLUE, weight=BOLD)
        header.to_edge(UP, buff=0.5)
        self.play(Write(header))

        sol = MathTex(
            r"\boxed{x = 2, \qquad y = 3, \qquad z = -1}",
            font_size=52, color=RESULT_COLOR
        )
        sol.next_to(header, DOWN, buff=0.6)
        self.play(Write(sol))
        self.play(sol.animate.scale(1.08), rate_func=there_and_back, run_time=1)
        self.wait(0.8)

        # Verificación
        ver_label = Text("Verificación — sustituimos en el sistema original:", font_size=26, color=GRAY)
        ver_label.next_to(sol, DOWN, buff=0.5)
        self.play(FadeIn(ver_label))

        v1 = MathTex(r"2(2) + (3) - (-1) = 4+3+1 = 8 \checkmark",   font_size=30, color=WHITE)
        v2 = MathTex(r"-3(2) - (3) + 2(-1) = -6-3-2 = -11 \checkmark", font_size=30, color=WHITE)
        v3 = MathTex(r"-2(2) + (3) + 2(-1) = -4+3-2 = -3 \checkmark",  font_size=30, color=WHITE)
        vers = VGroup(v1, v2, v3).arrange(DOWN, buff=0.35)
        vers.next_to(ver_label, DOWN, buff=0.35)

        self.play(LaggedStart(Write(v1), Write(v2), Write(v3), lag_ratio=0.4))
        self.wait(1)

        correcto = Text("¡Sistema resuelto correctamente! 🎓", font_size=34, color=PIVOT_COLOR, weight=BOLD)
        correcto.next_to(vers, DOWN, buff=0.45)
        self.play(Write(correcto))
        self.wait(3)
        self.play(FadeOut(VGroup(header, sol, ver_label, vers, correcto)))


# ═══════════════════════════════════════════════
# ESCENA COMPLETA
# ═══════════════════════════════════════════════
class EjemploGaussiana(Scene):
    def construct(self):
        for escena_cls in [
            E1_Sistema,
            E2_MatrizAumentada,
            E3_Pivoteo,
            E4_Elim_Iter1,
            E5_Elim_Iter2,
            E6_Sustitucion,
            E7_Solucion,
        ]:
            escena_cls.construct(self)