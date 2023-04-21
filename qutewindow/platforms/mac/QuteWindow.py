from typing import Optional

from PySide6.QtCore import Qt, QPoint
from PySide6.QtGui import QMouseEvent
from PySide6.QtWidgets import QWidget

from qutewindow.platforms.mac.utils import merge_content_area_and_title_bar, setWindowNonResizable, startSystemMove, \
    isWindowResizable


class QuteWindow(QWidget):
    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super().__init__(parent)
        self.setWindowFlags(Qt.Window)
        merge_content_area_and_title_bar(self.winId())
        self.resize(800, 800)

    def setNonResizable(self):
        setWindowNonResizable(self.winId())

    def isResizable(self) -> None:
        return isWindowResizable(self.winId())

    def mouseDoubleClickEvent(self, event: QMouseEvent) -> None:
        if not self.isFullScreen() and self.isTitleBarArea(event.pos()) and self.isResizable():
            self.toggleMaximized()

    def mouseMoveEvent(self, event: QMouseEvent) -> None:
        if not self.isFullScreen() and self.isTitleBarArea(event.pos()):
            startSystemMove(self.window(), event.globalPos())

    def isTitleBarArea(self, pos: QPoint) -> bool:
        return pos.y() <= 30

    def toggleMaximized(self) -> None:
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()

    def mouseMoveEvent(self, event: QMouseEvent) -> None:
        if self.isTitleBarArea(event.pos()):
            startSystemMove(self.window(), event.globalPos())
