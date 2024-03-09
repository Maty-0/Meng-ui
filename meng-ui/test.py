from style import Template, display
import time
from color import *

test = Template()
test.generate()
test.add_border()
test.add_text(["H","e","l", "l", "o"], 5, 5, foreground.green, background.black)

test2 = Template()
test2.generate(None, "\x1b[44;1m")
test2.add_text(["w","o","r","l","d"], 5, 5)


while True:
    display(test)
    time.sleep(1)
    display(test2)
    time.sleep(1)
