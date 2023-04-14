from ctypes import c_void_p
from functools import reduce

import Quartz
from AppKit import (NSView, NSMakeRect, NSWindow, NSWindowCloseButton, NSWindowMiniaturizeButton, NSWindowZoomButton)
from Quartz.CoreGraphics import (CGEventCreateMouseEvent,
                                 kCGEventLeftMouseDown, kCGMouseButtonLeft)
import Cocoa
import objc
from PySide6.QtCore import QPoint, QSize
from PySide6.QtWidgets import QWidget


def merge_content_area_and_title_bar(win_id: int) -> None:
    viewPtr = c_void_p(win_id)
    nsview = objc.objc_object(c_void_p=viewPtr)

    nswin = nsview.window()

    styleMasks = (
        nswin.styleMask(),
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


def setWindowNonResizable(win_id: int) -> None:
    viewPtr = c_void_p(win_id)
    nsview = objc.objc_object(c_void_p=viewPtr)

    nswin = nsview.window()

    styleMasks = nswin.styleMask()
    styleMasks &= ~Cocoa.NSWindowStyleMaskResizable
    nswin.setStyleMask_(styleMasks)

    nswin.standardWindowButton_(Cocoa.NSWindowZoomButton).setEnabled_(False)

def startSystemMove(widget: QWidget, pos: QPoint):
    viewPtr = c_void_p(widget.winId())
    nsview = objc.objc_object(c_void_p=viewPtr)

    nswin = nsview.window()

    cgEvent = CGEventCreateMouseEvent(None, kCGEventLeftMouseDown, pos.toTuple(), kCGMouseButtonLeft)
    clickEvent = Cocoa.NSEvent.eventWithCGEvent_(cgEvent)

    if not clickEvent:
        return
    nswin.performWindowDragWithEvent_(clickEvent)

def isWindowResizable(hwnd):
    viewPtr = c_void_p(hwnd)
    nsview = objc.objc_object(c_void_p=viewPtr)

    nswin = nsview.window()
    style_mask = nswin.styleMask()
    return style_mask & Cocoa.NSWindowStyleMaskResizable == Cocoa.NSWindowStyleMaskResizable
