from typing import Optional

from PySide6.QtGui import Qt
from PySide6.QtWidgets import QWidget

from qutewindow.base import QuteWindowMixin
from qutewindow.platforms.mac.title_bar.TitleBar import TitleBar


class QuteWindow(QuteWindowMixin, QWidget):
    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super().__init__(parent)
        self.setWindowFlag(Qt.WindowType.NoTitleBarBackgroundHint | Qt.WindowType.ExpandedClientAreaHint)
        self.resize(800, 800)
        self._title_bar = TitleBar(self)
