"""
Windows-specific QuteMainWindow implementation.

This module provides the Windows-specific implementation of the QuteMainWindow class,
which creates a frameless main window with native Windows styling and behavior.
It extends QMainWindow functionality while providing a customizable title bar
and native window management integration.
"""

from typing import Optional

from PySide6.QtCore import Qt, QByteArray
from PySide6.QtGui import QShowEvent
from PySide6.QtWidgets import QWidget, QMainWindow

from qutewindow.base import QuteWindowMixin
from qutewindow.platforms.windows.native_event import _nativeEvent
from qutewindow.platforms.windows.title_bar.TitleBar import TitleBar
from qutewindow.platforms.windows.utils import addShadowEffect, addWindowAnimation, setWindowNonResizable, \
    isWindowResizable


class QuteMainWindow(QuteWindowMixin, QMainWindow):
    """
    Windows-specific frameless main window implementation.
    
    This class provides a frameless main window for Windows with native styling and
    window management integration. It extends QMainWindow to support menus,
    toolbars, status bars, and central widgets while maintaining a frameless
    appearance with custom title bar.
    
    The window automatically handles:
    - Native window shadows and animations
    - Proper window layering and z-ordering
    - Integration with Windows window management features
    - Custom title bar with window controls (close, minimize, maximize)
    - QMainWindow features (menus, toolbars, dock widgets, etc.)
    - Native event handling for window operations
    
    Attributes:
        _title_bar (TitleBar): The custom title bar widget.
    
    Example:
        >>> main_window = QuteMainWindow()
        >>> main_window.setWindowTitle("My Application")
        >>> main_window.setCentralWidget(QWidget())
        >>> main_window.show()
    """
    
    def __init__(self, parent: Optional[QWidget] = None) -> None:
        """
        Initialize the Windows QuteMainWindow.
        
        Args:
            parent (Optional[QWidget]): The parent widget, defaults to None.
        """
        super().__init__(parent)

        self._title_bar = TitleBar(self)
        addShadowEffect(self.winId())
        addWindowAnimation(self.winId())
        self.resize(800, 800)

    def setNonResizable(self):
        """
        Make the window non-resizable.
        
        This method disables window resizing functionality by modifying the
        window style and hiding the maximize button from the title bar.
        """
        setWindowNonResizable(self.winId())
        # Hide maximize button if it exists on the title bar
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
