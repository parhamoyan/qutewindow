"""
Windows-specific QuteWindow implementation.

This module provides the Windows-specific implementation of the QuteWindow class,
which creates a frameless window with native Windows styling and behavior.
It integrates seamlessly with Windows window management while providing
a customizable title bar with native window controls.
"""

from typing import Optional

from PySide6.QtCore import Qt, QByteArray
from PySide6.QtGui import QShowEvent
from PySide6.QtWidgets import QWidget

from qutewindow.base import QuteWindowMixin
from qutewindow.platforms.windows.native_event import _nativeEvent
from qutewindow.platforms.windows.title_bar.TitleBar import TitleBar
from qutewindow.platforms.windows.utils import addShadowEffect, addWindowAnimation, setWindowNonResizable, \
    isWindowResizable


class QuteWindow(QuteWindowMixin, QWidget):
    """
    Windows-specific frameless window implementation.
    
    This class provides a frameless window for Windows with native styling and
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
        >>> window = QuteWindow()
        >>> window.setWindowTitle("My Application")
        >>> window.show()
    """
    
    def __init__(self, parent: Optional[QWidget] = None):
        """
        Initialize the Windows QuteWindow.
        
        Args:
            parent (Optional[QWidget]): The parent widget, defaults to None.
        """
        super(QuteWindow, self).__init__(parent)

        self._title_bar = TitleBar(self)
        addShadowEffect(self.winId())
        addWindowAnimation(self.winId())
        self.resize(800, 800)

    def setNonResizable(self):
        """Make the window non-resizable."""
        setWindowNonResizable(self.winId())
        if hasattr(self._title_bar, 'maximize_button'):
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
