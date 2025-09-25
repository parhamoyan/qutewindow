"""
macOS-specific CuteWindow implementation.

This module provides the macOS-specific implementation of the CuteWindow class,
which creates a customizable window with native macOS styling and behavior.
It integrates seamlessly with macOS window management while providing
a customizable title bar.
"""

from typing import Optional

from PySide6.QtGui import Qt
from PySide6.QtWidgets import QWidget

from cutewindow.base import CuteWindowMixin
from cutewindow.platforms.mac.title_bar.TitleBar import TitleBar


class CuteWindow(CuteWindowMixin, QWidget):
    """
    macOS-specific customizable window implementation.

    This class provides a customizable window for macOS with native styling and
    window management integration. It uses Qt's window flags to achieve
    native appearance while maintaining the ability to customize the title bar.

    The window automatically handles:
    - Native window shadows and animations
    - Proper window layering and z-ordering
    - Integration with macOS window management features
    - Custom title bar with window controls

    Attributes:
        _title_bar (TitleBar): The custom title bar widget.

    Example:
        >>> window = CuteWindow()
        >>> window.setWindowTitle("My Application")
        >>> window.show()
    """

    def __init__(self, parent: Optional[QWidget] = None) -> None:
        """
        Initialize the macOS CuteWindow.

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
