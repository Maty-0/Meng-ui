import msvcrt

def get_key():
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
        return None