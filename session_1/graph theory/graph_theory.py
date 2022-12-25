from manim import *
from numpy import *
from manim_slides import *

class Bridges(Slide):
    def construct(self):
        text = Tex(r"The Origins of \\ Graph Theory", color = BLUE).scale(1.5)
        self.play(Write(text))
        self.pause()
        self.play(Unwrite(text))

        text = Tex(r"The Seven Bridges of Konigsberg", color = BLUE).scale(1.2).shift(2.5 * UP)
        img = ImageMobject(r"C:\Users\haric\OneDrive\Desktop\Files\Code\Manim\MathClub\graph theory\\Konigsberg_bridges.png").scale(2.5).shift(DOWN)
        self.play(Write(text))
        self.pause()
        self.play(FadeIn(img))

        self.pause()
        self.wait(3)

        img1 = ImageMobject(r"7_bridges.png").scale(1.9).shift(DOWN)
        self.play(FadeOut(img), FadeIn(img1))
        self.pause()
        self.wait(2)

        img2 = ImageMobject(r"Konigsberg bridges.png").scale(0.7)
        self.play(FadeOut(img1), FadeIn(img2))
        self.pause()

        self.wait(2)

        self.play(*[FadeOut(object) for object in self.mobjects], run_time = 2)

        text = Tex(r"You need two things for the required path: \\ Starting Point \\ Ending Point")
        self.play(Write(text), run_time = 2)
        self.pause()
        self.play(Unwrite(text))
    
        text = Tex(r"In any path, \\ vertices other than the starting and ending vertices \\ have even number of edges")
        self.play(Write(text), run_time = 2)
        self.pause()
        self.play(Unwrite(text))

        img2 = ImageMobject(r"Konigsberg bridges with numbers.png").scale(0.6).shift(3 * LEFT)
        self.play(FadeIn(img2))
        self.pause()

        table = Table([["Node", r"# Edges"], [str(1), str(3)], [str(2), str(5)], [str(3), str(3)], [str(4), str(3)]]).shift(3.5 * RIGHT).scale(0.8)
        self.play(Create(table))
        self.pause()
        self.play(FadeOut(table), FadeOut(img2))

        text = Tex(r"For all of our nodes, \\ We have odd number of edges \\ Whichever two nodes we choose as starting and ending point, \\ two other nodes will have odd number of edges").scale(0.9)
        self.play(Write(text), run_time = 5)
        self.pause()
        self.play(FadeOut(text))
        text = Tex(r"So, it is not possible!!").scale(1.1)
        self.play(Create(text))
        self.pause()

        self.play(*[FadeOut(object) for object in self.mobjects], run_time = 2)
        self.pause()
        self.wait()        
        self.pause()
        self.wait()        



class Problem (Slide):
    def construct(self):
        text = Tex(r"A Problem in \\ Graph Theory", color = BLUE).scale(1.5)
        self.play(Write(text))
        self.pause()
        self.play(Unwrite(text))

        text = Tex(r"Say we're at a party \\ How many people need to be present such that \\ we are guaranteed that at least three of them are \\ (pairwise) mutual friends or\\  (pairwise) mutual strangers?", color = BLUE).scale(1.2)
        self.play(Write(text))
        self.pause()
        
        self.play(Unwrite(text))

        text1 = Tex(r"Solution using Graph Theory", color = BLUE).scale(1.2).shift(3 * UP + 2 * LEFT)
        text2 = Tex(r"\begin{itemize} \item Assume nodes are people \\ \item Blue edge indicates mutual friendship \\ \item Red edge indicates mutual enemity \end{itemize}", color = WHITE).scale(1.2)

        self.play(Write(text1))
        self.play(Write(text2))
        self.pause()
        
        self.play(*[FadeOut(object) for object in self.mobjects], run_time = 2)

        text1 = Tex(r"$$n = 5$$", color = BLUE).scale(1.2).shift(3 * UP + 2 * LEFT)
        img = ImageMobject(r"graph_5").scale(1)

        self.play(Write(text1))
        self.pause()

        self.play(FadeIn(img))
        self.pause()

        self.play(*[FadeOut(object) for object in self.mobjects], run_time = 2)

        text1 = Tex("$$n = 6$$", color = BLUE).scale(1.2).shift(3 * UP + 2 * LEFT)
        text2 = Tex(r"Consider a node P \\ It will have 5 edges connected to it \\ Now, if number of friends to be $\le$ 2,\\ there should be at most two blue edges. \\ $\implies$ there will be atleast three red edges, \\ which doesn't satisfy the requirement!").shift(DOWN)
        self.play(Write(text1))
        self.pause()

        self.play(Write(text2))
        self.pause()

        self.play(Unwrite(text2))

        text = Tex("$$n = 6$$", color = BLUE).scale(1.2).shift(3 * UP + 2 * LEFT)
        img = ImageMobject(r"graph_6").scale(1)

        self.play(FadeIn(img))
        self.pause()

        self.play(*[FadeOut(object) for object in self.mobjects], run_time = 2)

        text1 = Tex("Exercise:", color = BLUE).scale(1.2).shift(3 * UP + 2 * LEFT)
        text = Tex(r"How many people need to be present such that \\ we are guaranteed that at least $n$ of them are \\ (pairwise) mutual friends or \\ (pairwise) mutual strangers", color = BLUE)
        self.play(Write(text), Write(text1))
        self.pause()

        self.play(*[FadeOut(object) for object in self.mobjects], run_time = 2)


        self.pause()
        self.wait()        
        self.pause()
        self.wait()        