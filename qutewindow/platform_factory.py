"""
Platform factory for creating platform-specific QuteWindow components.

This module provides a factory pattern to create the appropriate platform-specific
implementations based on the current operating system.
"""

import platform
from typing import Type

from .base import BaseQuteWindow, BaseTitleBar


def get_platform_name() -> str:
    """Get the current platform name."""
    system = platform.system().lower()
    if system == "darwin":
        return "mac"
    elif system == "windows":
        return "windows"
    elif system == "linux":
        return "linux"
    else:
        raise NotImplementedError(f"Platform {system} is not supported")


def get_qute_window_class() -> Type[BaseQuteWindow]:
    """Get the appropriate QuteWindow class for the current platform."""
    platform_name = get_platform_name()
    
    if platform_name == "mac":
        from .platforms.mac.QuteWindow import QuteWindow
    elif platform_name == "windows":
        from .platforms.windows.QuteWindow import QuteWindow
    else:
        raise NotImplementedError(f"QuteWindow is not supported on {platform_name}")
    
    return QuteWindow


def get_qute_main_window_class() -> Type[BaseQuteWindow]:
    """Get the appropriate QuteMainWindow class for the current platform."""
    platform_name = get_platform_name()
    
    if platform_name == "mac":
        from .platforms.mac.QuteMainWindow import QuteMainWindow
    elif platform_name == "windows":
        from .platforms.windows.QuteMainWindow import QuteMainWindow
    else:
        raise NotImplementedError(f"QuteMainWindow is not supported on {platform_name}")
    
    return QuteMainWindow


def get_qute_dialog_class() -> Type[BaseQuteWindow]:
    """Get the appropriate QuteDialog class for the current platform."""
    platform_name = get_platform_name()
    
    if platform_name == "mac":
        from .platforms.mac.QuteDialog import QuteDialog
    elif platform_name == "windows":
        from .platforms.windows.QuteDialog import QuteDialog
    else:
        raise NotImplementedError(f"QuteDialog is not supported on {platform_name}")
    
    return QuteDialog


def get_title_bar_class() -> Type[BaseTitleBar]:
    """Get the appropriate TitleBar class for the current platform."""
    platform_name = get_platform_name()
    
    if platform_name == "mac":
        from .platforms.mac.title_bar.TitleBar import TitleBar
    elif platform_name == "windows":
        from .platforms.windows.title_bar.TitleBar import TitleBar
    else:
        raise NotImplementedError(f"TitleBar is not supported on {platform_name}")
    
    return TitleBar