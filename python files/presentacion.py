from manim import *
import numpy as np
from manim_slides import *

def ReemplazaComas(archivo):
    with open(archivo,mode="r") as file:
        datos = file.read()
        datos = datos.replace(",",".")

    with open(archivo,"w") as file:
        file.write(datos)
def SeparaVariables(array):
    x = array[:,1]
    y = array[:,0]
    return x,y

datos10g = np.loadtxt("datos10g.txt")
datos8g = np.loadtxt("datos8g.txt")
datos6g = np.loadtxt("datos6g.txt")
datos4g = np.loadtxt("datos4g.txt")
datos2g = np.loadtxt("datos2g.txt")
datos_primera_graf = np.loadtxt("datos_primera_graf.txt")
datos_grafica2 = np.loadtxt("datos_grafica2.txt")
datos10g_x, datos10g_y = SeparaVariables(datos10g)
datos8g_x, datos8g_y = SeparaVariables(datos8g)
datos6g_x, datos6g_y = SeparaVariables(datos6g)
datos4g_x, datos4g_y = SeparaVariables(datos4g)
datos2g_x, datos2g_y = SeparaVariables(datos2g)
datos_primera_graf_y, datos_primera_graf_x = SeparaVariables(datos_primera_graf)
datos_grafica2_x, datos_grafica2_y = SeparaVariables(datos_grafica2)

