"""
Platform factory for creating platform-specific CuteWindow components.

This module provides a factory pattern to create the appropriate platform-specific
implementations based on the current operating system. It abstracts away the
platform detection and import logic, providing a unified interface for creating
CuteWindow components regardless of the underlying platform.

Supported Platforms:
    - macOS (darwin): Uses native macOS window management and styling
    - Windows: Uses native Windows window management and styling
    - Linux: Currently not supported (raises NotImplementedError)

Example:
    >>> from cutewindow.platform_factory import get_cute_window_class
    >>> CuteWindow = get_cute_window_class()
    >>> window = CuteWindow()
"""

import platform
from typing import Type

from .base import BaseCuteWindow, BaseTitleBar


def get_platform_name() -> str:
    """
    Get the current platform name in a standardized format.

    Returns:
        str: The platform name ('mac', 'windows', or 'linux').

    Raises:
        NotImplementedError: If the platform is not supported.
    """
    system = platform.system().lower()

    platform_mapping = {"darwin": "mac", "windows": "windows", "linux": "linux"}

    if system in platform_mapping:
        return platform_mapping[system]
    else:
        raise NotImplementedError(f"Platform {system} is not supported")


def get_cute_window_class() -> Type[BaseCuteWindow]:
    """
    Get the appropriate CuteWindow class for the current platform.

    Returns:
        Type[BaseCuteWindow]: The platform-specific CuteWindow class.

    Raises:
        NotImplementedError: If the current platform is not supported.
    """
    platform_name = get_platform_name()

    if platform_name == "mac":
        from .platforms.mac.CuteWindow import CuteWindow
    elif platform_name == "windows":
        from .platforms.windows.CuteWindow import CuteWindow
    else:
        raise NotImplementedError(f"CuteWindow is not supported on {platform_name}")

    return CuteWindow  # type: ignore


def get_cute_main_window_class() -> Type[BaseCuteWindow]:
    """
    Get the appropriate CuteMainWindow class for the current platform.

    Returns:
        Type[BaseCuteWindow]: The platform-specific CuteMainWindow class.

    Raises:
        NotImplementedError: If the current platform is not supported.
    """
    platform_name = get_platform_name()

    if platform_name == "mac":
        from .platforms.mac.CuteMainWindow import CuteMainWindow
    elif platform_name == "windows":
        from .platforms.windows.CuteMainWindow import CuteMainWindow
    else:
        raise NotImplementedError(f"CuteMainWindow is not supported on {platform_name}")

    return CuteMainWindow  # type: ignore


def get_cute_dialog_class() -> Type[BaseCuteWindow]:
    """
    Get the appropriate CuteDialog class for the current platform.

    Returns:
        Type[BaseCuteWindow]: The platform-specific CuteDialog class.

    Raises:
        NotImplementedError: If the current platform is not supported.
    """
    platform_name = get_platform_name()

    if platform_name == "mac":
        from .platforms.mac.CuteDialog import CuteDialog
    elif platform_name == "windows":
        from .platforms.windows.CuteDialog import CuteDialog
    else:
        raise NotImplementedError(f"CuteDialog is not supported on {platform_name}")

    return CuteDialog  # type: ignore


def get_title_bar_class() -> Type[BaseTitleBar]:
    """
    Get the appropriate TitleBar class for the current platform.

    Returns:
        Type[BaseTitleBar]: The platform-specific TitleBar class.

    Raises:
        NotImplementedError: If the current platform is not supported.
    """
    platform_name = get_platform_name()

    if platform_name == "mac":
        from .platforms.mac.title_bar.TitleBar import TitleBar
    elif platform_name == "windows":
        from .platforms.windows.title_bar.TitleBar import TitleBar
    else:
        raise NotImplementedError(f"TitleBar is not supported on {platform_name}")

    return TitleBar  # type: ignore
