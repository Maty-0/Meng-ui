import os
from color import *
import sys
import threading

class Template:
    def __init__(self):
        self.matrix = []
        self.terminal_width, self.terminal_height = 50,50
        self.background_color = background.black
        self.text = []
        self.box = []
        self.regen = False


    def generate(self, preset=None, background_color=background.black):
        self.matrix = []
        
        if preset is None:
            width, height = os.get_terminal_size()
        else: 
            width, height = preset
        self.terminal_width, self.terminal_height = width, height

        for _ in range(self.terminal_height):
            data = []
            for _ in range(0, self.terminal_width):
                data.append(background_color + " ")
            self.matrix.append(data)
        self.background_color = background_color
    
    def regenerate(self):
        self.regen = True
        self.terminal_width, self.terminal_height = os.get_terminal_size()
        self.generate(background_color=self.background_color)
        for a in self.text:
            print(a)
            self.add_text(a[0], a[1], a[2], a[3], a[4])
        for y in self.box:
            self.add_box(y[0], y[1], y[2], y[3], y[4], y[5], y[6], y[7], y[8])
        self.regen = False
            


    def add_text(self, text, x, y, foreground_color = foreground.white, background_color = background.black):
        if self.regen == False:
            self.text.append([text,x,y,foreground_color,background_color])

        x_data = self.matrix[y]
        count = 0
        for chars in text:
            if x + count >= len(x_data):
                break
            x_data[x + count] = foreground_color + background_color + chars + "\u001b[0m"
            count += 1
        self.matrix[y] = x_data

    def add_box(self, x=0, y=0, width=1, height=1, top_bot = "-" ,side = "|",edge = "+" , foreground_color = foreground.white, background_color = background.black):
        if self.regen == False:
            self.box.append([x,y,width,height,top_bot,side,edge,foreground_color,background_color])

        if x + width > len(self.matrix[x]):
            return "Out of range"
        if y + height > len(self.matrix):
            return "Out of range"
        
        if width <= 1:
            width = int(self.terminal_width * width)
        if height <= 1:
            height = int(self.terminal_height * height)
        
        for a in range(height):
            x_data = self.matrix[y + a]
            for b in range(width):
                if a == 0 or a == height - 1:
                    if b == 0:
                        x_data[x + b] = foreground_color + background_color + edge + "\u001b[0m"
                    elif b == width - 1:
                        x_data[x + b] = foreground_color + background_color + edge + "\u001b[0m"
                    else:
                        x_data[x + b] = foreground_color + background_color + top_bot + "\u001b[0m"
                elif b == 0 or b == width - 1:
                    x_data[x + b] = foreground_color + background_color + side + "\u001b[0m"

                self.matrix[y + a] = x_data


def display(template):
    os.system('clear')
    if os.get_terminal_size() != (template.terminal_width, template.terminal_height):
        template.regenerate()
    count = 0
    for x in template.matrix:
        row = ""
        for z in x:
            row += z
        if count < len(template.matrix) -1:
            row += '\n'
        sys.stdout.write(row)
        sys.stdout.flush()
        count += 1
    sys.stdout.write("\033[?25l")
    sys.stdout.flush()