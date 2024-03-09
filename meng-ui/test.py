from style import Template, display
import time
from color import *

test = Template()
test.generate()
test.add_box()
test.add_text("Hello", 5, 5, foreground.green, background.black)

test2 = Template()
test2.generate(None, background.rgb(204,255,153))
test2.add_text("WORLD", 5, 5)


while True:
    display(test)
    time.sleep(1)
    display(test2)
    time.sleep(1)
