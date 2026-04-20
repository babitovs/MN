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
# ESCENA 1 – Presentación del sistema
# ═══════════════════════════════════════════════
class I1_Sistema(Scene):
    def construct(self):
        header = Text("Sistema Indeterminado 2x2", font_size=44, color=BLUE, weight=BOLD)
        header.to_edge(UP, buff=0.4)
        self.play(Write(header))

        subtitulo = Text("Analizaremos este sistema con Eliminacion Gaussiana:",
                         font_size=26, color=GRAY)
        subtitulo.next_to(header, DOWN, buff=0.3)
        self.play(FadeIn(subtitulo))

        eq1 = MathTex(r"x + y = 4",   font_size=52, color=WHITE)
        eq2 = MathTex(r"2x + 2y = 8", font_size=52, color=WHITE)
        sistema = VGroup(eq1, eq2).arrange(DOWN, buff=0.5)
        brace = Brace(sistema, LEFT, color=WHITE)
        sis_group = VGroup(brace, sistema).arrange(RIGHT, buff=0.2)
        sis_group.next_to(subtitulo, DOWN, buff=0.5)

        self.play(Create(brace))
        self.play(LaggedStart(Write(eq1), Write(eq2), lag_ratio=0.4))
        self.wait(1.5)

        obs = Text("Nota: la ecuacion 2 es exactamente el doble de la ecuacion 1.",
                   font_size=26, color=PIVOT_COLOR)
        obs.next_to(sis_group, DOWN, buff=0.45)
        self.play(FadeIn(obs))

        demo = MathTex(r"2 \times (x + y = 4) \;\Rightarrow\; 2x + 2y = 8 \checkmark",
                       font_size=32, color=HIGHLIGHT_COLOR)
        demo.next_to(obs, DOWN, buff=0.3)
        self.play(Write(demo))
        self.wait(2.5)
        self.play(FadeOut(VGroup(header, subtitulo, sis_group, obs, demo)))


# ═══════════════════════════════════════════════
# ESCENA 2 – Interpretación geométrica
# ═══════════════════════════════════════════════
class I2_Geometria(Scene):
    def construct(self):
        header = Text("Interpretacion Geometrica", font_size=40, color=BLUE, weight=BOLD)
        header.to_edge(UP, buff=0.4)
        self.play(Write(header))

        nota = Text("Cada ecuacion representa una recta en el plano.",
                    font_size=26, color=GRAY)
        nota.next_to(header, DOWN, buff=0.3)
        self.play(FadeIn(nota))

        axes = Axes(
            x_range=[-1, 6, 1], y_range=[-1, 6, 1],
            x_length=6, y_length=5,
            axis_config={"color": GRAY},
        )
        axes.next_to(nota, DOWN, buff=0.3).shift(LEFT * 1.5)
        self.play(Create(axes))

        # Recta 1: x + y = 4  → y = 4 - x
        r1 = axes.plot(lambda x: 4 - x, x_range=[-0.5, 5], color=BLUE, stroke_width=4)
        l1 = Text("x + y = 4", font_size=22, color=BLUE)
        l1.next_to(axes, RIGHT, buff=0.4).shift(UP * 1.2)

        # Recta 2: 2x + 2y = 8 → y = 4 - x (MISMA recta)
        r2 = axes.plot(lambda x: 4 - x, x_range=[-0.5, 5],
                       color=ORANGE, stroke_width=3, stroke_opacity=0.5)
        l2 = Text("2x + 2y = 8", font_size=22, color=ORANGE)
        l2.next_to(l1, DOWN, buff=0.3)

        self.play(Create(r1), Write(l1))
        self.wait(0.5)
        self.play(Create(r2), Write(l2))
        self.wait(1)

        obs = Text("Las rectas son IDENTICAS → infinitos puntos en comun",
                   font_size=25, color=RESULT_COLOR)
        obs.next_to(axes, DOWN, buff=0.3)
        self.play(FadeIn(obs))

        obs2 = Text("-> Infinitas soluciones", font_size=28, color=RESULT_COLOR, weight=BOLD)
        obs2.next_to(obs, DOWN, buff=0.2)
        self.play(Write(obs2))
        self.wait(2.5)
        self.play(FadeOut(VGroup(header, nota, axes, r1, r2, l1, l2, obs, obs2)))


