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
        # ~ F = ImageMobject("auto.png")
        # ~ F.scale(0.4)
        # ~ self.add(F)


def retocar(auto):
        auto.scale(0.3)
        auto.rotate(PI/2)
        return auto
        
def estacionar(self, nombre, largo):
        auto = ImageMobject(str(nombre)+".png")
        
        auto.scale(0.4)
        auto.rotate(PI)
        auto.to_edge(DOWN)
        self.play(FadeIn(auto))
        pos = auto.get_center()
        self.play(auto.shift,largo)
        self.wait(0)
        centro = auto.get_center() + RIGHT
        self.play(Rotating(auto,-PI/2,about_point = centro), run_time = 1)
        self.wait(0)
        self.play(auto.shift,0.8 * RIGHT)
        self.wait(1)

def estacionar2(self, auto, largo):
        pos = auto.get_center()
        self.play(auto.shift,largo)
        self.wait(0)
        centro = auto.get_center() + RIGHT
        self.play(Rotating(auto,-PI/2,about_point = centro), run_time = 1)
        self.wait(0)
        self.play(auto.shift,0.8 * RIGHT)
        self.wait(1)
        
def error(self, nombre, largo):
        auto = ImageMobject(str(nombre)+".png")
        
        auto.scale(0.4)
        auto.rotate(PI)
        auto.to_edge(DOWN)
        self.play(FadeIn(auto))
        pos = auto.get_center()
        self.play(auto.shift,largo)
        self.wait(0)
        centro = auto.get_center() + RIGHT
        self.play(Rotating(auto,-PI/4,about_point = centro), run_time = 1)
        self.wait(0)
        # ~ self.play(auto.shift,0.8 * RIGHT)
        # ~ self.wait(1)
        wrong = ImageMobject("wrong.png")
        self.play(FadeIn(wrong, run_time = 0.5))
        self.play(FadeOut(wrong, run_time = 0.5))
        self.play(Rotating(auto,PI/4,about_point = centro), run_time = 1)
        return auto

class solucion_auto(Scene):
    def construct(self):
        set_background(self)
        
        autoa = ImageMobject("autoa.png")
        autob = ImageMobject("autob.png")
        autoc = ImageMobject("autoc.png")
        autod = ImageMobject("autod.png")
        autoe = ImageMobject("autoe.png")
        
        seq = [3, 4, 2, 1, 3]
        
        autoa = retocar(autoa)
        autob = retocar(autob)
        autoc = retocar(autoc)
        autod = retocar(autod)
        autoe = retocar(autoe)
        
        autoa.to_corner(UP + LEFT)
        autob.next_to(autoa,DOWN)
        autoc.next_to(autob,DOWN)
        autod.next_to(autoc,DOWN)
        autoe.next_to(autod,DOWN)
        
        self.add(autoa)
        self.add(autob)
        self.add(autoc)
        self.add(autod)
        self.add(autoe)
        
        ai = VGroup(
                Integer(seq[0]),
                Integer(seq[1]),
                Integer(seq[2]),
                Integer(seq[3]),
                Integer(seq[4]),
        )
        
        ai[0].next_to(autoa, RIGHT)
        ai[1].next_to(autob, RIGHT)
        ai[2].next_to(autoc, RIGHT)
        ai[3].next_to(autod, RIGHT)
        ai[4].next_to(autoe, RIGHT)
        
        self.add(ai[0])
        self.add(ai[1])
        self.add(ai[2])
        self.add(ai[3])
        self.add(ai[4])
        
        
        estacionamiento = ImageMobject("estacionamiento.png")
        estacionamiento.scale(2)
        estacionamiento.shift(0.3 * RIGHT)
        estacionamiento.shift(0.1 * DOWN)
        self.add(estacionamiento)
        
        estacionar(self, "autoa", 1.8*UP)
        estacionar(self, "autob", 2.8*UP)
        estacionar(self, "autoc", 0.9*UP)
        estacionar(self, "autod", 0*UP)
        autobad = error(self, "autoe", 1.8*UP)
        estacionar2(self,autobad, 1.9 * UP)

def go_foward(self, auto):
        self.play(auto.move_to, 6 * UP, run_time = 2)

