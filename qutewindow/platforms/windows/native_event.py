import ctypes
from ctypes.wintypes import POINT

import win32con
from PySide6.QtCore import QByteArray, QPoint, Qt, QEvent
from PySide6.QtGui import QMouseEvent
from PySide6.QtWidgets import QWidget, QPushButton, QApplication

from qutewindow.platforms.windows.c_structures import LPNCCALCSIZE_PARAMS
from qutewindow.platforms.windows.title_bar.TitleBar import MaximizeButtonState
from qutewindow.platforms.windows.utils import isMaximized, isFullScreen


def _nativeEvent(widget: QWidget, event_type: QByteArray, message: int):
    msg = ctypes.wintypes.MSG.from_address(message.__int__())

    pt = POINT()
    ctypes.windll.user32.GetCursorPos(ctypes.byref(pt))
    r = widget.devicePixelRatioF()
    x = pt.x / r - widget.x()
    y = pt.y / r - widget.y()

    user32 = ctypes.windll.user32
    dpi = user32.GetDpiForWindow(msg.hWnd)
    borderWidth = user32.GetSystemMetricsForDpi(win32con.SM_CXSIZEFRAME, dpi) + user32.GetSystemMetricsForDpi(92, dpi)
    borderHeight = user32.GetSystemMetricsForDpi(win32con.SM_CYSIZEFRAME, dpi) + user32.GetSystemMetricsForDpi(92, dpi)

    if msg.message == win32con.WM_NCHITTEST:
        if widget.isResizable():
            w, h = widget.width(), widget.height()
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

        if widget.childAt(QPoint(x, y)) is widget.title_bar.maximize_button:
            widget.title_bar.maximize_button.setState(MaximizeButtonState.HOVER)
            return True, win32con.HTMAXBUTTON

        if widget.childAt(x, y) not in widget.title_bar.findChildren(QPushButton):
            if borderHeight < y < widget.title_bar.height():
                return True, win32con.HTCAPTION

    elif msg.message in [0x2A2, win32con.WM_MOUSELEAVE]:
        widget.title_bar.maximize_button.setState(MaximizeButtonState.NORMAL)
    elif msg.message in [win32con.WM_NCLBUTTONDOWN, win32con.WM_NCLBUTTONDBLCLK]:
        if widget.childAt(QPoint(x, y)) is widget.title_bar.maximize_button:
            QApplication.sendEvent(widget.title_bar.maximize_button, QMouseEvent(
                QEvent.MouseButtonPress, QPoint(), Qt.LeftButton, Qt.LeftButton, Qt.NoModifier))
            return True, 0
    elif msg.message in [win32con.WM_NCLBUTTONUP, win32con.WM_NCRBUTTONUP]:
        if widget.childAt(QPoint(x, y)) is widget.title_bar.maximize_button:
            QApplication.sendEvent(widget.title_bar.maximize_button, QMouseEvent(
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
