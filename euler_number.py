from manim import *
from numpy import *
#from manim_presentation import *
from manim_slides import *

class Euler_Number(Slide):
    def construct(self):
        text1 = Tex(r"Euler's Number \\ from \\ Compound Interest", color = BLUE).scale(1.3)
        self.play(Write(text1), run_time = 3)
        self.pause()

        self.play(FadeOut(text1))

        text1 = Tex(r"Euler, who has a dollar, \\ goes to a bank company and \\ asks for a loan under compound interest")
        self.play(Write(text1), run_time = 3)
        self.wait(5)
        self.pause()

        self.play(FadeOut(text1))

        text1 = Tex("The parameters he could tweak are:", color = ORANGE).shift(2 * UP).scale(1.2)      
        text2 = Tex(r"\begin{itemize} \item Yearly Interest rate, $r$, \\ \item The number of times of compounding per year, $n$ \\ \end{itemize}").scale(0.9)
        self.play(Write(text1), run_time = 1)
        self.play(Write(text2), run_time = 2)
        self.wait(5)

        self.pause()
        self.play(FadeOut(text1), FadeOut(text2))

        text1 = Tex(r"Consider r = 10\%, n = 1").shift(2.5 * UP)
        money = lambda p, r, t: p * ((1 + r)**t)

        arr = 0, 1, 2, 3
        arr = array([[str(i), '%.3f' % (money(1, 0.1, i))] for i in arr])
        
        table = Table(arr, col_labels = [Tex(r"Year"), Tex(r"Amount")]).scale(0.75)
        self.play(Create(text1))
        self.pause()

        self.play(Write(table), run_time = 2)
        self.pause()

        for i in range(1, 5):
            rect = SurroundingRectangle(table.get_rows()[i])
            self.play(Create(rect))
            self.wait(2)
            self.play(FadeOut(rect))

        self.play(*[FadeOut(object) for object in self.mobjects], run_time = 2)

        text1 = Tex(r"Amount in k$^{th}$ year $= (1 + r)$ Amount in k - 1$^{th}$ year").shift(2 * UP).scale(0.9)
        text2 = Tex(r"Amount in k$^{th}$ year $= (1 + r)^2$ Amount in k - 2$^{th}$ year").shift(0).scale(0.9)
        text4 = Tex(r"\vdots", color = BLUE).shift(DOWN)
        text3 = Tex(r"Amount in k$^{th}$ year $= (1 + r)^k$ Amount in $0^{th}$ year").shift(2 * DOWN).scale(0.9)

        self.play(Write(text1), run_time = 3)
        self.pause()

        self.play(Write(text2), run_time = 3)
        self.pause()

        self.play(Write(text4), run_time = 1   )
        self.pause()

        self.play(Write(text3), run_time = 3)
        self.pause()

        self.play(*[FadeOut(object) for object in self.mobjects], run_time = 2)
        
        text = Tex(r"Total amount in kth year = $(1 + r)^{k}\$ $")
        self.play(Write(text), run_time = 2)
        self.wait(2)
        self.pause()

        self.play(Unwrite(text))

        text1 = Tex(r"For rate of compounding $n$:").shift(2 * UP + LEFT)
        text2 = Tex(r"\begin{itemize} \item The rate per compounding becomes $\frac rn$ \\ \item We're compounding $kn$ times \end{itemize}").shift(1 * UP).scale(0.8)
        text4 = Tex(r"Total amount in kth year = $(1 + \frac rn)^{kn}$", color = YELLOW).shift(DOWN)

        self.play(Create(text1))
        self.play(Create(text2), run_time = 2)
        self.play(Create(text4))

        self.pause()

        self.play(*[FadeOut(object) for object in self.mobjects], run_time = 2)

        text4 = Tex(r"Consider k = 1", color = YELLOW).shift(DOWN)
        self.play(Create(text4))
        self.pause()
        self.wait()
        self.play(*[FadeOut(object) for object in self.mobjects], run_time = 2)

        text1 = Tex(r"Consider r = 100\%").shift(2.5 * UP)
        money = lambda p, r, n: p * ((1 + r/n)**(n))
        arr = 1, 2, 3, 4
        arr = array([[str(i), '%.4f' % (money(1, 1, i))] for i in arr])
        
        table = Table(arr, col_labels = [Tex(r"n Value"), Tex(r"Amount")]).scale(0.75)

        self.play(Create(text1))
        self.play(Write(table), run_time = 2)
        self.wait(5)
        self.pause()
        self.play(*[FadeOut(object) for object in self.mobjects], run_time = 2)

        arr = 1, 10, 100, 1000
        arr = array([[str(i), '%.4f' %(money(1, 1, i))] for i in arr])

        table = Table(arr, col_labels = [Tex(r"n Value"), Tex(r"Amount")]).scale(0.6)
        self.play(Create(text1))
        self.play(Write(table), run_time = 2)
        self.pause()

        for i in range(1, 5):
            rect = SurroundingRectangle(table.get_rows()[i])
            self.play(Create(rect))
            self.wait(2)
            self.play(FadeOut(rect))

        self.play(*[FadeOut(object) for object in self.mobjects], run_time = 2)

        arr = 1e4, 1e5, 1e6, 1e7
        arr = array([['%.0f' %(i), '%.4f' %(money(1, 1, i))] for i in arr])
        table = Table(arr, col_labels = [Tex(r"n Value"), Tex(r"Amount")]).scale(0.6)
        self.play(Create(text1))
        self.play(Write(table), run_time = 2)
        self.pause()

        for i in range(1, 5):
            rect = SurroundingRectangle(table.get_rows()[i])
            self.play(Create(rect))
            self.wait(2)
            self.play(FadeOut(rect))

        self.play(*[FadeOut(object) for object in self.mobjects], run_time = 2)


        text = Tex(r"We see that, as we keep increasing n, \\ it approaches some number. \\ That number is Euler's constant, $\mathbf{e}$")
        self.play(Write(text), run_time = 3)
        self.pause()
        self.play(Unwrite(text))

        text = Tex(r"$$\lim_{n \to \infty} (1 + \frac 1n)^n = e$$ \\which is awesome!!", color = BLUE)
        self.play(Write(text))
        self.wait(5)
        self.pause()
        self.play(Unwrite(text))

        text = Tex(r"Exercise: Prove that $\lim_{n \to \infty} (1 + \frac rn)^n = e^r$").shift(UP)
        self.play(Create(text), run_time = 2)
        self.wait(3)
        self.pause()

        text1 = Tex(r"Hint: Substitute $\frac rn = \frac {1}{n'}$").shift(DOWN)
        self.play(Create(text1))
        self.pause()
        self.play(*[FadeOut(object) for object in self.mobjects], run_time = 2)

        self.pause()
        self.wait()
        self.pause()
        self.wait()