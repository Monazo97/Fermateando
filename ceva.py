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


class Ceva(Scene):
    def construct(self):
        set_background(self)
        Titulo_ceva = MarkupText("<u>Teorema de Ceva</u>", size = 45, stroke_width = 0.3)
        self.play(FadeIn(Titulo_ceva),run_time = 3)
        self.play(Titulo_ceva.to_edge,UP, run_time = 1.8)
        
        A = Dot([-1.3,2.76,0])
        B = Dot([-2.74,-2.06,0])
        C = Dot([2,-2,0])
        D = Dot([-0.7,-2.04,0])
        E = Dot([0.14,0.68,0])
        F = Dot([-2.03,0.31,0])
        O = Dot([-0.92,-0.33,0])
        Pos = [UP, DOWN, DOWN, DOWN, RIGHT, LEFT, 0.01 * RIGHT + 1.3 * UP]
        Name = VGroup(Text("A"), Text("B"), Text("C"), Text("D"), Text("E"), Text("F"), Text("O"))
        Puntos = VGroup(
        A, B, C, D, E, F, O
        )
        Puntos.scale(0.4)
        Name.scale(0.5)
        Puntos.center()
        Puntos.shift(UP + 0.2 * RIGHT)
        Puntos.set_color(BLACK)
        
        AF = Line(A,F, buff = 0)
        FB = Line(F,B, buff = 0)
        BD = Line(B,D, buff = 0)
        DC = Line(D,C, buff = 0)
        CE = Line(C,E, buff = 0)
        EA = Line(E,A, buff = 0)
        AD = Line(A,D, buff = 0)
        BE = Line(B,E, buff = 0)
        CF = Line(C,F, buff = 0)
        Segmentos = VGroup(
        AF, FB, BD, DC, CE, EA, AD, BE, CF
        )
        
        
        ind = 0
        for i in Puntos:
          self.play(Write(i),run_time = 0.3)
          Name[ind].next_to(i,Pos[ind])
          self.play(Write(Name[ind]),run_time = 0.3)
          ind += 1
        
        for i in Segmentos:
          self.play(Write(i), run_time = 0.3)
          self.bring_to_front(Puntos)
          
        text1 = VGroup(
        TexText("Las cevianas $AD$, $BE$ y $CF$ concurren en un"),
        TexText("punto llamado $O$ si y sólo si se cumple:"),
        )
        text1.center()
        text1.arrange(DOWN,center = False, aligned_edge = LEFT)
        text1.scale(0.4)
        text1.shift(0.8 * DOWN)
        self.play(Write(text1), run_time = 5)
        self.wait(2)
        
        Formula = VGroup(
            Tex("\\frac{AF}{}"),
            Tex("FB"),
            Tex("\\cdot"),
            Tex("\\frac{BD}{}"),
            Tex("DC"),
            Tex("\\cdot"),
            Tex("\\frac{CE}{}"),
            Tex("EA"),
            Tex(" = 1")
        )

        for i in range(1,9):
          if(i % 3 == 1):
            Formula[i].next_to(Formula[i-1],DOWN)
            continue
          
          if(i % 3 == 2):
            Formula[i].next_to(Formula[i-2],RIGHT)
            continue
          if(i % 3 == 0):
            Formula[i].next_to(Formula[i-1],RIGHT)
            continue
        
        Formula[8].shift(0.2 * DOWN)
        
        Formula.scale(0.6)
        Formula.next_to(text1,3*DOWN)
        self.play(FadeIn(Formula))
        Sec = [AF, FB, BD, DC, CE, EA]
        Sec2 = [0,1,3,4,6,7]
        for i in range(0,6):
          if(i > 0):
            self.play(Sec[i-1].animate.set_color(WHITE),Formula[Sec2[i-1]].animate.set_color(WHITE))
          if(i%2 == 0):
            self.play(Sec[i].animate.set_color("#EDFE01"),Formula[Sec2[i]].animate.set_color("#EDFE01"))
          else:
            self.play(Sec[i].animate.set_color("#F44611"),Formula[Sec2[i]].animate.set_color("#F44611"))
        
        self.play(Sec[5].animate.set_color(WHITE),Formula[Sec2[5]].animate.set_color(WHITE))
        self.wait(1.5)
        
