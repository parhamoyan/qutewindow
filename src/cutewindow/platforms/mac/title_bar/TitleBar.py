"""
macOS-specific TitleBar implementation.

This module provides the macOS-specific implementation of the TitleBar class,
which creates a native-looking title bar for customizable windows on macOS.
Unlike the Windows version, the macOS title bar is minimal and relies on
macOS's native window controls and behavior.
"""

from typing import Optional

from PySide6.QtGui import QMouseEvent
from PySide6.QtWidgets import QFrame, QWidget

from cutewindow.platforms.mac.utils import isWindowResizable, startSystemMove


class TitleBar(QFrame):
    """
    macOS-specific title bar implementation.

    This class provides a minimal title bar for macOS customizable windows.
    On macOS, the title bar primarily serves as a drag area for window movement
    and handles double-click events for window maximization/restoration.

    The macOS title bar is intentionally minimal because:
    - macOS provides native window controls (close, minimize, maximize)
    - Native controls are automatically positioned and styled by the system
    - Custom controls would break the native macOS user experience

    Features:
    - Window dragging by clicking and dragging on the title bar
    - Double-click to maximize/restore window (if resizable)
    - Automatic integration with macOS window management
    - Proper event filtering for window state changes

    Attributes:
        None (minimal implementation with no custom widgets)

    Example:
        >>> title_bar = TitleBar(parent=window)
        >>> window.setTitleBar(title_bar)
    """

    def __init__(self, parent: Optional[QWidget] = None) -> None:
        """
        Initialize the macOS TitleBar.

        Args:
            parent (Optional[QWidget]): The parent widget (usually the window),
                                       defaults to None.
        """
        super(TitleBar, self).__init__(parent)

        # Set object name for styling purposes
        self.setObjectName("TitleBar")

        # Set standard title bar height (matches macOS title bar height)
        self.setFixedHeight(28)

        # Install event filter to monitor window state changes
        # This allows the title bar to respond to window events
        self.window().installEventFilter(self)

    def mouseMoveEvent(self, event: QMouseEvent) -> None:
        """
        Handle mouse move events for window dragging.

        This method enables window dragging when the user clicks and drags
        on the title bar area. It uses the native macOS system move function
        to provide smooth, native-feeling window movement.

        Args:
            event (QMouseEvent): The mouse move event object.
        """
        # Start system move operation with the current mouse position
        startSystemMove(self.window(), event.globalPos())

    def mouseDoubleClickEvent(self, event: QMouseEvent) -> None:
        """
        Handle mouse double-click events for window maximization.

        This method implements the standard macOS behavior of double-clicking
        the title bar to maximize or restore the window. The behavior only
        applies if the window is resizable and not in fullscreen mode.

        Args:
            event (QMouseEvent): The mouse double-click event object.
        """
        # Only handle double-click if window is not fullscreen and is resizable
        if not self.window().isFullScreen() and isWindowResizable(self.winId()):
            if self.window().isMaximized():
                # If window is maximized, restore it to normal size
                self.window().showNormal()
            else:
                # If window is normal size, maximize it
                self.window().showMaximized()
