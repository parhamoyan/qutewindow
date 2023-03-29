import platform

if platform.system() == "Darwin":
    from .mac import QuteWindow, QuteMainWindow
else:
    from .windows import QuteWindow, QuteMainWindow
