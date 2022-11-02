from manim import *
from numpy import *

class Bridges(Scene):
    def construct(self):
        text = Tex(r"The Origins of \\ Graph Theory", color = BLUE).scale(1.5)
        self.play(Write(text))
        self.play(Unwrite(text))

        text = Tex(r"The Seven Bridges of Konigsberg", color = BLUE).scale(1.2).shift(2.5 * UP)
        img = ImageMobject(r"C:\Users\haric\OneDrive\Desktop\Files\Code\Manim\MathClub\Konigsberg_bridges.png").scale(2.5).shift(DOWN)
        self.play(Write(text))
        self.play(FadeIn(img))
        self.wait(3)

        img1 = ImageMobject(r"7_bridges.png").scale(1.9).shift(DOWN)
        self.play(FadeOut(img), FadeIn(img1))
        self.wait(2)

        img2 = ImageMobject(r"Konigsberg bridges.png").scale(1.5)
        self.play(FadeOut(img1), FadeIn(img2))
        self.wait(2)

        self.play(*[FadeOut(object) for object in self.mobjects], run_time = 2)

        text = Tex(r"You need two things for the required path: \\ Starting Point \\ Ending Point")
        self.play(Write(text), run_time = 2)
        self.wait(2)
        self.play(Unwrite(text))
    
        text = Tex(r"In any path, \\ vertices other than the starting and ending vertices \\ have even number of edges")
        self.play(Write(text), run_time = 2)
        self.wait(2)
        self.play(Unwrite(text))

        img2 = ImageMobject(r"Konigsberg bridges with numbers.png").scale(2).shift(3 * LEFT)
        self.play(FadeIn(img2))
        self.wait(2)

        table = Table([["Node", r"# Edges"], [str(1), str(3)], [str(2), str(5)], [str(3), str(3)], [str(4), str(3)]]).shift(3.5 * RIGHT).scale(0.8)
        self.play(Create(table))
        self.wait(2)
        self.play(FadeOut(table), FadeOut(img2))

        text = Tex(r"For all of our nodes, \\ We have odd number of edges \\ Whichever two nodes we choose as starting and ending point, \\ two other nodes will have odd number of edges").scale(0.9)
        self.play(Write(text), run_time = 5)
        self.wait(2)
        self.play(FadeOut(text))
        text = Tex(r"So, it is not possible!!").scale(1.1)
        self.play(Create(text))

        self.play(*[FadeOut(object) for object in self.mobjects], run_time = 2)
        