# ═══════════════════════════════════════════════
# ESCENA 3 – Matriz Aumentada
# ═══════════════════════════════════════════════
class I3_MatrizAumentada(Scene):
    def construct(self):
        header = Text("Paso 1: Construir la Matriz Aumentada", font_size=38, color=BLUE, weight=BOLD)
        header.to_edge(UP, buff=0.4)
        self.play(Write(header))

        nota = Text("Extraemos los coeficientes de cada ecuacion:", font_size=26, color=GRAY)
        nota.next_to(header, DOWN, buff=0.3)
        self.play(FadeIn(nota))

        eq1 = MathTex(r"x + y = 4",   font_size=38)
        eq2 = MathTex(r"2x + 2y = 8", font_size=38)
        eqs = VGroup(eq1, eq2).arrange(DOWN, buff=0.4)
        brace = Brace(eqs, LEFT)
        sis = VGroup(brace, eqs).arrange(RIGHT, buff=0.15)
        sis.next_to(nota, DOWN, buff=0.45).shift(LEFT * 2.8)
        self.play(Create(brace), LaggedStart(Write(eq1), Write(eq2), lag_ratio=0.3))
        self.wait(0.8)

        flecha = Arrow(LEFT * 0.1, RIGHT * 0.1, color=YELLOW, buff=0.1)
        flecha.next_to(sis, RIGHT, buff=0.35)
        self.play(GrowArrow(flecha))

        mat = MathTex(
            r"\left[\begin{array}{cc|c}"
            r"1 & 1 & 4 \\"
            r"2 & 2 & 8"
            r"\end{array}\right]",
            font_size=46
        )
        mat.next_to(flecha, RIGHT, buff=0.35)
        self.play(Write(mat))
        self.wait(1)

        labels = VGroup(
            Text("x", font_size=22, color=PIVOT_COLOR),
            Text("y", font_size=22, color=PIVOT_COLOR),
            Text("b", font_size=22, color=RESULT_COLOR),
        ).arrange(RIGHT, buff=0.72)
        labels.next_to(mat, UP, buff=0.15).shift(LEFT * 0.1)
        self.play(FadeIn(labels))
        self.wait(2)
        self.play(FadeOut(VGroup(header, nota, sis, flecha, mat, labels)))


# ═══════════════════════════════════════════════
# ESCENA 4 – Pivoteo Parcial
# ═══════════════════════════════════════════════
class I4_Pivoteo(Scene):
    def construct(self):
        header = Text("Paso 2: Pivoteo Parcial", font_size=40, color=BLUE, weight=BOLD)
        header.to_edge(UP, buff=0.4)
        self.play(Write(header))

        nota = Text("Buscamos el mayor |valor| en la columna 1:", font_size=26, color=GRAY)
        nota.next_to(header, DOWN, buff=0.3)
        self.play(FadeIn(nota))

        mat = MathTex(
            r"\left[\begin{array}{cc|c}"
            r"1 & 1 & 4 \\"
            r"2 & 2 & 8"
            r"\end{array}\right]",
            font_size=46
        )
        mat.next_to(nota, DOWN, buff=0.45)
        self.play(Write(mat))
        self.wait(0.8)

        v1 = MathTex(r"|1| = 1", font_size=30, color=WHITE)
        v2 = MathTex(r"|2| = 2 \leftarrow \text{MAYOR}", font_size=30, color=PIVOT_COLOR)
        analisis = VGroup(
            Text("Columna 1:", font_size=26, color=HEADER_COLOR),
            v1, v2
        ).arrange(DOWN, buff=0.22, aligned_edge=LEFT)
        analisis.next_to(mat, DOWN, buff=0.4)
        self.play(Write(analisis[0]))
        self.play(Write(v1)); self.wait(0.3)
        self.play(Write(v2)); self.wait(0.8)

        swap = Text("->  Intercambiamos  F1  con  F2", font_size=28, color=ORANGE)
        swap.next_to(analisis, DOWN, buff=0.3)
        self.play(Write(swap))
        self.wait(1)

        self.play(FadeOut(VGroup(mat, analisis, swap)))

        resultado = Text("Matriz con pivoteo aplicado:", font_size=26, color=RESULT_COLOR)
        resultado.next_to(nota, DOWN, buff=0.4)
        mat2 = MathTex(
            r"\left[\begin{array}{cc|c}"
            r"2 & 2 & 8 \\"
            r"1 & 1 & 4"
            r"\end{array}\right]",
            font_size=46
        )
        mat2.next_to(resultado, DOWN, buff=0.3)
        self.play(Write(resultado), Write(mat2))
        self.wait(2.5)
        self.play(FadeOut(VGroup(header, nota, resultado, mat2)))


