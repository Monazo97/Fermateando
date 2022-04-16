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


class Pitagoras(Scene):
    def construct(self):
        set_background(self)
        Titulo_pitagoras = MarkupText("<u>Teorema de Pitágoras</u>", stroke_width = 0.3)
        Titulo_pitagoras.scale(0.7)
        self.play(FadeIn(Titulo_pitagoras),run_time = 1)
        self.play(Titulo_pitagoras.to_edge,UP, run_time = 1.8)
        
        A = Dot([0,4,0])
        B = Dot([0,0,0])
        C = Dot([3,0,0])
        Name = VGroup(Text("A"), Text("B"), Text("C"))
        Puntos = VGroup(
                A, B, C
        )
        Puntos.scale(0.4)
        Name.scale(0.5)
        Puntos.center()
        Puntos.shift(UP + 0.2 * RIGHT)
        Puntos.set_color(BLACK)
        
        AB = Line(A,B, buff = 0)
        BC = Line(B,C, buff = 0)
        CA = Line(C,A, buff = 0)
        
        Segmentos = VGroup(
                AB, BC, CA
        )        
        
        Pos = [UP, DOWN, DOWN]
        
        
        ind = 0
        for i in Puntos:
          self.play(Write(i),run_time = 0.3)
          Name[ind].next_to(i,Pos[ind])
          self.play(Write(Name[ind]),run_time = 0.3)
          ind += 1
        
        for i in Segmentos:
          self.play(Write(i), run_time = 0.3)
          self.bring_to_front(Puntos)
        
        ABC = Square(color = RED, fill_opacity = 0.6)
        vertices = ABC.get_vertices()
        ABC.scale(0.1)
        ABC.shift(B.get_center() - vertices[2])
        self.play(FadeIn(ABC),run_time = 1)
        self.bring_to_front(Puntos)
        
        
        text1 = VGroup(
                TexText("ABC es un triángulo rectángulo (en $B$)"),
                TexText("si y solo si:"),
        )
        text1.center()
        text1.arrange(DOWN,center = False, aligned_edge = LEFT)
        text1.scale(0.50)
        text1.shift(0.8 * DOWN)
        self.play(Write(text1), run_time = 1)
        self.wait(2)
        
        Formula = VGroup(
            TexText("$AB^2$"),
            TexText("$+$"),
            TexText("$BC^2$"),
            TexText("$=$"),
            TexText("$AC^2$"),
        )
        
        Formula.arrange(RIGHT)
        Formula.scale(0.6)
        Formula.next_to(text1,3*DOWN)
        
        self.play(FadeIn(Formula))
        
        idx = 0
        
        colores = [YELLOW, BLUE, ORANGE]
        
        for i in Segmentos:
                self.play(Formula[2*idx].animate.set_color(colores[idx]),Segmentos[idx].animate.set_color(colores[idx]), run_time = 1)
                idx += 1
        
        self.wait(1)
       
        
