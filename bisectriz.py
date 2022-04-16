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
        F = ImageMobject("F.png")
        F.scale(0.3)
        F.to_corner(RIGHT + DOWN, buff = -0.1)
        self.add(F)


class bisectriz(Scene):
    def construct(self):
        set_background(self)
        Titulo = MarkupText("<u>Teorema de la bisectriz</u>", stroke_width = 0.3)
        Titulo.scale(0.65)
        self.play(FadeIn(Titulo),run_time = 1.2)
        self.play(Titulo.to_edge,UP, run_time = 1)
        
        A = Dot([0,4,0])
        B = Dot([-1,-1,0])
        C = Dot([3,-1,0])
        D = Dot([1.68,1.2,0])
        Name = VGroup(Text("A"), Text("B"), Text("C"), Text("D"))
        Puntos = VGroup(
                A, B, C, D
        )
        Puntos.scale(0.4)
        Name.scale(0.5)
        Puntos.center()
        Puntos.shift(1.2 * UP + 0.2 * RIGHT)
        Puntos.set_color(BLACK)
        
        AB = Line(A,B, buff = 0)
        BC = Line(B,C, buff = 0)
        AD = Line(A,D, buff = 0)
        DC = Line(D,C, buff = 0)
        BD = Line(B,D, buff = 0)
        
        Segmentos = VGroup(
                AB, BC, AD, DC, BD
        )        
        
        Pos = [UP, DOWN, DOWN, 0.3*RIGHT + 0.3*UP]
        
        
        ind = 0
        for i in Puntos:
          self.play(Write(i),run_time = 0.3)
          Name[ind].next_to(i,Pos[ind])
          self.play(Write(Name[ind]),run_time = 0.3)
          ind += 1
        
        for i in Segmentos:
          self.play(Write(i), run_time = 0.3)
          self.bring_to_front(Puntos)
        
        PI = 3.14159
        
        ABD = Arc(
                color = RED, 
                fill_opacity = 0,
                stroke_width = 6,
                radius = 0.4,
                arc_center = B.get_center(),
                start_angle = BD.get_angle(),
                angle = AB.get_angle() + PI - BD.get_angle(),        
        )
        
        DBC = Arc(
                color = RED, 
                fill_opacity = 0,
                stroke_width = 6,
                radius = 0.4,
                arc_center = B.get_center(),
                start_angle = BC.get_angle(),
                angle = BD.get_angle() - BC.get_angle(),        
        )
        # ~ self.bring_to_front(Segmentos)
        self.play(Write(ABD), Write(DBC), run_time = 1)
        self.bring_to_front(Segmentos)
        
        Angles_name = VGroup(
                TexText("$\\alpha$", color = RED),
                TexText("$\\alpha$", color = RED),
        )
        Angles_name.scale(0.55)
        
        Angles_name[0].next_to(B,1.5 * UP + 0.8 * RIGHT)
        Angles_name[1].next_to(B,0.4 * UP + 1.7 * RIGHT)
        self.play(FadeIn(Angles_name), run_time = 0.5)
                
        text1 = VGroup(
                TexText("$BD$ es la bisectriz de $A\\widehat{B}C$"),
                TexText("si y solo si:"),
        )
        text1.center()
        text1.arrange(DOWN,center = False, aligned_edge = LEFT)
        text1.scale(0.55)
        text1.shift(0.8 * DOWN)
        self.play(Write(text1), run_time = 1.5)
        self.wait(1)
        
        Formula = VGroup(
            Tex("\\frac{AB}{}"),
            Tex("BC"),
            Tex("="),
            Tex("\\frac{AD}{}"),
            Tex("DC"),
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
                AB, BC, AD, DC
        )     
        
        for i in Seq:
                self.play(Formula[c].animate.set_color(colores[idx]),Seq[idx].animate.set_color(colores[idx]), run_time = 1)
                idx += 1
                c += 1
                if idx == 2:
                        c += 1
        
        self.wait(1)
       
        
