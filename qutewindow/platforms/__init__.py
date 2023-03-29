import platform

if platform.system() == "Darwin":
    from .mac import QuteWindow, QuteMainWindow, QuteDialog
else:
    from .windows import QuteWindow, QuteMainWindow, QuteDialog
