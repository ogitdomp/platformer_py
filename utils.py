import platform
from screeninfo import get_monitors

def get_screen_dimensions():
    system = platform.system()

    if system == 'Windows':
        import ctypes
        user32 = ctypes.windll.user32
        width = user32.GetSystemMetrics(0)
        height = user32.GetSystemMetrics(1)
    
    elif system == 'Darwin' or system == 'Linux':
        monitors = get_monitors()
        if monitors:
            width, height = monitors[0]
        else:
            width = height = None
    
    else:
        width = height = None
    
    return (width, height)