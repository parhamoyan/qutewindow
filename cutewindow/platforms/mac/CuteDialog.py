"""
macOS-specific CuteDialog implementation.

This module provides the macOS-specific implementation of the CuteDialog class,
which creates a customizable dialog with native macOS styling and behavior.
It extends QDialog functionality while providing a customizable title bar
and native window management integration.
"""

from typing import Optional

from PySide6.QtGui import Qt
from PySide6.QtWidgets import QDialog, QWidget

from cutewindow.base import CuteWindowMixin
from cutewindow.platforms.mac.title_bar.TitleBar import TitleBar


class CuteDialog(CuteWindowMixin, QDialog):
    """
    macOS-specific customizable dialog implementation.

    This class provides a customizable dialog for macOS with native styling and
    window management integration. It extends QDialog to support modal dialogs,
    input forms, and other dialog windows while maintaining a customizable
    appearance with custom title bar.

    The dialog automatically handles:
    - Native window shadows and animations
    - Proper window layering and z-ordering
    - Integration with macOS window management features
    - Custom title bar with window controls
    - QDialog features (modal execution, result codes, etc.)

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
        Initialize the macOS CuteDialog.

        Args:
            parent (Optional[QWidget]): The parent widget, defaults to None.
        """
        super().__init__(parent)

        self.createWinId()
        self.setWindowFlag(
            Qt.WindowType.NoTitleBarBackgroundHint
            | Qt.WindowType.ExpandedClientAreaHint
        )
        self.resize(800, 800)
        self._title_bar = TitleBar(self)