class Presentacion1(Slide):
    def construct(self):
        Nombre = Tex("Daniel Escribano Rodríguez")
        self.play(Write(Nombre))
        self.play(Nombre.animate.move_to([0,-2,0]).scale(0.5))
        Titulo = Tex("Fuerza, masa y aceleración").scale(2)
        self.play(Write(Titulo))
        # ^DIAPOSITIVA: Título de la presentación con autor
        tex_titulo_objetivos = Tex("Objetivos").scale(2)
        self.next_slide()
        self.play(FadeOut(Nombre),Transform(Titulo,tex_titulo_objetivos))
        self.play(Titulo.animate.move_to([0,3,0]).scale(0.5).set_color(YELLOW))
        self.next_slide()
        bulleted_list_objetivos = BulletedList(r"Obtener una medida de $g$",
                                               r"Obtener la masa total del sistema de la polea $M$ \\ (constante durante esta parte) a partir de las \\ aceleraciones observadas",
                                               r"Obtener la fricción $F_R$",
                                               r"Comprobar la segunda ley de Newton teniendo en \\ cuenta la aceleración producida por el rozamiento").shift(0.5*DOWN)
        self.play(Write(bulleted_list_objetivos[0]))
        self.next_slide()
        self.play(Write(bulleted_list_objetivos[1]))
        self.next_slide()
        self.play(Write(bulleted_list_objetivos[2]))
        self.next_slide()
        self.play(Write(bulleted_list_objetivos[3]))
        # ^DIAPOSITIVA: Todos los objetivos en pantalla
        self.next_slide()
        self.play(FadeOut(bulleted_list_objetivos))
        self.play(Titulo.animate.move_to(ORIGIN).scale(2).set_color(WHITE))
        tex_titulo_teoria = Tex("Fundamento teórico").scale(2)
        self.play(Transform(Titulo, tex_titulo_teoria))
        self.play(ShowPassingFlash(Underline(Titulo)))
        self.play(Titulo.animate.move_to([0, 3, 0]).scale(0.5).set_color(YELLOW))
        exp_inicial = Tex(r"Se tiene un sistema formado por una polea \\ de la que cuelgan dos masas a través de un hilo")
        self.play(Write(exp_inicial))
        # ^DIAPOSITIVA: explicación inicial del sistema
        self.next_slide()
        self.play(FadeOut(exp_inicial))
        eq_leynewton = MathTex("F = ma").scale(2)
        exp_eq_leynewton = Tex("La base es la segunda ley de Newton").move_to([0,-2,0])
        self.play(FadeIn(eq_leynewton), Write(exp_eq_leynewton))
        # ^DIAPOSITIVA: La ecuación de Newton en pantalla con su explicación
        self.next_slide()
        self.play(FadeOut(eq_leynewton), Unwrite(exp_eq_leynewton))
        eq_newton_ref1 = MathTex("M","=","m_1","+","m_2").scale(2)
        eq_newton_ref2 = MathTex("M", "=", "m_1", "+", "m_2", "+", "m_e").scale(2)
        eq_newton_expand = MathTex("M","=","m_1","+","m_2","+","m_e").scale(2)
        eq_newton_expand[0].move_to(ORIGIN)
        exp_M = Tex("Representa la masa total del sistema").move_to([0, -2, 0])
        for i in (1,2,3,4):
            eq_newton_expand[i].move_to(eq_newton_ref1[i])
        self.play(Write(eq_newton_expand[0]), FadeIn(exp_M))
        # ^DIAPOSITIVA: M escrita en pantalla con su explicación
        self.next_slide()
        self.play(FadeOut(exp_M))
        exp_m1_m2 = Tex("Donde $m_1$ y $m_2$ son las masas de las pesas").move_to([0, -2, 0])
        self.play(eq_newton_expand[0].animate.move_to(eq_newton_ref1[0]))
        self.play(FadeIn(exp_m1_m2), *[Write(eq_newton_expand[i]) for i in (1,2,3,4)])
        # ^DIAPOSITIVA: M = m1 + m2 con su explicación
        self.next_slide()
        exp_me = Tex("Se tiene en cuenta también la polea").move_to([0, -2, 0])
        self.play(FadeOut(exp_m1_m2), *[eq_newton_expand[i].animate.move_to(eq_newton_ref2[i]) for i in (0,1,2,3,4)])
        self.play(FadeIn(exp_me),Write(eq_newton_expand[5]), Write(eq_newton_expand[6]))
        # ^DIAPOSITIVA: M = m1 + m2 + m_e con su explicación
        self.next_slide()
        self.play(FadeOut(exp_me),*[FadeOut(eq_newton_expand[i]) for i in (1,2,3,4,5,6)])
        eq_M = MathTex("M").scale(2)
        eq_f_completa = MathTex("F","=","M","a","+","F_R").scale(2)
        eq_f_completa_parte2 = MathTex(r"\Delta m g", "=", "M", "a", "+", "F_R").scale(2)
        eq_M.move_to(eq_f_completa[2])
        exp_F_ma = Tex(r"El sistema se mueve con aceleración \\ e interviene cierto rozamiento").move_to([0, -2, 0])
        self.play(TransformMatchingShapes(eq_newton_expand[0], eq_M))
        self.play(FadeIn(exp_F_ma),*[Write(eq_f_completa[i]) for i in (0,1,3,4,5)])
        self.remove(eq_M)
        self.add(eq_f_completa[2])
        # ^DIAPOSITIVA: F = Ma + F_R y su explicación
        self.next_slide()
        exp_Dm_g = Tex(r"Pero $F$ también es $\Delta m g$").move_to([0,-2,0])
        self.play(FadeOut(exp_F_ma),*[eq_f_completa[i].animate.move_to(eq_f_completa_parte2[i]) for i in (1,2,3,4,5)])
        self.play(FadeIn(exp_Dm_g),Transform(eq_f_completa[0],eq_f_completa_parte2[0]))
        # ^DIAPOSITIVA: Dm*g = Ma + F_R y su explicación
        self.next_slide()
        eq_a_1_M = MathTex(r"a = (m_1 - m_2) g \frac{1}{M}").scale(2)
        exp_a_1_M = Tex(r"Manteniendo $F$ constante se puede \\deducir esta relación de $a$ con $\frac{1}{M}$").move_to([0,-2,0])
        self.play(FadeOut(exp_Dm_g), *[FadeOut(eq_f_completa[i]) for i in (0,1,2,3,4,5)])
        self.play(Write(eq_a_1_M),FadeIn(exp_a_1_M))
        self.next_slide()
        self.play(FadeOut(exp_a_1_M),Unwrite(eq_a_1_M))
        self.play(Titulo.animate.move_to(ORIGIN).scale(2).set_color(WHITE))
        self.play(Transform(Titulo, Tex("Procedimiento").scale(2)))
        self.play(Titulo.animate.move_to([0, 3, 0]).scale(0.5).set_color(YELLOW))

