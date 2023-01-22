from manim import *
from manim_presentation import Slide
from math import factorial

class Stuff(Slide):
    def construct(self):

        img1 = ImageMobject("clock_4.png").scale(1.3)
        self.play(FadeIn(img1))
        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)

        img2 = ImageMobject("clock_1.png").scale(1.3)
        self.play(FadeIn(img2))
        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)

        listing = Code(r"crypto_ws_code\euclid_division_algorithm.py",
            tab_width=4,
            background_stroke_width=1,
            background_stroke_color=WHITE,
            insert_line_no=True,
            style=Code.styles_list[15],
            background="window",
            language="python",
        )

        self.play(Create(listing))
        self.pause()
        self.play(FadeOut(listing))

        x_vals = list(range(1, 8))
        y_vals = [factorial(i - 1) % i - i for i in x_vals]
        t1 = DecimalTable(
            [x_vals, y_vals],
            row_labels=[MathTex("p"), MathTex("(p - 1)! \pmod p")],
            include_outer_lines=True).scale(0.5)

        self.play(Create(t1))
        self.pause()
        self.play(FadeOut(t1))

        x_vals = list(range(1, 8))
        y_vals = [3**(i - 1) % i for i in x_vals]
        t1 = DecimalTable(
            [x_vals, y_vals],
            row_labels=[MathTex("n"), MathTex("3^{(n - 1)} \pmod n")],
            include_outer_lines=True).scale(0.7)

        self.play(Create(t1))
        self.pause()
        self.play(FadeOut(t1))  

        img3 = ImageMobject("crypto_diagram.png")    
        self.play(FadeIn(img3))
        self.pause()
        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)

        x_vals = ["a", "b", "c", "...", "w", "x", "y", "z"]
        y_vals = ["f", "g", "h", "...", "b", "c", "d", "e"]
        t1 = Table(
            [x_vals, y_vals],
            include_outer_lines=True)
        self.play(Create(t1))
        self.pause()
        self.play(FadeOut(t1))  

        listing = Code(r"crypto_ws_code\caesar_cipher.py",
            tab_width=4,
            background_stroke_width=1,
            background_stroke_color=WHITE,
            insert_line_no=True,
            style=Code.styles_list[15],
            background="window",
            language="python",
        )

        self.play(Create(listing))
        self.pause()
        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)

        img4 = ImageMobject("crypto_flowchart.png")
        self.play(FadeIn(img4))
        self.pause()
        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)

        img4 = ImageMobject("diffie_hellman.png")
        self.play(FadeIn(img4))
        self.pause()
        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