# ═══════════════════════════════════════════════
# ESCENA 5 – Eliminación hacia adelante
# ═══════════════════════════════════════════════
class I5_Eliminacion(Scene):
    def construct(self):
        header = Text("Paso 3: Eliminacion hacia adelante", font_size=38, color=BLUE, weight=BOLD)
        header.to_edge(UP, buff=0.3)
        self.play(Write(header))

        objetivo = Text("Objetivo: hacer cero debajo del pivote en la columna 1",
                        font_size=25, color=GRAY)
        objetivo.next_to(header, DOWN, buff=0.25)
        self.play(FadeIn(objetivo))

        mat_ini = MathTex(
            r"\left[\begin{array}{cc|c}"
            r"2 & 2 & 8 \\"
            r"1 & 1 & 4"
            r"\end{array}\right]",
            font_size=42
        )
        pivote_label = Text("Pivote = 2  (F1, col 1)", font_size=24, color=PIVOT_COLOR)
        ini_group = VGroup(pivote_label, mat_ini).arrange(DOWN, buff=0.2)
        ini_group.next_to(objetivo, DOWN, buff=0.35)
        self.play(Write(pivote_label), Write(mat_ini))
        self.wait(0.8)

        sep = Line(LEFT*5.5, RIGHT*5.5, color=GRAY, stroke_width=1)
        sep.next_to(ini_group, DOWN, buff=0.3)
        self.play(Create(sep))

        # Multiplicador m21
        t_m21 = Text("Multiplicador para eliminar F2:", font_size=24, color=HEADER_COLOR)
        f_m21 = MathTex(r"m_{21} = \frac{a_{21}}{a_{11}} = \frac{1}{2} = 0.5",
                        font_size=34, color=ELIM_COLOR)
        g_m21 = VGroup(t_m21, f_m21).arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        g_m21.next_to(sep, DOWN, buff=0.3).shift(LEFT * 1)
        self.play(Write(t_m21)); self.play(Write(f_m21)); self.wait(0.8)

        op21 = MathTex(r"F_2 \leftarrow F_2 - 0.5 \cdot F_1",
                       font_size=32, color=ORANGE)
        op21.next_to(g_m21, DOWN, buff=0.3)
        self.play(Write(op21)); self.wait(1)

        calc21 = MathTex(
            r"F_2: \quad \left[1 - 0.5(2),\quad 1 - 0.5(2),\quad 4 - 0.5(8)\right]",
            font_size=28, color=WHITE
        )
        calc21.next_to(op21, DOWN, buff=0.25)
        self.play(Write(calc21)); self.wait(1)

        res21 = MathTex(r"F_2 \rightarrow \left[0,\quad 0,\quad 0\right]",
                        font_size=34, color=RESULT_COLOR)
        res21.next_to(calc21, DOWN, buff=0.25)
        self.play(Write(res21)); self.wait(1.5)

        self.play(FadeOut(VGroup(ini_group, sep, g_m21, op21, calc21, res21, objetivo)))

        # Resultado
        header2 = Text("Resultado de la eliminacion:", font_size=30, color=HEADER_COLOR)
        header2.next_to(header, DOWN, buff=0.35)
        mat_res = MathTex(
            r"\left[\begin{array}{cc|c}"
            r"2 & 2 & 8 \\"
            r"0 & 0 & 0"
            r"\end{array}\right]",
            font_size=46
        )
        mat_res.next_to(header2, DOWN, buff=0.4)
        self.play(Write(header2), Write(mat_res))
        self.wait(1)

        alerta = Text("Fila 2:  0x + 0y = 0   ->   0 = 0", font_size=30, color=PIVOT_COLOR, weight=BOLD)
        alerta.next_to(mat_res, DOWN, buff=0.4)
        self.play(FadeIn(alerta))
        self.wait(2.5)
        self.play(FadeOut(VGroup(header, header2, mat_res, alerta)))


