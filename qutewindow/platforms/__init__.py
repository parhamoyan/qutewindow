import platform

if platform.system() == "Darwin":
    from .mac import QuteWindow, QuteMainWindow, QuteDialog, TitleBar
else:
    from .windows import QuteWindow, QuteMainWindow, QuteDialog, TitleBar
