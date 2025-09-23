"""
QuteWindow - Cross-platform frameless window library for Python and Qt.

This package provides a unified interface for creating frameless windows
with native window controls and behaviors across different platforms.
"""

from .platforms import QuteDialog, QuteMainWindow, QuteWindow, TitleBar

__version__ = "0.2.0"
__author__ = "Parham Oyan"
__email__ = "parhamoyan@yahoo.com"
__license__ = "MIT"

__all__ = ["QuteWindow", "QuteMainWindow", "QuteDialog", "TitleBar"]