class not_valid(Scene):
    def construct(self):
        set_background(self)
        
        autoa = ImageMobject("autoa.png")
        autob = ImageMobject("autob.png")
        autoc = ImageMobject("autoc.png")
        autod = ImageMobject("autod.png")
        autoe = ImageMobject("autoe.png")
        
        seq = [4, 3, 5, 3, 2]
        
        autoa = retocar(autoa)
        autob = retocar(autob)
        autoc = retocar(autoc)
        autod = retocar(autod)
        autoe = retocar(autoe)
        
        autoa.to_corner(UP + LEFT)
        autob.next_to(autoa,DOWN)
        autoc.next_to(autob,DOWN)
        autod.next_to(autoc,DOWN)
        autoe.next_to(autod,DOWN)
        
        self.add(autoa)
        self.add(autob)
        self.add(autoc)
        self.add(autod)
        self.add(autoe)
        
        ai = VGroup(
                Integer(seq[0]),
                Integer(seq[1]),
                Integer(seq[2]),
                Integer(seq[3]),
                Integer(seq[4]),
        )
        
        ai[0].next_to(autoa, RIGHT)
        ai[1].next_to(autob, RIGHT)
        ai[2].next_to(autoc, RIGHT)
        ai[3].next_to(autod, RIGHT)
        ai[4].next_to(autoe, RIGHT)
        
        self.add(ai[0])
        self.add(ai[1])
        self.add(ai[2])
        self.add(ai[3])
        self.add(ai[4])
        
        
        estacionamiento = ImageMobject("estacionamiento.png")
        estacionamiento.scale(2)
        estacionamiento.shift(0.3 * RIGHT)
        estacionamiento.shift(0.1 * DOWN)
        self.add(estacionamiento)
        
        estacionar(self, "autoa", 2.8*UP)
        estacionar(self, "autob", 1.8*UP)
        estacionar(self, "autoc", 3.7*UP)
        autobad = error(self, "autod", 1.8*UP)
        go_foward(self, autobad)
        # ~ estacionar(self, "autod", 0*UP)
        # ~ estacionar2(self,autobad, 1.9 * UP)

def entrar(self, nombre):
    auto = ImageMobject(nombre + ".png")
    auto.scale(0.3)
    auto.rotate(PI)
    auto.to_edge(DOWN)
    auto.shift(0.3 * DOWN)
    auto.shift(2 * RIGHT)
    self.play(FadeIn(auto))
    self.play(auto.shift, 0.6 * UP, run_time = 1)
    centro = auto.get_center() + RIGHT
    self.play(Rotating(auto,-PI /4 - 0.2,about_point = centro), run_time = 1)
    return auto
    
def rotonda(self, auto, grados, tiempo):
    self.play(Rotating(auto,grados,about_point = [2,-0.5,0]), run_time = tiempo)

def girar(self,auto):
    pos = auto.get_center()
    centro = [2,-0.5,0]
    vector = pos - centro
    modulo = 0
    for i in vector:
        modulo += i * i
    modulo = modulo ** 0.5
    # ~ self.add(DecimalNumber(modulo))
    for i in range(0,3):
        vector[i] /= modulo

    # ~ x, y, z = DecimalNumber(vector[0]), DecimalNumber(vector[1]), DecimalNumber(vector[2])
    # ~ y.next_to(x,DOWN)    
    # ~ z.next_to(y,DOWN)
    # ~ self.add(x,y,z)
    # ~ self.add(Dot(pos + vector))
    self.play(Rotating(auto, -PI/2 + 0.2, about_point = pos + vector, run_time = 1)) 

def girar2(self,auto):
    pos = auto.get_center()
    centro = [2,-0.5,0]
    vector = pos - centro
    modulo = 0
    for i in vector:
        modulo += i * i
    modulo = modulo ** 0.5
    for i in range(0,3):
        vector[i] /= modulo

    self.play(Rotating(auto, -PI/2 + 0.75, about_point = pos + vector, run_time = 0.5)) 
    wrong = ImageMobject("wrong.png")
    self.play(FadeIn(wrong, run_time = 0.5))
    self.play(FadeOut(wrong, run_time = 0.5))
    self.play(Rotating(auto, +PI/2 - 0.75, about_point = pos + vector, run_time = 0.5)) 
    
    
    
