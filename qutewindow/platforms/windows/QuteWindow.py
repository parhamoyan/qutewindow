import ctypes
from ctypes.wintypes import POINT, LPRECT
from enum import Enum
from typing import Optional

import win32api
import win32con
import win32gui
from PySide6.QtCore import Qt, Slot, QByteArray, QPoint, QEvent
from PySide6.QtGui import QCursor, QMouseEvent
from PySide6.QtWidgets import QDialog, QWidget, QPushButton, QVBoxLayout, QApplication

from ctypes import c_int, cdll, byref

from Icon import Icon
from qutewindow.platforms.windows.c_structures import LPNCCALCSIZE_PARAMS, MARGINS
from qutewindow.platforms.windows.title_bar.TitleBar import TitleBar, MaximizeButtonState


class MaximizeButtonIcon(str, Enum):
    RESTORE = "restore"
    MAXIMIZE = "maximize"


class QuteWindow(QWidget):
    def __init__(self, parent: Optional[QWidget] = None):
        super(QuteWindow, self).__init__(parent)
        self.setWindowFlags(Qt.WindowType.Window)
        self.setStyleSheet("background-color: #333333;")

        style = win32gui.GetWindowLong(int(self.winId()), win32con.GWL_STYLE)
        win32gui.SetWindowLong(int(self.winId()), win32con.GWL_STYLE,
                               style | win32con.WS_THICKFRAME)

        self.addShadowEffect(self.winId())

        self.BORDER_WIDTH = 10

        self.title_bar = TitleBar(self)
        self.title_bar.minimize_button.clicked.connect(self.on_minimize_button_clicked)
        self.title_bar.maximize_button.clicked.connect(self.on_maximize_button_clicked)
        self.title_bar.close_button.clicked.connect(self.on_close_button_clicked)

        self.resize(800, 800)
        self.title_bar.raise_()

    @staticmethod
    def addShadowEffect(hWnd):
        hWnd = int(hWnd)
        margins = MARGINS(-1, -1, -1, -1)
        dwmapi = cdll.LoadLibrary("dwmapi")
        dwmapi.DwmExtendFrameIntoClientArea(hWnd, byref(margins))

    def nativeEvent(self, event_type: QByteArray, message: int):
        retval, result = super().nativeEvent(event_type, message)
        msg = ctypes.wintypes.MSG.from_address(message.__int__())
        if not msg.hWnd:
            return super().nativeEvent(event_type, message)

        pt = POINT()
        ctypes.windll.user32.GetCursorPos(ctypes.byref(pt))
        r = self.devicePixelRatioF()
        x = pt.x - self.x() * r
        y = pt.y - self.y() * r

        pt = POINT()
        ctypes.windll.user32.GetCursorPos(ctypes.byref(pt))
        r = self.devicePixelRatioF()
        x = pt.x / r - self.x()
        y = pt.y / r - self.y()

        if msg.message == win32con.WM_NCHITTEST:
            w, h = self.width(), self.height()
            lx = x < self.BORDER_WIDTH
            rx = x > w - 2 * self.BORDER_WIDTH
            ty = y < self.BORDER_WIDTH
            by = y > h - self.BORDER_WIDTH

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
                if self.BORDER_WIDTH < y < self.title_bar.height():
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

            isMax = self._isMaximized(msg.hWnd)
            isFull = self._isFullScreen(msg.hWnd)

            user32 = ctypes.windll.user32
            dpi = user32.GetDpiForWindow(msg.hWnd)
            borderWidth = user32.GetSystemMetricsForDpi(win32con.SM_CXSIZEFRAME, dpi) + user32.GetSystemMetricsForDpi(
                92, dpi)
            borderHeight = user32.GetSystemMetricsForDpi(win32con.SM_CYSIZEFRAME, dpi) + user32.GetSystemMetricsForDpi(
                92, dpi)

            # adjust the size of client rect
            if isMax and not isFull:
                rect.top += borderHeight
                rect.left += borderWidth
                rect.right -= borderWidth
                rect.bottom -= borderHeight

            result = 0 if not msg.wParam else win32con.WVR_REDRAW
            return True, result

        return super().nativeEvent(event_type, message)

    def _isMaximized(self, hWnd) -> bool:
        windowPlacement = win32gui.GetWindowPlacement(hWnd)
        if not windowPlacement:
            return False

        return windowPlacement[1] == win32con.SW_MAXIMIZE

    def _isFullScreen(self, hWnd) -> bool:
        hWnd = int(hWnd)
        winRect = win32gui.GetWindowRect(hWnd)
        if not winRect:
            return False

        monitor = win32api.MonitorFromWindow(hWnd, win32con.MONITOR_DEFAULTTOPRIMARY)
        monitorInfo = win32api.GetMonitorInfo(monitor)
        if not monitorInfo:
            return False

        monitorRect = monitorInfo["Monitor"]
        return all(i == j for i, j in zip(winRect, monitorRect))

    def resizeEvent(self, e):
        super().resizeEvent(e)
        if hasattr(self, "title_bar"):
            self.title_bar.resize(self.width(), self.title_bar.height())

    def on_close_button_clicked(self) -> None:
        self.close()

    def on_minimize_button_clicked(self) -> None:
        self.showMinimized()

    def set_maximize_button_icon(self, icon) -> None:
        if icon == MaximizeButtonIcon.MAXIMIZE:
            self.title_bar.maximize_button.setIcon(Icon(u":/icons/title-bar/maximize.png"))
        elif icon == MaximizeButtonIcon.RESTORE:
            self.title_bar.maximize_button.setIcon(Icon(u":/icons/title-bar/restore.png"))

    def on_maximize_button_clicked(self):
        status = self.isMaximized()
        if status:
            self.showNormal()
            self.set_maximize_button_icon(MaximizeButtonIcon.MAXIMIZE)
        else:
            self.showMaximized()
            self.set_maximize_button_icon(MaximizeButtonIcon.RESTORE)

    def changeEvent(self, event: QEvent) -> None:
        if event.type() == QEvent.Type.WindowStateChange:
            status = self.isMaximized()
            if not status:
                self.set_maximize_button_icon(MaximizeButtonIcon.MAXIMIZE)
            else:
                self.set_maximize_button_icon(MaximizeButtonIcon.RESTORE)
        super(QuteWindow, self).changeEvent(event)