class Presentacion2(Slide):
    def construct(self):
        Titulo = Tex("Procedimiento").move_to([0, 3, 0]).set_color(YELLOW)
        self.add(Titulo)
        esquema = SVGMobject('esquema_experimento_vectores.svg',stroke_width=2).scale(2.5).shift(DOWN)
        self.play(Write(esquema,run_time=3))
        self.next_slide()
        procedimientos = BulletedList(
            r"El sensor mide la velocidad y aceleración del sistema",
            r"Se mantienen constantes 120g repartidos entre los dos extremos",
            r"Se mide la aceleración del rozamiento manteniendo $\Delta m = 0$",
            r"Se miden aceleraciones para $\Delta m = 4$ g y se corrigen"
        )
        self.play(ReplacementTransform(esquema, procedimientos[0]))
        self.next_slide()
        self.play(Write(procedimientos[1]))
        self.next_slide()
        self.play(Write(procedimientos[2]))
        self.next_slide()
        self.play(Write(procedimientos[3]))
        self.next_slide()
        self.play(Uncreate(procedimientos))
        self.play(Titulo.animate.move_to(ORIGIN).scale(2).set_color(WHITE))
        self.play(Transform(Titulo, Tex("Resultados").scale(2)))
        self.play(Titulo.animate.move_to([0, 3, 0]).scale(0.5).set_color(YELLOW))
        tex_inicial = Tex(r"Para una masa total de 120g en las pesas con \\ $\Delta m$ desde 2g hasta 10g")
        self.play(Write(tex_inicial))
        self.next_slide()
        self.play(FadeOut(tex_inicial, Titulo))

class Resultados1(Slide):
    def construct(self):
        ax = Axes(
            x_range=[0,1,0.1],
            y_range=[0.1,1.1,0.1],
            tips=False,
            axis_config={"include_numbers":True}
        )
        titulo_ejes = ax.get_axis_labels(
            x_label=r"t \textrm{ (s)}",
            y_label=r"v \textrm{ (m} \cdot \textrm{s}^{-1})"
        )
        puntos10g = ax.plot_line_graph(
            x_values=datos10g_x,
            y_values=datos10g_y
        )
        recta10g = ax.plot(
            lambda x: 0.732*x + 0.317,
            x_range=[0,1],
            color=MAROON_E
        )
        recta8g = ax.plot(
            lambda x: 0.575*x + 0.145,
            x_range=[0,1],
            color=MAROON_E
        )
        recta6g = ax.plot(
            lambda x: 0.421 * x + 0.0838,
            x_range=[0.05, 1],
            color=MAROON_E,
        )
        recta4g = ax.plot(
            lambda x: 0.261 * x + 0.174,
            x_range=[0, 1],
            color=MAROON_E
        )
        recta2g = ax.plot(
            lambda x: 0.104 * x + 0.0937,
            x_range=[0, 1],
            color=MAROON_E
        )
        puntos10g = puntos10g["vertex_dots"]
        tex_Dm = Tex(r"$\Delta m = 10$g").to_edge(UP)
        self.play(Write(titulo_ejes),Create(ax),Create(recta10g),DrawBorderThenFill(puntos10g), Write(tex_Dm))
        puntos8g = ax.plot_line_graph(
            x_values=datos8g_x,
            y_values=datos8g_y
        )["vertex_dots"]
        puntos6g = ax.plot_line_graph(
            x_values=datos6g_x,
            y_values=datos6g_y
        )["vertex_dots"]
        puntos4g = ax.plot_line_graph(
            x_values=datos4g_x,
            y_values=datos4g_y
        )["vertex_dots"]
        puntos2g = ax.plot_line_graph(
            x_values=datos2g_x,
            y_values=datos2g_y
        )["vertex_dots"]
        self.next_slide()
        self.play(Transform(puntos10g,puntos8g),Transform(recta10g,recta8g), Transform(tex_Dm, Tex(r"$\Delta m = 8$g").to_edge(UP)))
        self.next_slide()
        self.play(Transform(puntos10g, puntos6g),Transform(recta10g,recta6g), Transform(tex_Dm, Tex(r"$\Delta m = 6$g").to_edge(UP)))
        self.next_slide()
        self.play(Transform(puntos10g,puntos4g),Transform(recta10g,recta4g), Transform(tex_Dm, Tex(r"$\Delta m = 4$g").to_edge(UP)))
        self.next_slide()
        self.play(Transform(puntos10g, puntos2g), Transform(recta10g, recta2g), Transform(tex_Dm, Tex(r"$\Delta m = 2$g").to_edge(UP)))
        self.next_slide()
        tabla_valores = MathTable(
            [[r"0.7310 \pm 0.0007", "0.098"],
             [r"0.5730 \pm 0.0004", "0.0784"],
             [r"0.4200 \pm 0.0003", "0.0588"],
             [r"0.2630 \pm 0.0003", "0.0392"],
             [r"0.1120 \pm 0.0003", "0.0196"]],
            col_labels=[Tex(r"$a$ (m$\cdot$s$^{-2}$)"), Tex(r"$\Delta m\cdot g$ (N)")],
            top_left_entry=Star().scale(0.3),
            include_outer_lines=True
        )
        grupo_grafica = VGroup(puntos10g,recta10g,ax,titulo_ejes)
        self.play(FadeOut(tex_Dm), Transform(grupo_grafica,tabla_valores))
        self.next_slide()
        ax_2 = Axes(
            x_range=[0.1,0.8,0.1],
            y_range=[0.01,0.1,0.01],
            tips=False,
            axis_config={"include_numbers":True}
        )
        titulo_ejes_2 = ax_2.get_axis_labels(
            x_label=r"a \textrm{ (m} \cdot \textrm{s}^{-2})",
            y_label=r"\Delta m g \textrm{ (N)}"
        )
        puntos_grafica1 = ax_2.plot_line_graph(
            x_values=datos_primera_graf_x,
            y_values=datos_primera_graf_y
        )["vertex_dots"]
        recta_grafica1 = ax_2.plot(
            lambda x: 0.1266 * x + 0.0056,
            x_range=[0.1,0.8,0.1],
            color=DARK_BLUE
        )
        R2_graf1 = Tex(r"$R^2 = 0.9999$").move_to(2.5 * UP + 3 * LEFT)
        eq_recta_graf1 = Tex(r"$y = 0.1266 x + 0.0056$").next_to(R2_graf1, DOWN)
        self.play(ReplacementTransform(grupo_grafica, ax_2), Write(titulo_ejes_2))
        self.play(DrawBorderThenFill(recta_grafica1), Write(puntos_grafica1))
        self.next_slide()
        self.play(TransformFromCopy(recta_grafica1, eq_recta_graf1), Write(R2_graf1))
        self.wait(0.1)
        self.next_slide()
        self.play(FadeOut(recta_grafica1),FadeOut(R2_graf1),FadeOut(ax_2),FadeOut(titulo_ejes_2),FadeOut(puntos_grafica1))
        self.play(eq_recta_graf1.animate.move_to(ORIGIN).scale(2))

