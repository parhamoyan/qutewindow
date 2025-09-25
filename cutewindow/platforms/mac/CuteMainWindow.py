"""
macOS-specific CuteMainWindow implementation.

This module provides the macOS-specific implementation of the CuteMainWindow class,
which creates a customizable main window with native macOS styling and behavior.
It extends QMainWindow functionality while providing a customizable title bar
and native window management integration.
"""

from typing import Optional

from PySide6.QtGui import Qt
from PySide6.QtWidgets import QMainWindow, QWidget

from cutewindow.base import CuteWindowMixin
from cutewindow.platforms.mac.title_bar.TitleBar import TitleBar


class CuteMainWindow(CuteWindowMixin, QMainWindow):
    """
    macOS-specific customizable main window implementation.

    This class provides a customizable main window for macOS with native styling and
    window management integration. It extends QMainWindow to support menus,
    toolbars, status bars, and central widgets while maintaining a customizable
    appearance with custom title bar.

    The window automatically handles:
    - Native window shadows and animations
    - Proper window layering and z-ordering
    - Integration with macOS window management features
    - Custom title bar with window controls
    - QMainWindow features (menus, toolbars, dock widgets, etc.)

    Attributes:
        _title_bar (TitleBar): The custom title bar widget.

    Example:
        >>> main_window = CuteMainWindow()
        >>> main_window.setWindowTitle("My Application")
        >>> main_window.setCentralWidget(QWidget())
        >>> main_window.show()
    """

    def __init__(self, parent: Optional[QWidget] = None) -> None:
        """
        Initialize the macOS CuteMainWindow.

        Args:
            parent (Optional[QWidget]): The parent widget, defaults to None.
        """
        super().__init__(parent)

        self.setWindowFlag(
            Qt.WindowType.NoTitleBarBackgroundHint
            | Qt.WindowType.ExpandedClientAreaHint
        )
        self.resize(800, 800)
        self._title_bar = TitleBar(self)