# ═══════════════════════════════════════════════
# ESCENA 6 – Detección de indeterminación
# ═══════════════════════════════════════════════
class I6_Indeterminado(Scene):
    def construct(self):
        header = Text("Deteccion de Indeterminacion", font_size=40, color=PIVOT_COLOR, weight=BOLD)
        header.to_edge(UP, buff=0.4)
        self.play(Write(header))

        mat_res = MathTex(
            r"\left[\begin{array}{cc|c}"
            r"2 & 2 & 8 \\"
            r"0 & 0 & 0"
            r"\end{array}\right]",
            font_size=44
        )
        mat_res.next_to(header, DOWN, buff=0.45)
        self.play(Write(mat_res))
        self.wait(0.8)

        fila2 = Text("Fila 2 nos dice:", font_size=28, color=HEADER_COLOR)
        fila2.next_to(mat_res, DOWN, buff=0.4)
        self.play(FadeIn(fila2))

        eq_trivial = MathTex(r"0 \cdot x + 0 \cdot y = 0", font_size=40, color=WHITE)
        eq_trivial.next_to(fila2, DOWN, buff=0.3)
        self.play(Write(eq_trivial))
        self.wait(0.8)

        simplifica = MathTex(r"0 = 0", font_size=50, color=RESULT_COLOR)
        simplifica.next_to(eq_trivial, DOWN, buff=0.3)
        self.play(Write(simplifica))
        self.wait(0.8)

        verdad = Text("Esto es SIEMPRE verdadero → no aporta informacion.",
                      font_size=26, color=RESULT_COLOR)
        verdad.next_to(simplifica, DOWN, buff=0.4)
        self.play(FadeIn(verdad))
        self.wait(1)

        conclusion = Text("-> Solo tenemos 1 ecuacion util para 2 incognitas",
                          font_size=26, color=PIVOT_COLOR, weight=BOLD)
        conclusion.next_to(verdad, DOWN, buff=0.3)
        self.play(Write(conclusion))
        self.wait(1)

        conclusion2 = Text("-> Sistema Indeterminado: infinitas soluciones",
                           font_size=28, color=PIVOT_COLOR, weight=BOLD)
        conclusion2.next_to(conclusion, DOWN, buff=0.3)
        self.play(Write(conclusion2))
        self.wait(3)
        self.play(FadeOut(VGroup(header, mat_res, fila2, eq_trivial,
                                 simplifica, verdad, conclusion, conclusion2)))


