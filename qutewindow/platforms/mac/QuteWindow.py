from typing import Optional

from AppKit import NSView, NSMakeRect, NSWindow, NSWindowCloseButton, NSWindowMiniaturizeButton, NSWindowZoomButton

from ctypes import c_void_p
from functools import reduce
import Cocoa
import objc

from PySide6.QtCore import Qt, QPoint, QSize
from PySide6.QtGui import QMouseEvent, QColor, QPalette
from PySide6.QtWidgets import QWidget, QHBoxLayout


class QuteWindow(QWidget):
    def __init__(self, parent: Optional[QWidget] = None) -> None:
        QWidget.__init__(self, parent)
        self.setWindowFlags(Qt.Window)
        self.setAttribute(Qt.WA_TranslucentBackground)
        QuteWindow.merge_content_area_and_title_bar(self.winId())
        QuteWindow.setTrafficLightsPosition(self.winId(), QPoint(0, 0))

    @staticmethod
    def merge_content_area_and_title_bar(win_id: int) -> None:
        viewPtr = c_void_p(win_id)
        nsview = objc.objc_object(c_void_p=viewPtr)

        # get NSView's NSWindow for styling
        nswin = nsview.window()

        # set frameless but enable buttons
        styleMasks = (
            nswin.styleMask(),  # retain default flags
            Cocoa.NSWindowStyleMaskFullSizeContentView,
            Cocoa.NSWindowTitleHidden,
            Cocoa.NSWindowStyleMaskClosable,
            Cocoa.NSWindowStyleMaskMiniaturizable,
            Cocoa.NSWindowStyleMaskResizable,
            Cocoa.NSWindowStyleMaskFullSizeContentView
        )
        nswin.setStyleMask_(reduce(lambda a, b: a | b, styleMasks, 0))

        nswin.setTitlebarAppearsTransparent_(True)
        nswin.setMovableByWindowBackground_(False)

    @staticmethod
    def setTrafficLightsPosition(win_id: int, pos = QPoint(0, 0)) -> None:
        viewPtr = c_void_p(win_id)
        nsview = objc.objc_object(c_void_p=viewPtr)
        window = nsview.window()

        box_size = QSize(72, 30)

        # Create an instance of NSView
        trafficLightsView = NSView.alloc().initWithFrame_(NSMakeRect(pos.x(), pos.y(), box_size.width(), box_size.height()))

        # Add the trafficLightsView as a subview of the window's contentView
        window.contentView().addSubview_(trafficLightsView)

        # Get the standard window buttons
        closeButton = window.standardWindowButton_(NSWindowCloseButton)
        minimizeButton = window.standardWindowButton_(NSWindowMiniaturizeButton)
        maximizeButton = window.standardWindowButton_(NSWindowZoomButton)

        # Add the buttons as subviews of the trafficLightsView
        trafficLightsView.addSubview_(closeButton)
        trafficLightsView.addSubview_(minimizeButton)
        trafficLightsView.addSubview_(maximizeButton)

    def mouseDoubleClickEvent(self, event: QMouseEvent) -> None:
        if not self.isFullScreen() and self.isTitleBarArea(event.pos()):
            self.toggleMaximized()

    def isTitleBarArea(self, pos: QPoint) -> bool:
        title_bar_height = self.titleBarHeight()
        return pos.y() <= title_bar_height

    def titleBarHeight(self) -> int:
        return 30

    def toggleMaximized(self) -> None:
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()
