import platform

if platform.system() == "Darwin":
    from .mac import QuteWindow
    from .mac import QuteMainWindow
else:
    from .windows import QuteWindow