# ═══════════════════════════════════════════════
# ESCENA 7 – Expresar la solución general
# ═══════════════════════════════════════════════
class I7_SolucionGeneral(Scene):
    def construct(self):
        header = Text("Solucion General", font_size=48, color=BLUE, weight=BOLD)
        header.to_edge(UP, buff=0.4)
        self.play(Write(header))

        nota = Text("De la unica ecuacion util despejamos x en terminos de y:",
                    font_size=26, color=GRAY)
        nota.next_to(header, DOWN, buff=0.35)
        self.play(FadeIn(nota))

        # Despejar x
        paso1 = MathTex(r"2x + 2y = 8", font_size=40)
        paso2 = MathTex(r"2x = 8 - 2y", font_size=40)
        paso3 = MathTex(r"x = 4 - y", font_size=40, color=RESULT_COLOR)
        pasos = VGroup(paso1, paso2, paso3).arrange(DOWN, buff=0.35)
        pasos.next_to(nota, DOWN, buff=0.4)
        self.play(Write(paso1)); self.wait(0.4)
        self.play(Write(paso2)); self.wait(0.4)
        self.play(Write(paso3)); self.wait(1)

        # Parámetro libre
        param = Text("Llamamos  t  al parametro libre (y = t):", font_size=26, color=HEADER_COLOR)
        param.next_to(pasos, DOWN, buff=0.45)
        self.play(FadeIn(param))

        sol_general = MathTex(
            r"\begin{cases} x = 4 - t \\ y = t \end{cases} \quad t \in \mathbb{R}",
            font_size=42, color=RESULT_COLOR
        )
        sol_general.next_to(param, DOWN, buff=0.3)
        self.play(Write(sol_general))
        self.wait(1)

        # Ejemplos de soluciones
        ejemplos_label = Text("Algunos ejemplos de soluciones validas:", font_size=24, color=GRAY)
        ejemplos_label.next_to(sol_general, DOWN, buff=0.4)
        self.play(FadeIn(ejemplos_label))

        ejs = VGroup(
            MathTex(r"t=0 \;\Rightarrow\; x=4,\; y=0", font_size=30, color=WHITE),
            MathTex(r"t=1 \;\Rightarrow\; x=3,\; y=1", font_size=30, color=WHITE),
            MathTex(r"t=4 \;\Rightarrow\; x=0,\; y=4", font_size=30, color=WHITE),
        ).arrange(DOWN, buff=0.25)
        ejs.next_to(ejemplos_label, DOWN, buff=0.3)
        self.play(LaggedStart(*[Write(e) for e in ejs], lag_ratio=0.4))
        self.wait(3)
        self.play(FadeOut(VGroup(header, nota, pasos, param, sol_general, ejemplos_label, ejs)))


# ═══════════════════════════════════════════════
# ESCENA 8 – Resumen y conclusión
# ═══════════════════════════════════════════════
class I8_Conclusion(Scene):
    def construct(self):
        header = Text("Conclusion", font_size=48, color=BLUE, weight=BOLD)
        header.to_edge(UP, buff=0.5)
        self.play(Write(header))

        sistema = MathTex(
            r"\begin{cases} x + y = 4 \\ 2x + 2y = 8 \end{cases}",
            font_size=44
        )
        sistema.next_to(header, DOWN, buff=0.5)
        self.play(Write(sistema))
        self.wait(0.8)

        razon = Text("La segunda ecuacion es 2 x (primera) con mismo termino independiente:",
                     font_size=24, color=GRAY)
        razon.next_to(sistema, DOWN, buff=0.4)
        self.play(FadeIn(razon))

        demo = MathTex(r"2(x + y = 4) \;\Rightarrow\; 2x + 2y = 8 \checkmark",
                       font_size=34, color=RESULT_COLOR)
        demo.next_to(razon, DOWN, buff=0.3)
        self.play(Write(demo))
        self.wait(1)

        resumen = VGroup(
            Text("Las rectas son identicas (se superponen)", font_size=26, color=WHITE),
            Text("La eliminacion produce  0 = 0  (fila trivial)", font_size=26, color=WHITE),
            Text("Sistema Indeterminado -> Infinitas soluciones", font_size=26, color=RESULT_COLOR),
            Text("Solucion general:  x = 4 - t,  y = t", font_size=26, color=PIVOT_COLOR),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        resumen.next_to(demo, DOWN, buff=0.45)
        self.play(LaggedStart(*[FadeIn(r, shift=RIGHT*0.3) for r in resumen], lag_ratio=0.3))
        self.wait(1.5)

        fin = Text("Sistema indeterminado detectado con Gauss", font_size=28,
                   color=PIVOT_COLOR, weight=BOLD)
        fin.next_to(resumen, DOWN, buff=0.4)
        self.play(Write(fin))
        self.wait(3)
        self.play(FadeOut(VGroup(header, sistema, razon, demo, resumen, fin)))


# ═══════════════════════════════════════════════
# ESCENA COMPLETA
# ═══════════════════════════════════════════════
class SistemaIndeterminado(Scene):
    def construct(self):
        for escena_cls in [
            I1_Sistema,
            I2_Geometria,
            I3_MatrizAumentada,
            I4_Pivoteo,
            I5_Eliminacion,
            I6_Indeterminado,
            I7_SolucionGeneral,
            I8_Conclusion,
        ]:
            escena_cls.construct(self)