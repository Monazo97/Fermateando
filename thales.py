from manimlib import *
import numpy as np


def set_background(self):
        background = Rectangle(
                width = FRAME_WIDTH,
                height = FRAME_HEIGHT,
                stroke_width = 0,
                fill_color = FERMATEANDO,
                fill_opacity = 1
        )
        self.add(background)


class Thales(Scene):
    def construct(self):
        set_background(self)
        Titulo_thales = MarkupText("<u>Teorema de Thales</u>", stroke_width = 0.3)
        Titulo_thales.scale(0.7)
        self.play(FadeIn(Titulo_thales),run_time = 1)
        self.play(Titulo_thales.to_edge,UP, run_time = 1)
        
        A = Dot([-0.38,1.58,0])
        B = Dot([-1,0,0])
        C = Dot([2,0,0])
        D = Dot([-1.78,-2.01,0])
        E = Dot([5.03,-2.01,0])
        Name = VGroup(Text("A"), Text("B"), Text("C"), Text("D"), Text("E"))
        Puntos = VGroup(
                A, B, C, D, E
        )
        Puntos.scale(0.4)
        Name.scale(0.5)
        Puntos.center()
        Puntos.shift(1.3 * UP + 0.2 * RIGHT)
        Puntos.set_color(BLACK)
        
        AB = Line(A,B, buff = 0)
        AC = Line(C,A, buff = 0)
        BC = Line(B,C, buff = 0)
        BD = Line(B,D, buff = 0)
        CE = Line(C,E, buff = 0)
        DE = Line(D,E, buff = 0)
        
        Segmentos = VGroup(
                AB, BC, AC, BD, CE, DE
        )        
        
        Pos = [UP, 0.7 * LEFT + 0.05 * UP, 0.5 * RIGHT + 0.05 * UP, DOWN , DOWN]
        
        ind = 0
        for i in Puntos:
          self.play(Write(i),run_time = 0.15)
          Name[ind].next_to(i,Pos[ind])
          self.play(Write(Name[ind]),run_time = 0.15)
          ind += 1
        
        for i in Segmentos:
          self.play(Write(i), run_time = 0.3)
          self.bring_to_front(Puntos)
        
        text1 = VGroup(
                TexText("Las rectas $BC$ y $DE$ son paralelas"),
                TexText("si y sólo si:"),
        )
        text1.center()
        text1.arrange(DOWN,center = False, aligned_edge = LEFT)
        text1.scale(0.50)
        text1.shift(0.5 * DOWN)
        self.play(Write(text1), run_time = 2)
        self.wait(0.3)
        
        Formula = VGroup(
            Tex("\\frac{AB}{}"),
            Tex("BD"),
            Tex("="),
            Tex("\\frac{AC}{}"),
            Tex("CE"),
        )
        
        
        Formula[1].next_to(Formula[0],DOWN)
        Formula[2].next_to(Formula[0],RIGHT)
        Formula[3].next_to(Formula[2],RIGHT)
        Formula[2].shift(0.25 * DOWN)
        Formula[4].next_to(Formula[3],DOWN)
        Formula.scale(0.6)
        Formula.next_to(text1,2.5*DOWN)
        
        self.play(FadeIn(Formula))
        
        idx = 0
        c = 0
        
        colores = [YELLOW, GREEN_SCREEN, BLUE, ORANGE]
        
        Seq = VGroup(
                AB, BD, AC, CE
        )     
        
        for i in Seq:
                self.play(Formula[c].animate.set_color(colores[idx]),Seq[idx].animate.set_color(colores[idx]), run_time = 0.75)
                idx += 1
                c += 1
                if idx == 2:
                        c += 1
        
        self.wait(1.5)
       
        
