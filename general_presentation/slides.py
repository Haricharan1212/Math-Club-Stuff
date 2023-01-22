
from manim_presentation import Slide
from manim import *
from math import *

class Scene1(Slide):
    def construct(self):
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

            
        text = Tex(r"Theorem 2: Cancellation Law", color = GREEN).shift(3.0 * UP).scale(1.8)
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

            
        text = Tex(r"Theorem 5:", color = ORANGE).shift(3.0 * UP).scale(1.4)
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

            
        text = Tex(r"Theorem 5:", color = ORANGE).shift(3.0 * UP).scale(1.4)
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

            
        text = Tex(r"Theorem 5:", color = ORANGE).shift(3.0 * UP).scale(1.4)
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

            
        text = Tex(r"Theorem 6: Wilson\'s Theorem", color = ORANGE).shift(3.0 * UP).scale(1.4)
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

            
        text = Tex(r"Theorem 6: Wilson\'s Theorem", color = ORANGE).shift(3.0 * UP).scale(1.4)
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

            
        text = Tex(r"Theorem 6: Wilson\'s Theorem", color = ORANGE).shift(3.0 * UP).scale(1.4)
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

            
        text = Tex(r"Theorem 7: Fermat\'s Little Theorem", color = ORANGE).shift(3.0 * UP).scale(1.4)
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

            
        text = Tex(r"Theorem 7: Fermat\'s Little Theorem", color = ORANGE).shift(3.0 * UP).scale(1.4)
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

            
        text = Tex(r"Theorem 7: Fermat\'s Little Theorem", color = ORANGE).shift(3.0 * UP).scale(1.4)
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

            
        self.wait(2)
        self.pause()
        self.wait(2)
        self.pause()

    