def adelante(self, auto, distancia):
    pos = auto.get_center()
    centro = [2,-0.5,0]
    vector = pos - centro
    modulo = 0
    for i in vector:
        modulo += i * i
    modulo = modulo ** 0.5
    # ~ self.add(DecimalNumber(modulo))
    for i in range(0,3):
        vector[i] /= modulo
    
    self.play(auto.shift,vector * distancia, run_time = 0.5)

radio_de_giro = [0, 0.15, 1, 1.94, 2.93, 3.93, 4.63]

def estacionar_rotonda(self, parking,nombre):
    if parking == 1:
        cur_auto = entrar(self,nombre)
        rotonda(self,cur_auto, 0.15, 0.5)
        girar(self,cur_auto)
        adelante(self,cur_auto,0.8)
    if parking == 2:
        cur_auto = entrar(self,nombre)
        rotonda(self,cur_auto, 1, 1.3)
        girar(self,cur_auto)
        adelante(self,cur_auto,0.8)
    if parking == 3:
        cur_auto = entrar(self,nombre)
        rotonda(self,cur_auto, 1.94, 1.7)
        girar(self,cur_auto)
        adelante(self,cur_auto,0.8)
    if parking == 4:
        cur_auto = entrar(self,nombre)
        rotonda(self,cur_auto, 2.93 , 2)
        girar(self,cur_auto)
        adelante(self,cur_auto,0.8)
    if parking == 5:
        cur_auto = entrar(self,nombre)
        rotonda(self,cur_auto, 3.93, 3.00)
        girar(self,cur_auto)
        adelante(self,cur_auto,0.8)
    if parking == 6:
        cur_auto = entrar(self,nombre)
        rotonda(self,cur_auto, 4.63, 3.15)
        girar(self,cur_auto)
        adelante(self,cur_auto,0.8)
    return cur_auto

def estacionamiento_con_error(self,parking,segundo,nombre):
    if parking == 1:
        cur_auto = entrar(self,nombre)
        rotonda(self,cur_auto, 0.15, 0.5)
        girar2(self,cur_auto)
    if parking == 2:
        cur_auto = entrar(self,nombre)
        rotonda(self,cur_auto, 1, 1.3)
        girar2(self,cur_auto)
    if parking == 3:
        cur_auto = entrar(self,nombre)
        rotonda(self,cur_auto, 1.94, 1.7)
        girar2(self,cur_auto)
    if parking == 4:
        cur_auto = entrar(self,nombre)
        rotonda(self,cur_auto, 2.93 , 2)
        girar2(self,cur_auto)
    if parking == 5:
        cur_auto = entrar(self,nombre)
        rotonda(self,cur_auto, 3.93, 3.00)
        girar2(self,cur_auto)
    if parking == 6:
        cur_auto = entrar(self,nombre)
        rotonda(self,cur_auto, 4.63, 3.15)
        girar2(self,cur_auto)
    
    if segundo > parking:
        rotonda(self,cur_auto,radio_de_giro[segundo] - radio_de_giro[parking], 1.5)
    else:
        rotonda(self,cur_auto,2*PI + radio_de_giro[segundo] - radio_de_giro[parking], 1.5)
        
    girar(self,cur_auto)
    adelante(self,cur_auto,0.8)
    return cur_auto
        

