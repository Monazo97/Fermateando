from manimlib import *
import numpy as np

# To watch one of these scenes, run the following:
# python -m manim example_scenes.py SquareToCircle
# Use -s to skip to the end and just save the final frame
# Use -w to write the animation to a file
# Use -o to write it to a file and open it once done
# Use -n <number> to skip ahead to the n'th animation of a scene.

def set_background(self):
	background = Rectangle(
		width = FRAME_WIDTH,
		height = FRAME_HEIGHT,
		stroke_width = 0,
		fill_color = FERMATEANDO,
		# ~ fill_color = '#0D3EA4',
		fill_opacity = 1
	)
	self.add(background)

class Menelao(Scene):
  def construct(self):
    set_background(self)
    Title = Text("""
            Teorema de Menelao
            """)
    Title.to_edge(UP)
    self.play(GrowFromCenter(Title))
    #self.wait(2)
    A = Dot([-2,-2,0])
    B = Dot([-0.82,2.12,0])
    C = Dot([1.2,-2,0])
    D = Dot([-1.53,-0.36,0])
    E = Dot([0.7,-1,0])
    F = Dot([4.29,-2,0])
    Pos = [DOWN, UP, DOWN, LEFT, UP + RIGHT, DOWN]
    Name = VGroup(Text("A"), Text("B"), Text("C"), Text("D"), Text("E"), Text("F"))
    Puntos = VGroup(
        A, B, C, D, E, F
    )
    Puntos.shift(0.5 * DOWN)
    ind = 0
    for i in Puntos:
      self.play(Write(i),run_time = 0.3)
      Name[ind].next_to(i,Pos[ind])
      self.play(Write(Name[ind]),run_time = 0.3)
      ind += 1
    #Name[0].next_to(Puntos[0],Pos[0])
    #self.play(Write(Name[0]))
    
    AD = Line(A,D)
    DB = Line(D,B)
    BE = Line(B,E)
    EC = Line(E,C)
    FC = Line(F,C)
    CA = Line(C,A)
    DE = Line(D,E)
    EF = Line(E,F)
    Segmentos = VGroup(
        AD, DB, BE, EC, FC, CA, DE, EF
    )
    for i in Segmentos:
      self.play(Write(i), run_time = 0.3)
      
    Figura = VGroup(
        #A,B,C,D,E,F,AD,DB,BE,EC,FC,CA,DE,EF
        Puntos,Segmentos,Name
    )
    
    self.play(Figura.shift,4 * LEFT)
    #NameA = Text("A")
    #NameA.next_to(A,LEFT)
    #self.play(Write(NameA))
    
    # ------------------- Codigo que anda -------------------
    
    Formula = VGroup(
        Tex("\\frac{AD}{}"),
        Tex("DB"),
        Tex("\\cdot"),
        Tex("\\frac{BE}{}"),
        Tex("EC"),
        Tex("\\cdot"),
        Tex("\\frac{CF}{}"),
        Tex("AF"),
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
    
    Enunciado = TexText(
        """
        Los puntos $D$, $E$ y $F$ son colineales \\
        si y sólo si se cumple:
        """
    )
    
    Enunciado.scale(0.8);
    Enunciado.shift(1.5 * RIGHT + UP);
    
    self.play(FadeIn(Enunciado), run_time = 3);
    
    Formula.shift(0.5 * DOWN + RIGHT)
    self.play(FadeIn(Formula))
    Sec = [AD, DB, BE, EC, FC, CA, FC]
    Sec2 = [0,1,3,4,6,7]
    for i in range(0,6):
      if(i > 0):
        self.play(Sec[i-1].animate.set_color(WHITE),Formula[Sec2[i-1]].animate.set_color(WHITE))
      if(i%2 == 0):
        # Amarillo self.play(Sec[i].animate.set_color("#EDFE01"),Formula[Sec2[i]].animate.set_color("#EDFE01"))
        self.play(Sec[i].animate.set_color(PINK),Formula[Sec2[i]].animate.set_color(PINK))
      else:
        if(i == 5):
          self.play(Sec[i].animate.set_color("#F44611"),Sec[i+1].animate.set_color("#F44611"),Formula[Sec2[i]].animate.set_color("#F44611"))
          continue
        self.play(Sec[i].animate.set_color("#F44611"),Formula[Sec2[i]].animate.set_color("#F44611"))
    
    self.play(Sec[5].animate.set_color(WHITE),Sec[6].animate.set_color(WHITE),Formula[Sec2[5]].animate.set_color(WHITE))
    self.wait(1.5)
      
class Ceva(Scene):
  def construct(self):
    set_background(self)
    Title = Text("Teorema de Ceva")
    Title.to_edge(UP)
    self.play(GrowFromCenter(Title))
    #self.wait(2)
    # ~ self.add(Integer(FRAME_WIDTH))
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
    Puntos.shift(0.8 * DOWN)
    Puntos.scale(0.8)
    #Name[0].next_to(Puntos[0],Pos[0])
    #self.play(Write(Name[0]))
    
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
      
    
    
    Figura = VGroup(
        #A,B,C,D,E,F,AD,DB,BE,EC,FC,CA,DE,EF
        Puntos,Segmentos,Name
    )
    
    
  
    self.play(Figura.shift,4 * LEFT)
    
    
    text1 = TexText("""
    Las cevianas $AD$, $BE$ y $CF$ concurren en un 
    
    punto llamado $O$ si y sólo si se cumple:""")
    text1.scale(0.9)
    text1.next_to(A,10 * RIGHT)
    self.play(Write(text1))
    self.wait(2)
    ##NameA = Text("A")
    ##NameA.next_to(A,LEFT)
    ##self.play(Write(NameA))
    #
    ## ------------------- Codigo que anda -------------------
    #
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
      
