"""
Base classes and interfaces for CuteWindow components.

This module provides the abstract base classes that define the common interface
for all platform-specific implementations, as well as concrete base classes
to prevent code duplication. The architecture follows a mixin pattern to share
common functionality across different window types while maintaining platform
specificity.
"""

from abc import abstractmethod
from typing import Optional

from PySide6.QtGui import QResizeEvent, QShowEvent
from PySide6.QtWidgets import QWidget


class BaseCuteWindow(QWidget):
    """
    Abstract base class for all CuteWindow implementations.

    This class defines the common interface that all platform-specific CuteWindow
    implementations must follow. It provides the contract for window management
    functionality including title bar handling, resizing, and platform-specific setup.

    Attributes:
        _title_bar (Optional[QWidget]): The title bar widget instance.
    """

    def __init__(self, parent: Optional[QWidget] = None) -> None:
        """
        Initialize the base CuteWindow.

        Args:
            parent (Optional[QWidget]): The parent widget, defaults to None.
        """
        super().__init__(parent)
        self._title_bar: Optional[QWidget] = None
        self._setup_window()

    @abstractmethod
    def _setup_window(self) -> None:
        """
        Platform-specific window setup.

        This method must be implemented by subclasses to perform platform-specific
        window initialization such as setting window flags, applying native styling,
        and configuring platform-specific behaviors.

        Raises:
            NotImplementedError: If not implemented by subclass.
        """
        pass

    @abstractmethod
    def titleBar(self) -> QWidget:
        """Get the title bar widget."""
        pass

    @abstractmethod
    def setTitleBar(self, title_bar: QWidget) -> None:
        """Set a custom title bar widget."""
        pass

    @abstractmethod
    def setNonResizable(self) -> None:
        """Make the window non-resizable."""
        pass

    @abstractmethod
    def isResizable(self) -> bool:
        """Check if the window is resizable."""
        pass


class BaseTitleBar(QWidget):
    """
    Abstract base class for all TitleBar implementations.

    This class defines the common interface for platform-specific title bar
    implementations. It provides standard title bar dimensions and setup patterns
    while allowing platform-specific customization.

    Attributes:
        DEFAULT_HEIGHT (int): The default height for title bars (28 pixels).
    """

    DEFAULT_HEIGHT = 28

    def __init__(self, parent: Optional[QWidget] = None) -> None:
        """
        Initialize the base title bar.

        Args:
            parent (Optional[QWidget]): The parent widget, defaults to None.
        """
        super().__init__(parent)
        self.setObjectName("TitleBar")
        self.setFixedHeight(self.DEFAULT_HEIGHT)
        self._setup_title_bar()

    @abstractmethod
    def _setup_title_bar(self) -> None:
        """
        Platform-specific title bar setup.

        This method must be implemented by subclasses to create and configure
        platform-specific title bar elements such as window controls, icons,
        and event handlers.

        Raises:
            NotImplementedError: If not implemented by subclass.
        """
        pass


class CuteWindowMixin:
    """
    Mixin class containing common functionality for CuteWindow implementations.

    This mixin provides shared functionality for all CuteWindow implementations,
    including title bar management, event handling, and window state management.
    It eliminates code duplication across different window types and platforms.

    Note:
        This mixin is designed to be used with QWidget subclasses that provide
        the standard Qt widget interface including update(), showEvent(),
        resizeEvent(), width(), and winId() methods.

    Attributes:
        _title_bar (Optional[QWidget]): The title bar widget instance.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize the CuteWindow mixin.

        Args:
            *args: Variable length argument list passed to parent class.
            **kwargs: Arbitrary keyword arguments passed to parent class.
        """
        super().__init__(*args, **kwargs)
        self._title_bar: Optional[QWidget] = None

    def titleBar(self) -> QWidget:
        """
        Get the title bar widget.

        Returns:
            QWidget: The title bar widget instance.

        Raises:
            RuntimeError: If the title bar has not been initialized.
        """
        if self._title_bar is None:
            raise RuntimeError("Title bar not initialized")
        return self._title_bar

    def setTitleBar(self, title_bar: QWidget) -> None:
        """Set a custom title bar widget."""
        self._title_bar = title_bar
        if hasattr(self, "update"):
            self.update()  # type: ignore

    def showEvent(self, event: QShowEvent) -> None:
        """Handle show event to raise title bar."""
        if hasattr(self, "_title_bar") and self._title_bar:
            self._title_bar.raise_()
        if hasattr(super(), "showEvent"):
            super().showEvent(event)  # type: ignore

    def resizeEvent(self, event: QResizeEvent) -> None:
        """Handle resize event to adjust title bar size."""
        if hasattr(super(), "resizeEvent"):
            super().resizeEvent(event)  # type: ignore
        if hasattr(self, "_title_bar") and self._title_bar and hasattr(self, "width"):
            self._title_bar.resize(
                self.width(), self._title_bar.height()  # type: ignore
            )

    def setNonResizable(self) -> None:
        """Make the window non-resizable."""
        if hasattr(self, "winId"):
            from cutewindow.platforms.mac.utils import setWindowNonResizable

            setWindowNonResizable(self.winId())  # type: ignore[attr-defined]

    def isResizable(self) -> bool:
        """Check if the window is resizable."""
        if hasattr(self, "winId"):
            from cutewindow.platforms.mac.utils import isWindowResizable

            return isWindowResizable(self.winId())  # type: ignore[attr-defined]
        return False
