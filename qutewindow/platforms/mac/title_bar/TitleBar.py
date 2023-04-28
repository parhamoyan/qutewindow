from typing import Optional
from typing import Optional

from PySide6.QtGui import QMouseEvent
from PySide6.QtWidgets import QWidget, QFrame

from qutewindow.platforms.mac.utils import startSystemMove, isWindowResizable


class TitleBar(QFrame):
    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super(TitleBar, self).__init__(parent)
        self.setObjectName("TitleBar")
        self.setFixedHeight(28)
        self.window().installEventFilter(self)

    def mouseMoveEvent(self, event: QMouseEvent) -> None:
        startSystemMove(self.window(), event.globalPos())

    def mouseDoubleClickEvent(self, event: QMouseEvent) -> None:
        if not self.window().isFullScreen() and isWindowResizable(self.winId()):
            if self.window().isMaximized():
                self.window().showNormal()
            else:
                self.window().showMaximized()

