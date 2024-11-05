import sys
import os
import copy
from mengui.eol import clear_screen


class display:
    def __init__(self):
        self.last_print = None
        clear_screen()

    def print(self,template):
        if os.get_terminal_size() != (template.terminal_width, template.terminal_height):   
                template.regenerate()

        if self.last_print != template.matrix:
            for count, x in enumerate(template.matrix):
                if self.last_print is None or template.regen or x != self.last_print[count]:
                    for char_count, a in enumerate(x):
                        if self.last_print is None or template.regen or a != self.last_print[count][char_count]:
                            sys.stdout.write(f"\033[{count + 1};{char_count + 1}H{a}")

            if template.regen: template.regen = False
            sys.stdout.write("\033[?25l")
            sys.stdout.flush()
            self.last_print = copy.deepcopy(template.matrix)
        else:
            pass