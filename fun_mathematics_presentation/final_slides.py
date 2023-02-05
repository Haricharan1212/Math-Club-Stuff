from manim_presentation import Slide
from manim import *
from math import *

class Scene1(Slide):
    def construct(self):
        text = Tex(r"1", color = BLACK).shift(3.0 * UP).scale(1.8)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Sampark Event", color = GREEN).shift(1.8 * UP).scale(1.8)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Shaastra", color = GREEN).shift(0.6000000000000001 * UP).scale(1.8)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"1", color = BLACK).shift(-0.5999999999999996 * UP).scale(1.8)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Indian Institute of", color = ORANGE).shift(-1.7999999999999998 * UP).scale(1.4)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Technology, Madras", color = ORANGE).shift(-3.0 * UP).scale(1.4)
        self.play(Write(text), run_time = 2)
        self.pause()
        

        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        self.pause()


        text = Tex(r"1", color = BLACK).shift(3.0 * UP).scale(1.8)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Section 1", color = ORANGE).shift(1.5 * UP).scale(1.4)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Chessboard Problems", color = ORANGE).shift(0.0 * UP).scale(1.4)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"1", color = BLACK).shift(-1.5 * UP).scale(1.8)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"1", color = BLACK).shift(-3.0 * UP).scale(1.8)
        self.play(Write(text), run_time = 2)
        self.pause()
        

        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        self.pause()

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
            
        text = Tex(r"1", color = BLACK).shift(3.0 * UP).scale(1.8)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Section 2", color = ORANGE).shift(1.5 * UP).scale(1.4)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Expected Value", color = ORANGE).shift(0.0 * UP).scale(1.4)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"1", color = BLACK).shift(-1.5 * UP).scale(1.8)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"1", color = BLACK).shift(-3.0 * UP).scale(1.8)
        self.play(Write(text), run_time = 2)
        self.pause()
        

        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        self.pause()

            
        text = Tex(r"Motivation", color = BLUE).shift(3.0 * UP).scale(1.2)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"There is a coin, which is tossed $100$ times.", color = WHITE).shift(1.8 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Heads $\rightarrow$ 1 point, Tails $\rightarrow$ 0 points", color = WHITE).shift(0.6000000000000001 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"What will be my score at the end of all tosses?", color = WHITE).shift(-0.5999999999999996 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"1", color = BLACK).shift(-1.7999999999999998 * UP).scale(1.8)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"1", color = BLACK).shift(-3.0 * UP).scale(1.8)
        self.play(Write(text), run_time = 2)
        self.pause()
        

        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        self.pause()

            
        text = Tex(r"Motivation", color = BLUE).shift(3.0 * UP).scale(1.2)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"There is no way to tell the score, without", color = WHITE).shift(1.8 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"actually tossing it $100$ times", color = WHITE).shift(0.6000000000000001 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"But you could talk about the 'average' score!", color = WHITE).shift(-0.5999999999999996 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"The average score would be $50$ points", color = WHITE).shift(-1.7999999999999998 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"This is the notion of \textbf{Expected Value}", color = WHITE).shift(-3.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        

        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        self.pause()

            
        text = Tex(r"An interesting problem", color = BLUE).shift(3.0 * UP).scale(1.2)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"There is a 6-sided die, with", color = WHITE).shift(1.8 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"$1, 2, 3, 4, 5, 6$ equally likely.", color = WHITE).shift(0.6000000000000001 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Your score is the number on your die.", color = WHITE).shift(-0.5999999999999996 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"If you roll the die,", color = WHITE).shift(-1.7999999999999998 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"what score are you expected to get?", color = WHITE).shift(-3.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        

        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        self.pause()

            
        text = Tex(r"Solution", color = BLUE).shift(3.0 * UP).scale(1.2)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"You're likely to get the average score", color = WHITE).shift(1.8 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"$$\frac{1 + 2 + 3 + 4 + 5 + 6}{6} = 3.5$$", color = WHITE).shift(0.6000000000000001 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"1", color = BLACK).shift(-0.5999999999999996 * UP).scale(1.8)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"The expected score is $3.5$,", color = WHITE).shift(-1.7999999999999998 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"which is not on the die", color = WHITE).shift(-3.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        

        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        self.pause()

            
        text = Tex(r"Another problem", color = BLUE).shift(3.0 * UP).scale(1.2)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Consider a biased coin", color = WHITE).shift(1.8 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Heads $\rightarrow$ 1 point $\rightarrow$ $\frac 23$ probability", color = WHITE).shift(0.6000000000000001 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Tails $\rightarrow$ 0 points $\rightarrow$ $\frac 13$ probability", color = WHITE).shift(-0.5999999999999996 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"If you toss the coin 100 times,", color = WHITE).shift(-1.7999999999999998 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"what score are you expected to get?", color = WHITE).shift(-3.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        

        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        self.pause()

            
        text = Tex(r"Solution", color = BLUE).shift(3.0 * UP).scale(1.2)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"A head is twice as likely as a tail", color = WHITE).shift(2.142857142857143 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Expected score is:", color = WHITE).shift(1.2857142857142858 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"$100 \times \left( 1 \times \frac{2}{3} + 0 \times \frac{1}{3} \right) = 66.66..$", color = WHITE).shift(0.4285714285714288 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"In general, it would be:", color = WHITE).shift(-0.4285714285714284 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Heads $\rightarrow$ $s_h$ points $\rightarrow$ $p_h$ probability", color = WHITE).shift(-1.2857142857142856 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Tails $\rightarrow$ $s_t$ points $\rightarrow$ $p_t$ probability", color = WHITE).shift(-2.1428571428571423 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"$\text{n} \times \left( s_h \times p_h + s_t \times p_h \right)$", color = WHITE).shift(-3.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        

        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        self.pause()


        text = Tex(r"Random Variable", color = BLUE).shift(3.0 * UP).scale(1.2)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Consider a probabilistic experiment", color = WHITE).shift(2.142857142857143 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"The outcomes belong to a certain set $S$,", color = WHITE).shift(1.2857142857142858 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"with some probability for each element of S", color = WHITE).shift(0.4285714285714288 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"So, X is a random variable in S", color = WHITE).shift(-0.4285714285714284 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Consider a die roll", color = WHITE).shift(-1.2857142857142856 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"X is a random variable that can take values", color = WHITE).shift(-2.1428571428571423 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"in $\{1, 2, 3, 4, 5, 6 \}$", color = WHITE).shift(-3.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        self.pause()        


        text = Tex(r"Expected Value", color = BLUE).shift(3.0 * UP).scale(1.2)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Random Variable X takes values", color = WHITE).shift(2.142857142857143 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"$X_1$ with probability $p_1$", color = WHITE).shift(1.2857142857142858 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"$X_2$ with probability $p_2$", color = WHITE).shift(0.4285714285714288 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"$\vdots$", color = WHITE).shift(-0.4285714285714284 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"$X_n$ with probability $p_n$", color = WHITE).shift(-1.2857142857142856 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"$E[X] = X_1 p_1 + X_2 p_2 + \dots + X_n p_n$", color = WHITE).shift(-2.1428571428571423 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"So, it is a weighted average!", color = WHITE).shift(-3.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        

        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        self.pause()

            
        # text = Tex(r"1", color = BLACK).shift(3.0 * UP).scale(1.8)
        # self.play(Write(text), run_time = 2)
        # self.pause()
        
        # text = Tex(r"Section 2", color = ORANGE).shift(1.5 * UP).scale(1.4)
        # self.play(Write(text), run_time = 2)
        # self.pause()
        
        # text = Tex(r"Gradient Descent", color = ORANGE).shift(0.0 * UP).scale(1.4)
        # self.play(Write(text), run_time = 2)
        # self.pause()
        
        # text = Tex(r"1", color = BLACK).shift(-1.5 * UP).scale(1.8)
        # self.play(Write(text), run_time = 2)
        # self.pause()
        
        # text = Tex(r"1", color = BLACK).shift(-3.0 * UP).scale(1.8)
        # self.play(Write(text), run_time = 2)
        # self.pause()
        

        # self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        # self.pause()

            
        # text = Tex(r"Motivation", color = ORANGE).shift(3.0 * UP).scale(1.4)
        # self.play(Write(text), run_time = 2)
        # self.pause()
        
        # img = ImageMobject(r"x^2+y^2.png").scale(1.3)      
        # self.play(FadeIn(img))

        # text = Tex(r"$z = x^2 + y^2$", color = GREEN).shift(-3 * UP)
        # self.play(Write(text), run_time = 2)
        # self.pause()
        
        

        # self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        # self.pause()

            
        # text = Tex(r"$$z = f(x, y) = x^2 + y^2$$", color = ORANGE).shift(3.0 * UP).scale(1.4)
        # self.play(Write(text), run_time = 2)
        # self.pause()
        
        # text = Tex(r"Consider the loss function,", color = WHITE).shift(1.8 * UP).scale(1.0)
        # self.play(Write(text), run_time = 2)
        # self.pause()
        
        # text = Tex(r"as in the previous image", color = WHITE).shift(0.6000000000000001 * UP).scale(1.0)
        # self.play(Write(text), run_time = 2)
        # self.pause()
        
        # text = Tex(r"We have to minimize the loss", color = WHITE).shift(-0.5999999999999996 * UP).scale(1.0)
        # self.play(Write(text), run_time = 2)
        # self.pause()
        
        # text = Tex(r"Gradient is direction of steepest ascent", color = WHITE).shift(-1.7999999999999998 * UP).scale(1.0)
        # self.play(Write(text), run_time = 2)
        # self.pause()
        
        # text = Tex(r"So, -gradient is direction of steepest descent", color = WHITE).shift(-3.0 * UP).scale(1.0)
        # self.play(Write(text), run_time = 2)
        # self.pause()
        

        # self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        # self.pause()

            
        # text = Tex(r"We initialize at some random position", color = WHITE).shift(3.0 * UP).scale(1.0)
        # self.play(Write(text), run_time = 2)
        # self.pause()
        
        # text = Tex(r"$\text{Current position} = \text{Current position} - \text{Gradient}$", color = WHITE).shift(2.0 * UP).scale(1.0)
        # self.play(Write(text), run_time = 2)
        # self.pause()
        
        # text = Tex(r"We would move towards the minimum point", color = WHITE).shift(1.0 * UP).scale(1.0)
        # self.play(Write(text), run_time = 2)
        # self.pause()
        
        # text = Tex(r"Note that", color = WHITE).shift(0.0 * UP).scale(1.0)
        # self.play(Write(text), run_time = 2)
        # self.pause()
        
        # text = Tex(r"$\text{Current position} = \text{Current position} - \alpha \text{Gradient}, \alpha > 0$", color = WHITE).shift(-1.0 * UP).scale(1.0)
        # self.play(Write(text), run_time = 2)
        # self.pause()
        
        # text = Tex(r"would also make it move towards the minimum point", color = WHITE).shift(-2.0 * UP).scale(1.0)
        # self.play(Write(text), run_time = 2)
        # self.pause()
        
        # text = Tex(r"This concept is called the gradient descent.", color = WHITE).shift(-3.0 * UP).scale(1.0)
        # self.play(Write(text), run_time = 2)
        # self.pause()
        

        # self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        # self.pause()

            
        # text = Tex(r"Motivation", color = ORANGE).shift(3.0 * UP).scale(1.4)
        # self.play(Write(text), run_time = 2)
        # self.pause()

        # img2 = ImageMobject(r"x^2+y^2_2.png").scale(1.3)      
        # self.play(FadeIn(img2))

        # text = Tex(r"$z = x^2 + y^2$", color = GREEN).shift(-3 * UP)
        # self.play(Write(text), run_time = 2)
        # self.pause()
                

        # self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        # self.pause()

            
        # text = Tex(r"1", color = BLACK).shift(3.0 * UP).scale(1.8)
        # self.play(Write(text), run_time = 2)
        # self.pause()
        
        # text = Tex(r"Section 3", color = ORANGE).shift(1.5 * UP).scale(1.4)
        # self.play(Write(text), run_time = 2)
        # self.pause()
        
        # text = Tex(r"Euler's method for", color = GREEN).shift(0.0 * UP).scale(1.8)
        # self.play(Write(text), run_time = 2)
        # self.pause()
        
        # text = Tex(r"Solving Differential Equations", color = GREEN).shift(-1.5 * UP).scale(1.8)
        # self.play(Write(text), run_time = 2)
        # self.pause()
        
        # text = Tex(r"1", color = BLACK).shift(-3.0 * UP).scale(1.8)
        # self.play(Write(text), run_time = 2)
        # self.pause()
        

        # self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        # self.pause()

            
        # text = Tex(r"Motivating Example", color = GREEN).shift(3.0 * UP).scale(1.8)
        # self.play(Write(text), run_time = 2)
        # self.pause()
        
        # text = Tex(r"Consider the differential equation", color = WHITE).shift(1.8 * UP).scale(1.0)
        # self.play(Write(text), run_time = 2)
        # self.pause()
        
        # text = Tex(r"$\frac{d y(x)}{dx} = x, y(1) = \frac 12$", color = WHITE).shift(0.6000000000000001 * UP).scale(1.0)
        # self.play(Write(text), run_time = 2)
        # self.pause()
        
        # text = Tex(r"The solution, as everyone knows, is:", color = WHITE).shift(-0.5999999999999996 * UP).scale(1.0)
        # self.play(Write(text), run_time = 2)
        # self.pause()
        
        # text = Tex(r"$y(x) = \int x dx = \frac {x^2}2 + C$", color = WHITE).shift(-1.7999999999999998 * UP).scale(1.0)
        # self.play(Write(text), run_time = 2)
        # self.pause()
        
        # text = Tex(r"where solving for $C$, $C = 0$", color = WHITE).shift(-3.0 * UP).scale(1.0)
        # self.play(Write(text), run_time = 2)
        # self.pause()
        

        # self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        # self.pause()

            
        # text = Tex(r"Note that the derivative is defined as", color = WHITE).shift(3.0 * UP).scale(1.0)
        # self.play(Write(text), run_time = 2)
        # self.pause()
        
        # text = Tex(r"$\frac{d y(x)}{dx} = \lim_{h \to 0} \frac{y(x + h) - y(x)}{h}$", color = WHITE).shift(1.5 * UP).scale(1.0)
        # self.play(Write(text), run_time = 2)
        # self.pause()
        
        # text = Tex(r"Here, let's approximate $h \approx 1$", color = WHITE).shift(0.0 * UP).scale(1.0)
        # self.play(Write(text), run_time = 2)
        # self.pause()
        
        # text = Tex(r"Now, rearranging the equation.", color = WHITE).shift(-1.5 * UP).scale(1.0)
        # self.play(Write(text), run_time = 2)
        # self.pause()
        
        # text = Tex(r"$y(x + h) = y(x) + h \frac{d y(x)}{dx}$", color = WHITE).shift(-3.0 * UP).scale(1.0)
        # self.play(Write(text), run_time = 2)
        # self.pause()
        

        # self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        # self.pause()

            
        # text = Tex(r"$y(x + h) = y(x) + h \frac{d y(x)}{dx}$", color = BLUE).shift(3.0 * UP).scale(1.2)
        # self.play(Write(text), run_time = 2)
        # self.pause()
        
        # text = Tex(r"This gives us a wonderful method:", color = WHITE).shift(1.8 * UP).scale(1.0)
        # self.play(Write(text), run_time = 2)
        # self.pause()
        
        # text = Tex(r"$y(2) = y(1) + 1 \times \frac{d y(x)}{dx} |_1$", color = WHITE).shift(0.6000000000000001 * UP).scale(1.0)
        # self.play(Write(text), run_time = 2)
        # self.pause()
        
        # text = Tex(r"$y(2) = y(1) + 1 \times 1 = 2$", color = WHITE).shift(-0.5999999999999996 * UP).scale(1.0)
        # self.play(Write(text), run_time = 2)
        # self.pause()
        
        # text = Tex(r"$y(3) = y(2) + 1 \times 2 = 4$", color = WHITE).shift(-1.7999999999999998 * UP).scale(1.0)
        # self.play(Write(text), run_time = 2)
        # self.pause()
        
        # text = Tex(r"$y(4) = y(3) + 1 \times 3 = 7$", color = WHITE).shift(-3.0 * UP).scale(1.0)
        # self.play(Write(text), run_time = 2)
        # self.pause()
        

        # self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        # self.pause()

            
        # text = Tex(r"$y(x + h) = y(x) + h \frac{d y(x)}{dx}$", color = BLUE).shift(3.0 * UP).scale(1.2)
        # self.play(Write(text), run_time = 2)
        # self.pause()
        
        # img = ImageMobject(r"euler_method.png").scale(1).shift(DOWN)
        # self.play(FadeIn(img))        
        # self.pause()

        # self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        # self.pause()

            
        # text = Tex(r"$y(x + h) = y(x) + h \frac{d y(x)}{dx}$", color = BLUE).shift(3.0 * UP).scale(1.2)
        # self.play(Write(text), run_time = 2)
        # self.pause()

        # text = Tex(r"This might seem like not a very good approximation", color = BLUE).shift(1.25 * UP).scale(1.2)
        # self.play(Write(text), run_time = 2)
        # self.pause()

        # text = Tex(r"That is because, our h is too large", color = BLUE).shift(-1.25 * UP).scale(1.2)
        # self.play(Write(text), run_time = 2)
        # self.pause()

        # text = Tex(r"As an exercise, reduce h and plot the graphs!", color = BLUE).shift(-3 * UP).scale(1.2)
        # self.play(Write(text), run_time = 2)
        # self.pause()


        # self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        # self.pause()

        text = Tex(r"1", color = BLACK).shift(3.0 * UP).scale(1.8)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Section 3", color = ORANGE).shift(1.5 * UP).scale(1.4)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Convolution in", color = GREEN).shift(0.0 * UP).scale(1.8)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Edge Detection", color = GREEN).shift(-1.5 * UP).scale(1.8)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"1", color = BLACK).shift(-3.0 * UP).scale(1.8)
        self.play(Write(text), run_time = 2)
        self.pause()
        

        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        self.pause()

        text = Tex(r"Images in computers", color = BLUE).shift(3.0 * UP).scale(1.2)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Consider a $100 \times 100$ B \& W image", color = WHITE).shift(2.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"An image is stored as a 2-D array", color = WHITE).shift(1.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"$0 \rightarrow$ Black", color = WHITE).shift(0.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"$255 \rightarrow$ White", color = WHITE).shift(-1.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"So, for our purposes,", color = WHITE).shift(-2.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"an image is just a $100 \times 100$ array", color = WHITE).shift(-3.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        

        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        self.pause()

            
        text = Tex(r"What is an edge?", color = BLUE).shift(3.0 * UP).scale(1.2)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"1", color = BLACK).shift(1.5 * UP).scale(1.8)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"An edge is a bunch of pixels,", color = WHITE).shift(0.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"in which the color of the edge pixels", color = WHITE).shift(-1.5 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"is different from the neighbouring pixels", color = WHITE).shift(-3.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        

        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        self.pause()

            
        img3 = ImageMobject("convolution.jpg").scale(1.3)
        self.play(FadeIn(img3))
        self.pause()        

        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        self.pause()

          
        text = Tex(r"Convolution", color = BLUE).shift(3.0 * UP).scale(1.2)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        matrix1 = Matrix([[3, 1, 2, 1], [2, 1, 0, 4], [3, 2, 1, 3], [4, 0, 3, 2]]).scale(0.8).shift(4 * LEFT)
        self.play(Create(matrix1))

        matrix2 = Matrix([[0, 1, 0], [0, 1, 0], [0, 1, 0]]).scale(0.7)
        self.play(Create(matrix2))

        text = Tex(r"$*$").shift(1.6 * LEFT).scale(1.5)
        self.play(Create(text))

        matrix3 = Matrix([[4, 3], [3, 4]]).scale(0.7).shift(5 * RIGHT)
        self.play(FadeIn(matrix3.get_brackets()))

        lists = [0, 1, 4, 5]
        listss = [2, 3, 6, 7]
        listsss = [10, 11, 14, 15]
        listssss = [8, 9, 12, 13]
        for i in range(4):
            rect = Polygon(matrix1.get_entries()[lists[i]].get_corner(UP + LEFT), matrix1.get_entries()[listss[i]].get_corner(UP + RIGHT), matrix1.get_entries()[listsss[i]].get_corner(DOWN + RIGHT), matrix1.get_entries()[listssss[i]].get_corner(DOWN + LEFT), color = YELLOW).scale(1.1)
            self.play(Create(rect))
            self.play(FadeIn(matrix3.get_entries()[i]))
            self.pause()
            self.play(FadeOut(rect))
        self.pause()
        

        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        self.pause()

            
        text = Tex(r"Edge detection and Convolution", color = BLUE).shift(3.0 * UP).scale(1.2)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Let's think of a kernel matrix,", color = WHITE).shift(2.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"that will help us detect edges", color = WHITE).shift(1.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"$A = \begin{bmatrix} -1 & -1 & -1 \\ -1 & 8 & -1 \\ -1 & -1 & -1 \end{bmatrix}$", color = WHITE).shift(-2 * UP).scale(1.2)
        self.play(Write(text), run_time = 2)
        self.pause()
                

        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        self.pause()

        text = Tex(r"Edge detection performed on an image", color = BLUE).shift(3.0 * UP).scale(1.2)
        self.play(Write(text), run_time = 2)
        self.pause()

        img4 = ImageMobject(r"Vd-Orig.png").shift(3 * LEFT).scale(2)
        self.play(FadeIn(img4))

        self.pause()

        img5 = ImageMobject(r"Vd-Rige2.png").shift(3 * RIGHT).scale(2)
        self.play(FadeIn(img5))        

        self.pause()

        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        self.pause()

        text = Tex(r"1", color = BLACK).shift(3.0 * UP).scale(1.8)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Section 4", color = ORANGE).shift(1.5 * UP).scale(1.4)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"An Adventure with", color = GREEN).shift(0.0 * UP).scale(1.8)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Fibonacci Numbers", color = GREEN).shift(-1.5 * UP).scale(1.8)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"1", color = BLACK).shift(-3.0 * UP).scale(1.8)
        self.play(Write(text), run_time = 2)
        self.pause()

        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        self.pause()

        text1 = Tex(r"Recipe for Fibonacci Sequence:", color = BLUE).shift(LEFT + 3 * UP).scale(1.3)
        text2 = Tex(r"\begin{itemize} \item Start with the numbers 0, 1 \\ \item For the next number, add up the previous two numbers \end{itemize}", color = BLUE)

        self.play(Write(text1), run_time = 2)
        self.pause()
        self.play(Write(text2), run_time = 3)        
        self.pause()

        lis = [0, 1, 1, 2, 3, 5, 8, 13, 21]

        for i in range(0, 9):
            text = Tex(str(lis[i])).shift(3 * LEFT + 0.75 * i * RIGHT + 2 * DOWN)
            self.play(Write(text), run_time = 0.5)
            self.pause()

        self.play(*[FadeOut(object) for object in self.mobjects], run_time = 2)

        text1 = Tex(r"Formalism", color = ORANGE).shift(3 * LEFT + 3 * UP).scale(1.3)
        text2 = Tex(r"\begin{itemize} \item Let $F_k$ be kth term \\ \item $F_0 = 0, F_1 = 1$ \\ \item $F_k = F_{k -1} + F_{k - 2}, k \ge 2$ \end{itemize}", color = WHITE)

        self.play(Write(text1), run_time = 2)
        self.play(Write(text2), run_time = 3)        

        self.pause()

        self.play(*[FadeOut(object) for object in self.mobjects], run_time = 2)

        text1 = Tex(r"Consider a vector $$u_k = \begin{bmatrix} F_k \\ F_{k - 1} \end{bmatrix}$$", color = BLUE).shift(1.5 * UP).scale(1.3)
        text2 = Tex(r"Let's package our problem into a nice matrix equation", color = WHITE).shift(2 * DOWN)
        self.pause()

        self.play(Write(text1), run_time = 3)
        self.play(Write(text2), run_time = 3)

        self.pause()

        self.play(*[FadeOut(object) for object in self.mobjects], run_time = 2)

        text1 = Tex(r"$$\begin{bmatrix} F_k \\ F_{k - 1} \end{bmatrix} = \begin{bmatrix} 1 & 1 \\ 1 & 0 \end{bmatrix} \begin{bmatrix} F_{k -1 } \\ F_{k - 2} \end{bmatrix}, u_1 = \begin{bmatrix} 1 \\ 0 \end{bmatrix}$$", color = ORANGE).shift(2 * UP).scale(1.3)
        text2 = Tex(r"$$u_k = \begin{bmatrix} 1 & 1 \\ 1 & 0 \end{bmatrix} u_{k - 1}$$", color = ORANGE).shift(0).scale(1.3)
        text3 = Tex(r"Let $A =  \begin{bmatrix} 1 & 1 \\ 1 & 0 \end{bmatrix}$", color = BLUE).shift(2 * DOWN).scale(1.3)

        self.play(Write(text1), run_time = 3)
        self.pause()
        self.play(Write(text2), run_time = 3)
        self.pause()
        self.play(Write(text3), run_time = 3)
        self.pause()

        self.play(*[FadeOut(object) for object in self.mobjects], run_time = 2)

        text1 = Tex(r"$$u_{k + 1} = A u_{k}$$").shift(2 * UP).scale(1.3)
        text2 = Tex(r"$$u_{k + 1} = A^2 u_{k - 1}$$").shift(UP).scale(1.3)
        text3 = Tex(r"$\vdots$").shift(0).scale(1.3)
        text4 = Tex(r"$$u_{k + 1} = A^k u_1$$").shift(DOWN).scale(1.3)

        self.play(Write(text1), run_time = 3)
        self.pause()
        self.play(Write(text2), run_time = 3)
        self.pause()

        self.play(Write(text3), run_time = 1)
        self.play(Write(text4), run_time = 3)
        self.pause()

        self.play(*[FadeOut(object) for object in self.mobjects], run_time = 2)

        text1 = Tex(r"Consider $A =  \begin{bmatrix} 1 & 1 \\ 1 & 0 \end{bmatrix}$", color = ORANGE).shift(2 * UP)
        text2 = Tex(r"Claim: $A = PDP^{-1}$", color = ORANGE).shift(0.66 * UP)
        text3 = Tex(r"$$P = \begin{bmatrix} \frac{1 - \sqrt{5}}{2} &  \frac{1 + \sqrt{5}}{2} \\ 1 & 1 \end{bmatrix}$$").shift(0.66 * DOWN).scale(0.8)
        text4 = Tex(r"$$D = \begin{bmatrix}  \frac{1 - \sqrt{5}}{2} &  0 \\ 0 & \frac{1 + \sqrt{5}}{2} \end{bmatrix}$$").shift(2 * DOWN).scale(0.8)
        
        self.play(Write(text1), run_time = 3)
        self.pause()
        self.play(Write(text2), run_time = 3)
        self.pause()
        self.play(Write(text3), run_time = 3)
        self.pause()
        self.play(Write(text4), run_time = 3)
        self.pause()

        self.play(*[FadeOut(object) for object in self.mobjects], run_time = 2)

        text1 = Tex(r"$$A = PDP^{-1}$$", color = ORANGE).shift(2 * UP)
        text2 = Tex(r"$$A^2 = PDP^{-1} PDP^{-1} = PD^2P^{-1}$$", color = ORANGE).shift(0.66 *  UP)
        text3 = Tex(r"$\vdots$", color = BLUE).shift(0.66 * DOWN)
        text4 = Tex(r"$$A^k = PD^kP^{-1}$$", color = ORANGE).shift(2 * DOWN)

        self.play(Write(text1), run_time = 3)
        self.pause()
        self.play(Write(text2), run_time = 3)
        self.pause()
        self.play(Write(text3), run_time = 3)
        self.pause()
        self.play(Write(text4), run_time = 3)
        self.pause()

        self.play(*[FadeOut(object) for object in self.mobjects], run_time = 2)

        text1 = Tex(r"$$u_{k + 1} = A^k u_1$$", color = ORANGE).shift(2 * UP)
        text2 = Tex(r"$$u_{k + 1} = P D^k P^{-1} u_1$$", color = ORANGE).shift(0)
        text3 = Tex(r"$$u_{k + 1} = \begin{bmatrix} \frac{1 - \sqrt{5}}{2} & \frac{1 + \sqrt{5}}{2} \\ 1 & 1 \end{bmatrix} \begin{bmatrix} \frac{1 - \sqrt{5}}{2} &  0 \\ 0 & \frac{1 + \sqrt{5}}{2} \end{bmatrix}^k \begin{bmatrix} \frac{1 - \sqrt{5}}{2} &  \frac{1 + \sqrt{5}}{2} \\ 1 & 1 \end{bmatrix}^{-1} \begin{bmatrix} 1 \\ 0 \end{bmatrix}$$").shift(2 * DOWN).scale(0.8)

        self.play(Write(text1), run_time = 3)
        self.pause()
        self.play(Write(text2), run_time = 3)
        self.pause()
        self.play(Write(text3), run_time = 3)
        self.pause()

        self.play(*[FadeOut(object) for object in self.mobjects], run_time = 2)

        text1 = Tex(r"$$u_{k + 1} = \begin{bmatrix} \frac{1 - \sqrt{5}}{2} & \frac{1 + \sqrt{5}}{2} \\ 1 & 1 \end{bmatrix} \begin{bmatrix} \frac{1 - \sqrt{5}}{2} &  0 \\ 0 & \frac{1 + \sqrt{5}}{2} \end{bmatrix}^k \begin{bmatrix} \frac{1 - \sqrt{5}}{2} &  \frac{1 + \sqrt{5}}{2} \\ 1 & 1 \end{bmatrix}^{-1} \begin{bmatrix} 1 \\ 0 \end{bmatrix}$$").shift(2 * UP).scale(0.8)
        text2 = Tex(r"$$u_{k + 1} = \begin{bmatrix} \frac{1 - \sqrt{5}}{2} & \frac{1 + \sqrt{5}}{2} \\ 1 & 1 \end{bmatrix} \begin{bmatrix} \left( \frac{1 - \sqrt{5}}{2}\right)^k &  0 \\ 0 & \left(\frac{1 + \sqrt{5}}{2}\right)^k \end{bmatrix} \frac{1}{-\sqrt{5}}\begin{bmatrix} 1 & - \frac{1 + \sqrt{5}}{2} \\ -1 & \frac{1 - \sqrt{5}}{2} \end{bmatrix} \begin{bmatrix} 1 \\ 0 \end{bmatrix}$$").shift(0).scale(0.8)
        text3 = Tex(r"$$u_{k + 1} = \begin{bmatrix} \frac{1 - \sqrt{5}}{2} & \frac{1 + \sqrt{5}}{2} \\ 1 & 1 \end{bmatrix} \begin{bmatrix} \left(\frac{1 - \sqrt{5}}{2}\right)^k &  0 \\ 0 & \left(\frac{1 + \sqrt{5}}{2}\right)^k \end{bmatrix}  \begin{bmatrix} -\frac{1}{\sqrt{5}} \\ \frac{1}{\sqrt{5}} \end{bmatrix}$$").shift(2 * DOWN).scale(0.8)
        text4 = Tex(r"$$u_{k + 1} = \begin{bmatrix} \frac{1 - \sqrt{5}}{2} & \frac{1 + \sqrt{5}}{2} \\ 1 & 1 \end{bmatrix} \begin{bmatrix} - \frac{1}{\sqrt{5}} \left(\frac{1 - \sqrt{5}}{2}\right)^k \\ \frac{1}{\sqrt{5}} \left(\frac{1 + \sqrt{5}}{2}\right)^k \end{bmatrix}$$").shift(2 * DOWN).scale(0.8)
        text5 = Tex(r"$$F_k = \frac{1}{\sqrt{5}} \left( \left(\frac{1 + \sqrt{5}}{2} \right)^k - \left(\frac{1 - \sqrt{5}}{2}\right)^k \right)$$").shift(2 * DOWN).scale(0.8)

        self.play(Write(text1), run_time = 3)
        self.pause()
        self.play(Write(text2), run_time = 3)
        self.pause()
        self.play(Write(text3), run_time = 3)
        self.pause()
        self.play(FadeOut(text3), FadeIn(text4), run_time = 2)
        self.pause()
        self.play(FadeOut(text4), FadeIn(text5), run_time = 2)
        self.pause()

        self.wait(3)
        self.play(*[FadeOut(object) for object in self.mobjects], run_time = 2)

        text1 = Tex(r"This is Binet's Formula:").shift(2 * UP)
        text2 = Tex(r"$$F_k = \frac{1}{\sqrt{5}} \left( \left( \frac{1 + \sqrt{5}}{2} \right)^k - \left(\frac{1 - \sqrt{5}}{2} \right)^k \right)$$").shift(DOWN)

        self.play(Write(text1), run_time = 3)
        self.pause()
        self.play(Write(text2), run_time = 3)
        self.pause()

        self.play(*[FadeOut(object) for object in self.mobjects], run_time = 2)
        text1 = Tex(r"Exercise: Lucas Numbers").shift(UP)
        text2 = Tex(r"Assume $F_0 = 2, F_1 = 1$, solve for $F_k$").shift(DOWN)

        self.play(Write(text1), run_time = 3)
        self.pause()
        self.play(Write(text2), run_time = 3)
        self.pause()
        self.play(*[FadeOut(object) for object in self.mobjects], run_time = 2)

        text = Tex(r"1", color = BLACK).shift(3.0 * UP).scale(1.8)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Section 5", color = ORANGE).shift(1.5 * UP).scale(1.4)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Exploring Number Theory", color = ORANGE).shift(0.0 * UP).scale(1.4)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"1", color = BLACK).shift(-1.5 * UP).scale(1.8)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"1", color = BLACK).shift(-3.0 * UP).scale(1.8)
        self.play(Write(text), run_time = 2)
        self.pause()
        

        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        self.pause()

        text = Tex(r"Greatest Common Divisor (GCD)", color = ORANGE).shift(3.0 * UP).scale(1.4)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"$\gcd(a, b)$: Greatest number which divides both a and b", color = WHITE).shift(1.8 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"1", color = BLACK).shift(0.6000000000000001 * UP).scale(1.8)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"$\gcd(3, 9) = 3$", color = WHITE).shift(-0.5999999999999996 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"$\gcd(6, 9) = 3$", color = WHITE).shift(-1.7999999999999998 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"$\gcd(20, 15) = 5$", color = WHITE).shift(-3.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        

        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        self.pause()

            
        text = Tex(r"We say that $c = \gcd(a, b)$ iff:", color = BLUE).shift(3.0 * UP).scale(1.2)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"- \textbf{Common Divisor} Condition: $d | a$ and $d | b$", color = WHITE).shift(2.142857142857143 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"- \textbf{Greatest} Condition: $c | a$ and $c | b \implies c \le d$", color = WHITE).shift(1.2857142857142858 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Example: $\gcd (12, 18) = 6$", color = BLUE).shift(0.4285714285714288 * UP).scale(1.2)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"- $1 | 12$ and $1 | 18 \implies 1 \le 6$", color = WHITE).shift(-0.4285714285714284 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"- $2 | 12$ and $2 | 18 \implies 2 \le 6$", color = WHITE).shift(-1.2857142857142856 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"- $3 | 12$ and $3 | 18 \implies 3 \le 6$", color = WHITE).shift(-2.1428571428571423 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"- $6 | 12$ and $6 | 18 \implies6 \le 6$", color = WHITE).shift(-3.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        

        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        self.pause()

            
        text = Tex(r"Modular Arithmetic", color = BLUE).shift(3.0 * UP).scale(1.2)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"$a \equiv b \pmod n$", color = WHITE).shift(2.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"(a is congruent to b modulo n)", color = WHITE).shift(1.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"iff $n | (a - b)$", color = WHITE).shift(0.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"$13 \equiv 3 \pmod 5$ because $13 - 3 = 10$, $5 | 10$", color = WHITE).shift(-1.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"$49 \equiv 0 \pmod 7$ because $49 - 0 = 49$, $7 | 49$", color = WHITE).shift(-2.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"$-4 \equiv 2 \pmod 6$ because $-4 - 2 = -6$, $6 | -6$", color = WHITE).shift(-3.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        

        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        self.pause()

            
        text = Tex(r"Theorem 1: Cancellation Law", color = GREEN).shift(3.0 * UP).scale(1.8)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"If $ar \equiv br \pmod p$ and $\gcd(p, r) = 1$, $a \equiv b \pmod p$", color = WHITE).shift(1.8 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Proof", color = BLUE).shift(0.6000000000000001 * UP).scale(1.2)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"$ar \equiv br \pmod p \implies p | (ar - br)$", color = WHITE).shift(-0.5999999999999996 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"$ar \equiv br \pmod p \implies p | (a - b)$, as $p \nmid r$", color = WHITE).shift(-1.7999999999999998 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"$a \equiv b \pmod p$", color = WHITE).shift(-3.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        

        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        self.pause()

            
        text = Tex(r"1", color = BLACK).shift(3.0 * UP).scale(1.8)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Euclids Division Algorithm", color = GREEN).shift(1.0 * UP).scale(1.8)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"for GCD", color = GREEN).shift(-1.0 * UP).scale(1.8)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"1", color = BLACK).shift(-3.0 * UP).scale(1.8)
        self.play(Write(text), run_time = 2)
        self.pause()
        

        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        self.pause()

            
        text = Tex(r"Theorem 2:", color = ORANGE).shift(3.0 * UP).scale(1.4)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"$\gcd(a, b) = \gcd(b, a \% b)$", color = WHITE).shift(1.8 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"For instance,", color = WHITE).shift(0.6000000000000001 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"$\gcd(32, 24) = \gcd(24, 8) = 8$", color = WHITE).shift(-0.5999999999999996 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"$\gcd(42, 27) = \gcd(27, 15)$", color = WHITE).shift(-1.7999999999999998 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"$= \gcd(15, 12) = \gcd(12, 3) = 3$", color = WHITE).shift(-3.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        

        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        self.pause()

            
        text = Tex(r"Theorem 2:", color = ORANGE).shift(3.0 * UP).scale(1.4)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"$\gcd(a, b) = \gcd(b, r)$, where $r = a \% b$", color = WHITE).shift(2.142857142857143 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Proof:", color = ORANGE).shift(1.2857142857142858 * UP).scale(1.4)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"i) Proof of common divisor", color = BLUE).shift(0.4285714285714288 * UP).scale(1.2)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Let $g = \gcd(a, b)$", color = WHITE).shift(-0.4285714285714284 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"$a = kb + r$", color = WHITE).shift(-1.2857142857142856 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"$g | a, g | b \implies g|r$", color = WHITE).shift(-2.1428571428571423 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"So, r is a common divisor for b, r", color = WHITE).shift(-3.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        

        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        self.pause()

            
        text = Tex(r"Theorem 2:", color = ORANGE).shift(3.0 * UP).scale(1.4)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"$\gcd(a, b) = \gcd(b, r)$, where $r = a \% b$", color = WHITE).shift(2.142857142857143 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Proof:", color = ORANGE).shift(1.2857142857142858 * UP).scale(1.4)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"ii) Proof that it is greatest", color = BLUE).shift(0.4285714285714288 * UP).scale(1.2)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Consider $c: c | a, c | b$", color = WHITE).shift(-0.4285714285714284 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"$\implies c | r$", color = WHITE).shift(-1.2857142857142856 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Also, $c \le g$, by definition", color = WHITE).shift(-2.1428571428571423 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"So, g is $\gcd(b, r)$!", color = WHITE).shift(-3.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        

        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        self.pause()

            
        text = Tex(r"Euclid\'s Division Algorithm", color = ORANGE).shift(3.0 * UP).scale(1.4)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Aim: find $\gcd(39, 15)$", color = WHITE).shift(2.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"$39 = 15 \times 2 + 9$", color = WHITE).shift(1.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"$15 = 9 \times 1 + 6$ $[\gcd(39, 15) = \gcd(15, 9)]$", color = WHITE).shift(0.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"$9 = 6 \times 1 + 3$ $[\gcd(15, 9) = \gcd(9, 6)]$", color = WHITE).shift(-1.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"$6 = 3 \times 2 + 0$ $[\gcd(9, 6) = \gcd(6, 3) = 3]$", color = WHITE).shift(-2.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"$\boxed{\gcd(39, 15) = 3}$", color = WHITE).shift(-3.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        

        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        self.pause()

            
        text = Tex(r"1", color = BLACK).shift(3.0 * UP).scale(1.8)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Exercise:", color = GREEN).shift(1.8 * UP).scale(1.8)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"1", color = BLACK).shift(0.6000000000000001 * UP).scale(1.8)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Write code in a programming language", color = ORANGE).shift(-0.5999999999999996 * UP).scale(1.4)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"that implements GCD", color = ORANGE).shift(-1.7999999999999998 * UP).scale(1.4)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"1", color = BLACK).shift(-3.0 * UP).scale(1.8)
        self.play(Write(text), run_time = 2)
        self.pause()
        

        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        self.pause()

            
        text = Tex(r"Euclid\'s Division Algorithm", color = ORANGE).shift(3.0 * UP).scale(1.4)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Aim: find $\gcd(5, 14)$", color = WHITE).shift(1.8 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"$14 = 5 \times 2 + 4$", color = WHITE).shift(0.6000000000000001 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"$5 = 4 \times 1 + 1$", color = WHITE).shift(-0.5999999999999996 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"$4 = 1 \times 4 + 0$", color = WHITE).shift(-1.7999999999999998 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"$\boxed{\gcd(5, 14) = 1}$", color = WHITE).shift(-3.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        

        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        self.pause()

            
        text = Tex(r"Interesting Problem:", color = ORANGE).shift(3.0 * UP).scale(1.4)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"You have a large number of two Rupee coins", color = WHITE).shift(1.8 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"and a large number of five Rupee coins.", color = WHITE).shift(0.6000000000000001 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"How can you create Rupees 17?", color = WHITE).shift(-0.5999999999999996 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Mathematical Reformulation", color = BLUE).shift(-1.7999999999999998 * UP).scale(1.2)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Find integers s, t, such that $2s + 5t = 17$", color = WHITE).shift(-3.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        

        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        self.pause()

            
        text = Tex(r"Mathematical Reformulation", color = BLUE).shift(3.0 * UP).scale(1.2)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Find integers s, t, such that $2s + 5t = 17$", color = WHITE).shift(2.142857142857143 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Try solving it on your own now!", color = WHITE).shift(1.2857142857142858 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"You need two things:", color = WHITE).shift(0.4285714285714288 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"- Extended Euclidean Algorithm", color = WHITE).shift(-0.4285714285714284 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"- If $(s_0, t_0)$ are solutions,", color = WHITE).shift(-1.2857142857142856 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"$(s_0 + 5 \theta, s_0 - 2 \theta),  \theta \in \mathbb{Z}$ is solution", color = WHITE).shift(-2.1428571428571423 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Solutions are: $(1, 3)$ and $(6, 1)$", color = WHITE).shift(-3.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        

        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        self.pause()

            
        text = Tex(r"Theorem 3: Wilson\'s Theorem", color = ORANGE).shift(3.0 * UP).scale(1.4)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"$(p - 1)! \equiv -1 \pmod{p}$", color = WHITE).shift(2.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Proof:", color = BLUE).shift(1.0 * UP).scale(1.2)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"\textbf{Lemma:}", color = WHITE).shift(0.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Solutions to $x^2 = 1 \pmod p$", color = WHITE).shift(-1.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"are $1 \pmod p$ and $(p - 1) \pmod p$", color = WHITE).shift(-2.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Proof of Lemma: Substitute and check!", color = WHITE).shift(-3.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        

        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        self.pause()

            
        text = Tex(r"Theorem 3: Wilson\'s Theorem", color = ORANGE).shift(3.0 * UP).scale(1.4)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"$(p - 1)! \equiv -1 \pmod{p}$", color = WHITE).shift(2.142857142857143 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Proof:", color = BLUE).shift(1.2857142857142858 * UP).scale(1.2)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"$(p - 1)! = 1 \times 2 \times 3 \times \dots \times (p - 1)$", color = WHITE).shift(0.4285714285714288 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Now, pairs of a number and its inverse", color = WHITE).shift(-0.4285714285714284 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"can be cancelled out", color = WHITE).shift(-1.2857142857142856 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Only $1$ and $p - 1$ cannot be cancelled out,", color = WHITE).shift(-2.1428571428571423 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"as they are their own inverses", color = WHITE).shift(-3.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        

        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        self.pause()

            
        text = Tex(r"Theorem 3: Wilson\'s Theorem", color = ORANGE).shift(3.0 * UP).scale(1.4)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"$(p - 1)! \equiv -1 \pmod{p}$", color = WHITE).shift(2.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Proof:", color = BLUE).shift(1.0 * UP).scale(1.2)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"$(p - 1)! \equiv 1 \times 2 \times 3 \times \dots \times (p - 1) \pmod p$", color = WHITE).shift(0.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Cancel out corresponding terms", color = WHITE).shift(-1.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"$(p - 1)! \equiv 1 \times (p - 1) \pmod p$", color = WHITE).shift(-2.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"$(p - 1)! \equiv -1 \pmod p$", color = WHITE).shift(-3.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        

        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        self.pause()

            
        text = Tex(r"1", color = BLACK).shift(3.0 * UP).scale(1.8)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Wilson\'s theorem is a", color = BLUE).shift(1.5 * UP).scale(1.2)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Primality Test!", color = ORANGE).shift(0.0 * UP).scale(1.4)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"(Although usually better methods are used)", color = WHITE).shift(-1.5 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"1", color = BLACK).shift(-3.0 * UP).scale(1.8)
        self.play(Write(text), run_time = 2)
        self.pause()
        

        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        self.pause()

            
        text = Tex(r"Theorem 4: Fermat\'s Little Theorem", color = ORANGE).shift(3.0 * UP).scale(1.4)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"If $\gcd(a, p) = 1$, $a^{p - 1} \equiv 1 \pmod p$", color = WHITE).shift(2.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Proof:", color = BLUE).shift(1.0 * UP).scale(1.2)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Consider the set", color = WHITE).shift(0.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"$S = \{1, 2, \dots, (p - 1)\}$", color = WHITE).shift(-1.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Multiply each of these numbers with $a$ and take $\% p$", color = WHITE).shift(-2.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"$T = \{a \% p , 2a \% p, \dots, (p - 1)a \% p \}$", color = WHITE).shift(-3.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        

        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        self.pause()

            
        text = Tex(r"Lemma: $S \rightarrow T$ is an injection", color = BLUE).shift(3.0 * UP).scale(1.2)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"By contradiction, for $r, s \in S, r \ne s$", color = WHITE).shift(2.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Consider $ar \% p$, $as \% p \in T$", color = WHITE).shift(1.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Let $ar \% p = as \% p$", color = WHITE).shift(0.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"$\implies ar \equiv as \pmod p$", color = WHITE).shift(-1.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"$\implies p | (r - s)$ (as $p \nmid a$)", color = WHITE).shift(-2.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"$2 - p \le r - s \le p - 2$ $\implies \boxed{r - s = 0}$", color = WHITE).shift(-3.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        

        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        self.pause()

            
        text = Tex(r"Theorem 4: Fermat\'s Little Theorem", color = ORANGE).shift(3.0 * UP).scale(1.4)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"If $\gcd(a, p) = 1$, $a^{p - 1} \equiv 1 \pmod p$", color = WHITE).shift(2.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Proof:", color = BLUE).shift(1.0 * UP).scale(1.2)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Number of elements in $S$ = Number of elements in $T$", color = WHITE).shift(0.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"If it\'s an injection, it\'s a bijection!", color = WHITE).shift(-1.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"$\implies S \rightarrow T$ is a bijection", color = WHITE).shift(-2.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"$\implies$ $S$ is a permutation of $T$", color = WHITE).shift(-3.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        

        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        self.pause()

            
        text = Tex(r"Theorem 4: Fermat\'s Little Theorem", color = ORANGE).shift(3.0 * UP).scale(1.4)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"If $\gcd(a, p) = 1$, $a^{p - 1} \equiv 1 \pmod p$", color = WHITE).shift(2.142857142857143 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Proof:", color = BLUE).shift(1.2857142857142858 * UP).scale(1.2)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Product of all elements in $S$ = Product of all elements in $T$", color = WHITE).shift(0.4285714285714288 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"$1 \times 2 \times \dots \times (p - 1) \equiv a \times 2a \times \dots \times (p - 1)a \mod p$", color = WHITE).shift(-0.4285714285714284 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"$(p - 1)! \equiv a^{p - 1} (p - 1)! \pmod p$", color = WHITE).shift(-1.2857142857142856 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"$\gcd((p - 1)!, p) = 1$", color = WHITE).shift(-2.1428571428571423 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"By cancellation law, $1 \equiv a^{p - 1} \pmod p$", color = WHITE).shift(-3.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        

        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        self.pause()


        self.wait()
        self.pause()
        self.wait()
        self.pause()
        self.wait()



