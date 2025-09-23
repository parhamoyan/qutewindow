import platform

if platform.system() == "Darwin":
    from .mac import QuteDialog, QuteMainWindow, QuteWindow, TitleBar
else:
    from .windows import QuteDialog, QuteMainWindow, QuteWindow, TitleBar
