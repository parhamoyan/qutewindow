"""
Windows-specific CuteDialog implementation.

This module provides the Windows-specific implementation of the CuteDialog class,
which creates a customizable dialog with native Windows styling and behavior.
It extends QDialog functionality while providing a customizable title bar
and native window management integration.
"""

from typing import Optional

from PySide6.QtCore import QByteArray
from PySide6.QtWidgets import QDialog, QWidget

from cutewindow.base import CuteWindowMixin
from cutewindow.platforms.windows.native_event import _nativeEvent
from cutewindow.platforms.windows.title_bar.TitleBar import TitleBar
from cutewindow.platforms.windows.utils import (
    addShadowEffect,
    addWindowAnimation,
    isWindowResizable,
    setWindowNonResizable,
)


class CuteDialog(CuteWindowMixin, QDialog):
    """
    Windows-specific customizable dialog implementation.

    This class provides a customizable dialog for Windows with native styling and
    window management integration. It extends QDialog to support modal dialogs,
    input forms, and other dialog windows while maintaining a customizable
    appearance with custom title bar.

    The dialog automatically handles:
    - Native window shadows and animations
    - Proper window layering and z-ordering
    - Integration with Windows window management features
    - Custom title bar with window controls (close, minimize, maximize)
    - QDialog features (modal execution, result codes, etc.)
    - Native event handling for window operations

    Attributes:
        _title_bar (TitleBar): The custom title bar widget.

    Example:
        >>> dialog = CuteDialog()
        >>> dialog.setWindowTitle("Settings")
        >>> result = dialog.exec()  # Show as modal dialog
        >>> if result == QDialog.Accepted:
        ...     print("Dialog accepted")
    """

    def __init__(self, parent: Optional[QWidget] = None) -> None:
        """
        Initialize the Windows CuteDialog.

        Args:
            parent (Optional[QWidget]): The parent widget, defaults to None.
        """
        super().__init__(parent)

        self._title_bar = TitleBar(self)
        self.createWinId()
        addShadowEffect(self.winId())
        addWindowAnimation(self.winId())
        self.resize(800, 800)

    def setNonResizable(self):
        """
        Make the dialog non-resizable.

        This method disables dialog resizing functionality by modifying the
        window style and hiding the maximize button from the title bar.
        """
        setWindowNonResizable(self.winId())
        # Hide maximize button if it exists on the title bar
        if hasattr(self._title_bar, "maximize_button"):
            self._title_bar.maximize_button.hide()  # type: ignore

    def isResizable(self) -> bool:
        """
        Check if the dialog is resizable.

        Returns:
            bool: True if the dialog is resizable, False otherwise.
        """
        return isWindowResizable(self.winId())

    def nativeEvent(self, event_type: QByteArray, message: int):  # type: ignore
        """
        Handle native Windows events.

        This method processes native Windows messages to enable proper
        dialog behavior, including resizing, moving, and other system
        interactions that require native event handling.

        Args:
            event_type (QByteArray): The type of the native event.
            message (int): The native event message.

        Returns:
            Tuple[bool, int]: A tuple containing a boolean indicating if the
                             event was handled and an optional result value.
        """
        return _nativeEvent(self, event_type, message)
