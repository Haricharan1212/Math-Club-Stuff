from manim import *
from numpy import *

class Euler_Number(Scene):
    def construct(self):
        text1 = Tex(r"Euler's Number \\ from \\ Compound Interest", color = BLUE).scale(1.3)
        self.play(Write(text1), run_time = 3)
        self.wait(5)
        self.play(FadeOut(text1))
        
        text1 = Tex(r"Consider Euler, who has a dollar, \\ goes to a bank company and \\ asks for a loan under compound interest")
        self.play(Write(text1), run_time = 3)
        self.wait(5)
        self.play(FadeOut(text1))
        
        text1 = Tex("The parameters he could tweak are:").shift(2 * UP).scale(1.2)      
        text2 = Tex(r"\begin{itemize} \item Yearly Interest rate, $r$, \\ \item The number of times of compounding per year, $n$ \\ \end{itemize}").scale(0.9)
        self.play(Write(text1), run_time = 1)
        self.play(Write(text2), run_time = 2)
        self.wait(5)
        self.play(FadeOut(text1), FadeOut(text2))
        
        text1 = Tex(r"Consider r = 10\%, n = 1").shift(2.5 * UP)
        money = lambda p, r, t: p * ((1 + r)**t)
        arr = array([[0, money(1, 0.1, 0)], [1, money(1, 0.1, 1)], [2, money(1, 0.1, 2)], [3, money(1, 0.1, 3)]])
        
        table = DecimalTable(arr, col_labels = [Tex(r"Year"), Tex(r"Amount")], element_to_mobject_config={"num_decimal_places": 4}).scale(0.75)
        self.play(Create(text1))
        self.play(Write(table), run_time = 2)

        for i in range(1, 5):
            rect = SurroundingRectangle(table.get_rows()[i])
            self.play(Create(rect))
            self.wait(2)
            self.play(FadeOut(rect))

        self.play(*[FadeOut(object) for object in self.mobjects], run_time = 2)

        text1 = Tex(r"Amount in k$^{th}$ year $= (1 + r)$ Amount in k - 1$^{th}$ year").shift(2 * UP).scale(0.9)
        text2 = Tex(r"Amount in k$^{th}$ year $= (1 + r)^2$ Amount in k - 2$^{th}$ year").shift(0).scale(0.9)
        text4 = Tex(r"\vdots").shift(DOWN)
        text3 = Tex(r"Amount in k$^{th}$ year $= (1 + r)^k$ Amount in $0^{th}$ year").shift(2 * DOWN).scale(0.9)

        self.play(Create(text1), run_time = 3)
        self.play(Create(text2), run_time = 3)
        self.play(Create(text4), run_time = 1   )
        self.play(Create(text3), run_time = 3)

        self.play(*[FadeOut(object) for object in self.mobjects], run_time = 2)
        
        text = Tex(r"Total amount in kth year = $(1 + r)^{k}\$ $")
        self.play(Create(text), run_time = 2)
        self.wait(2)
        self.play(Unwrite(text))

        text1 = Tex(r"For rate of compounding $n$:").shift(2 * UP + LEFT)
        self.play(Create(text1))

        text2 = Tex(r"\begin{itemize} \item The rate per compounding becomes $\frac rn$ \\ \item We're compounding $kn$ times \end{itemize}").shift(1 * UP).scale(0.8)
        self.play(Create(text2))

        text4 = Tex(r"Total amount in kth year = $(1 + \frac rn)^{kn}$").shift(DOWN)
        self.play(Create(text4))

        self.play(*[FadeOut(object) for object in self.mobjects], run_time = 2)

        text1 = Tex(r"Consider r = 100\%").shift(2.5 * UP)
        money = lambda p, r, n: p * ((1 + r/n)**(n))
        arr = array([[1, money(1, 1, 1)], [2, money(1, 1, 2)], [3, money(1, 1, 3)], [4, money(1, 1, 4)]])
        
        table = DecimalTable(arr, col_labels = [Tex(r"n Value"), Tex(r"Amount")], element_to_mobject_config={"num_decimal_places": 4}).scale(0.75)
        self.play(Create(text1))
        self.play(Write(table), run_time = 2)
        self.wait(5)
        self.play(*[FadeOut(object) for object in self.mobjects], run_time = 2)

        arr = array([[1, money(1, 1, 1)], [10, money(1, 1, 10)], [100, money(1, 1, 100)], [1000, money(1, 1, 1000)]])
        table = DecimalTable(arr, col_labels = [Tex(r"n Value"), Tex(r"Amount")], element_to_mobject_config={"num_decimal_places": 4}).scale(0.75)
        self.play(Create(text1))
        self.play(Write(table), run_time = 2)

        for i in range(1, 5):
            rect = SurroundingRectangle(table.get_rows()[i])
            self.play(Create(rect))
            self.wait(2)
            self.play(FadeOut(rect))

        self.play(*[FadeOut(object) for object in self.mobjects], run_time = 2)

        arr = array([[1e4, money(1, 1, 1e4)], [1e5, money(1, 1, 1e5)], [1e6, money(1, 1, 1e6)], [1e7, money(1, 1, 1e7)]])
        table = DecimalTable(arr, col_labels = [Tex(r"n Value"), Tex(r"Amount")], element_to_mobject_config={"num_decimal_places": 4}).scale(0.75)
        self.play(Create(text1))
        self.play(Write(table), run_time = 2)

        for i in range(1, 5):
            rect = SurroundingRectangle(table.get_rows()[i])
            self.play(Create(rect))
            self.wait(2)
            self.play(FadeOut(rect))

        self.play(*[FadeOut(object) for object in self.mobjects], run_time = 2)


        text = Tex(r"We see that, as we keep increasing n, \\ it approaches some number. \\ That number is Euler's constant, $e$")
        self.play(Create(text))
        self.play(Unwrite(text))


        text = Tex(r"$$\lim_{n \to \infty} (1 + \frac 1n)^n = e$$ \\which is awesome!!")
        self.play(Create(text))
        self.wait(5)
        self.play(Unwrite(text))

        text = Tex(r"Exercise: Prove that $\lim_{n \to \infty} (1 + \frac rn)^n = e^r$").shift(UP)
        self.play(Create(text), run_time = 2)
        self.wait(3)
        text1 = Tex(r"Hint: Substitute $\frac rn = \frac {1}{n'}$").shift(DOWN)
        self.play(Create(text1))

        self.play(*[FadeOut(object) for object in self.mobjects], run_time = 2)

