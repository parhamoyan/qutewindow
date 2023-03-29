import ctypes
from ctypes.wintypes import POINT
from typing import Optional

import win32con
import win32gui
from PySide6.QtCore import Qt, QEvent, QPoint, QByteArray
from PySide6.QtGui import QMouseEvent
from PySide6.QtWidgets import QWidget, QMainWindow, QApplication, QPushButton

from qutewindow.platforms.windows.c_structures import LPNCCALCSIZE_PARAMS
from qutewindow.platforms.windows.native_event import _nativeEvent
from qutewindow.platforms.windows.title_bar.TitleBar import MaximizeButtonState, TitleBar
from qutewindow.platforms.windows.utils import isMaximized, isFullScreen, addShadowEffect, addWindowAnimation


class QuteMainWindow(QMainWindow):
    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super().__init__(parent)
        self.setWindowFlags(Qt.WindowType.Window | Qt.FramelessWindowHint)
        self.setStyleSheet("background-color: #333333;")

        addShadowEffect(self.winId())
        addWindowAnimation(self.winId())

        self.title_bar = TitleBar(self)

        self.resize(800, 800)
        self.title_bar.raise_()

    def nativeEvent(self, event_type: QByteArray, message: int):
        ret_tuple = _nativeEvent(self, event_type, message)
        if ret_tuple is not None:
            ret, value = ret_tuple
            if ret:
                return ret, value
        super().nativeEvent(event_type, message)

    def resizeEvent(self, e):
        super().resizeEvent(e)
        if hasattr(self, "title_bar"):
            self.title_bar.resize(self.width(), self.title_bar.height())