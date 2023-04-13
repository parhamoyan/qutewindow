from ctypes import cdll, byref

import win32api
import win32con
import win32gui
from PySide6.QtCore import QPoint
from PySide6.QtWidgets import QWidget

from qutewindow.platforms.windows.c_structures import MARGINS


def addShadowEffect(hWnd):
    hWnd = int(hWnd)
    margins = MARGINS(-1, -1, -1, -1)
    dwmapi = cdll.LoadLibrary("dwmapi")
    dwmapi.DwmExtendFrameIntoClientArea(hWnd, byref(margins))


def addWindowAnimation(hWnd):
    hWnd = int(hWnd)
    style = win32gui.GetWindowLong(hWnd, win32con.GWL_STYLE)
    win32gui.SetWindowLong(
        hWnd,
        win32con.GWL_STYLE,
        style
        | win32con.WS_MINIMIZEBOX
        | win32con.WS_MAXIMIZEBOX
        | win32con.WS_CAPTION
        | win32con.CS_DBLCLKS
        | win32con.WS_THICKFRAME,
    )


def setWindowNonResizable(hwnd):
    style = win32gui.GetWindowLong(hwnd, win32con.GWL_STYLE)
    style &= ~win32con.WS_SIZEBOX
    style &= ~win32con.WS_THICKFRAME
    style &= ~win32con.WS_MAXIMIZEBOX
    win32gui.SetWindowLong(hwnd, win32con.GWL_STYLE, style)


def isWindowResizable(hwnd):
    style = win32api.GetWindowLong(hwnd, win32con.GWL_STYLE)
    return style & win32con.WS_SIZEBOX != 0


def isMaximized(hWnd) -> bool:
    windowPlacement = win32gui.GetWindowPlacement(hWnd)
    if not windowPlacement:
        return False

    return windowPlacement[1] == win32con.SW_MAXIMIZE


def isFullScreen(hWnd) -> bool:
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


def startSystemMove(widget: QWidget, pos: QPoint) -> None:
    win32gui.ReleaseCapture()
    win32api.SendMessage(
        int(widget.winId()),
        win32con.WM_SYSCOMMAND,
        win32con.SC_MOVE | win32con.HTCAPTION,
        0
    )
