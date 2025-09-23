from typing import Optional

from PySide6.QtCore import Qt, QByteArray
from PySide6.QtGui import QShowEvent
from PySide6.QtWidgets import QWidget, QDialog

from qutewindow.base import QuteWindowMixin
from qutewindow.platforms.windows.native_event import _nativeEvent
from qutewindow.platforms.windows.title_bar.TitleBar import TitleBar
from qutewindow.platforms.windows.utils import addShadowEffect, addWindowAnimation, setWindowNonResizable, \
    isWindowResizable


class QuteDialog(QuteWindowMixin, QDialog):
    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super().__init__(parent)
        self._title_bar = TitleBar(self)

        self.createWinId()

        addShadowEffect(self.winId())
        addWindowAnimation(self.winId())

        self.resize(800, 800)

    def setNonResizable(self):
        setWindowNonResizable(self.winId())
        if hasattr(self._title_bar, 'maximize_button'):
            self._title_bar.maximize_button.hide()

    def isResizable(self) -> bool:
        return isWindowResizable(self.winId())

    def nativeEvent(self, event_type: QByteArray, message: int):
        return _nativeEvent(self, event_type, message)
