import math
from manim import *
from manim_slides import Slide

class Problem(Slide):
    def construct(self):
        text = Tex(r"A Problem in \\ Graph Theory", color = BLUE).scale(1.5)
        self.play(Write(text))
        self.pause()
        self.play(Unwrite(text))

        text = Tex(r"Say we're at a party \\ How many people need to be present such that \\ we are guaranteed that at least three of them are \\ (pairwise) mutual friends or\\  (pairwise) mutual strangers?", color = BLUE).scale(1.2)
        self.play(Write(text))
        self.pause()
        
        self.play(Unwrite(text))

        text1 = Tex(r"Solution using Graph Theory", color = BLUE).scale(1.2).shift(3 * UP + 2 * LEFT)
        text2 = Tex(r"\begin{itemize} \item Assume nodes are people \\ \item Blue edge indicates mutual friendship \\ \item Red edge indicates mutual enemity \end{itemize}", color = WHITE).scale(1.2)

        self.play(Write(text1))
        self.play(Write(text2))
        self.pause()
 
        self.play(*[FadeOut(object) for object in self.mobjects], run_time = 2)

        text1 = Tex(r"$$n = 5$$", color = BLUE).scale(1.2).shift(3 * UP + 2 * LEFT)
        self.play(Create(text1))

        cpent=[[2*math.sin(i*TAU/5),2*math.cos(i*TAU/5),0] for i in range(5)]
        chex=[[2*math.sin(i*TAU/6),2*math.cos(i*TAU/6),0] for i in range(6)]
        
        p=[Dot(point=i) for i in cpent]
        red = [(0,1),(0,2),(1,4),(2,3),(3,4)]
        [self.add(j) for j in p]
        lines=[]

        for i in range(5):
            for j in range(i+1,5):
                l1=Line(start=p[i],end=p[j])
                lines.append(l1)
                if (i,j) in red:
                    l1.set_color(RED)
                else:
                    l1.set_color(BLUE)
                self.play(Create(l1))
        
                self.pause()

        for lin in lines:
            self.remove(lin)
        self.add(Dot(point=chex[0]))
        paths=[Line(start=cpent[i],end=chex[i+1]) for i in range(5)]
        self.play(*[MoveAlongPath(p[i],paths[i]) for i in range(5)])
        p=[Dot(point=i) for i in chex]

        self.remove(text1)
        text1 = Tex(r"$$n = 6$$", color = BLUE).scale(1.2).shift(3 * UP + 2 * LEFT)

        self.play(Write(text1))

        self.pause()
        for i in range(2,5):
            l1=Line(start=p[0],end=p[i])
            l1.set_color(RED)
            self.play(Create(l1))
            
            self.pause()
        for i in range(2,5):
            l1=Line(start=p[3],end=p[i])
            l1.set_color(BLUE)
            self.play(Create(l1))
            self.pause()
        l1=Line(start=p[4],end=p[2])
        l1.set_color(RED)
        self.play(Create(l1))
        self.pause()
        self.remove(l1)
        l1=Line(start=p[4],end=p[2])
        l1.set_color(BLUE)
        self.play(Create(l1))

        self.pause()
        self.wait()
        self.pause()
        self.wait()
        self.pause()
        self.wait()
        


        





    