from style import Template, Button, Text, Box
from terminal import display
from color import *
import time
from eol import get_key

#new class define test
button1 = Button("test",1,2,15,3, foreground_hover=foreground.red, background_hover=background.green)
text1 = Text("hey", 5, 10)
box1 = Box()


test2 = Template()
test2.generate(None, background.rgb(204,255,153))
test2.add_button([button1])
test2.add_text([text1])
test2.add_box([box1])



terminal = display()


while True:
    terminal.print(test2)
    #terminal.print(test)
    #test2.button[0].hover = not test2.button[0].hover
    #test2.regen = True
    #test2.add_button(test2.button[0])
    #test2.regen = False
    key = get_key()
    if key:
        print(key)

    time.sleep(0.1)