from mengui.style import Template, Button, Text, Box
from mengui.terminal import display
from mengui.color import *
import time
from mengui.eol import get_key

#new class define test
button1 = Button("test",70,30,15,3, foreground_hover=foreground.red, background_hover=background.green)
text1 = Text("hey", 5, 10)
text2 = Text("yo", 15, 15)
text3 = Text("lol", 70, 25)
box1 = Box(x=70, width=70,  height=10)


test2 = Template()
test2.generate((70,70), background.rgb(204,255,153))
test2.add_button([button1])
test2.add_text([text1])
test2.add_text([text2,text3])
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
    test2.move()
    time.sleep(0.1)