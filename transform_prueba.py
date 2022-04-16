from manimlib import *
import numpy as np

class TexTransformExample(Scene):
    def construct(self):
        Title = Text("Esto es una prueba")
        self.play(FadeIn(Title), run_time = 2)
        self.play(FadeToColor(Title, RED), run_time = 1)		
        self.play(ScaleInPlace(Title, 2), run_time = 1)		
        self.play(ShrinkToCenter(Title), run_time = 1)		
        ejes = Axes([-2,2],[-1,1])
        ejes.add_coordinate_labels("Tiempo","Espacio")
        self.add(ejes)
        
