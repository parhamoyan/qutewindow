"""
Base classes and interfaces for QuteWindow components.

This module provides the abstract base classes that define the common interface
for all platform-specific implementations.
"""

from abc import ABC, abstractmethod
from typing import Optional

from PySide6.QtWidgets import QWidget


class BaseQuteWindow(QWidget, ABC):
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


class BaseTitleBar(QWidget, ABC):
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