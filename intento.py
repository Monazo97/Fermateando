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
		height = FRAME_HEIGHT,
		width = FRAME_HEIGHT * 9 / 16,
		stroke_width = 0,
		fill_color = FERMATEANDO,
		#fill_color = BLUE,
		# ~ fill_color = '#0D3EA4',
		fill_opacity = 1
	)
	self.add(background)

def show_equation(self, titulo, lines): 
	#lines.arrange(RIGHT, buff=SMALL_BUFF)
	# ~ lines.scale(1.3)
	# ~ lines.scale(0.9)
	self.play(GrowFromCenter(titulo))
	self.wait(1)
	
	tam = 0
	for line in lines:
		tam += 1
	
	for i in range(0,tam):
	    lines[i]	.set_color_by_tex_to_color_map({
	        "a": BLUE,
	        "b": YELLOW,
	        "c": RED,
	        "cdot": WHITE,
	    })
	    # ~ lines[i].scale(0.6)
	        
	# ~ lines[1].next_to(lines[0],3 * RIGHT)
	for i in range(1,tam):
		lines[i].next_to(lines[i-1],0.3 * RIGHT)
	
	# ~ x = Integer(FRAME_HEIGHT)
	# ~ self.add(x)
	    
	play_kw = {"run_time": 2}
	self.play(GrowFromCenter(lines[0]))
	self.wait(1)
	
	for i in range(1,tam):	
		self.play(
			TransformMatchingTex(
		        lines[i-1].copy(), lines[i],
		        path_arc=90 * DEGREES,
		    ),
		    **play_kw
		)
		self.wait(1)
	

class TexTransformExample(Scene):
    def construct(self):
        set_background(self)
        # ~ config.frame_height = 30.0
        Title = Text("Factorizaciones copadas")
        Title.to_edge(UP)
        Title.scale(0.5)
        self.play(GrowFromCenter(Title))
        
        
        # ~ x = Integer(self.camera.pixel_height)
        # ~ self.add(x)
        # ~ y = Integer(self.camera.pixel_width)
        # ~ y.next_to(x,RIGHT)
        # ~ self.add(y)
        
        titulos = VGroup(
        	TexText("\\textbf{Factor común}"),
        	TexText("\\textbf{Diferencia de cuadrados}"),
        	TexText("\\textbf{Suma de cubos}"),
		)        	
        
        titulos.scale(0.3)
        
        factor_comun = VGroup(
        	#TexText("\\textbf{Factor común}"),
        	Tex("a" , "b", "+", "a" , "c"),
        	Tex("=", "a", "\\cdot", "(", "b", "+", "c", ")")
        )
        
        diferencia_de_cuadrados  = VGroup(
        	#TexText("\\textbf{Diferencia de cuadrados}"),
        	Tex("a", "^2", "-", "b", "^2"),
        	Tex("=", "(", "a", "+", "b", ")", "\\cdot", "(", "a", "-", "b", ")")
        )
        
        
        suma_de_cubos = VGroup(
        	#TexText("\\textbf{Suma de cubos}"),
        	Tex("a" , "^3", "+", "b" , "^3"),
        	Tex("=", "(", "a", "+", "b", ")", "\\cdot", "(", "a", "^2", "-", "a", "b", "+", "b", "^", "2", ")")
        )
        
        
        
        factorizaciones = VGroup(
        	factor_comun,
        	diferencia_de_cuadrados,
        	suma_de_cubos
        )
        
        factorizaciones.scale(0.3)
        
        titulos.arrange(DOWN, buff=LARGE_BUFF)
        titulos.shift(1.4 * UP + LEFT)
        factorizaciones.arrange(DOWN, buff=LARGE_BUFF)
        # ~ factorizaciones[0].next_to(titulos[0],
        factorizaciones.shift(1.35 * UP + 0.4 * RIGHT)
        
        
        
        show_equation(self, titulos[0], factor_comun)
        show_equation(self, titulos[1], diferencia_de_cuadrados)
        show_equation(self, titulos[2], suma_de_cubos)
	
