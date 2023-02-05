from manim import *
from numpy import *
from manim_slides import *

class Problem(Slide):
    def construct(self):
        text = Tex(r"Chessboard Problems", color = BLUE).scale(1.5)
        self.play(Write(text))

        self.pause()
        self.play(Unwrite(text))

        text = Tex(r"Part 1: Rooks!", color = BLUE).scale(1.5)
        self.play(Write(text))
        self.pause()

        self.play(Unwrite(text))

        img = ImageMobject("Rook-Move.png").scale(1.5)
        self.play(FadeIn(img))
        self.pause()

        self.play(FadeOut(img))

        text = Tex(r"How many rooks can you place in a chessboard \\ such that none on them control \\ the square on which another lies?\\ In how many ways can this be done?", color = BLUE).shift(UP)
        self.play(Write(text), run_time = 3)
        text1 = Tex(r"Do the same for a $n \times n$ chessboard", color = YELLOW).shift(3 * DOWN).scale(0.8)
        self.play(Write(text1))
        self.pause()

        self.play(*[FadeOut(object) for object in self.mobjects], run_time = 2)

        img = ImageMobject("rook soln.png").scale(1.3)
        self.play(FadeIn(img))
        self.pause()

        self.play(FadeOut(img))
        
        text = Tex(r"In every row, there is one rook \textit{for sure} \\ Each column can contain only one rook \\ First row rook $\rightarrow$ any of the $n$ columns \\ Second row rook $\rightarrow$ any of the $n - 1$ columns \\ . \\ .\\ .\\ nth row rook $\rightarrow$ only $1$ column").shift(UP)
        self.play(Write(text), run_time = 3)

        text2 = Tex(r"Total number of ways = $n \times n - 1 \times n - 2 \times \dots \times 1 = n!$", color = ORANGE).shift(2.5 * DOWN)
        self.play(Write(text2))
        self.pause()

        self.play(*[FadeOut(object) for object in self.mobjects], run_time = 2)

        text = Tex(r"Part 2: Bishops!", color = BLUE).scale(1.5)
        self.play(Write(text))
        self.pause()
        self.play(Unwrite(text))

        img = ImageMobject("Bishop-Move.png").scale(1.5)
        self.play(FadeIn(img))
        self.pause()

        self.play(FadeOut(img))

        text = Tex(r"How many Bishops can you place in a chessboard \\ such that none on them control \\ the square on which another lies?", color = BLUE).shift(UP)
        self.play(Write(text), run_time = 3)
        text1 = Tex(r"Do the same for a $n \times n$ chessboard", color = YELLOW).shift(3 * DOWN).scale(0.8)
        self.play(Write(text1))
        self.pause()

        self.play(*[FadeOut(object) for object in self.mobjects], run_time = 2)

        img = ImageMobject("bishop soln.png").scale(1.3)
        self.play(FadeIn(img))
        self.pause()
        self.play(FadeOut(img))
    
        text2 = Tex(r"Total number of bishops = $2 n - 2$")
        self.play(Write(text2))
        self.pause()        
        self.play(Unwrite(text2))

        text = Tex(r"Part 3: Knights", color = BLUE).scale(1.5)
        self.play(Write(text))
        self.pause()
        self.play(Unwrite(text))

        img = ImageMobject("Knight-Move.png").scale(1.5)
        self.play(FadeIn(img))
        self.pause()
        self.play(FadeOut(img))

        text = Tex(r"How many knights can you place in a chessboard \\ such that none on them control \\ the square on which another lies?\\ In how many ways can this be done?", color = BLUE).shift(UP)
        self.play(Write(text), run_time = 3)
        self.pause()
        self.play(Unwrite(text))

        text = Tex(r"Observe: \\ A knight in a white square \\ always attacks a black square \\ and vice versa", color = BLUE).scale(1.2)
        self.play(Write(text), run_time = 3)
        self.pause()
        self.play(Unwrite(text))

        img2 = ImageMobject("knight soln2.png").scale(1.3)
        self.play(FadeIn(img2))
        self.pause()
        self.play(FadeOut(img2))

        text2 = Tex(r"Total number of knights = 32 \\ Number of ways = 2")
        self.play(Write(text2), run_time = 2)
        self.pause()
        self.play(Unwrite(text2))

        self.pause()
        self.wait()
        self.pause()
        self.wait()
