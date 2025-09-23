"""
macOS-specific QuteWindow implementation.

This module provides the macOS-specific implementation of the QuteWindow class,
which creates a frameless window with native macOS styling and behavior.
It integrates seamlessly with macOS window management while providing
a customizable title bar.
"""

from typing import Optional

from PySide6.QtGui import Qt
from PySide6.QtWidgets import QWidget

from qutewindow.base import QuteWindowMixin
from qutewindow.platforms.mac.title_bar.TitleBar import TitleBar


class QuteWindow(QuteWindowMixin, QWidget):
    """
    macOS-specific frameless window implementation.
    
    This class provides a frameless window for macOS with native styling and
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
        >>> window = QuteWindow()
        >>> window.setWindowTitle("My Application")
        >>> window.show()
    """
    
    def __init__(self, parent: Optional[QWidget] = None) -> None:
        """
        Initialize the macOS QuteWindow.
        
        Args:
            parent (Optional[QWidget]): The parent widget, defaults to None.
        """
        super().__init__(parent)
        
        self.setWindowFlag(Qt.WindowType.NoTitleBarBackgroundHint | Qt.WindowType.ExpandedClientAreaHint)
        self.resize(800, 800)
        self._title_bar = TitleBar(self)
