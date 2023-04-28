from typing import Optional

from PySide6.QtCore import Qt
from PySide6.QtGui import QResizeEvent
from PySide6.QtWidgets import QMainWindow, QWidget

from qutewindow.platforms.mac.title_bar.TitleBar import TitleBar
from qutewindow.platforms.mac.utils import isWindowResizable
from qutewindow.platforms.mac.utils import merge_content_area_and_title_bar, setWindowNonResizable


class QuteMainWindow(QMainWindow):
    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super().__init__(parent)
        self.setWindowFlags(Qt.Window)
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

    def resizeEvent(self, e: QResizeEvent) -> None:
        super().resizeEvent(e)
        self.title_bar.resize(self.width(), self.title_bar.height())
