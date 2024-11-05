import os
import sys

def get_key(osp = None):
    if osp == None:
        osp = check_os()
        if osp == "windows":
            import msvcrt
        else:
            import tty
            import termios
    
    if osp == "windows":
        #todo linux support
        if msvcrt.kbhit():
            key = msvcrt.getch()
            if key == b'\xe0':  # Special key prefix
                key = msvcrt.getch()
                if key == b'H':
                    return 'UP'
                elif key == b'P':
                    return 'DOWN'
                elif key == b'K':
                    return 'LEFT'
                elif key == b'M':
                    return 'RIGHT'
            else:
                try:
                    return key.decode('utf-8', errors='ignore')
                except UnicodeDecodeError:
                    return None
    else:
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            key = sys.stdin.read(1)
            if key == '\x1b':  # Escape sequence (for arrow keys)
                extra = sys.stdin.read(2)
                if extra == '[A':
                    return 'UP'
                elif extra == '[B':
                    return 'DOWN'
                elif extra == '[C':
                    return 'RIGHT'
                elif extra == '[D':
                    return 'LEFT'
            else:
                return key
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

def check_os():
    if os.name == 'nt':
        return "windows"
    else:
        return "linux/mac"
    
def clear_screen(osp = None):
    if osp == None:
        osp = check_os()
    if osp == "windows":
        os.system('cls')
    else:
        os.system('clear')