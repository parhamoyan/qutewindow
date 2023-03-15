import platform

if platform.system() == "Darwin":
    from .mac import QuteWindow
else:
    from .windows import QuteWindow