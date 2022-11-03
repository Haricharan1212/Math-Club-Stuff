from manim import *
from numpy import *
from manim_slides import *

class Fibonacci(Slide):
    def construct(self):        
        text1 = Tex(r"Fibonacci Sequence \\using Matrices", color = BLUE).scale(1.5)
        self.play(Write(text1), run_time = 3)
        
        self.pause()

        self.play(FadeOut(text1))
        
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


        self.wait()
        self.pause()
        self.wait()
        self.pause()
        self.wait()

