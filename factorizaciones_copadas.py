from manimlib import *

import numpy as np


def set_background(self):
	# ~ self.set_height(FRAME_HEIGHT)
    # ~ self.set_width(FRAME_WIDTH)
	#reset_pixel_shape(self, 400, 400)
	background = Rectangle(
		width = FRAME_WIDTH,
		height = FRAME_HEIGHT,
		stroke_width = 0,
		fill_color = '#146F44',
		fill_opacity = 1
	)
	self.add(background)

def show_equation(self, titulo, lines): 
	#lines.arrange(RIGHT, buff=SMALL_BUFF)
	# ~ lines.scale(1.3)
	lines.scale(0.9)
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
		lines[i].next_to(lines[i-1],RIGHT)
	
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
        self.play(GrowFromCenter(Title))
        
        x = Integer(self.camera.pixel_height)
        self.add(x)
        y = Integer(self.camera.pixel_width)
        y.next_to(x,RIGHT)
        self.add(y)
        
        titulos = VGroup(
        	TexText("\\textbf{Factor común}"),
        	TexText("\\textbf{Diferencia de cuadrados}"),
        	TexText("\\textbf{Suma de cubos}"),
		)        	
        
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
        
        
        titulos.arrange(DOWN, buff=LARGE_BUFF)
        titulos.shift(0.7 * UP + 4 * LEFT)
        factorizaciones.arrange(DOWN, buff=LARGE_BUFF)
        # ~ factorizaciones[0].next_to(titulos[0],
        factorizaciones.shift(0.7 * UP + 1.3 * RIGHT)
        
        
        
        show_equation(self, titulos[0], factor_comun)
        show_equation(self, titulos[1], diferencia_de_cuadrados)
        show_equation(self, titulos[2], suma_de_cubos)
        #factor_comun.next_to(suma_de_cubos,DOWN)
        
        # lines.arrange(DOWN, buff=LARGE_BUFF)
        # lines.scale(1.3)
        # lines.shift(UP)
        # 
        # for line in lines:
        #     line	.set_color_by_tex_to_color_map({
        #         "a": BLUE,
        #         "b": YELLOW,
        #     })
        #     
        # play_kw = {"run_time": 2}
        # self.play(GrowFromCenter(lines[0]))
        # self.play(
        # 	TransformMatchingTex(
        #         lines[0].copy(), lines[1],
        #         path_arc=90 * DEGREES,
        #     ),
        #     **play_kw
        #  )
        # self.wait()
        # to_isolate = ["B", "C", "=", "(", ")"]
        # lines = VGroup(
        #     # Passing in muliple arguments to Tex will result
        #     # in the same expression as if those arguments had
        #     # been joined together, except that the submobject
        #     # heirarchy of the resulting mobject ensure that the
        #     # Tex mobject has a subject corresponding to
        #     # each of these strings.  For example, the Tex mobject
        #     # below will have 5 subjects, corresponding to the
        #     # expressions [A^2, +, B^2, =, C^2]
        #     Tex("A^2", "+", "B^2", "=", "C^2"),
        #     # Likewise here
        #     Tex("A^2", "=", "C^2", "-", "B^2"),
        #     # Alternatively, you can pass in the keyword argument
        #     # "isolate" with a list of strings that should be out as
        #     # their own submobject.  So the line below is equivalent
        #     # to the commented out line below it.
        #     Tex("A^2 = (C + B)(C - B)", isolate=["A^2", *to_isolate]),
        #     # Tex("A^2", "=", "(", "C", "+", "B", ")", "(", "C", "-", "B", ")"),
        #     Tex("A = \\sqrt{(C + B)(C - B)}", isolate=["A", *to_isolate])
        # )
        # lines.arrange(DOWN, buff=LARGE_BUFF)
        # for line in lines:
        #     line.set_color_by_tex_to_color_map({
        #         "A": BLUE,
        #         "B": TEAL,
        #         "C": GREEN,
        #     })
		# 
        # play_kw = {"run_time": 2}
        # self.add(lines[0])
        # # The animation TransformMatchingTex will line up parts
        # # of the source and target which have matching tex strings.
        # # Here, giving it a little path_arc makes each part sort of
        # # rotate into their final positions, which feels appropriate
        # # for the idea of rearranging an equation
        # self.play(
        #     TransformMatchingTex(
        #         lines[0].copy(), lines[1],
        #         path_arc=90 * DEGREES,
        #     ),
        #     **play_kw
        # )
        # self.wait()
		# 
        # # Now, we could try this again on the next line...
        # self.play(
        #     TransformMatchingTex(lines[1].copy(), lines[2]),
        #     **play_kw
        # )
        # self.wait()
        # # ...and this looks nice enough, but since there's no tex
        # # in lines[2] which matches "C^2" or "B^2", those terms fade
        # # out to nothing while the C and B terms fade in from nothing.
        # # If, however, we want the C^2 to go to C, and B^2 to go to B,
        # # we can specify that with a key map.
        # self.play(FadeOut(lines[2]))
        # self.play(
        #     TransformMatchingTex(
        #         lines[1].copy(), lines[2],
        #         key_map={
        #             "C^2": "C",
        #             "B^2": "B",
        #         }
        #     ),
        #     **play_kw
        # )
        # self.wait()
		# 
        # # And to finish off, a simple TransformMatchingShapes would work
        # # just fine.  But perhaps we want that exponent on A^2 to transform into
        # # the square root symbol.  At the moment, lines[2] treats the expression
        # # A^2 as a unit, so we might create a new version of the same line which
        # # separates out just the A.  This way, when TransformMatchingTex lines up
        # # all matching parts, the only mismatch will be between the "^2" from
        # # new_line2 and the "\sqrt" from the final line.  By passing in,
        # # transform_mismatches=True, it will transform this "^2" part into
        # # the "\sqrt" part.
        # new_line2 = Tex("A^2 = (C + B)(C - B)", isolate=["A", *to_isolate])
        # new_line2.replace(lines[2])
        # new_line2.match_style(lines[2])
		# 
        # self.play(
        #     TransformMatchingTex(
        #         new_line2, lines[3],
        #         transform_mismatches=True,
        #     ),
        #     **play_kw
        # )
        # self.wait(3)
        # self.play(FadeOut(lines, RIGHT))

        # Alternatively, if you don't want to think about breaking up
        # the tex strings deliberately, you can TransformMatchingShapes,
        # which will try to line up all pieces of a source mobject with
        # those of a target, regardless of the submobject hierarchy in
        # each one, according to whether those pieces have the same
        # shape (as best it can).
        
        # ------------- EXAMPLE ------------------
        
        # source = Text("the morse code", height=1)
        # target = Text("here come dots", height=1)
		# 
        # self.play(Write(source))
        # self.wait()
        # kw = {"run_time": 3, "path_arc": PI / 2}
        # self.play(TransformMatchingShapes(source, target, **kw))
        # self.wait()
        # self.play(TransformMatchingShapes(target, source, **kw))
        # self.wait()
