from manim_presentation import Slide
from manim import *
from math import *

class stuff(Slide):
    def construct(self):
        # text = Tex(r"Dihedral Group of order 6", color = BLUE).shift(3.0 * UP).scale(1.2)
        # self.play(Write(text), run_time = 2)
        # self.pause()
        
        # img = ImageMobject("D6_cayley").shift(0.5 * DOWN).scale(0.8)

        # self.play(FadeIn(img))
        # self.pause()        

        # text = Tex(r"Cosets of $\{1, b, b^2 \}$", color = BLUE).shift(3.0 * UP).scale(1.2)
        # self.play(Write(text), run_time = 2)
        # self.pause()
        
        # img = ImageMobject("D6_cosets").shift(0.5 * DOWN).scale(0.8)

        # self.play(FadeIn(img))
        # self.pause()  

        # text = Tex(r"Left cosets of $\{1, a\}$", color = BLUE).shift(3.0 * UP).scale(1.2)
        # self.play(Write(text), run_time = 2)
        # self.pause()
        
        # img = ImageMobject("D6_left_cosets").shift(0.5 * DOWN).scale(0.8)

        # self.play(FadeIn(img))
        # self.pause()  

        # text = Tex(r"Right cosets of $\{1, a\}$", color = BLUE).shift(3.0 * UP).scale(1.2)
        # self.play(Write(text), run_time = 2)
        # self.pause()
        
        # img = ImageMobject("D6_right_cosets").shift(0.5 * DOWN).scale(0.8)

        # self.play(FadeIn(img))
        # self.pause()  

        # text = Tex(r"Tower Law explored visually", color = BLUE).shift(3.0 * UP).scale(1.2)
        # self.play(Write(text), run_time = 2)
        # self.pause()
        
        # img = ImageMobject("venn_diagram_rationals").shift(0.5 * DOWN).scale(0.8)

        # self.play(FadeIn(img))
        # self.pause()  

        # self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        # self.pause()

        # text = Tex(r"Galois Group ($\mathbb D_8$)", color = BLUE).shift(3.0 * UP).scale(1.2)
        # self.play(Write(text), run_time = 2)
        # self.pause()
        
        # img = ImageMobject("D8_cayley").shift(0.5 * DOWN).scale(0.8)

        # self.play(FadeIn(img))
        # self.pause()  

        # self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        # self.pause()


        # text = Tex(r"4. Inclusion Diagram", color = BLUE).shift(3.0 * UP).scale(1.2)
        # self.play(Write(text), run_time = 2)
        # self.pause()
        
        # img = ImageMobject("inclusion_diagram").shift(0.5 * DOWN).scale(0.8)

        # self.play(FadeIn(img))
        # self.pause()  

        # self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        # self.pause()

        # text = Tex(r"Construction of $\sqrt 2$", color = BLUE).shift(3.0 * UP).scale(1.2)
        # self.play(Write(text), run_time = 2)
        # self.pause()
        
        # img = ImageMobject("sqrt_2").shift(0.5 * DOWN).scale(0.8)

        # self.play(FadeIn(img))
        # self.pause()  

        # self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        # self.pause()

        text = Tex(r"Square root of $a$", color = BLUE).shift(3.0 * UP).scale(1.2)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        img = ImageMobject("root_construction").shift(0.5 * DOWN).scale(0.8)

        self.play(FadeIn(img))
        self.pause()  

        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        self.pause()
