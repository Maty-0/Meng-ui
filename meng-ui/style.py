import os
from color import *
import sys
import threading

class Template:
    def __init__(self):
        self.matrix = []
        self.terminal_width, self.terminal_height = 50,50
        self.background_color = background.black
        self.priority = []
        self.text_cache = []
        self.box_cache = []
        self.button_cache = []
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
        os.system('cls')
        self.generate(background_color=self.background_color)
        for a in self.text_cache:
            self.add_text([a])
        self.add_box(self.box_cache)
        for b in self.button_cache:
            self.add_button([b])
            
    def move(self, direction, template_only=False):
        for a in self.button:
            pass
    
#           _,'|             _.-''``-...___..--';)
#          /_ \'.      __..-' ,      ,--...--'''
#         <\    .`--'''       `     /'
#          `-';'   features   ;   ; ;
#    __...--''     ___...--_..'  .;.'
#   (,__....----'''       (,..--''   

    def add_text(self, texts):
        for text in texts:
            if self.regen == False:
                self.text_cache.append(text)

            x_data = self.matrix[text.y]
            count = 0
            for chars in text.text:
                if text.x + count >= len(x_data):
                    break
                x_data[text.x + count] = text.foreground_color + text.background_color + chars + "\u001b[0m"
                count += 1
            self.matrix[text.y] = x_data

    def add_box(self, boxes):
        for box in boxes:
            if self.regen == False:
                self.box_cache.append(box)

            if box.x + box.width > len(self.matrix[box.x]):
                return "Out of range"
            if box.y + box.height > len(self.matrix):
                return "Out of range"
            
            render_width, render_height = box.width, box.height
        
            if box.width <= 1:
                render_width = int(self.terminal_width * box.width)
            if box.height <= 1:
                render_height = int(self.terminal_height * box.height)
            
            for a in range(render_height):
                x_data = self.matrix[box.y + a]
                for b in range(render_width):
                    if a == 0 or a == render_height - 1:
                        if b == 0:
                            x_data[box.x + b] = box.foreground_color + box.background_color + box.edge + "\u001b[0m"
                        elif b == render_width - 1:
                            x_data[box.x + b] = box.foreground_color + box.background_color + box.edge + "\u001b[0m"
                        else:
                            x_data[box.x + b] = box.foreground_color + box.background_color + box.top_bot + "\u001b[0m"
                    elif b == 0 or b == render_width - 1:
                        x_data[box.x + b] = box.foreground_color + box.background_color + box.side + "\u001b[0m"

                    self.matrix[box.y + a] = x_data

    def edit_matrix(self, x,y,string):
        for count, char in enumerate(string):
            self.matrix[y][x+count] = char

        
    def add_button(self, buttons):
        for button in buttons:
            if self.regen == False:
                self.button_cache.append(button)

            background_color, foreground_color = button.background_color, button.foreground_color
            if button.hover:
                background_color, foreground_color = button.background_hover, button.foreground_hover

            #generate background
            for b in range(button.height):
                x_data = self.matrix[button.y+b]
                for a in range(button.width):
                    if button.x + a >= len(x_data):
                        break
                    x_data[button.x+a] = background_color + " " + "\u001b[0m"
        
            #generate text
            x,y = 0,0
            if button.width > len(button.text)+1:
                x = int((button.width - len(button.text)) / 2)
            if button.height > 2:
                y = int((button.height -1) /2)
        
            x_data = self.matrix[button.y + y]
            count = 0
            for chars in button.text:
                if (x + button.x) + count >= len(x_data):
                    break
                x_data[(x + button.x) + count] = foreground_color + background_color + chars + "\u001b[0m"
                count += 1
            self.matrix[button.y + y] = x_data

#           __..--''``---....___   _..._    __
# /// //_.-'    .-/";  `        ``<._  ``.''_ `. / // /
#///_.-' _..--.'_    \   CLASSES          `( ) ) // //
#/ (_..-' // (< _     ;_..__               ; `' / ///
# / // // //  `-._,_)' // / ``--...____..-' /// / //
            
class Button:
    def __init__(self, text, x = 0, y = 0, width=5, height=1, foreground_color = foreground.white, background_color = background.black, foreground_hover=foreground.black, background_hover=background.green, callback=None):
        self.text = text
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.foreground_color = foreground_color
        self.background_color = background_color
        self.foreground_hover = foreground_hover
        self.background_hover = background_hover
        self.callback = callback
        self.hover = False
    
    def press(self):
        if self.callback:
            self.callback()

class Box:
    def __init__(self, x=0, y=0, width=1, height=1, top_bot = "-" ,side = "|",edge = "+" , foreground_color = foreground.white, background_color = background.black):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.top_bot = top_bot
        self.side = side
        self.edge = edge
        self.foreground_color = foreground_color
        self.background_color = background_color

class Text:
    def __init__(self, text, x, y, foreground_color = foreground.white, background_color = background.black):
        self.text = text
        self.x = x
        self.y = y
        self.foreground_color = foreground_color
        self.background_color = background_color