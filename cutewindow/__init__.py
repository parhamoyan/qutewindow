"""
CuteWindow - Cross-platform window library for Python and Qt with enhanced control
and customization.

This package provides a unified interface for creating customizable windows
with native window controls and behaviors across different platforms.
"""

from .platforms import CuteDialog, CuteMainWindow, CuteWindow, TitleBar

__version__ = "0.1.0"
__author__ = "Parham Oyan"
__email__ = "parhamoyan@yahoo.com"
__license__ = "MIT"

__all__ = ["CuteWindow", "CuteMainWindow", "CuteDialog", "TitleBar"]