class Resultados2(Slide):
    def construct(self):
        eq_recta_graf1 = MathTex(r"y = ",r"0.1266",r" x + ",r"0.0056").scale(2)
        eq_teorica_graf1 = Tex(r"De $\Delta m g = Ma + F_R$ se deduce que la pendiente es $M$ \\ y la ordenada en el origen $F_R$").next_to(eq_recta_graf1,DOWN)
        self.add(eq_recta_graf1)
        self.next_slide()
        self.play(Write(eq_teorica_graf1))
        self.next_slide()
        self.play(Unwrite(eq_teorica_graf1))
        eq_M_valor = MathTex(r"M = (",r"0.1266",r" \pm 0.0005)\textrm{ kg}").shift(UP)
        eq_Fr_valor = MathTex(r"F_R = (",r"0.0056",r" \pm 0.0002)\textrm{ N}")
        self.play(eq_recta_graf1.animate.shift(2*DOWN).scale(0.5))
        self.play(Write(eq_M_valor[0]),Write(eq_Fr_valor[0]),TransformFromCopy(eq_recta_graf1[1], eq_M_valor[1]),TransformFromCopy(eq_recta_graf1[3],eq_Fr_valor[1]))
        self.play(Write(eq_M_valor[2]),Write(eq_Fr_valor[2]),FadeOut(eq_recta_graf1))
        self.play(eq_M_valor.animate.move_to(np.array([0,0.5,0])), eq_Fr_valor.animate.move_to(np.array([0,-0.5,0])))
        self.next_slide()
        self.play(FadeOut(eq_M_valor),FadeOut(eq_Fr_valor))
        eq_M_m1_m2 = MathTex(r"M = m_1 + m_2 + m_e = 0.1266")
        eq_me_valor = MathTex(r"m_e = (0.0066 \pm 0.0005)\textrm{ kg}")
        self.play(Write(eq_M_m1_m2))
        self.next_slide()
        exp_me = Tex("Es la masa que le corresponde a la polea").shift(DOWN)
        self.play(TransformMatchingShapes(eq_M_m1_m2,eq_me_valor), FadeIn(exp_me))
        self.next_slide()
        self.play(FadeOut(exp_me,eq_me_valor))
        exp_compensa_Fr = Tex("Para compensar $F_R$ habría que modificar la masa de manera que:").shift(0.5*UP)
        eq_compensa_Fr = MathTex(r"\Delta m^\prime g = M^\prime a").shift(0.5*DOWN)
        exp_compensa_Fr2 = Tex(r"Despejando $m_1^\prime$:").shift(0.5 * UP)
        eq_compensa_Fr2 = MathTex(r"m_1^\prime = \frac{(m_2 + m_e)a + m_2 g}{g - a}").shift(0.5 * DOWN)
        eq_compensa_Fr3 = MathTex(r"m_1^\prime = (0.0644 \pm 0.0002)\textrm{ kg}")
        eq_compensa_Fr4 = MathTex(r"m_1^\prime - m_1 = (-5.8 \pm 1.1)\cdot 10^{-4} \textrm{ kg}")
        self.play(FadeIn(exp_compensa_Fr),Write(eq_compensa_Fr))
        self.next_slide()
        self.play(Unwrite(eq_compensa_Fr), FadeOut(exp_compensa_Fr))
        self.play(Write(eq_compensa_Fr2), FadeIn(exp_compensa_Fr2))
        self.next_slide()
        self.play(ReplacementTransform(eq_compensa_Fr2,eq_compensa_Fr3), FadeOut(exp_compensa_Fr2))
        self.next_slide()
        self.play(ReplacementTransform(eq_compensa_Fr3, eq_compensa_Fr4))
        self.next_slide()
        self.play(FadeOut(eq_compensa_Fr4))

