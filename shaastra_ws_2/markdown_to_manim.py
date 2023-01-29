from numpy import linspace

def markdown_to_manim(filename, h1_color = 'BLUE', h2_color = 'ORANGE', h3_color = 'GREEN', text_color = 'WHITE'):

    with open(filename) as f:
        string = f.read()
    
    slides = string.split('---')

    out = f'''
from manim_presentation import Slide
from manim import *
from math import *

class {filename[:-3]}(Slide):
    def construct(self):'''

    for slide in slides:

        content = [i.strip() for i in slide.split('\n') if i.strip() != '']
        shift = len(content)

        # assert shift <= 8, 'There should be less than 8 lines in the slide' 

        array = linspace(3, -3, num = shift)

    #     if (content[0][0] == '%'):

    #         out += f'''
    #     obj = SVGMobject("{content[0][1:]}")
    #     self.play(FadeIn(obj), run_time = 3)
    #     self.pause()
    #     text = text("{content[1]}").shift(3 * DOWN)
    #     self.play(Write(text), run_time = 2)
    #     self.pause()        
    # '''
    #         continue

        for i in (range(shift)):

            if (content[i][0:3] == '###'):
                factor = 1.2
                content[i] = content[i][3:]
                color = h1_color
            elif (content[i][0:2] == '##'):
                factor = 1.4
                content[i] = content[i][2:]
                color = h2_color
            elif (content[i][0] == '#'):
                factor = 1.8
                content[i] = content[i][1:]
                color = h3_color
            else:
                factor = 1.0
                color = text_color

            if content[i] == "":
                content[i] = "1"
                color = "BLACK"

            content[i] = content[i].strip()
            out += f'''
        text = Tex(r"{content[i]}", color = {color}).shift({array[i]} * UP).scale({factor})
        self.play(Write(text), run_time = 2)
        self.pause()
        '''        

        out += f'''

        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time = 3)
        self.pause()

            '''


    out += """
        self.wait()
        self.pause()

        self.wait()
        self.pause()

        self.wait()
        self.pause()

"""

    with open (filename[:-3] + '.py', 'w') as f:




        f.write(out)

# markdown_to_manim("galois_theory.md")