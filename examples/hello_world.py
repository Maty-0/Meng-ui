from mengui.style import Template, Text, Box
from mengui.terminal import display
import time
from mengui.color import *

#create our template and generate it
test = Template()
test.generate()

#define the classes that will be used in this template, these classes can be reused in other templates
box = Box()
text = Text("Hello", 5, 10, foreground.green, background.black)

#add the created elements to our template
test.add_text([text])
test.add_box([box])

#lets do the same for the world text, notice how we can reuse the box we created earlier
test2 = Template()

#in this genarate we define the background color of the template
test2.generate(None, background.rgb(204,255,153))


text2 = Text("WORLD", 5, 10)
test2.add_text([text2])
test2.add_box([box])

#create our terminal view (this will allow us later to put multiple templates inside a terminal,...)
terminal = display()

#A loop to draw to the terminal, this is needed so we can rescale the terminal view.
#The terminal will only redraw if needed
while True:
    terminal.print(test)
    time.sleep(1)
    terminal.print(test2)
    time.sleep(1)
