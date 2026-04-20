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
class S1_Sistema(Scene):
    def construct(self):
        header = Text("Sistema Incompatible 2x2", font_size=44, color=BLUE, weight=BOLD)
        header.to_edge(UP, buff=0.4)
        self.play(Write(header))

        subtitulo = Text("Analizaremos este sistema con Eliminación Gaussiana:",
                         font_size=26, color=GRAY)
        subtitulo.next_to(header, DOWN, buff=0.3)
        self.play(FadeIn(subtitulo))

        eq1 = MathTex(r"x + y = 2",   font_size=52, color=WHITE)
        eq2 = MathTex(r"2x + 2y = 5", font_size=52, color=WHITE)
        sistema = VGroup(eq1, eq2).arrange(DOWN, buff=0.5)
        brace = Brace(sistema, LEFT, color=WHITE)
        sis_group = VGroup(brace, sistema).arrange(RIGHT, buff=0.2)
        sis_group.next_to(subtitulo, DOWN, buff=0.5)

        self.play(Create(brace))
        self.play(LaggedStart(Write(eq1), Write(eq2), lag_ratio=0.4))
        self.wait(1.5)

        pregunta = Text("¿Tiene solución este sistema?", font_size=30, color=PIVOT_COLOR)
        pregunta.next_to(sis_group, DOWN, buff=0.5)
        self.play(FadeIn(pregunta))
        self.wait(2.5)
        self.play(FadeOut(VGroup(header, subtitulo, sis_group, pregunta)))


# ═══════════════════════════════════════════════
# ESCENA 2 – Interpretación geométrica
# ═══════════════════════════════════════════════
class S2_Geometria(Scene):
    def construct(self):
        header = Text("Interpretación Geométrica", font_size=40, color=BLUE, weight=BOLD)
        header.to_edge(UP, buff=0.4)
        self.play(Write(header))

        nota = Text("Cada ecuación representa una recta en el plano.", font_size=26, color=GRAY)
        nota.next_to(header, DOWN, buff=0.3)
        self.play(FadeIn(nota))

        # Ejes
        axes = Axes(
            x_range=[-1, 4, 1], y_range=[-1, 4, 1],
            x_length=6, y_length=5,
            axis_config={"color": GRAY},
        )
        axes.next_to(nota, DOWN, buff=0.3).shift(LEFT * 1.5)
        self.play(Create(axes))

        # Recta 1: x + y = 2  →  y = 2 - x
        r1 = axes.plot(lambda x: 2 - x, x_range=[-0.5, 3.5], color=BLUE, stroke_width=3)
        l1 = Text("x + y = 2", font_size=22, color=BLUE)
        l1.next_to(axes, RIGHT, buff=0.4).shift(UP * 1.2)

        # Recta 2: 2x + 2y = 5  →  y = 2.5 - x
        r2 = axes.plot(lambda x: 2.5 - x, x_range=[-0.5, 3.5], color=ORANGE, stroke_width=3)
        l2 = Text("2x + 2y = 5", font_size=22, color=ORANGE)
        l2.next_to(l1, DOWN, buff=0.3)

        self.play(Create(r1), Write(l1))
        self.play(Create(r2), Write(l2))
        self.wait(1)

        obs = Text("Las rectas son PARALELAS → nunca se intersectan", font_size=26, color=ELIM_COLOR)
        obs.next_to(axes, DOWN, buff=0.3)
        self.play(FadeIn(obs))
        self.wait(1)

        obs2 = Text("→ El sistema NO tiene solución", font_size=28, color=ELIM_COLOR, weight=BOLD)
        obs2.next_to(obs, DOWN, buff=0.2)
        self.play(Write(obs2))
        self.wait(2.5)
        self.play(FadeOut(VGroup(header, nota, axes, r1, r2, l1, l2, obs, obs2)))