class circular(Scene):
    def construct(self):
        set_background(self)
        fondo = ImageMobject("parking_circular.png")
        fondo.scale(1.8)
        fondo.shift(2 * RIGHT)
        self.add(fondo)
        autoa = ImageMobject("autoa.png")
        autob = ImageMobject("autob.png")
        autoc = ImageMobject("autoc.png")
        autod = ImageMobject("autod.png")
        autoe = ImageMobject("autoe.png")
        
        seq = [2, 3, 5, 3, 4]
        
        autoa = retocar(autoa)
        autob = retocar(autob)
        autoc = retocar(autoc)
        autod = retocar(autod)
        autoe = retocar(autoe)
        
        autoa.to_corner(UP + LEFT)
        autob.next_to(autoa,DOWN)
        autoc.next_to(autob,DOWN)
        autod.next_to(autoc,DOWN)
        autoe.next_to(autod,DOWN)
        
        self.add(autoa)
        self.add(autob)
        self.add(autoc)
        self.add(autod)
        self.add(autoe)
        
        ai = VGroup(
                Integer(seq[0]),
                Integer(seq[1]),
                Integer(seq[2]),
                Integer(seq[3]),
                Integer(seq[4]),
        )
        
        ai[0].next_to(autoa, RIGHT)
        ai[1].next_to(autob, RIGHT)
        ai[2].next_to(autoc, RIGHT)
        ai[3].next_to(autod, RIGHT)
        ai[4].next_to(autoe, RIGHT)
        
        self.add(ai[0])
        self.add(ai[1])
        self.add(ai[2])
        self.add(ai[3])
        self.add(ai[4])
        
        # ~ self.add(Dot([2,-0.5,0]))
        estacionar_rotonda(self,seq[0],"autoa")
        estacionar_rotonda(self,seq[1],"autob")
        estacionar_rotonda(self,seq[2],"autoc")
        # ~ estacionar_rotonda(self,seq[3],"autod")
        estacionamiento_con_error(self,seq[3],6,"autod")
        estacionar_rotonda(self,seq[4],"autoe")

class circular_con_vuelta(Scene):
    def construct(self):
        set_background(self)
        fondo = ImageMobject("parking_circular.png")
        fondo.scale(1.8)
        fondo.shift(2 * RIGHT)
        self.add(fondo)
        autoa = ImageMobject("autoa.png")
        autob = ImageMobject("autob.png")
        autoc = ImageMobject("autoc.png")
        autod = ImageMobject("autod.png")
        autoe = ImageMobject("autoe.png")
        
        seq = [4, 3, 5, 3, 4]
        
        autoa = retocar(autoa)
        autob = retocar(autob)
        autoc = retocar(autoc)
        autod = retocar(autod)
        autoe = retocar(autoe)
        
        autoa.to_corner(UP + LEFT)
        autob.next_to(autoa,DOWN)
        autoc.next_to(autob,DOWN)
        autod.next_to(autoc,DOWN)
        autoe.next_to(autod,DOWN)
        
        self.add(autoa)
        self.add(autob)
        self.add(autoc)
        self.add(autod)
        self.add(autoe)
        
        ai = VGroup(
                Integer(seq[0]),
                Integer(seq[1]),
                Integer(seq[2]),
                Integer(seq[3]),
                Integer(seq[4]),
        )
        
        ai[0].next_to(autoa, RIGHT)
        ai[1].next_to(autob, RIGHT)
        ai[2].next_to(autoc, RIGHT)
        ai[3].next_to(autod, RIGHT)
        ai[4].next_to(autoe, RIGHT)
        
        self.add(ai[0])
        self.add(ai[1])
        self.add(ai[2])
        self.add(ai[3])
        self.add(ai[4])
        
        # ~ self.add(Dot([2,-0.5,0]))
        auto1 = estacionar_rotonda(self,seq[0],"autoa")
        auto2 = estacionar_rotonda(self,seq[1],"autob")
        auto3 = estacionar_rotonda(self,seq[2],"autoc")
        # ~ estacionar_rotonda(self,seq[3],"autod")
        auto4 = estacionamiento_con_error(self,seq[3],6,"autod")
        auto5 = estacionamiento_con_error(self,seq[4],1,"autoe")
        
        self.wait(2)
        
        self.play(
                FadeOut(autoa),
                FadeOut(autob),
                FadeOut(autoc),
                FadeOut(autod),
                FadeOut(autoe),
                FadeOut(ai),
                run_time = 0.5
        )
        
        todos = Group(fondo,auto1,auto2,auto3,auto4,auto5)
        
        self.play(
                todos.scale,0.7,
                todos.shift, 1.3 * RIGHT,
                run_time = 1
        )
	
        Titulo = MarkupText("<u>Observaciones finales</u>", size = 40, stroke_width = 0.3)
        Titulo. to_edge(UP)
        Titulo.shift(3.5*LEFT)
        self.play(FadeIn(Titulo),run_time = 1)
        pasos = VGroup(
                TexText('''$\\bullet$ Siempre queda un lugar libre'''),
                TexText("$\\bullet$ Cantidad de sucesiones $= (n+1)^{n}$"),
                TexText('''$\\bullet$ Cantidad donde el lugar $n+1$ 
                
                queda libre $ = (n+1)^{n-1}$.'''),
        )
        pasos.arrange(3 * DOWN,center = False, aligned_edge = LEFT)
        pasos.scale(0.9)
        pasos.shift(1.5 * UP)
        pasos.to_edge(LEFT)
        for i in pasos:
                self.play(Write(i),run_time = 1)
                self.wait(1)
        
        self.play(
                FadeOut(Titulo),
                FadeOut(pasos),
                FadeOut(todos),
                run_time = 3
        )
        
        final = VGroup(
                TexText("La cantidad de soluciones donde el estacionamiento de la "),
                TexText("posición $n+1$ queda libre, coincide con la cantidad de"),
                TexText("soluciones de nuestro problema original!!"),
                
        )
        final.arrange(1.5 * DOWN,center = False, aligned_edge = LEFT)
        final.scale(1)
        final.shift(2 * UP)
        
        
        self.play(Write(final), run_time = 6)
        respuesta = TexText("La respuesta es: $(n+1)^{n-1}$")
        respuesta.scale(1.5)
        respuesta.set_color(YELLOW)
        respuesta.next_to(final, 4 * DOWN)
        self.play(Write(respuesta),run_time = 2)
        
