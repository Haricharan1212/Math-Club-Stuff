
from manim_presentation import Slide
from manim import *
from math import *

class galois_theory_2(Slide):
    def construct(self):
        text = Tex(r"Galois Theory and", color = GREEN).shift(3.0 * UP).scale(1.8)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Insolvability of the Quintic", color = GREEN).shift(1.5 * UP).scale(1.8)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"1", color = BLACK).shift(0.0 * UP).scale(1.8)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Shaastra Workshop", color = ORANGE).shift(-1.5 * UP).scale(1.4)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"1", color = BLACK).shift(-3.0 * UP).scale(1.8)
        self.play(Write(text), run_time = 2)
        self.pause()
        

        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        self.pause()

            
        text = Tex(r"1", color = BLACK).shift(3.0 * UP).scale(1.8)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Module 6", color = ORANGE).shift(1.5 * UP).scale(1.4)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Fundamental Theorem", color = GREEN).shift(0.0 * UP).scale(1.8)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"of Algebra", color = GREEN).shift(-1.5 * UP).scale(1.8)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"1", color = BLACK).shift(-3.0 * UP).scale(1.8)
        self.play(Write(text), run_time = 2)
        self.pause()
        

        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        self.pause()

            
        text = Tex(r"Statement:", color = ORANGE).shift(3.0 * UP).scale(1.4)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Every non-constant polynomial", color = WHITE).shift(1.8 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"over $C[t]$ has atleast one complex root", color = WHITE).shift(0.6000000000000001 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Proof:", color = WHITE).shift(-0.5999999999999996 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Can be proven using Galois theory!", color = WHITE).shift(-1.7999999999999998 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"This will be an exercise", color = WHITE).shift(-3.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        

        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        self.pause()

            
        text = Tex(r"1", color = BLACK).shift(3.0 * UP).scale(1.8)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Module 7", color = ORANGE).shift(1.5 * UP).scale(1.4)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"1", color = BLACK).shift(0.0 * UP).scale(1.8)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Galois Theory", color = GREEN).shift(-1.5 * UP).scale(1.8)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"1", color = BLACK).shift(-3.0 * UP).scale(1.8)
        self.play(Write(text), run_time = 2)
        self.pause()
        

        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        self.pause()

            
        text = Tex(r"Some general points", color = BLUE).shift(3.0 * UP).scale(1.2)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"We will be analyzing Galois Theory", color = WHITE).shift(2.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"through an example", color = WHITE).shift(1.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"We will prove theorems along the way", color = WHITE).shift(0.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"The example we will take is $f = t^4 - 3$, whose", color = WHITE).shift(-1.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"roots are clearly $\eta, -\eta, i \eta, -i \eta$,", color = WHITE).shift(-2.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"where $\eta = \sqrt[4]{3}$.", color = WHITE).shift(-3.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        

        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        self.pause()

            
        text = Tex(r"1. Splitting Field", color = BLUE).shift(3.0 * UP).scale(1.2)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"A splitting field of a polynomial", color = WHITE).shift(2.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"is the field generated by the", color = WHITE).shift(1.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"roots of a polynomial", color = WHITE).shift(0.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"For our example, the", color = WHITE).shift(-1.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"splitting field is $K = \mathbb Q(\eta, -\eta, i \eta, -i \eta)$,", color = WHITE).shift(-2.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"which is also represented as $\mathbb Q(i, \eta)$", color = WHITE).shift(-3.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        

        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        self.pause()

            
        text = Tex(r"2. Degree of $K$ in $\mathbb Q$", color = BLUE).shift(3.0 * UP).scale(1.2)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Consider $K$ to be a vector", color = WHITE).shift(1.8 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"space in $Q$. We will find the", color = WHITE).shift(0.6000000000000001 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"degree of $K$ in $Q$", color = WHITE).shift(-0.5999999999999996 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Consider three field extensions", color = WHITE).shift(-1.7999999999999998 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"$K : \mathbb Q(\eta), \mathbb Q(\eta): \mathbb Q(\eta^2), \mathbb Q(\eta^2): \mathbb Q$", color = WHITE).shift(-3.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        

        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        self.pause()

            
        text = Tex(r"Finding $[\mathbb Q(\eta^2): \mathbb Q]$", color = ORANGE).shift(3.0 * UP).scale(1.4)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"We will prove that $\{ 1, \sqrt 3\}$", color = BLUE).shift(2.142857142857143 * UP).scale(1.2)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"is a basis", color = BLUE).shift(1.2857142857142858 * UP).scale(1.2)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Linear independence: Let $w \in \mathbb Q(\eta^2)$", color = WHITE).shift(0.4285714285714288 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Let $w = a + b \sqrt 3, a, b, \in \mathbb Q = 0, a, b \ne 0$", color = WHITE).shift(-0.4285714285714284 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"$\implies \sqrt 3 = \frac ab$", color = WHITE).shift(-1.2857142857142856 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"But as $\sqrt 3$ is irrational, this is a contradiction", color = WHITE).shift(-2.1428571428571423 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"So, $a = b = 0$", color = WHITE).shift(-3.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        

        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        self.pause()

            
        text = Tex(r"Theorem 3: $[\mathbb Q(\eta^2): \mathbb Q]$", color = ORANGE).shift(3.0 * UP).scale(1.4)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"We will prove that $\{ 1, \sqrt 3\}$", color = BLUE).shift(1.8 * UP).scale(1.2)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"is a basis", color = BLUE).shift(0.6000000000000001 * UP).scale(1.2)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"1", color = BLACK).shift(-0.5999999999999996 * UP).scale(1.8)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Span: Follows trivially from definition", color = WHITE).shift(-1.7999999999999998 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Hence, $[\mathbb Q(\eta^2): \mathbb Q] = 2$", color = WHITE).shift(-3.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        

        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        self.pause()

            
        text = Tex(r"Finding $[\mathbb Q(\eta): \mathbb Q(\eta^2)]$", color = ORANGE).shift(3.0 * UP).scale(1.4)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"We will prove that $\{ 1, \sqrt [4] 3\}$", color = BLUE).shift(2.142857142857143 * UP).scale(1.2)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"is a basis", color = BLUE).shift(1.2857142857142858 * UP).scale(1.2)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Let $w \in \mathbb Q(\eta)$", color = WHITE).shift(0.4285714285714288 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"$w = a + b \eta + c \eta^2 + d \eta^3, a, b, c, d \in \mathbb Q$", color = WHITE).shift(-0.4285714285714284 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"$w = a + c \eta^2 + \eta (b + d \eta^2)$", color = WHITE).shift(-1.2857142857142856 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"$w = 0 \implies a + c \eta^2 = b + d \eta^2 = 0$", color = WHITE).shift(-2.1428571428571423 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"$\implies a = b = c = d = 0$", color = WHITE).shift(-3.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        

        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        self.pause()

            
        text = Tex(r"Finding $[\mathbb Q(\eta): \mathbb Q(\eta^2)]$", color = ORANGE).shift(3.0 * UP).scale(1.4)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"We will prove that $\{ 1, \sqrt [4] 3\}$", color = BLUE).shift(1.8 * UP).scale(1.2)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"is a basis", color = BLUE).shift(0.6000000000000001 * UP).scale(1.2)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"1", color = BLACK).shift(-0.5999999999999996 * UP).scale(1.8)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Span: Follows trivially from definition", color = WHITE).shift(-1.7999999999999998 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Hence, $[\mathbb Q(\eta): \mathbb Q(\eta^2)] = 2$", color = WHITE).shift(-3.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        

        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        self.pause()

            
        text = Tex(r"Similarly, $[\mathbb Q (\eta, i) : \mathbb Q (\eta) ] = 2$", color = WHITE).shift(3.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Degree of $K$ in $\mathbb Q$", color = ORANGE).shift(2.0 * UP).scale(1.4)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Tower Law", color = BLUE).shift(1.0 * UP).scale(1.2)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"For subfields $K \subseteq L \subseteq M$, $[M : K] = [M : L][L : K]$", color = WHITE).shift(0.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"$[K : \mathbb Q] = [K : \mathbb Q (\eta)] [\mathbb Q (\eta) : \mathbb Q (\eta^2)][\mathbb Q (\eta^2): \mathbb Q]$", color = WHITE).shift(-1.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"$[K : \mathbb Q] = 2 \times 2 \times 2 = \boxed{8}$", color = WHITE).shift(-2.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Hence, the degree of $K$ in $\mathbb Q$ is 8", color = WHITE).shift(-3.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        

        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        self.pause()

        text = Tex(r"Tower Law explored visually", color = BLUE).shift(3.0 * UP).scale(1.2)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        img = ImageMobject("venn_diagram_rationals").shift(0.5 * DOWN).scale(0.8)

        self.play(FadeIn(img))
        self.pause()  

        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        self.pause()
            
        text = Tex(r"3. Symmetries of the Roots", color = BLUE).shift(3.0 * UP).scale(1.2)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"- This is arguably the most", color = WHITE).shift(2.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"beautiful part of Galois theory", color = WHITE).shift(1.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"- This talks about the roots in a", color = WHITE).shift(0.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"given field extension", color = WHITE).shift(-1.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"- We will start by finding all", color = WHITE).shift(-2.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"the $\mathbb Q$-automorphisms", color = WHITE).shift(-3.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        

        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        self.pause()

            
        text = Tex(r"$\mathbb Q$-automorphism", color = BLUE).shift(3.0 * UP).scale(1.2)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"An automorphism is a bijective", color = WHITE).shift(2.142857142857143 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"homomorphism from a set", color = WHITE).shift(1.2857142857142858 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"to itself", color = WHITE).shift(0.4285714285714288 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"In our case, we want bijective", color = WHITE).shift(-0.4285714285714284 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"homomorphisms from $K \to K$,", color = WHITE).shift(-1.2857142857142856 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"such that elements of $\mathbb Q$", color = WHITE).shift(-2.1428571428571423 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"remain fixed!", color = WHITE).shift(-3.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        

        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        self.pause()

            
        text = Tex(r"$\mathbb Q$-automorphism", color = BLUE).shift(3.0 * UP).scale(1.2)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"For instance, consider $\sigma (\eta) = i \eta$", color = WHITE).shift(2.142857142857143 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"To prove that elements of $\mathbb Q$", color = WHITE).shift(1.2857142857142858 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"remain fixed, consider $3 = \eta \times i \eta \times - \eta \times -i \eta$", color = WHITE).shift(0.4285714285714288 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"If we apply $\sigma$,", color = WHITE).shift(-0.4285714285714284 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"$3 = i \eta \times i^2 \eta \times - i \eta \times -i i \eta$", color = WHITE).shift(-1.2857142857142856 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"As $3$ is fixed, $1 = \frac 33$ also remains fixed", color = WHITE).shift(-2.1428571428571423 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"If $1$ is fixed, $\mathbb N$ and hence $\mathbb Q$ if fixed", color = WHITE).shift(-3.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        

        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        self.pause()

            
        text = Tex(r"$\mathbb Q$-automorphism", color = BLUE).shift(3.0 * UP).scale(1.2)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Also consider $\tau(i) = - i$", color = WHITE).shift(2.142857142857143 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"To prove that elements of $\mathbb Q$", color = WHITE).shift(1.2857142857142858 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"remain fixed, consider $3 = \eta \times i \eta \times - \eta \times -i \eta$", color = WHITE).shift(0.4285714285714288 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"If we apply $\tau$,", color = WHITE).shift(-0.4285714285714284 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"$\eta \times - i \eta \times - \eta \times i \eta$", color = WHITE).shift(-1.2857142857142856 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"As $3$ is fixed, $1 = \frac 33$ also remains fixed", color = WHITE).shift(-2.1428571428571423 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"If $1$ is fixed, $\mathbb N$ and hence $\mathbb Q$ if fixed", color = WHITE).shift(-3.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        

        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        self.pause()

            
        text = Tex(r"$\mathbb Q$-automorphism", color = BLUE).shift(3.0 * UP).scale(1.2)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"- Identity function is also a $\mathbb Q$-automorphism", color = WHITE).shift(2.142857142857143 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"- If $\sigma$ is a $\mathbb Q$-automorphism,", color = WHITE).shift(1.2857142857142858 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"$\sigma \sigma$ is also a $\mathbb Q$-automorphism.", color = WHITE).shift(0.4285714285714288 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"This is the function $\sigma^2 (\eta) = - \eta$", color = WHITE).shift(-0.4285714285714284 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"- Intuitively, the $\mathbb Q$-automorphisms", color = WHITE).shift(-1.2857142857142856 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"for a \text{Group} under composition", color = WHITE).shift(-2.1428571428571423 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"- This Group is called the Galois group!", color = WHITE).shift(-3.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        

        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        self.pause()

        
        text = Tex(r"Galois Group ($\mathbb D_8$)", color = BLUE).shift(3.0 * UP).scale(1.2)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        img = ImageMobject("D8_cayley").shift(0.5 * DOWN).scale(0.8)

        self.play(FadeIn(img))
        self.pause()  
        
        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        self.pause()

        text = Tex(r"Galois Group: Symmetries of Cube", color = BLUE).shift(3.0 * UP).scale(1.2)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        img = ImageMobject("symmetries_of_cube").shift(0.5 * DOWN).scale(0.8)

        self.play(FadeIn(img))
        self.pause()  

        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        self.pause()


        text = Tex(r"4. Inclusion Diagram", color = BLUE).shift(3.0 * UP).scale(1.2)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        img = ImageMobject("inclusion_diagram").shift(0.5 * DOWN).scale(0.8)

        self.play(FadeIn(img))
        self.pause()  

        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        self.pause()

            
        text = Tex(r"5. Fixed field", color = BLUE).shift(3.0 * UP).scale(1.2)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Consider an operation $\dagger$ on", color = WHITE).shift(2.142857142857143 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"an element $H$ of the Galois group", color = WHITE).shift(1.2857142857142858 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"This is an operation from $\{ \text{subsets of } G\}$", color = WHITE).shift(0.4285714285714288 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"$\to \{ \text{subfields of} \} K$", color = WHITE).shift(-0.4285714285714284 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Under this operation, some subfield", color = WHITE).shift(-1.2857142857142856 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"of $K$ will be fixed. The 'largest'", color = WHITE).shift(-2.1428571428571423 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"such subfield is the fixed field.", color = WHITE).shift(-3.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        

        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        self.pause()

            
        text = Tex(r"$\{1, \tau \}^\dagger$", color = BLUE).shift(3.0 * UP).scale(1.2)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"We want to find the subfield fixed by $\tau$,", color = WHITE).shift(1.5 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"i.e. the field which is fixed if $i \to -i$", color = WHITE).shift(0.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Intuitively, $B^{\dagger} = Q(\eta)$", color = WHITE).shift(-1.5 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"As $Q(\eta)$ is purely real, it is a fixed field", color = WHITE).shift(-3.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        

        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        self.pause()

            
        text = Tex(r"$\{1, \tau \}^\dagger$", color = BLUE).shift(3.0 * UP).scale(1.2)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"To prove that there is no larger subfield which", color = WHITE).shift(1.8 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"is fixed, consider K, the only larger subfield.", color = WHITE).shift(0.6000000000000001 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Note that $i = \frac{i \eta}{\eta}$", color = WHITE).shift(-0.5999999999999996 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"$\tau (i) = \frac{-i \eta}{\eta} \ne i$", color = WHITE).shift(-1.7999999999999998 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"So, it is not fixed", color = WHITE).shift(-3.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        

        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        self.pause()

            
        text = Tex(r"The $\dagger$ operation", color = BLUE).shift(3.0 * UP).scale(1.2)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Note that we could do the $\dagger$", color = WHITE).shift(2.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"operation on every subgroup of G", color = WHITE).shift(1.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"We will end up with the", color = WHITE).shift(0.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"fixed fields of each of the subgroups.", color = WHITE).shift(-1.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"As a sidenote, $\forall H \subseteq G$,", color = WHITE).shift(-2.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"$|H| = [H^\dagger : \mathbb Q]$", color = WHITE).shift(-3.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        

        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        self.pause()

            
        text = Tex(r"Add Inclusion diagram", color = GREEN).shift(3.0 * UP).scale(1.8)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Big image", color = GREEN).shift(-3.0 * UP).scale(1.8)
        self.play(Write(text), run_time = 2)
        self.pause()
        

        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        self.pause()

            
        text = Tex(r"6. Some observations", color = BLUE).shift(3.0 * UP).scale(1.2)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"The deep symmetry is the \textbf{Galois correspondence}", color = WHITE).shift(1.5 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"It is the bijection", color = WHITE).shift(0.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"between subgroups of the Galois groups ($\mathfrak G$)", color = WHITE).shift(-1.5 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"and subfields of the field K ($\mathfrak F$)", color = WHITE).shift(-3.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        

        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        self.pause()

            
        text = Tex(r"1", color = BLACK).shift(3.0 * UP).scale(1.8)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Module 8", color = ORANGE).shift(1.5 * UP).scale(1.4)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"1", color = BLACK).shift(0.0 * UP).scale(1.8)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Problems of Antiquity", color = GREEN).shift(-1.5 * UP).scale(1.8)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"1", color = BLACK).shift(-3.0 * UP).scale(1.8)
        self.play(Write(text), run_time = 2)
        self.pause()
        

        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        self.pause()

            
        text = Tex(r"Compass and Straightedge Constructions", color = BLUE).shift(3.0 * UP).scale(1.2)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"- We are allowed only a compass", color = WHITE).shift(2.142857142857143 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"and an \textit{unmarked} ruler", color = WHITE).shift(1.2857142857142858 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"- If a point $(x, y)$ can be obtained", color = WHITE).shift(0.4285714285714288 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"by compass and straightedge,", color = WHITE).shift(-0.4285714285714284 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"we call it constructible", color = WHITE).shift(-1.2857142857142856 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"- It is natural to associate a", color = WHITE).shift(-2.1428571428571423 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"field to this construction", color = WHITE).shift(-3.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        

        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        self.pause()

            
        text = Tex(r"Assume we are given an initial", color = WHITE).shift(3.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"set of points $P_0 = (x_0, y_0)$", color = WHITE).shift(2.142857142857143 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"One step means intersection", color = WHITE).shift(1.2857142857142858 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"of two lines, two circles, or", color = WHITE).shift(0.4285714285714288 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"one line and one circle", color = WHITE).shift(-0.4285714285714284 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Now, the set of all the points", color = WHITE).shift(-1.2857142857142856 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"we can reach from $P_0$ in one", color = WHITE).shift(-2.1428571428571423 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"step would be $P_1$.", color = WHITE).shift(-3.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        

        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        self.pause()

            
        text = Tex(r"Let $K_i$ be field of all numbers", color = WHITE).shift(3.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"generated by $x_i$ and $y_i$", color = WHITE).shift(2.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Say $P_0 = {(0, 0), (0, 1)}$", color = WHITE).shift(1.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"$K_0 = \mathbb Q$", color = WHITE).shift(0.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"In one construction, we can", color = WHITE).shift(-1.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"construct say $P_1 = {0, \sqrt 2}$", color = WHITE).shift(-2.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()        
        
        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        self.pause()

        text = Tex(r"Construction of $\sqrt 2$", color = BLUE).shift(3.0 * UP).scale(1.2)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        img = ImageMobject("sqrt_2").shift(0.5 * DOWN).scale(0.8)

        self.play(FadeIn(img))
        self.pause()  

        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        self.pause()


        text = Tex(r"Detailed example", color = BLUE).shift(3.0 * UP).scale(1.2)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Say you wanted to create $\sqrt[4]2$", color = WHITE).shift(2.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"from $P_0 = {(0, 0), (0, 1)}$", color = WHITE).shift(1.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Draw a right triangle with sides 1,", color = WHITE).shift(0.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"so that its hypotenuse would be $\sqrt 2$", color = WHITE).shift(-1.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Go to next slide", color = BLUE).shift(-2.0 * UP).scale(1.2)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"$K_0 = \mathbb Q$, $K_1 = \mathbb Q(\sqrt 2)$, $K_2 = \mathbb Q(\sqrt[4]{2})$", color = WHITE).shift(-3.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        

        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        self.pause()

        text = Tex(r"Square root of $a$", color = BLUE).shift(3.0 * UP).scale(1.2)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        img = ImageMobject("root_construction").shift(0.5 * DOWN).scale(0.8)

        self.play(FadeIn(img))
        self.pause()  

        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        self.pause()

        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        self.pause()
            
        text = Tex(r"Theorem 4", color = ORANGE).shift(3.0 * UP).scale(1.4)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"$x_j, y_j \in K_j$ are zeroes of quad. polynomials in $K_{j - 1}$", color = WHITE).shift(2.142857142857143 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Proof", color = BLUE).shift(1.2857142857142858 * UP).scale(1.2)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Note that $$x_j, y_j$$ must", color = WHITE).shift(0.4285714285714288 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"be the intersection of", color = WHITE).shift(-0.4285714285714284 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"1. Line and Circle", color = WHITE).shift(-1.2857142857142856 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"2. Line and Line", color = WHITE).shift(-2.1428571428571423 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"3. Circle and Circle", color = WHITE).shift(-3.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        

        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        self.pause()

            
        text = Tex(r"1. Line and Circle", color = BLUE).shift(3.0 * UP).scale(1.2)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Line passes through $(p, q), (r, s), p, q, r, s \in K_{j - 1}$", color = WHITE).shift(2.142857142857143 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"$\implies \frac{x - p}{r - p} = \frac{y - q}{s - q}$", color = WHITE).shift(1.2857142857142858 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Circle has center $(t, u)$, radius $w$, $t, u, w \in K_{j - 1}$", color = WHITE).shift(0.4285714285714288 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"$(x - t)^2 + (y - u)^2 =  w^2$", color = WHITE).shift(-0.4285714285714284 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"$(x - t)^2 + (\frac{s - q}{r - p} (x - p) + q - u)^2 = w^2$", color = WHITE).shift(-1.2857142857142856 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Likewise for $y$", color = WHITE).shift(-2.1428571428571423 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"$x, y \in K_j$ are zeroes in $K_{j - 1}$", color = WHITE).shift(-3.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        

        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        self.pause()

            
        text = Tex(r"Theorem 4", color = GREEN).shift(3.0 * UP).scale(1.8)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"$x_j, y_j \in K_j$ are zeroes of quadratic polynomials in $K_{j - 1}$", color = WHITE).shift(2.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Proof", color = BLUE).shift(1.0 * UP).scale(1.2)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"2. Line and Line", color = WHITE).shift(0.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"3. Circle and Circle", color = WHITE).shift(-1.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Can be done as an exercise", color = WHITE).shift(-2.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Conclusion: $[K_j : K_{j - 1}] = 1$ or $2$", color = WHITE).shift(-3.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        

        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        self.pause()

            
        text = Tex(r"Theorem 5", color = GREEN).shift(3.0 * UP).scale(1.8)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Consider a constructible point $P$. Then, $P$", color = WHITE).shift(2.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"is constructible by some tower of fields,", color = WHITE).shift(1.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"and let $K(P) = K_n$", color = WHITE).shift(0.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"$[K_n : \mathbb Q]$ is some power of 2", color = WHITE).shift(-1.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Note the contradiction also: if $[K_n : \mathbb Q]$", color = WHITE).shift(-2.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"is not a power of 2, $P$ is not constructible", color = WHITE).shift(-3.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        

        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        self.pause()

            
        text = Tex(r"Trisecting a general angle", color = GREEN).shift(3.0 * UP).scale(1.8)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Say we want to trisect $\frac \pi 3$", color = WHITE).shift(2.142857142857143 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"So, we want an angle $\frac \pi 9$.", color = WHITE).shift(1.2857142857142858 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"If we want to construct $\frac \pi 9$,", color = WHITE).shift(0.4285714285714288 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"we need our field to contain", color = WHITE).shift(-0.4285714285714284 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"$\sin \frac \pi 9 = 2^{- \frac 43} (\sqrt[3] {i - \sqrt 3} - \sqrt[3] {i + \sqrt 3})$", color = WHITE).shift(-1.2857142857142856 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"and $\cos \frac \pi 9 = 2^{- \frac 43} (\sqrt[3] {1 +  i \sqrt 3} + \sqrt[3] {1 - i \sqrt 3})$", color = WHITE).shift(-2.1428571428571423 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"It can be proven that $[\mathbb Q(\sin \frac \pi 9, \cos \frac \pi 9) : \mathbb Q] = 3$", color = WHITE).shift(-3.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        

        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        self.pause()

            
        text = Tex(r"1", color = BLACK).shift(3.0 * UP).scale(1.8)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Module 9", color = ORANGE).shift(1.5 * UP).scale(1.4)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"1", color = BLACK).shift(0.0 * UP).scale(1.8)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Insolvability of the Quintic", color = GREEN).shift(-1.5 * UP).scale(1.8)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"1", color = BLACK).shift(-3.0 * UP).scale(1.8)
        self.play(Write(text), run_time = 2)
        self.pause()
        

        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        self.pause()

            
        text = Tex(r"What does it mean?", color = ORANGE).shift(3.0 * UP).scale(1.4)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"A polynomial is solvable by radicals", color = WHITE).shift(2.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"if you can write its roots", color = WHITE).shift(1.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"in terms of its coefficients,", color = WHITE).shift(0.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"4 arithmetic operations, and nth roots", color = WHITE).shift(-1.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"It means that the general quintic", color = WHITE).shift(-2.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"is not solvable by radicals", color = WHITE).shift(-3.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        

        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        self.pause()

            
        text = Tex(r"What does it mean?", color = ORANGE).shift(3.0 * UP).scale(1.4)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Some particular quintics", color = WHITE).shift(2.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"are certainly solvable by radicals", color = WHITE).shift(1.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Example", color = BLUE).shift(0.0 * UP).scale(1.2)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"$t^5 - 1$ is solvable by radicals", color = WHITE).shift(-1.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Roots are $1, \alpha, \alpha^2, \alpha^3, \alpha^4$", color = WHITE).shift(-2.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"where $\alpha = \frac {(\sqrt{5} - 1)} 4 + i \sqrt{\frac 58 + \frac{\sqrt 5}{8}}$", color = WHITE).shift(-3.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        

        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        self.pause()

            
        text = Tex(r"Solvable Groups", color = BLUE).shift(3.0 * UP).scale(1.2)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"$G$ is solvable if it has a finite", color = WHITE).shift(2.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"series of subgroups such that", color = WHITE).shift(1.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"$1 = G_0 = \subseteq G_1 \dots \subseteq G_n = G$,", color = WHITE).shift(0.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"such that", color = WHITE).shift(-1.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"1. $G_i \triangleleft G_{i + 1}$", color = WHITE).shift(-2.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"2. $G_{i + 1} / G_i$ is abelian", color = WHITE).shift(-3.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        

        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        self.pause()

            
        text = Tex(r"Intuitive explanation", color = ORANGE).shift(3.0 * UP).scale(1.4)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"1. For a polynomial, look at its", color = WHITE).shift(1.8 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Galois group $\Gamma$", color = WHITE).shift(0.6000000000000001 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"2. Check solvability of the $\Gamma$", color = WHITE).shift(-0.5999999999999996 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"3. If $\Gamma$ is solvable, the roots", color = WHITE).shift(-1.7999999999999998 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"can be expressed by radicals", color = WHITE).shift(-3.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        

        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        self.pause()

            
        text = Tex(r"The Symmetric Group", color = BLUE).shift(3.0 * UP).scale(1.2)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"The group of all permutations of", color = WHITE).shift(2.142857142857143 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"$(1, 2, \dots,  n)$ is $\mathbb S_n$", color = WHITE).shift(1.2857142857142858 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Note that $\mathbb S_1, \mathbb S_2$ are", color = WHITE).shift(0.4285714285714288 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"trivially solvable", color = WHITE).shift(-0.4285714285714284 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"$\mathbb S_3$ is solvable, as there is", color = WHITE).shift(-1.2857142857142856 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"a nice sequence, $1 \triangleleft \mathbb C_3 \triangleleft \mathbb S_3$", color = WHITE).shift(-2.1428571428571423 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"$\mathbb S_4$ is also solvable", color = WHITE).shift(-3.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        

        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        self.pause()

            
        text = Tex(r"$\mathbb S_5$ is not solvable", color = BLUE).shift(3.0 * UP).scale(1.2)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Consider the normal subgroups of $\mathbb S_5$", color = WHITE).shift(2.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"One such subgroup is $\mathbb A_5$,", color = WHITE).shift(1.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"which is the alternating group,", color = WHITE).shift(0.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"the set of even permutations", color = WHITE).shift(-1.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"But, $\mathbb A_5$ is not solvable,", color = WHITE).shift(-2.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"hence $\mathbb S_5$ is not solvable", color = WHITE).shift(-3.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        

        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        self.pause()

            
        text = Tex(r"Specific Example $t^5 - 6t + 3$", color = BLUE).shift(3.0 * UP).scale(1.2)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Now, this polynomial's Galois group", color = WHITE).shift(1.8 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"is the group is $\mathbb S_5$", color = WHITE).shift(0.6000000000000001 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Thus, that Galois group is not solvable", color = WHITE).shift(-0.5999999999999996 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Hence, the polynomial is not", color = WHITE).shift(-1.7999999999999998 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"solvable by radicals!", color = WHITE).shift(-3.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        

        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        self.pause()

            