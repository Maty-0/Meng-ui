from mengui.style import Template, Text
from mengui.terminal import display
from mengui.color import *
import os
from random import randint
import time


template1 = Template()
template1.generate()
text = Text("MENGUI", 0, 0, foreground.white, background.black)
template1.add_text([text])
terminal = display()

def random_foreground():
    rr, rg, rb = randint(1, 255), randint(1, 255) ,randint(1, 255)
    text.foreground_color = foreground.rgb(rr,rg,rb)

def check_border():
    global bounce_direction
    width, height = os.get_terminal_size()
    if width <= (text.x + 6): #+6 acounting for the space the string takes up after the location
        bounce_direction = bounce_direction[0] + "L" #change direction from right to left but keep the old up/down
        return True
    if height <= text.y + 1:
        bounce_direction =  "U" + bounce_direction[1]
        return True
    if text.y - 1 <= 0:
        bounce_direction = "D" + bounce_direction[1]
        return True
    if text.x - 1 <= 0:
        bounce_direction = bounce_direction[0]+ "R"
        return True
    return False

def bounce():
    
    if check_border():
        random_foreground()

    match bounce_direction:
        case "DR":
            text.x += 1 
            text.y += 1
        case "DL":
            text.x -= 1
            text.y += 1
        case "UR":
            text.x += 1
            text.y -= 1
        case "UL":
            text.x -= 1 
            text.y -= 1


bounce_direction = "DR" #DL = down reight, UL = up left,...

while True:
    terminal.print(template1)
    bounce()
    time.sleep(0.1)
    template1.regenerate() #after editing values on the fly we have to manualy give the regenerate call so we have the correct matrix