# ═══════════════════════════════════════════════
# ESCENA 3 – Matriz Aumentada
# ═══════════════════════════════════════════════
class S3_MatrizAumentada(Scene):
    def construct(self):
        header = Text("Paso 1: Construir la Matriz Aumentada", font_size=38, color=BLUE, weight=BOLD)
        header.to_edge(UP, buff=0.4)
        self.play(Write(header))

        nota = Text("Extraemos los coeficientes de cada ecuación:", font_size=26, color=GRAY)
        nota.next_to(header, DOWN, buff=0.3)
        self.play(FadeIn(nota))

        eq1 = MathTex(r"x + y = 2",   font_size=38)
        eq2 = MathTex(r"2x + 2y = 5", font_size=38)
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
            r"1 & 1 & 2 \\"
            r"2 & 2 & 5"
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
class S4_Pivoteo(Scene):
    def construct(self):
        header = Text("Paso 2: Pivoteo Parcial", font_size=40, color=BLUE, weight=BOLD)
        header.to_edge(UP, buff=0.4)
        self.play(Write(header))

        nota = Text("Buscamos el mayor |valor| en la columna 1:", font_size=26, color=GRAY)
        nota.next_to(header, DOWN, buff=0.3)
        self.play(FadeIn(nota))

        mat = MathTex(
            r"\left[\begin{array}{cc|c}"
            r"1 & 1 & 2 \\"
            r"2 & 2 & 5"
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

        swap = Text("→  Intercambiamos  F1  ↔  F2", font_size=28, color=ORANGE)
        swap.next_to(analisis, DOWN, buff=0.3)
        self.play(Write(swap))
        self.wait(1)

        self.play(FadeOut(VGroup(mat, analisis, swap)))

        resultado = Text("Matriz con pivoteo aplicado:", font_size=26, color=RESULT_COLOR)
        resultado.next_to(nota, DOWN, buff=0.4)
        mat2 = MathTex(
            r"\left[\begin{array}{cc|c}"
            r"2 & 2 & 5 \\"
            r"1 & 1 & 2"
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
class S5_Eliminacion(Scene):
    def construct(self):
        header = Text("Paso 3: Eliminación hacia adelante", font_size=38, color=BLUE, weight=BOLD)
        header.to_edge(UP, buff=0.3)
        self.play(Write(header))

        objetivo = Text("Objetivo: hacer cero debajo del pivote en la columna 1",
                        font_size=25, color=GRAY)
        objetivo.next_to(header, DOWN, buff=0.25)
        self.play(FadeIn(objetivo))

        mat_ini = MathTex(
            r"\left[\begin{array}{cc|c}"
            r"2 & 2 & 5 \\"
            r"1 & 1 & 2"
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
        f_m21 = MathTex(r"m_{21} = \frac{a_{21}}{a_{11}} = \frac{1}{2}",
                        font_size=34, color=ELIM_COLOR)
        g_m21 = VGroup(t_m21, f_m21).arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        g_m21.next_to(sep, DOWN, buff=0.3).shift(LEFT * 1)
        self.play(Write(t_m21)); self.play(Write(f_m21)); self.wait(0.8)

        op21 = MathTex(r"F_2 \leftarrow F_2 - \frac{1}{2} \cdot F_1",
                       font_size=32, color=ORANGE)
        op21.next_to(g_m21, DOWN, buff=0.3)
        self.play(Write(op21)); self.wait(1)

        calc21 = MathTex(
            r"F_2: \quad \left[1 - \tfrac{1}{2}(2),\quad 1 - \tfrac{1}{2}(2),\quad 2 - \tfrac{1}{2}(5)\right]",
            font_size=28, color=WHITE
        )
        calc21.next_to(op21, DOWN, buff=0.25)
        self.play(Write(calc21)); self.wait(1)

        res21 = MathTex(r"F_2 \rightarrow \left[0,\quad 0,\quad -\frac{1}{2}\right]",
                        font_size=34, color=ELIM_COLOR)
        res21.next_to(calc21, DOWN, buff=0.25)
        self.play(Write(res21)); self.wait(1.5)

        self.play(FadeOut(VGroup(ini_group, sep, g_m21, op21, calc21, res21, objetivo)))

        # Resultado
        header2 = Text("Resultado de la eliminacion:", font_size=30, color=HEADER_COLOR)
        header2.next_to(header, DOWN, buff=0.35)
        mat_res = MathTex(
            r"\left[\begin{array}{cc|c}"
            r"2 & 2 & 5 \\"
            r"0 & 0 & -\tfrac{1}{2}"
            r"\end{array}\right]",
            font_size=46
        )
        mat_res.next_to(header2, DOWN, buff=0.4)
        self.play(Write(header2), Write(mat_res))
        self.wait(1)

        alerta = Text("⚠  Fila 2:  0x + 0y = -1/2", font_size=30, color=ELIM_COLOR, weight=BOLD)
        alerta.next_to(mat_res, DOWN, buff=0.4)
        self.play(FadeIn(alerta))
        self.wait(2.5)
        self.play(FadeOut(VGroup(header, header2, mat_res, alerta)))


# ═══════════════════════════════════════════════
# ESCENA 6 – Detección de incompatibilidad
# ═══════════════════════════════════════════════
class S6_Incompatible(Scene):
    def construct(self):
        header = Text("Deteccion de Incompatibilidad", font_size=40, color=ELIM_COLOR, weight=BOLD)
        header.to_edge(UP, buff=0.4)
        self.play(Write(header))

        mat_res = MathTex(
            r"\left[\begin{array}{cc|c}"
            r"2 & 2 & 5 \\"
            r"0 & 0 & -\tfrac{1}{2}"
            r"\end{array}\right]",
            font_size=44
        )
        mat_res.next_to(header, DOWN, buff=0.45)
        self.play(Write(mat_res))
        self.wait(0.8)

        fila2 = Text("Fila 2 nos dice:", font_size=28, color=HEADER_COLOR)
        fila2.next_to(mat_res, DOWN, buff=0.4)
        self.play(FadeIn(fila2))

        eq_absurda = MathTex(r"0 \cdot x + 0 \cdot y = -\frac{1}{2}", font_size=40, color=ELIM_COLOR)
        eq_absurda.next_to(fila2, DOWN, buff=0.3)
        self.play(Write(eq_absurda))
        self.wait(0.8)

        simplifica = MathTex(r"0 = -\frac{1}{2}", font_size=46, color=ELIM_COLOR)
        simplifica.next_to(eq_absurda, DOWN, buff=0.3)
        self.play(Write(simplifica))
        self.wait(0.8)

        contradiccion = Text("¡Contradicción! Esto es FALSO para cualquier x, y.",
                             font_size=26, color=ELIM_COLOR, weight=BOLD)
        contradiccion.next_to(simplifica, DOWN, buff=0.4)
        self.play(FadeIn(contradiccion))
        self.wait(1)

        conclusion = Text("→ El sistema NO tiene solución → Sistema Incompatible",
                          font_size=28, color=PIVOT_COLOR, weight=BOLD)
        conclusion.next_to(contradiccion, DOWN, buff=0.35)
        self.play(Write(conclusion))
        self.wait(3)
        self.play(FadeOut(VGroup(header, mat_res, fila2, eq_absurda, simplifica, contradiccion, conclusion)))


# ═══════════════════════════════════════════════
# ESCENA 7 – Resumen y conclusión
# ═══════════════════════════════════════════════
class S7_Conclusion(Scene):
    def construct(self):
        header = Text("Conclusion", font_size=48, color=BLUE, weight=BOLD)
        header.to_edge(UP, buff=0.5)
        self.play(Write(header))

        sistema = MathTex(  
            r"\begin{cases} x + y = 2 \\ 2x + 2y = 5 \end{cases}",
            font_size=44
        )
        sistema.next_to(header, DOWN, buff=0.5)
        self.play(Write(sistema))
        self.wait(0.8)

        razon = Text("La segunda ecuación es  2 × (primera)  pero con distinto término independiente:",
                     font_size=24, color=GRAY)
        razon.next_to(sistema, DOWN, buff=0.4)
        self.play(FadeIn(razon))

        demo = MathTex(r"2(x + y) = 2(2) = 4 \quad \neq \quad 5",
                       font_size=36, color=ELIM_COLOR)
        demo.next_to(razon, DOWN, buff=0.3)
        self.play(Write(demo))
        self.wait(1)

        resumen = VGroup(
            Text("✦ Las rectas son paralelas (misma pendiente)", font_size=26, color=WHITE),
            Text("✦ La eliminacion produce  0 = -1/2", font_size=26, color=WHITE),
            Text("✦ Sistema Incompatible → Sin solucion", font_size=26, color=ELIM_COLOR),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        resumen.next_to(demo, DOWN, buff=0.45)
        self.play(LaggedStart(*[FadeIn(r, shift=RIGHT*0.3) for r in resumen], lag_ratio=0.3))
        self.wait(1.5)

        fin = Text("Sistema sin solucion detectado con Gauss 🎓", font_size=30, color=PIVOT_COLOR, weight=BOLD)
        fin.next_to(resumen, DOWN, buff=0.45)
        self.play(Write(fin))
        self.wait(3)
        self.play(FadeOut(VGroup(header, sistema, razon, demo, resumen, fin)))


# ═══════════════════════════════════════════════
# ESCENA COMPLETA
# ═══════════════════════════════════════════════
class SistemaIncompatible(Scene):
    def construct(self):
        for escena_cls in [
            S1_Sistema,
            S2_Geometria,
            S3_MatrizAumentada,
            S4_Pivoteo,
            S5_Eliminacion,
            S6_Incompatible,
            S7_Conclusion,
        ]:
            escena_cls.construct(self)