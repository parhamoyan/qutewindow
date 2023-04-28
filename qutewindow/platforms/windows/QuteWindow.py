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

        self._title_bar = TitleBar(self)

        addShadowEffect(self.winId())
        addWindowAnimation(self.winId())

        self.resize(800, 800)

    def titleBar(self) -> QWidget:
        return self._title_bar

    def setTitleBar(self, titleBar: QWidget) -> None:
        self._title_bar = titleBar
        self.update()

    def setNonResizable(self):
        setWindowNonResizable(self.winId())
        self._title_bar.maximize_button.hide()

    def isResizable(self) -> None:
        return isWindowResizable(self.winId())

    def showEvent(self, event: QShowEvent) -> None:
        self._title_bar.raise_()
        super(QuteWindow, self).showEvent(event)

    def nativeEvent(self, event_type: QByteArray, message: int):
        return _nativeEvent(self, event_type, message)

    def resizeEvent(self, e):
        super().resizeEvent(e)
        self._title_bar.resize(self.width(), self._title_bar.height())
