"""
Platform factory for creating platform-specific QuteWindow components.

This module provides a factory pattern to create the appropriate platform-specific
implementations based on the current operating system. It abstracts away the
platform detection and import logic, providing a unified interface for creating
QuteWindow components regardless of the underlying platform.

Supported Platforms:
    - macOS (darwin): Uses native macOS window management and styling
    - Windows: Uses native Windows window management and styling
    - Linux: Currently not supported (raises NotImplementedError)

Example:
    >>> from cutewindow.platform_factory import get_qute_window_class
    >>> QuteWindow = get_qute_window_class()
    >>> window = QuteWindow()
"""

import platform
from typing import Type, Union

from .base import BaseQuteWindow, BaseTitleBar


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


def get_qute_window_class() -> Type[BaseQuteWindow]:
    """
    Get the appropriate QuteWindow class for the current platform.

    Returns:
        Type[BaseQuteWindow]: The platform-specific QuteWindow class.

    Raises:
        NotImplementedError: If the current platform is not supported.
    """
    platform_name = get_platform_name()

    if platform_name == "mac":
        from .platforms.mac.QuteWindow import QuteWindow
    elif platform_name == "windows":
        from .platforms.windows.QuteWindow import QuteWindow
    else:
        raise NotImplementedError(f"QuteWindow is not supported on {platform_name}")

    return QuteWindow  # type: ignore


def get_qute_main_window_class() -> Type[BaseQuteWindow]:
    """
    Get the appropriate QuteMainWindow class for the current platform.

    Returns:
        Type[BaseQuteWindow]: The platform-specific QuteMainWindow class.

    Raises:
        NotImplementedError: If the current platform is not supported.
    """
    platform_name = get_platform_name()

    if platform_name == "mac":
        from .platforms.mac.QuteMainWindow import QuteMainWindow
    elif platform_name == "windows":
        from .platforms.windows.QuteMainWindow import QuteMainWindow
    else:
        raise NotImplementedError(f"QuteMainWindow is not supported on {platform_name}")

    return QuteMainWindow  # type: ignore


def get_qute_dialog_class() -> Type[BaseQuteWindow]:
    """
    Get the appropriate QuteDialog class for the current platform.

    Returns:
        Type[BaseQuteWindow]: The platform-specific QuteDialog class.

    Raises:
        NotImplementedError: If the current platform is not supported.
    """
    platform_name = get_platform_name()

    if platform_name == "mac":
        from .platforms.mac.QuteDialog import QuteDialog
    elif platform_name == "windows":
        from .platforms.windows.QuteDialog import QuteDialog
    else:
        raise NotImplementedError(f"QuteDialog is not supported on {platform_name}")

    return QuteDialog  # type: ignore


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
