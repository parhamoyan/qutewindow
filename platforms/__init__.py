import platform

if platform.system() == "Darwin":
    from .mac import FramelessWindow
else:
    from .windows import FramelessWindow