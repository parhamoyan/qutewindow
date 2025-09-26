"""
Windows-specific CuteWindow implementation.

This module provides the Windows-specific implementation of the CuteWindow class,
which creates a customizable window with native Windows styling and behavior.
It integrates seamlessly with Windows window management while providing
a customizable title bar with native window controls.
"""

from typing import Optional

from PySide6.QtCore import QByteArray
from PySide6.QtWidgets import QWidget

from cutewindow.base import CuteWindowMixin
from cutewindow.platforms.windows.native_event import _nativeEvent
from cutewindow.platforms.windows.title_bar.TitleBar import TitleBar
from cutewindow.platforms.windows.utils import (
    addShadowEffect,
    addWindowAnimation,
    isWindowResizable,
    setWindowNonResizable,
)


class CuteWindow(CuteWindowMixin, QWidget):
    """
    Windows-specific customizable window implementation.

    This class provides a customizable window for Windows with native styling and
    window management integration. It uses Windows API calls to achieve
    native appearance while maintaining the ability to customize the title bar.

    The window automatically handles:
    - Native window shadows and animations
    - Proper window layering and z-ordering
    - Integration with Windows window management features
    - Custom title bar with window controls (close, minimize, maximize)
    - Native event handling for window operations

    Attributes:
        _title_bar (TitleBar): The custom title bar widget.

    Example:
        >>> window = CuteWindow()
        >>> window.setWindowTitle("My Application")
        >>> window.show()
    """

    def __init__(self, parent: Optional[QWidget] = None):
        """
        Initialize the Windows CuteWindow.

        Args:
            parent (Optional[QWidget]): The parent widget, defaults to None.
        """
        super(CuteWindow, self).__init__(parent)

        self._title_bar = TitleBar(self)
        addShadowEffect(self.winId())
        addWindowAnimation(self.winId())
        self.resize(800, 800)

    def setNonResizable(self):
        """Make the window non-resizable."""
        setWindowNonResizable(self.winId())
        if hasattr(self._title_bar, "maximize_button"):
            self._title_bar.maximize_button.hide()  # type: ignore

    def isResizable(self) -> bool:
        """
        Check if the window is resizable.

        Returns:
            bool: True if the window is resizable, False otherwise.
        """
        return isWindowResizable(self.winId())

    def nativeEvent(self, event_type: QByteArray, message: int):  # type: ignore
        """
        Handle native Windows events.

        This method processes native Windows messages to enable proper
        window behavior, including resizing, moving, and other system
        interactions that require native event handling.

        Args:
            event_type (QByteArray): The type of the native event.
            message (int): The native event message.

        Returns:
            Tuple[bool, int]: A tuple containing a boolean indicating if the
                             event was handled and an optional result value.
        """
        return _nativeEvent(self, event_type, message)
