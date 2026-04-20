from manim import *

# ─────────────────────────────────────────────
#  COLORES PERSONALIZADOS
# ─────────────────────────────────────────────
PIVOT_COLOR    = YELLOW
ELIM_COLOR     = RED
RESULT_COLOR   = GREEN
HEADER_COLOR   = BLUE
HIGHLIGHT_COLOR= ORANGE


# ═══════════════════════════════════════════════
# ESCENA 1 – Título y presentación
# ═══════════════════════════════════════════════
class Escena1_Titulo(Scene):
    def construct(self):
        titulo = Text("Eliminación Gaussiana", font_size=64, color=BLUE, weight=BOLD)
        subtitulo = Text("Métodos Numéricos", font_size=36, color=WHITE)
        subtitulo.next_to(titulo, DOWN, buff=0.4)

        linea = Line(LEFT * 5, RIGHT * 5, color=BLUE, stroke_width=2)
        linea.next_to(subtitulo, DOWN, buff=0.3)

        temas = VGroup(
            Text("✦ Teoría y fundamentos",      font_size=26, color=GRAY),
            Text("✦ Matriz aumentada",           font_size=26, color=GRAY),
            Text("✦ Pivoteo parcial",            font_size=26, color=GRAY),
            Text("✦ Sustitución hacia atrás",    font_size=26, color=GRAY),
            Text("✦ Ejemplo de aplicación real", font_size=26, color=GRAY),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        temas.next_to(linea, DOWN, buff=0.35)

        self.play(Write(titulo))
        self.play(FadeIn(subtitulo), Create(linea))
        self.play(LaggedStart(*[FadeIn(t, shift=RIGHT*0.3) for t in temas], lag_ratio=0.2))
        self.wait(3)
        self.play(FadeOut(VGroup(titulo, subtitulo, linea, temas)))


# ═══════════════════════════════════════════════
# ESCENA 2 – ¿Qué es la Eliminación Gaussiana?
# ═══════════════════════════════════════════════
class Escena2_Teoria(Scene):
    def construct(self):
        header = Text("¿Qué es la Eliminación Gaussiana?", font_size=40, color=BLUE, weight=BOLD)
        header.to_edge(UP, buff=0.5)
        self.play(Write(header))

        definicion = Text(
            "Es un método algebraico para resolver\nsistemas de ecuaciones lineales.",
            font_size=30, color=WHITE, line_spacing=1.4
        ).next_to(header, DOWN, buff=0.5)
        self.play(FadeIn(definicion))
        self.wait(1.5)

        # Sistema de ecuaciones de ejemplo
        sistema_label = Text("Sistema a resolver:", font_size=28, color=HEADER_COLOR)
        sistema_label.next_to(definicion, DOWN, buff=0.5)

        eq1 = MathTex(r"2x + y - z = 8",  font_size=36)
        eq2 = MathTex(r"-3x - y + 2z = -11", font_size=36)
        eq3 = MathTex(r"-2x + y + 2z = -3",  font_size=36)
        sistema = VGroup(eq1, eq2, eq3).arrange(DOWN, buff=0.3)
        brace = Brace(sistema, LEFT, color=WHITE)
        sistema_group = VGroup(brace, sistema).next_to(sistema_label, DOWN, buff=0.3)

        self.play(Write(sistema_label))
        self.play(Create(brace), LaggedStart(Write(eq1), Write(eq2), Write(eq3), lag_ratio=0.3))
        self.wait(1.5)

        # Solución conocida
        sol_label = Text("Solución esperada:", font_size=28, color=GREEN)
        sol_text  = MathTex(r"x = 2, \quad y = 3, \quad z = -1", font_size=34, color=GREEN)
        sol_group = VGroup(sol_label, sol_text).arrange(DOWN, buff=0.2)
        sol_group.next_to(sistema_group, DOWN, buff=0.45)

        self.play(Write(sol_label))
        self.play(Write(sol_text))
        self.wait(2)
        self.play(FadeOut(VGroup(header, definicion, sistema_label, sistema_group, sol_group)))


# ═══════════════════════════════════════════════
# ESCENA 3 – Construcción de la Matriz Aumentada
# ═══════════════════════════════════════════════
class Escena3_MatrizAumentada(Scene):
    def construct(self):
        header = Text("Paso 1: Matriz Aumentada", font_size=40, color=BLUE, weight=BOLD)
        header.to_edge(UP, buff=0.4)
        self.play(Write(header))

        # Sistema
        eq1 = MathTex(r"2x + y - z = 8",     font_size=34)
        eq2 = MathTex(r"-3x - y + 2z = -11", font_size=34)
        eq3 = MathTex(r"-2x + y + 2z = -3",  font_size=34)
        sistema = VGroup(eq1, eq2, eq3).arrange(DOWN, buff=0.35)
        brace = Brace(sistema, LEFT)
        sis_group = VGroup(brace, sistema)
        sis_group.move_to(LEFT * 3)

        self.play(Create(brace), LaggedStart(Write(eq1), Write(eq2), Write(eq3), lag_ratio=0.25))
        self.wait(1)

        flecha = Arrow(LEFT*0.5, RIGHT*0.5, color=YELLOW)
        flecha.move_to(ORIGIN)
        self.play(GrowArrow(flecha))

        # Matriz aumentada
        matriz = MathTex(
            r"\left[\begin{array}{ccc|c}"
            r"2 & 1 & -1 & 8 \\"
            r"-3 & -1 & 2 & -11 \\"
            r"-2 & 1 & 2 & -3"
            r"\end{array}\right]",
            font_size=38
        ).move_to(RIGHT * 3)

        self.play(Write(matriz))
        self.wait(1)

        explicacion = Text(
            "Extraemos los coeficientes y los términos\nindependientes en una sola matriz.",
            font_size=26, color=GRAY, line_spacing=1.3
        ).to_edge(DOWN, buff=0.5)
        self.play(FadeIn(explicacion))
        self.wait(2.5)
        self.play(FadeOut(VGroup(header, sis_group, flecha, matriz, explicacion)))


# ═══════════════════════════════════════════════
# ESCENA 4 – Pivoteo Parcial
# ═══════════════════════════════════════════════
class Escena4_Pivoteo(Scene):
    def construct(self):
        header = Text("Paso 2: Pivoteo Parcial", font_size=40, color=BLUE, weight=BOLD)
        header.to_edge(UP, buff=0.4)
        self.play(Write(header))

        explicacion = Text(
            "Buscamos el mayor valor absoluto en la columna del pivote y reordenamos las filas.",
            font_size=26, color=WHITE
        ).next_to(header, DOWN, buff=0.3)
        self.play(FadeIn(explicacion))
        self.wait(1.5)

        # PASO 1: Matriz original al centro
        mat_label = Text("Matriz original:", font_size=26, color=HEADER_COLOR)
        matriz = MathTex(
            r"\left[\begin{array}{ccc|c}"
            r"2 & 1 & -1 & 8 \\"
            r"-3 & -1 & 2 & -11 \\"
            r"-2 & 1 & 2 & -3"
            r"\end{array}\right]",
            font_size=36
        )
        mat_group = VGroup(mat_label, matriz).arrange(DOWN, buff=0.25)
        mat_group.move_to(ORIGIN + DOWN * 0.5)
        self.play(Write(mat_label), Write(matriz))
        self.wait(1)

        # PASO 2: Notas debajo
        col1_note = Text("Columna 1: |2|=2,  |-3|=3,  |-2|=2", font_size=24, color=PIVOT_COLOR)
        mayor_note = Text("El mayor valor absoluto es |-3| = 3  →  Fila 2 es el pivote", font_size=24, color=PIVOT_COLOR)
        swap_note  = Text("Intercambiamos Fila 1 con Fila 2", font_size=26, color=ORANGE)
        notas = VGroup(col1_note, mayor_note, swap_note).arrange(DOWN, buff=0.25)
        notas.next_to(mat_group, DOWN, buff=0.4)

        self.play(FadeIn(col1_note)); self.wait(0.8)
        self.play(FadeIn(mayor_note)); self.wait(0.8)
        self.play(Write(swap_note)); self.wait(1)

        # PASO 3: Fade out y mostrar resultado
        self.play(FadeOut(mat_group), FadeOut(notas))

        mat_label2 = Text("Despues del pivoteo:", font_size=26, color=GREEN)
        matriz2 = MathTex(
            r"\left[\begin{array}{ccc|c}"
            r"-3 & -1 & 2 & -11 \\"
            r"2 & 1 & -1 & 8 \\"
            r"-2 & 1 & 2 & -3"
            r"\end{array}\right]",
            font_size=36
        )
        mat_group2 = VGroup(mat_label2, matriz2).arrange(DOWN, buff=0.25)
        mat_group2.move_to(ORIGIN + DOWN * 0.3)
        self.play(FadeIn(mat_group2))
        self.wait(2.5)
        self.play(FadeOut(VGroup(header, explicacion, mat_group2)))


# ═══════════════════════════════════════════════
# ESCENA 5 – Eliminación hacia adelante paso a paso
# ═══════════════════════════════════════════════
class Escena5_Eliminacion(Scene):
    def construct(self):
        header = Text("Paso 3: Eliminación hacia adelante", font_size=38, color=BLUE, weight=BOLD)
        header.to_edge(UP, buff=0.3)
        self.play(Write(header))

        # ── Iteración 1: eliminar columna 1 ──
        sub1 = Text("Iteración 1 — Eliminar x de F2 y F3", font_size=28, color=YELLOW)
        sub1.next_to(header, DOWN, buff=0.3)
        self.play(FadeIn(sub1))

        m0 = MathTex(
            r"\left[\begin{array}{ccc|c}"
            r"-3 & -1 & 2 & -11 \\"
            r"2 & 1 & -1 & 8 \\"
            r"-2 & 1 & 2 & -3"
            r"\end{array}\right]",
            font_size=34
        ).next_to(sub1, DOWN, buff=0.3).shift(LEFT*2)
        self.play(Write(m0))
        self.wait(0.5)

        mult1 = MathTex(r"m_{21} = \frac{2}{-3} = -\tfrac{2}{3}", font_size=30, color=ELIM_COLOR)
        mult2 = MathTex(r"m_{31} = \frac{-2}{-3} = \tfrac{2}{3}", font_size=30, color=ELIM_COLOR)
        mults = VGroup(mult1, mult2).arrange(DOWN, buff=0.3)
        mults.next_to(m0, RIGHT, buff=0.8)
        self.play(Write(mult1), Write(mult2))
        self.wait(1)

        op1 = MathTex(r"F_2 \leftarrow F_2 - m_{21} \cdot F_1", font_size=28, color=ORANGE)
        op2 = MathTex(r"F_3 \leftarrow F_3 - m_{31} \cdot F_1", font_size=28, color=ORANGE)
        ops = VGroup(op1, op2).arrange(DOWN, buff=0.25)
        ops.next_to(mults, DOWN, buff=0.4)
        self.play(Write(op1), Write(op2))
        self.wait(1)

        m1 = MathTex(
            r"\left[\begin{array}{ccc|c}"
            r"-3 & -1 & 2 & -11 \\"
            r"0 & \tfrac{1}{3} & \tfrac{1}{3} & \tfrac{2}{3} \\"
            r"0 & \tfrac{5}{3} & \tfrac{2}{3} & \tfrac{13}{3}"
            r"\end{array}\right]",
            font_size=32
        ).next_to(ops, DOWN, buff=0.35).shift(LEFT*1)

        arrow = Arrow(m0.get_bottom(), m1.get_top(), color=GREEN, buff=0.1)
        self.play(GrowArrow(arrow))
        self.play(Write(m1))
        self.wait(2)
        self.play(FadeOut(VGroup(sub1, m0, mults, ops, arrow, m1)))

        # ── Iteración 2: eliminar columna 2 ──
        sub2 = Text("Iteración 2 — Eliminar y de F3", font_size=28, color=YELLOW)
        sub2.next_to(header, DOWN, buff=0.3)
        self.play(FadeIn(sub2))

        m1b = MathTex(
            r"\left[\begin{array}{ccc|c}"
            r"-3 & -1 & 2 & -11 \\"
            r"0 & \tfrac{1}{3} & \tfrac{1}{3} & \tfrac{2}{3} \\"
            r"0 & \tfrac{5}{3} & \tfrac{2}{3} & \tfrac{13}{3}"
            r"\end{array}\right]",
            font_size=34
        ).next_to(sub2, DOWN, buff=0.35).shift(LEFT*2)
        self.play(Write(m1b))

        mult3 = MathTex(r"m_{32} = \frac{5/3}{1/3} = 5", font_size=30, color=ELIM_COLOR)
        mult3.next_to(m1b, RIGHT, buff=0.8)
        op3 = MathTex(r"F_3 \leftarrow F_3 - 5 \cdot F_2", font_size=28, color=ORANGE)
        op3.next_to(mult3, DOWN, buff=0.3)
        self.play(Write(mult3), Write(op3))
        self.wait(1)

        m2 = MathTex(
            r"\left[\begin{array}{ccc|c}"
            r"-3 & -1 & 2 & -11 \\"
            r"0 & \tfrac{1}{3} & \tfrac{1}{3} & \tfrac{2}{3} \\"
            r"0 & 0 & -\tfrac{1}{3} & \tfrac{1}{3}"
            r"\end{array}\right]",
            font_size=32
        ).next_to(op3, DOWN, buff=0.4).shift(LEFT*1)

        arrow2 = Arrow(m1b.get_bottom(), m2.get_top(), color=GREEN, buff=0.1)
        self.play(GrowArrow(arrow2))
        self.play(Write(m2))

        triangular = Text("✓ Forma triangular superior lograda", font_size=26, color=GREEN)
        triangular.next_to(m2, DOWN, buff=0.3)
        self.play(FadeIn(triangular))
        self.wait(2.5)
        self.play(FadeOut(VGroup(header, sub2, m1b, mult3, op3, arrow2, m2, triangular)))


# ═══════════════════════════════════════════════
# ESCENA 6 – Sustitución hacia atrás
# ═══════════════════════════════════════════════
class Escena6_Sustitucion(Scene):
    def construct(self):
        header = Text("Paso 4: Sustitución hacia atrás", font_size=40, color=BLUE, weight=BOLD)
        header.to_edge(UP, buff=0.4)
        self.play(Write(header))

        mat_label = Text("Matriz triangular superior:", font_size=26, color=HEADER_COLOR)
        m_tri = MathTex(
            r"\left[\begin{array}{ccc|c}"
            r"-3 & -1 & 2 & -11 \\"
            r"0 & \tfrac{1}{3} & \tfrac{1}{3} & \tfrac{2}{3} \\"
            r"0 & 0 & -\tfrac{1}{3} & \tfrac{1}{3}"
            r"\end{array}\right]",
            font_size=36
        )
        mat_group = VGroup(mat_label, m_tri).arrange(DOWN, buff=0.2)
        mat_group.next_to(header, DOWN, buff=0.4).shift(LEFT*2)
        self.play(Write(mat_label), Write(m_tri))
        self.wait(1)

        # Paso a paso
        paso_z = MathTex(r"z = \frac{1/3}{-1/3} = -1", font_size=34, color=RESULT_COLOR)
        paso_y = MathTex(r"y = \frac{2/3 - (1/3)(-1)}{1/3} = \frac{1}{1/3} = 3", font_size=30, color=RESULT_COLOR)
        paso_x = MathTex(r"x = \frac{-11 - (-1)(3) - (2)(-1)}{-3} = \frac{-6}{-3} = 2", font_size=28, color=RESULT_COLOR)

        pasos = VGroup(paso_z, paso_y, paso_x).arrange(DOWN, buff=0.4)
        pasos.next_to(mat_group, RIGHT, buff=0.8)

        self.play(Write(paso_z)); self.wait(1)
        self.play(Write(paso_y)); self.wait(1)
        self.play(Write(paso_x)); self.wait(1)

        solucion = MathTex(r"\boxed{x = 2, \quad y = 3, \quad z = -1}", font_size=40, color=GREEN)
        solucion.next_to(pasos, DOWN, buff=0.5)
        self.play(Write(solucion))
        self.play(solucion.animate.scale(1.1), rate_func=there_and_back, run_time=1)
        self.wait(2.5)
        self.play(FadeOut(VGroup(header, mat_group, pasos, solucion)))


# ═══════════════════════════════════════════════
# ESCENA 7 – Aplicación real
# ═══════════════════════════════════════════════
class Escena7_Aplicacion(Scene):
    def construct(self):
        header = Text("Aplicación Real", font_size=44, color=BLUE, weight=BOLD)
        header.to_edge(UP, buff=0.4)
        self.play(Write(header))

        contexto = Text(
            "Circuito eléctrico con 3 mallas\n(Leyes de Kirchhoff)",
            font_size=30, color=WHITE, line_spacing=1.4
        ).next_to(header, DOWN, buff=0.4)
        self.play(FadeIn(contexto))
        self.wait(1.5)

        sistema_label = Text("Sistema de ecuaciones del circuito:", font_size=26, color=HEADER_COLOR)
        eq1 = MathTex(r"2I_1 + I_2 - I_3 = 8 \text{ V}",     font_size=32)
        eq2 = MathTex(r"-3I_1 - I_2 + 2I_3 = -11 \text{ V}", font_size=32)
        eq3 = MathTex(r"-2I_1 + I_2 + 2I_3 = -3 \text{ V}",  font_size=32)

        sistema = VGroup(eq1, eq2, eq3).arrange(DOWN, buff=0.3)
        brace = Brace(sistema, LEFT, color=WHITE)
        sis_group = VGroup(sistema_label, VGroup(brace, sistema).arrange(RIGHT, buff=0.2))
        sis_group.arrange(DOWN, buff=0.3).next_to(contexto, DOWN, buff=0.4)

        self.play(Write(sistema_label))
        self.play(Create(brace), LaggedStart(Write(eq1), Write(eq2), Write(eq3), lag_ratio=0.3))
        self.wait(1)

        solucion = MathTex(
            r"\Rightarrow I_1 = 2\,A, \quad I_2 = 3\,A, \quad I_3 = -1\,A",
            font_size=34, color=GREEN
        ).next_to(sis_group, DOWN, buff=0.4)
        self.play(Write(solucion))

        nota = Text(
            "La solución da las corrientes en cada\nmalla del circuito.",
            font_size=24, color=GRAY, line_spacing=1.3
        ).next_to(solucion, DOWN, buff=0.35)
        self.play(FadeIn(nota))
        self.wait(3)
        self.play(FadeOut(VGroup(header, contexto, sis_group, solucion, nota)))


# ═══════════════════════════════════════════════
# ESCENA 8 – Resumen final
# ═══════════════════════════════════════════════
class Escena8_Resumen(Scene):
    def construct(self):
        titulo = Text("Resumen del Método", font_size=46, color=BLUE, weight=BOLD)
        titulo.to_edge(UP, buff=0.5)
        self.play(Write(titulo))

        pasos = VGroup(
            Text("1. Escribir la Matriz Aumentada  [A|b]",        font_size=28, color=WHITE),
            Text("2. Aplicar Pivoteo Parcial (reordenar filas)",  font_size=28, color=YELLOW),
            Text("3. Eliminación hacia adelante → forma triangular", font_size=28, color=ORANGE),
            Text("4. Sustitución hacia atrás → solución",         font_size=28, color=GREEN),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.45)
        pasos.next_to(titulo, DOWN, buff=0.6)

        for p in pasos:
            self.play(FadeIn(p, shift=RIGHT*0.4))
            self.wait(0.5)

        self.wait(1)

        ventajas = Text(
            "✦ Eficiente  ✦ Sistemático  ✦ Base de muchos métodos numéricos",
            font_size=24, color=GRAY
        ).to_edge(DOWN, buff=0.8)
        self.play(FadeIn(ventajas))

        fin = Text("¡Listo! 🎓", font_size=50, color=BLUE, weight=BOLD)
        fin.next_to(ventajas, UP, buff=0.5)
        self.play(Write(fin))
        self.wait(3)
        self.play(FadeOut(VGroup(titulo, pasos, ventajas, fin)))


# ═══════════════════════════════════════════════
# ESCENA COMPLETA (todas juntas en secuencia)
# ═══════════════════════════════════════════════
class EliminacionGaussiana(Scene):
    def construct(self):
        for escena_cls in [
            Escena1_Titulo,
            Escena2_Teoria,
            Escena3_MatrizAumentada,
            Escena4_Pivoteo,
            Escena5_Eliminacion,
            Escena6_Sustitucion,
            Escena7_Aplicacion,
            Escena8_Resumen,
        ]:
            escena_cls.construct(self)