class Resultados3(Slide):
    def construct(self):
        exp_apartado2 = Tex(r"Para $\Delta m = 4$g y $\Delta m = 0$g se miden \\aceleraciones $a$ y $a_r$, respectivamente. \\Se mantiene $F$ constante, pero \\$M$ va desde los $60.6$g hasta los $160.6$g")
        self.play(DrawBorderThenFill(exp_apartado2))
        self.next_slide()
        tabla_aceleraciones =  MathTable(
            [[r"0.5890 \pm 0.0007", r"-0.0650 \pm 0.0010", r"0.6540 \pm 0.0017" ,r"0.0606 \pm 0.0005" ,r"16.50 \pm 0.14"],
             [r"0.4450 \pm 0.0007", r"-0.0383 \pm 0.0006", r"0.4833 \pm 0.0013", r"0.0806 \pm 0.0005", r"12.41 \pm 0.08"],
             [r"0.3500 \pm 0.0003", r"-0.0146 \pm 0.0004", r"0.3646 \pm 0.0007", r"0.1006 \pm 0.0005", r"9.94 \pm 0.05"],
             [r"0.2820 \pm 0.0004", r"-0.0556 \pm 0.0004", r"0.3376 \pm 0.0008", r"0.1206 \pm 0.0005", r"8.29 \pm 0.04"],
             [r"0.2360 \pm 0.0003", r"-0.0611 \pm 0.0007", r"0.2971 \pm 0.0010", r"0.1406 \pm 0.0005", r"7.11 \pm 0.03"],
             [r"0.1850 \pm 0.0012", r"-0.0416 \pm 0.0004", r"0.2266 \pm 0.0016", r"0.1606 \pm 0.0005", r"6.23 \pm 0.02"]],
            col_labels=[Tex(r"$a$ (m$\cdot$s$^{-2}$)").scale(1.5),
                        Tex(r"$a_r$ (m$\cdot$s$^{-2}$)").scale(1.5),
                        Tex(r"$a_c$ (m$\cdot$s$^{-2}$)").scale(1.5),
                        Tex(r"$M$ (kg)").scale(1.5),
                        Tex(r"$M^{-1}$ (kg$^{-1}$)").scale(1.5)
                        ],
            top_left_entry=Star().scale(0.3),
            include_outer_lines=True
        ).scale(0.5)
        self.play(Uncreate(exp_apartado2))
        self.play(Write(tabla_aceleraciones))
        self.next_slide()
        self.play(Unwrite(tabla_aceleraciones))
        ax = Axes(
            x_range=[6,17,2],
            y_range=[0.2,0.7,0.1],
            tips=False,
            axis_config={"include_numbers":True}
        )
        titulo_ejes = ax.get_axis_labels(
            x_label=r"M^{-1} \textrm{ (kg$^{-1}$)}",
            y_label=r"a_c \textrm{ (m} \cdot \textrm{s}^{-2})"
        )
        puntos_grafica2 = ax.plot_line_graph(
            x_values=datos_grafica2_x,
            y_values=datos_grafica2_y
        )["vertex_dots"]
        recta_grafica2 = ax.plot(
            lambda x: 0.0396 * x - 0.0058,
            x_range=[6,17,2],
            color=GREEN_E
        )
        self.play(Write(ax),Write(titulo_ejes))
        self.play(Write(recta_grafica2), Write(puntos_grafica2))
        R2_graf2 = Tex(r"$R^2 = 0.9875$").move_to(2.5 * UP + 3 * LEFT)
        eq_recta_graf2 = Tex(r"$y = 0.040 x - 0.006$").next_to(R2_graf2, DOWN)
        exp_graf2 = VGroup(R2_graf2, eq_recta_graf2)
        self.play(TransformFromCopy(recta_grafica2, exp_graf2))
        self.wait(0.1)
        self.next_slide()
        self.play(FadeOut(exp_graf2), FadeOut(recta_grafica2),FadeOut(ax),FadeOut(puntos_grafica2),FadeOut(titulo_ejes))
        eq_recta = Tex(r"$a_c = 0.040 \frac{1}{M} - 0.006$").shift(0.5*UP)
        eq_ac = MathTex(r"a_c = (m_1 - m_2) g \frac{1}{M}").shift(0.5*DOWN)
        self.play(Write(eq_recta),Write(eq_ac))
        eq_vgrupo = VGroup(eq_ac,eq_recta)
        self.next_slide()
        eq_pendiente = MathTex(r"(m_1 - m_2) g = (0.040 \pm 0.002) \textrm{ N}")
        self.play(ReplacementTransform(eq_vgrupo, eq_pendiente))
        self.next_slide()
        eq_valor_g = MathTex(r"g = (9.912 \pm 0.002)\textrm{ m$\cdot$s$^{-2}$}").scale(2)
        eq_valor_g_real = MathTex(r"g_{\textrm{conocido}} = 9.807 \textrm{ m$\cdot$s$^{-2}$}").shift(DOWN).scale(2)
        self.play(ReplacementTransform(eq_pendiente, eq_valor_g))
        self.play(eq_valor_g.animate.shift(UP), Write(eq_valor_g_real))
        eq_g_diferencia = Tex(r"Difieren un 1\%").next_to(eq_valor_g_real,DOWN)
        self.play(Write(eq_g_diferencia))
        self.next_slide()
        vgrupo_final = VGroup(eq_valor_g_real, eq_valor_g, eq_g_diferencia)
        tex_titulo_final = Tex("Resumen").scale(2)
        self.play(ReplacementTransform(vgrupo_final, tex_titulo_final))
        self.play(tex_titulo_final.animate.move_to([0, 3, 0]).scale(0.5).set_color(YELLOW))

class Resumen(Slide):
    def construct(self):
        titulo = Tex("Resumen").move_to([0, 3, 0]).set_color(YELLOW)
        self.add(titulo)
        bl_resumen = BulletedList(
            r"Se ha comprobado la segunda ley de Newton",
            r"Se ha obtenido la masa equivalente de la polea \\ $m_e = (0.0066 \pm 0.0005)$ kg",
            r"Se ha obtenido la fuerza de rozamiento \\$F_R = 0.0056 \pm 0.0002$ N",
            r"Se ha obtenido el valor de $g$, \\$g = (9.912 \pm 0.002)\textrm{ m$\cdot$s$^{-2}$}$"
        ).shift(0.5*DOWN)
        self.next_slide()
        self.play(Write(bl_resumen[0]))
        self.next_slide()
        self.play(Write(bl_resumen[1]))
        self.next_slide()
        self.play(Write(bl_resumen[2]))
        self.next_slide()
        self.play(Write(bl_resumen[3]))
        self.next_slide()
        self.play(FadeOut(bl_resumen),FadeOut(titulo))
