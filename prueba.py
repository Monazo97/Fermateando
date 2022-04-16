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


class TexTransformExample(Scene):
    def construct(self):
        set_background(self)
        self.camera.resize_frame_shape(1)
        Titulo_cuadrado = Text("Cuadrado", size = 75)
        self.play(FadeIn(Titulo_cuadrado),run_time = 3)
        self.play(Titulo_cuadrado.to_edge,UP,Titulo_cuadrado.scale, 0.9, run_time = 3)
        Cuadrado = Square()
        Cuadrado.shift(UP)
        self.play(FadeIn(Cuadrado,run_time = 3))
        Propiedades = VGroup(
        TexText("$\\bullet$ Todos sus lados son iguales", size = 40),
        TexText("$\\bullet$ Su perímetro es $4 \\cdot$ lado", size = 40),
        TexText("$\\bullet$ Su área es lado $\\cdot$ lado", size = 40),
        )
        Propiedades.scale(0.5)
        Propiedades.arrange(1.2 * DOWN)
        Propiedades.shift(0.3 * LEFT + 1.3 * DOWN)
        pos = 0
        for line in Propiedades:
                if pos >= 1:
                        line.align_to(Propiedades[pos-1],LEFT)
                self.play(Write(line),run_time = 3)
                pos += 1
        self.wait(3)
