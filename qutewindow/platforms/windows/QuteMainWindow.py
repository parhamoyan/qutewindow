import ctypes
from ctypes.wintypes import POINT
from typing import Optional

import win32con
import win32gui
from PySide6.QtCore import Qt, QEvent, QPoint, QByteArray
from PySide6.QtGui import QMouseEvent
from PySide6.QtWidgets import QWidget, QMainWindow, QApplication, QPushButton

from qutewindow.platforms.windows.c_structures import LPNCCALCSIZE_PARAMS
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
        msg = ctypes.wintypes.MSG.from_address(message.__int__())
        if not msg.hWnd:
            return super().nativeEvent(event_type, message)

        pt = POINT()
        ctypes.windll.user32.GetCursorPos(ctypes.byref(pt))
        r = self.devicePixelRatioF()
        x = pt.x - self.x()
        y = pt.y - self.y()

        user32 = ctypes.windll.user32
        dpi = user32.GetDpiForWindow(msg.hWnd)
        borderWidth = user32.GetSystemMetricsForDpi(win32con.SM_CXSIZEFRAME, dpi) + user32.GetSystemMetricsForDpi(
            92, dpi)
        borderHeight = user32.GetSystemMetricsForDpi(win32con.SM_CYSIZEFRAME, dpi) + user32.GetSystemMetricsForDpi(
            92, dpi)

        if msg.message == win32con.WM_NCHITTEST:
            w, h = self.width(), self.height()
            lx = x < borderWidth
            rx = x > w - 2 * borderWidth
            ty = y < borderHeight
            by = y > h - borderHeight

            if lx and ty:
                return True, win32con.HTTOPLEFT
            if rx and by:
                return True, win32con.HTBOTTOMRIGHT
            if rx and ty:
                return True, win32con.HTTOPRIGHT
            if lx and by:
                return True, win32con.HTBOTTOMLEFT
            if ty:
                return True, win32con.HTTOP
            if by:
                return True, win32con.HTBOTTOM
            if lx:
                return True, win32con.HTLEFT
            if rx:
                return True, win32con.HTRIGHT
            elif self.childAt(QPoint(x, y)) is self.title_bar.maximize_button:
                self.title_bar.maximize_button.setState(MaximizeButtonState.HOVER)
                return True, win32con.HTMAXBUTTON

            if self.childAt(x, y) not in self.title_bar.findChildren(QPushButton):
                if borderHeight < y < self.title_bar.height():
                    return True, win32con.HTCAPTION

        elif msg.message in [0x2A2, win32con.WM_MOUSELEAVE]:
            self.title_bar.maximize_button.setState(MaximizeButtonState.NORMAL)
        elif msg.message in [win32con.WM_NCLBUTTONDOWN, win32con.WM_NCLBUTTONDBLCLK]:
            if self.childAt(QPoint(x, y)) is self.title_bar.maximize_button:
                QApplication.sendEvent(self.title_bar.maximize_button, QMouseEvent(
                    QEvent.MouseButtonPress, QPoint(), Qt.LeftButton, Qt.LeftButton, Qt.NoModifier))
                return True, 0
        elif msg.message in [win32con.WM_NCLBUTTONUP, win32con.WM_NCRBUTTONUP]:
            if self.childAt(QPoint(x, y)) is self.title_bar.maximize_button:
                QApplication.sendEvent(self.title_bar.maximize_button, QMouseEvent(
                    QEvent.MouseButtonRelease, QPoint(), Qt.LeftButton, Qt.LeftButton, Qt.NoModifier))

        elif msg.message == win32con.WM_NCCALCSIZE:
            rect = ctypes.cast(msg.lParam, LPNCCALCSIZE_PARAMS).contents.rgrc[0]

            isMax = isMaximized(msg.hWnd)
            isFull = isFullScreen(msg.hWnd)

            # adjust the size of client rect
            if isMax and not isFull:
                rect.top += borderHeight
                rect.left += borderWidth
                rect.right -= borderWidth
                rect.bottom -= borderHeight

            return True, win32con.WVR_REDRAW

        return super().nativeEvent(event_type, message)

    def resizeEvent(self, e):
        super().resizeEvent(e)
        if hasattr(self, "title_bar"):
            self.title_bar.resize(self.width(), self.title_bar.height())