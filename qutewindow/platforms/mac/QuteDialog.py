from typing import Optional

from PySide6.QtCore import Qt
from PySide6.QtGui import QResizeEvent, QShowEvent
from PySide6.QtWidgets import QWidget, QDialog

from qutewindow.platforms.mac.title_bar.TitleBar import TitleBar
from qutewindow.platforms.mac.utils import merge_content_area_and_title_bar, setWindowNonResizable, isWindowResizable


class QuteDialog(QDialog):
    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super().__init__(parent)
        self.createWinId()
        merge_content_area_and_title_bar(self.winId())
        self.resize(800, 800)
        self._title_bar = TitleBar(self)

    def titleBar(self) -> QWidget:
        return self._title_bar

    def setTitleBar(self, titleBar: QWidget) -> None:
        self._title_bar = titleBar
        self.update()

    def setNonResizable(self) -> None:
        setWindowNonResizable(self.winId())

    def isResizable(self) -> None:
        return isWindowResizable(self.winId())

    def showEvent(self, event: QShowEvent) -> None:
        self._title_bar.raise_()
        super().showEvent(event)

    def resizeEvent(self, e: QResizeEvent) -> None:
        super().resizeEvent(e)
        self.titleBar().resize(self.width(), self.titleBar().height())
