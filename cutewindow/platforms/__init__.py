import platform

if platform.system() == "Darwin":
    from .mac import CuteDialog, CuteMainWindow, CuteWindow, TitleBar
else:
    from .windows import CuteDialog, CuteMainWindow, CuteWindow, TitleBar