class nuevo_juego(Scene):
    def construct(self):
        set_background(self)
        Titulo = MarkupText("<u>Nuevo juego propuesto</u>", size = 45, stroke_width = 0.3)
        Titulo.to_edge(UP)
        self.play(FadeIn(Titulo),run_time = 1)
        pasos = VGroup(
                TexText("$\\bullet$ Estacionamiento circular."),
                TexText("$\\bullet$ Nuevo lugar para estacionar ($n$ autos y $n+1$ lugares)."),
                TexText("$\\bullet$ Cada auto girará en la rotonda hasta encontrar el primer lugar libre."),
        )
        pasos.arrange(3 * DOWN,center = False, aligned_edge = LEFT)
        pasos.scale(0.9)
        pasos.shift(1.5 * UP)
        pasos.to_edge(LEFT)
        for i in pasos:
                self.play(FadeIn(i),run_time = 1)
                self.wait(1)


class enunciado(Scene):
        def construct(self):
                set_background(self)
                Titulo = MarkupText("<u>Enunciado</u>", size = 45, stroke_width = 0.3, color = BLUE)
                Titulo.to_edge(UP)
                self.play(FadeIn(Titulo))
                Texto = VGroup(
                        TexText("Hay $n$ autos, numerados de $1$ a $n$, y una hilera de $n$ lugares para estacionar, "),
                        TexText("también numerados de $1$ a $n$. Cada auto $i$ tiene su lugar preferido $a_i$: cuando"), 
                        TexText("le toca estacionar, se dirige a dicho lugar, si está libre estaciona, y si está     "),
                        TexText("ocupado, avanza hasta encontrar el primer lugar libre, y allí estaciona. Si no      "),
                        TexText("encuentra lugar de este modo, se va y no regresa más. Determinar cuántas            "),
                        TexText("sucesiones de lugares preferidos $a_1$, $a_2$, ... , $a_n$ hay tales que todos      "),
                        TexText("logras estacionar.                                                                  "),
                        TexText("Nota. Autos distintos pueden tener el mismo lugar preferido.                        "),
                )
                Texto.scale(0.8)
                Texto.arrange(DOWN,center = False, aligned_edge = LEFT)
                Texto.shift(2*UP)
                for i in Texto:
                        self.play(AddTextWordByWord(i))

class ultimo(Scene):
        def construct(self):
                set_background(self)
                texto = Text("¿Cómo hacemos para contar las sucesiones que son válidas?")
                texto.set_color(YELLOW)
                texto.move_to(ORIGIN)
                texto.scale(0.9)
                self.play(FadeIn(texto),run_time = 1.5)
                self.wait(1)
                self.play(FadeOut(texto),run_time = 1.5)
