from manim_presentation import Slide
from manim import *
from math import *

class stuff(Slide):
    def construct(self):
        text = Tex(r"1", color = BLACK).shift(3.0 * UP).scale(1.8)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"$a_i$ to AI", color = GREEN).shift(1.8 * UP).scale(1.8)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Math Contest", color = GREEN).shift(0.6000000000000001 * UP).scale(1.8)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"1", color = BLACK).shift(-0.5999999999999996 * UP).scale(1.8)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Analytics Club", color = ORANGE).shift(-1.7999999999999998 * UP).scale(1.4)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Mathematics Club", color = ORANGE).shift(-3.0 * UP).scale(1.4)
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

            
        text = Tex(r"1", color = BLACK).shift(3.0 * UP).scale(1.8)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Section 2", color = ORANGE).shift(1.5 * UP).scale(1.4)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Gradient Descent", color = ORANGE).shift(0.0 * UP).scale(1.4)
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

            
        text = Tex(r"Motivation", color = ORANGE).shift(3.0 * UP).scale(1.4)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        img = ImageMobject(r"x^2+y^2.png").scale(1.3)      
        self.play(FadeIn(img))

        text = Tex(r"$z = x^2 + y^2$", color = GREEN).shift(-3 * UP)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        

        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        self.pause()

            
        text = Tex(r"$$z = f(x, y) = x^2 + y^2$$", color = ORANGE).shift(3.0 * UP).scale(1.4)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Consider the loss function,", color = WHITE).shift(1.8 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"as in the previous image", color = WHITE).shift(0.6000000000000001 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"We have to minimize the loss", color = WHITE).shift(-0.5999999999999996 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Gradient is direction of steepest ascent", color = WHITE).shift(-1.7999999999999998 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"So, -gradient is direction of steepest descent", color = WHITE).shift(-3.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        

        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        self.pause()

            
        text = Tex(r"We initialize at some random position", color = WHITE).shift(3.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"$\text{Current position} = \text{Current position} - \text{Gradient}$", color = WHITE).shift(2.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"We would move towards the minimum point", color = WHITE).shift(1.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Note that", color = WHITE).shift(0.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"$\text{Current position} = \text{Current position} - \alpha \text{Gradient}, \alpha > 0$", color = WHITE).shift(-1.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"would also make it move towards the minimum point", color = WHITE).shift(-2.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"This concept is called the gradient descent.", color = WHITE).shift(-3.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        

        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        self.pause()

            
        text = Tex(r"Motivation", color = ORANGE).shift(3.0 * UP).scale(1.4)
        self.play(Write(text), run_time = 2)
        self.pause()

        img2 = ImageMobject(r"x^2+y^2_2.png").scale(1.3)      
        self.play(FadeIn(img2))

        text = Tex(r"$z = x^2 + y^2$", color = GREEN).shift(-3 * UP)
        self.play(Write(text), run_time = 2)
        self.pause()
                

        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        self.pause()

            
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

        img5 = ImageMobject(r"Vd-Rige2.png").shift(3 * RIGHT).scale(2)
        self.play(FadeIn(img5))        

        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        self.pause()

        self.wait(2)
        self.pause()    
        self.wait(2)
        self.pause()    