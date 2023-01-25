
from manim_presentation import Slide
from manim import *
from math import *

class galois_theory(Slide):
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
        
        text = Tex(r"Module 1", color = ORANGE).shift(1.5 * UP).scale(1.4)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Introduction to", color = GREEN).shift(0.0 * UP).scale(1.8)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Abstract Algebra", color = GREEN).shift(-1.5 * UP).scale(1.8)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"1", color = BLACK).shift(-3.0 * UP).scale(1.8)
        self.play(Write(text), run_time = 2)
        self.pause()
        

        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        self.pause()

            
        text = Tex(r"Why abstract algebra?", color = ORANGE).shift(3.0 * UP).scale(1.4)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Abstract algebra might seem", color = WHITE).shift(1.8 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"very vague and might sound like", color = WHITE).shift(0.6000000000000001 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"a mathematical curiosity", color = WHITE).shift(-0.5999999999999996 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"But be assured that they have", color = WHITE).shift(-1.7999999999999998 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"wide-ranging applications", color = WHITE).shift(-3.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        

        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        self.pause()

            
        text = Tex(r"Why abstract algebra?", color = ORANGE).shift(3.0 * UP).scale(1.4)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Error control coding", color = BLUE).shift(1.8 * UP).scale(1.2)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"In coding theory, group codes", color = WHITE).shift(0.6000000000000001 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"are a type of code", color = WHITE).shift(-0.5999999999999996 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"They are a fundamental part", color = WHITE).shift(-1.7999999999999998 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"of coding theory", color = WHITE).shift(-3.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        

        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        self.pause()

            
        text = Tex(r"Why abstract algebra?", color = ORANGE).shift(3.0 * UP).scale(1.4)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"3D Modelling", color = BLUE).shift(1.8 * UP).scale(1.2)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Quaternions are used extensively", color = WHITE).shift(0.6000000000000001 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"in 3D modelling", color = WHITE).shift(-0.5999999999999996 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Quaternions are an example of an", color = WHITE).shift(-1.7999999999999998 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"algebraic structure called \textbf{ring}", color = WHITE).shift(-3.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        

        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        self.pause()

            
        text = Tex(r"Why abstract algebra?", color = ORANGE).shift(3.0 * UP).scale(1.4)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Chemistry", color = BLUE).shift(2.142857142857143 * UP).scale(1.2)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Chemists use Group theory to", color = WHITE).shift(1.2857142857142858 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"analyze the symmetries of lattices", color = WHITE).shift(0.4285714285714288 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Group theory is an elegant way", color = WHITE).shift(-0.4285714285714284 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"to capture symmetries, as for", color = WHITE).shift(-1.2857142857142856 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"describing symmetries, the nature", color = WHITE).shift(-2.1428571428571423 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"of the molecule does not matter", color = WHITE).shift(-3.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        

        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        self.pause()

            
        text = Tex(r"What is abstract algebra?", color = BLUE).shift(3.0 * UP).scale(1.2)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Abstract algebra consists of algebraic structures", color = WHITE).shift(1.5 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"An algebraic structure is a set, with", color = WHITE).shift(0.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"some operations, and some axioms (rules)", color = WHITE).shift(-1.5 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Some examples are groups, rings, and fields", color = WHITE).shift(-3.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        

        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        self.pause()

            
        text = Tex(r"The idea of homomorphism", color = BLUE).shift(3.0 * UP).scale(1.2)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"A homomorphism is a structure-preserving", color = WHITE).shift(2.142857142857143 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"map between two algebraic structures", color = WHITE).shift(1.2857142857142858 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Consider a structure $A$, with some", color = WHITE).shift(0.4285714285714288 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"operation $\cdot$, another structure $B$", color = WHITE).shift(-0.4285714285714284 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"with some operation $\times$", color = WHITE).shift(-1.2857142857142856 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"$f : A \to B$ is a homomorphism", color = WHITE).shift(-2.1428571428571423 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"iff $f(a \cdot b) = f(a) \times f(b) \forall a, b \in A$", color = WHITE).shift(-3.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        

        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        self.pause()

            
        text = Tex(r"Vector space", color = GREEN).shift(3.0 * UP).scale(1.8)
        self.play(Write(text), run_time = 2)
        self.pause()
        

        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        self.pause()

            
        text = Tex(r"1", color = BLACK).shift(3.0 * UP).scale(1.8)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Reading Assignment", color = ORANGE).shift(1.5 * UP).scale(1.4)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"1", color = BLACK).shift(0.0 * UP).scale(1.8)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Intuition and Applications", color = WHITE).shift(-1.5 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"of Category Theory", color = WHITE).shift(-3.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        

        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        self.pause()

            
        text = Tex(r"1", color = BLACK).shift(3.0 * UP).scale(1.8)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Module 2", color = ORANGE).shift(1.5 * UP).scale(1.4)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"1", color = BLACK).shift(0.0 * UP).scale(1.8)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Group Theory", color = GREEN).shift(-1.5 * UP).scale(1.8)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"1", color = BLACK).shift(-3.0 * UP).scale(1.8)
        self.play(Write(text), run_time = 2)
        self.pause()
        

        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        self.pause()

            
        text = Tex(r"Example 1", color = BLUE).shift(3.0 * UP).scale(1.2)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"$\mathbb{Z}$ under $+$", color = WHITE).shift(2.142857142857143 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"- Addition of two integers", color = WHITE).shift(1.2857142857142858 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"results in an integer (closure)", color = WHITE).shift(0.4285714285714288 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"- Addition of integers is", color = WHITE).shift(-0.4285714285714284 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"associative, $a + (b + c) = (a + b) + c$", color = WHITE).shift(-1.2857142857142856 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"- 0 is the additive identity", color = WHITE).shift(-2.1428571428571423 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"- $\forall a \in \mathbb{Z}, \exists a^{-1}: a + a^{-1} = 0$", color = WHITE).shift(-3.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        

        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        self.pause()

            
        text = Tex(r"What is a group?", color = BLUE).shift(3.0 * UP).scale(1.2)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"It consists of a set $S$ with binary operation $\odot$", color = WHITE).shift(1.8 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"- The set is closed under $\odot$", color = WHITE).shift(0.6000000000000001 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"- The operation is associative", color = WHITE).shift(-0.5999999999999996 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"- There exists an identity e: $a \odot e = a \forall a \in S$", color = WHITE).shift(-1.7999999999999998 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"- $\forall a \exists a^{-1} : a a^{-1} = e$", color = WHITE).shift(-3.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        

        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        self.pause()

            
        text = Tex(r"Example 2", color = BLUE).shift(3.0 * UP).scale(1.2)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"$\{ 1, w, w^2 \}$ under $\times$", color = WHITE).shift(2.25 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"- It is closed (by observation)", color = WHITE).shift(1.5 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"- It is associative (by associativity", color = WHITE).shift(0.75 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"of multiplication of complex numbers)", color = WHITE).shift(0.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"- There exists a multiplicative identity", color = WHITE).shift(-0.75 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"$1$", color = WHITE).shift(-1.5 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"- There exists a multiplicative inverse", color = WHITE).shift(-2.25 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"$1^{-1} = 1$, $w^{-1} = w^2$", color = WHITE).shift(-3.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        

        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        self.pause()

            
        text = Tex(r"Abelian Group", color = BLUE).shift(3.0 * UP).scale(1.2)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Groups which are commutative", color = WHITE).shift(1.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"are called Abelian Groups", color = WHITE).shift(-1.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Eg. $(\mathbb{Z}, +), (\mathbb{R}, +)$", color = WHITE).shift(-3.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        

        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        self.pause()

            
        text = Tex(r"Example of non-Group", color = BLUE).shift(3.0 * UP).scale(1.2)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"$(\mathbb{R}, \times)$", color = WHITE).shift(2.142857142857143 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"- It is closed", color = WHITE).shift(1.2857142857142858 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"- It is associative", color = WHITE).shift(0.4285714285714288 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"- Identity element 1 exists", color = WHITE).shift(-0.4285714285714284 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"- Inverse exits for all non-zero elements", color = WHITE).shift(-1.2857142857142856 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"But, $0$ does not have multiplicative inverse!", color = WHITE).shift(-2.1428571428571423 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"$R^* = R - \{0 \}$ is a group under $\times$", color = WHITE).shift(-3.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        

        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        self.pause()

            
        text = Tex(r"Groups and Symmetries", color = BLUE).shift(3.0 * UP).scale(1.2)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"1", color = BLACK).shift(1.8 * UP).scale(1.8)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Go to", color = ORANGE).shift(0.6000000000000001 * UP).scale(1.4)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Image", color = ORANGE).shift(-0.5999999999999996 * UP).scale(1.4)
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
            
        text = Tex(r"Dihedral Group of order 6", color = BLUE).shift(3.0 * UP).scale(1.2)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        img = ImageMobject("D6_cayley").shift(0.5 * DOWN).scale(0.8)

        self.play(FadeIn(img))
        self.pause()        

        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        self.pause()

            
        text = Tex(r"Subgroup", color = BLUE).shift(3.0 * UP).scale(1.2)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"A subset of a group which is also", color = WHITE).shift(2.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"a group is a subgroup", color = WHITE).shift(1.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"$H \subseteq G$ and H is a group", color = WHITE).shift(0.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"$\implies$ H is a subgroup", color = WHITE).shift(-1.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Eg. $\mathbb{R}_+$ is a subgroup", color = WHITE).shift(-2.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"of $\mathbb{R}^*$", color = WHITE).shift(-3.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        

        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        self.pause()

            
        text = Tex(r"Subgroups of Dihedral group", color = BLUE).shift(3.0 * UP).scale(1.2)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Subgroups of $D_6$ are", color = WHITE).shift(1.8 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"$\{e\}$", color = WHITE).shift(0.6000000000000001 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"$\{e, a\}$", color = WHITE).shift(-0.5999999999999996 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"$\{e, r, r^2\}$", color = WHITE).shift(-1.7999999999999998 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"$D_6$ itself", color = WHITE).shift(-3.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        

        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        self.pause()

            
        text = Tex(r"Cosets of $\{1, b, b^2 \}$", color = BLUE).shift(3.0 * UP).scale(1.2)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        img = ImageMobject("D6_cosets").shift(0.5 * DOWN).scale(0.8)

        self.play(FadeIn(img))
        self.pause()        
        
        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        self.pause()

        text = Tex(r"Left cosets of $\{1, a\}$", color = BLUE).shift(3.0 * UP).scale(1.2)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        img = ImageMobject("D6_left_cosets").shift(0.5 * DOWN).scale(0.8)

        self.play(FadeIn(img))
        self.pause()  

        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        self.pause()

        text = Tex(r"Right cosets of $\{1, a\}$", color = BLUE).shift(3.0 * UP).scale(1.2)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        img = ImageMobject("D6_right_cosets").shift(0.5 * DOWN).scale(0.8)

        self.play(FadeIn(img))
        self.pause()  

        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        self.pause()

        text = Tex(r"Normal subgroup", color = BLUE).shift(3.0 * UP).scale(1.2)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"A subgroup is said to be normal", color = WHITE).shift(2.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"iff its left and right cosets", color = WHITE).shift(1.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"are equal (denoted by $H \triangleleft G$)", color = WHITE).shift(0.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"For $D_6$, $\{e\}$, $\{e, r, r^2\}$,", color = WHITE).shift(-1.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"$D_6$ are normal subgroups", color = WHITE).shift(-2.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"$\{e, a\}$ is \textbf{not} normal!", color = WHITE).shift(-3.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        

        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        self.pause()

            
        text = Tex(r"Exercise", color = BLUE).shift(3.0 * UP).scale(1.2)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Prove that all left cosets", color = WHITE).shift(1.8 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"of a subgroup have the same size", color = WHITE).shift(0.6000000000000001 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"\textbf{Method: } Prove that", color = WHITE).shift(-0.5999999999999996 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"there is a bijection between", color = WHITE).shift(-1.7999999999999998 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"a subgroup and its left coset", color = WHITE).shift(-3.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        

        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        self.pause()

            
        text = Tex(r"Index of a subgroup", color = BLUE).shift(3.0 * UP).scale(1.2)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Index of a subgroup H in G", color = WHITE).shift(2.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"is the number of left cosets,", color = WHITE).shift(1.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"and is denoted by $[G : H]$", color = WHITE).shift(0.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Note that the", color = WHITE).shift(-1.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"number of left cosets =", color = WHITE).shift(-2.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"number of right cosets", color = WHITE).shift(-3.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        

        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        self.pause()

            
        text = Tex(r"Theorem 1: Lagrange's theorem", color = ORANGE).shift(3.0 * UP).scale(1.4)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"$$|G| = [G: H] |H|$$", color = WHITE).shift(2.142857142857143 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Proof", color = BLUE).shift(1.2857142857142858 * UP).scale(1.2)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"All cosets are of equal size", color = WHITE).shift(0.4285714285714288 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"The number of cosets is $[G : H]$", color = WHITE).shift(-0.4285714285714284 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Number of elements in each coset is $|H|$", color = WHITE).shift(-1.2857142857142856 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Total number of elements in the group", color = WHITE).shift(-2.1428571428571423 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"has to be product of the above two", color = WHITE).shift(-3.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        

        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        self.pause()

            
        text = Tex(r"Quotient Group", color = BLUE).shift(3.0 * UP).scale(1.2)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"For $N \triangleleft G$, consider", color = WHITE).shift(2.142857142857143 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"cosets of N. The set of cosets is", color = WHITE).shift(1.2857142857142858 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"called a quotient group.", color = WHITE).shift(0.4285714285714288 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Consider $C_2 \triangleleft C_6$.", color = WHITE).shift(-0.4285714285714284 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"$C_6 / C_2 = \{ \{0, 3\}, \{1, 4\}, \{2, 5\} \}$", color = WHITE).shift(-1.2857142857142856 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"The set of left cosets", color = WHITE).shift(-2.1428571428571423 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"has the same structure as $C_3$", color = WHITE).shift(-3.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        

        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        self.pause()

            
        text = Tex(r"1", color = BLACK).shift(3.0 * UP).scale(1.8)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Module 3", color = ORANGE).shift(1.5 * UP).scale(1.4)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"1", color = BLACK).shift(0.0 * UP).scale(1.8)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Frieze Groups", color = GREEN).shift(-1.5 * UP).scale(1.8)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"1", color = BLACK).shift(-3.0 * UP).scale(1.8)
        self.play(Write(text), run_time = 2)
        self.pause()
        

        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        self.pause()

            
        text = Tex(r"Do we have time?", color = BLUE).shift(3.0 * UP).scale(1.2)
        self.play(Write(text), run_time = 2)
        self.pause()
        

        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        self.pause()

            
        text = Tex(r"1", color = BLACK).shift(3.0 * UP).scale(1.8)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Module 4", color = ORANGE).shift(1.5 * UP).scale(1.4)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"1", color = BLACK).shift(0.0 * UP).scale(1.8)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Ring Theory", color = GREEN).shift(-1.5 * UP).scale(1.8)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"1", color = BLACK).shift(-3.0 * UP).scale(1.8)
        self.play(Write(text), run_time = 2)
        self.pause()
        

        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        self.pause()

            
        text = Tex(r"Definition of a Ring", color = BLUE).shift(3.0 * UP).scale(1.2)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"A ring is a set $R$ with two binary operations", color = WHITE).shift(2.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"$+$ and $\times$, such that", color = WHITE).shift(1.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"$1 \in R$", color = WHITE).shift(0.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"$x, y \in R \implies x + y, xy, -x \in R$", color = WHITE).shift(-1.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Note that a multiplicative inverse", color = WHITE).shift(-2.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"does not have to exist", color = WHITE).shift(-3.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        

        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        self.pause()

            
        text = Tex(r"Example 1", color = BLUE).shift(3.0 * UP).scale(1.2)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"$\{a + b i : a, b \in \mathbb{Z} \}$", color = WHITE).shift(2.142857142857143 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"It is clearly a group under addition", color = WHITE).shift(1.2857142857142858 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"It is closed under multiplication", color = WHITE).shift(0.4285714285714288 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"It is associative under multiplication", color = WHITE).shift(-0.4285714285714284 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"1 is the identity element", color = WHITE).shift(-1.2857142857142856 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Except $\pm 1, \pm i$, no other element", color = WHITE).shift(-2.1428571428571423 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"has multiplicative inverse", color = WHITE).shift(-3.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        

        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        self.pause()

            
        text = Tex(r"Rethinking about Polynomials", color = BLUE).shift(3.0 * UP).scale(1.2)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"A polynomial is a function that", color = WHITE).shift(2.142857142857143 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"takes in some t as input and returns", color = WHITE).shift(1.2857142857142858 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"some $f(t) = a_n t^n + a_{n - 1} t^{n - 1} + \dots + a_0$", color = WHITE).shift(0.4285714285714288 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"A polynomial in the indeterminate t", color = WHITE).shift(-0.4285714285714284 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"is the expression $a_n t^n + a_{n - 1} t^{n - 1} + \dots + a_0$", color = WHITE).shift(-1.2857142857142856 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"$t$ is just a placeholder.", color = WHITE).shift(-2.1428571428571423 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Degree of polynomial is largest $n: a_n \ne 0$", color = WHITE).shift(-3.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        

        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        self.pause()

            
        text = Tex(r"Polynomial Rings", color = BLUE).shift(3.0 * UP).scale(1.2)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"A polynomial over a ring R is denoted by $R[t]$.", color = WHITE).shift(2.142857142857143 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"It consists of all polynomials with coefficients in", color = WHITE).shift(1.2857142857142858 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"R. The degree can be anything", color = WHITE).shift(0.4285714285714288 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"- Polynomials are clearly a group under addition", color = WHITE).shift(-0.4285714285714284 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"- It is closed under multiplication", color = WHITE).shift(-1.2857142857142856 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"- There is a multiplicative identity,", color = WHITE).shift(-2.1428571428571423 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"the 1 polynomial", color = WHITE).shift(-3.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        

        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        self.pause()

            
        text = Tex(r"Irreducibility of Polynomials", color = BLUE).shift(3.0 * UP).scale(1.2)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"A polynomial over a subring R of $\mathbb{C}$", color = WHITE).shift(2.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"is reducible if it can be written as a product", color = WHITE).shift(1.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"of two polynomials in R of smaller degree", color = WHITE).shift(0.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"All polynomials of degree 0 or 1", color = WHITE).shift(-1.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"are irreducible", color = WHITE).shift(-2.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"They are analogous to primes!", color = WHITE).shift(-3.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        

        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        self.pause()

            
        text = Tex(r"Examples of irreducible polynomials", color = BLUE).shift(3.0 * UP).scale(1.2)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Consider $t^2 + 2$", color = WHITE).shift(2.142857142857143 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"It is irreducible over $\mathbb{Z}$. To prove,", color = WHITE).shift(1.2857142857142858 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"let $t^2 + 2 = (at + b)(ct + d)$,", color = WHITE).shift(0.4285714285714288 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"$a, b, c, d, \in \mathbb{Z}$.", color = WHITE).shift(-0.4285714285714284 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Now, $ac = 1 \implies a = c = 1$, or $a = c = -1$.", color = WHITE).shift(-1.2857142857142856 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Also, $bc + ad = 0 \implies b + d = 0$.", color = WHITE).shift(-2.1428571428571423 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Also, $2 = bd \implies -2 = d^2$.", color = WHITE).shift(-3.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        

        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        self.pause()

            
        text = Tex(r"Zeroes of a Polynomial", color = BLUE).shift(3.0 * UP).scale(1.2)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"For a polynomial $f \in \mathbb{R}[t]$,", color = WHITE).shift(2.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"$\alpha \in R$ is said to be a zero iff", color = WHITE).shift(1.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"$f(\alpha) = 0$", color = WHITE).shift(0.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Example", color = WHITE).shift(-1.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"$\sqrt 2 i $ is a zero of $t^2 + 2i \in C[t]$", color = WHITE).shift(-2.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"$-\sqrt 2 i $ is a zero of $t^2 + 2i \in C[t]$", color = WHITE).shift(-3.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        

        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        self.pause()

            
        text = Tex(r"1", color = BLACK).shift(3.0 * UP).scale(1.8)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Module 5", color = ORANGE).shift(1.5 * UP).scale(1.4)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"1", color = BLACK).shift(0.0 * UP).scale(1.8)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Field Theory", color = GREEN).shift(-1.5 * UP).scale(1.8)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"1", color = BLACK).shift(-3.0 * UP).scale(1.8)
        self.play(Write(text), run_time = 2)
        self.pause()
        

        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        self.pause()

            
        text = Tex(r"What is a field?", color = BLUE).shift(3.0 * UP).scale(1.2)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"A field is a ring in which", color = WHITE).shift(2.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"multiplication is commutative and", color = WHITE).shift(1.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"inverses exist for all elements other", color = WHITE).shift(0.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"than $0$, the additive identity", color = WHITE).shift(-1.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"$\mathbb{Q}, \mathbb{R}, \mathbb C$ are fields", color = WHITE).shift(-2.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"$\mathbb a + b\sqrt{2}, a, b \in \mathbb Q$ is a field", color = WHITE).shift(-3.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        

        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        self.pause()

            
        text = Tex(r"Motivation", color = BLUE).shift(3.0 * UP).scale(1.2)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Consider the polynomial $f = t^2 - \sqrt 2 \in \mathbb Q [t]$", color = WHITE).shift(2.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"This polynomial is irreducible over $\mathbb Q$,", color = WHITE).shift(1.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"but it is reducible in $\mathbb R$", color = WHITE).shift(0.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Consider a set $S = {a + b \sqrt{2}: a, b \in Q}$", color = WHITE).shift(-1.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"This set S is a field!", color = WHITE).shift(-2.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Also note that $f$ is reducible over $S$", color = WHITE).shift(-3.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        

        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        self.pause()

            
        text = Tex(r"Field extension", color = ORANGE).shift(3.0 * UP).scale(1.4)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"A field extension $f: A \to B$ is an", color = WHITE).shift(2.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"injective homomorphism, where $A, B \in \mathbb C$", color = WHITE).shift(1.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"The homomorphism is usually unambigious", color = WHITE).shift(0.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Example", color = BLUE).shift(-1.0 * UP).scale(1.2)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"The identity map in $\mathbb Q \to \mathbb R$", color = WHITE).shift(-2.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"The identity map in $\mathbb R \to \mathbb C$", color = WHITE).shift(-3.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        

        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        self.pause()

            
        text = Tex(r"Generator of a field", color = BLUE).shift(3.0 * UP).scale(1.2)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"A field $F$ is said to be generated by", color = WHITE).shift(2.142857142857143 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"a set $S$ if it is the intersection", color = WHITE).shift(1.2857142857142858 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"of all subfields that contain $S$", color = WHITE).shift(0.4285714285714288 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"It is considered the 'smallest'", color = WHITE).shift(-0.4285714285714284 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"subfield containing $S$", color = WHITE).shift(-1.2857142857142856 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"$\mathbb Q (\sqrt 2)$ is the field", color = WHITE).shift(-2.1428571428571423 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"generated by $\{\sqrt{2}\}$", color = WHITE).shift(-3.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        

        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        self.pause()

            
        text = Tex(r"Field extension as a vector space", color = BLUE).shift(3.0 * UP).scale(1.2)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Consider the set $\mathbb Q (\sqrt 2)$.", color = WHITE).shift(2.142857142857143 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"This consists of $w = a + \sqrt b, a, b, \in \mathbb Q$", color = WHITE).shift(1.2857142857142858 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Think of $w$ as a degree 2 vector space,with", color = WHITE).shift(0.4285714285714288 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"basis $\{ 1, \sqrt 2 \}$, and field $\mathbb Q$", color = WHITE).shift(-0.4285714285714284 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"In general, the degree of a field extension", color = WHITE).shift(-1.2857142857142856 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"$L$ over $K$ is the degree of the vector space $L$,", color = WHITE).shift(-2.1428571428571423 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"over the field $K$ and is denoted by $[L : K]$", color = WHITE).shift(-3.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        

        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        self.pause()

            
        text = Tex(r"Theorem 2: Tower Law", color = ORANGE).shift(3.0 * UP).scale(1.4)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"For subfields $K \subseteq L \subseteq M$, $[M : K] = [M : L][L : K]$", color = WHITE).shift(2.25 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Proof", color = BLUE).shift(1.5 * UP).scale(1.2)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Let $x_i$ be a basis for $L$ in $K$", color = WHITE).shift(0.75 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"let $y_j$ be a basis for $M$ in $L$", color = WHITE).shift(0.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Our aim is to prove that", color = WHITE).shift(-0.75 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"$x_i y_j$ is a basis for $M$ in $K$", color = WHITE).shift(-1.5 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"We have to prove linear", color = WHITE).shift(-2.25 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"independence and spanning", color = WHITE).shift(-3.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        

        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        self.pause()

            
        text = Tex(r"Linear independence", color = BLUE).shift(3.0 * UP).scale(1.2)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Let $\sum_{ij} k_{ij} x_i y_j \in M$", color = WHITE).shift(1.8 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"As $M$ is linearly independent in $L$,", color = WHITE).shift(0.6000000000000001 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"$\sum_j (\sum_i k_{ij} x_i) y_j = 0 \implies \sum_{k_{ij} x_i} = 0$", color = WHITE).shift(-0.5999999999999996 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"As $L$ is linearly independent in $K$,", color = WHITE).shift(-1.7999999999999998 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"$\sum_{k_{ij} x_i} = 0 \implies k_{ij} = 0 \forall j$", color = WHITE).shift(-3.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        

        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        self.pause()

            
        text = Tex(r"Spanning", color = ORANGE).shift(3.0 * UP).scale(1.4)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Let $x \in M$", color = WHITE).shift(2.142857142857143 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"As $y_j$ spans $M$,", color = WHITE).shift(1.2857142857142858 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"$x = \sum_j \lambda_j y_j$", color = WHITE).shift(0.4285714285714288 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"As $x_i$ spans $L$,", color = WHITE).shift(-0.4285714285714284 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"$y_j = \sum \lambda_i x_i$", color = WHITE).shift(-1.2857142857142856 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"$x = \sum_{ij} \lambda_{ij} x_i y_j$,", color = WHITE).shift(-2.1428571428571423 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"where $\lambda_{ij} = \lambda_i \lambda_j$", color = WHITE).shift(-3.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        

        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        self.pause()

            
        text = Tex(r"Detailed example: $\mathbb Q (\sqrt 2, i)$", color = BLUE).shift(3.0 * UP).scale(1.2)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"It consists of numbers of the form", color = WHITE).shift(2.142857142857143 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"$\alpha = a + b \sqrt 2 + c i + d \sqrt 2 i, a, b, c, d, \in \mathbb Q$", color = WHITE).shift(1.2857142857142858 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"$\mathbb Q (\sqrt 2, i)$ is an extension of $\mathbb Q (\sqrt 2)$", color = WHITE).shift(0.4285714285714288 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"$\mathbb Q (\sqrt 2, i)$ is an extension of $\mathbb Q (i)$", color = WHITE).shift(-0.4285714285714284 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"$\mathbb Q (\sqrt 2, i)$ is an extension of $\mathbb Q (\sqrt 2 i)$", color = WHITE).shift(-1.2857142857142856 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"Exercise: Prove that $\alpha^{-1} \in \mathbb Q (\sqrt 2, i)$", color = WHITE).shift(-2.1428571428571423 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"By tower law, degree is 4", color = WHITE).shift(-3.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        

        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        self.pause()

            
        text = Tex(r"Subfield", color = BLUE).shift(3.0 * UP).scale(1.2)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"A field $K$ is said to be a subfield", color = WHITE).shift(1.8 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"of a field $L$ if $K \subset L$", color = WHITE).shift(0.6000000000000001 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"$\mathbb Q$ is a subfield of $\mathbb Q (\sqrt 2)$", color = WHITE).shift(-0.5999999999999996 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"$\mathbb Q$ is a subfield of $\mathbb Q (\sqrt [4] 2)$", color = WHITE).shift(-1.7999999999999998 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
        
        text = Tex(r"$\mathbb R$ is a subfield of $\mathbb C$", color = WHITE).shift(-3.0 * UP).scale(1.0)
        self.play(Write(text), run_time = 2)
        self.pause()
                    

        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        self.pause()


            