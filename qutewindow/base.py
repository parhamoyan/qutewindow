"""
Base classes and interfaces for QuteWindow components.

This module provides the abstract base classes that define the common interface
for all platform-specific implementations, as well as concrete base classes
to prevent code duplication.
"""

from abc import ABC, abstractmethod
from typing import Optional

from PySide6.QtCore import Qt, QByteArray
from PySide6.QtGui import QResizeEvent, QShowEvent
from PySide6.QtWidgets import QWidget

from qutewindow.platforms.mac.utils import setWindowNonResizable, isWindowResizable


class BaseQuteWindow(QWidget):
    """Abstract base class for all QuteWindow implementations."""
    
    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super().__init__(parent)
        self._title_bar: Optional[QWidget] = None
        self._setup_window()
    
    @abstractmethod
    def _setup_window(self) -> None:
        """Platform-specific window setup."""
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
    """Abstract base class for all TitleBar implementations."""
    
    DEFAULT_HEIGHT = 28
    
    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super().__init__(parent)
        self.setObjectName("TitleBar")
        self.setFixedHeight(self.DEFAULT_HEIGHT)
        self._setup_title_bar()
    
    @abstractmethod
    def _setup_title_bar(self) -> None:
        """Platform-specific title bar setup."""
        pass


class QuteWindowMixin:
    """Mixin class containing common functionality for QuteWindow implementations."""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._title_bar: Optional[QWidget] = None
    
    def titleBar(self) -> QWidget:
        """Get the title bar widget."""
        if self._title_bar is None:
            raise RuntimeError("Title bar not initialized")
        return self._title_bar
    
    def setTitleBar(self, title_bar: QWidget) -> None:
        """Set a custom title bar widget."""
        self._title_bar = title_bar
        if hasattr(self, 'update'):
            self.update()
    
    def showEvent(self, event: QShowEvent) -> None:
        """Handle show event to raise title bar."""
        if hasattr(self, '_title_bar') and self._title_bar:
            self._title_bar.raise_()
        super().showEvent(event)
    
    def resizeEvent(self, event: QResizeEvent) -> None:
        """Handle resize event to adjust title bar size."""
        super().resizeEvent(event)
        if hasattr(self, '_title_bar') and self._title_bar and hasattr(self, 'width'):
            self._title_bar.resize(self.width(), self._title_bar.height())

    def setNonResizable(self) -> None:
        setWindowNonResizable(self.winId())

    def isResizable(self) -> bool:
        return isWindowResizable(self.winId())
