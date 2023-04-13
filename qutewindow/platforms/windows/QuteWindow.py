from typing import Optional

from PySide6.QtCore import Qt, QByteArray
from PySide6.QtGui import QShowEvent
from PySide6.QtWidgets import QWidget

from qutewindow.platforms.windows.native_event import _nativeEvent
from qutewindow.platforms.windows.title_bar.TitleBar import TitleBar
from qutewindow.platforms.windows.utils import addShadowEffect, addWindowAnimation, setWindowNonResizable, \
    isWindowResizable


class QuteWindow(QWidget):
    def __init__(self, parent: Optional[QWidget] = None):
        super(QuteWindow, self).__init__(parent)
        self.setWindowFlags(Qt.WindowType.Window | Qt.FramelessWindowHint)

        addShadowEffect(self.winId())
        addWindowAnimation(self.winId())

        self.title_bar = TitleBar(self)

        self.resize(800, 800)

    def setNonResizable(self):
        setWindowNonResizable(self.winId())
        self.title_bar.maximize_button.hide()

    def isResizable(self) -> None:
        return isWindowResizable(self.winId())

    def showEvent(self, event: QShowEvent) -> None:
        self.title_bar.raise_()
        super(QuteWindow, self).showEvent(event)

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
