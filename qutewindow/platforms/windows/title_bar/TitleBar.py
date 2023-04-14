from enum import IntEnum, auto, Enum
from typing import Optional
from PySide6.QtCore import QSize, QEvent
from PySide6.QtGui import QMouseEvent
from PySide6.QtWidgets import QWidget, QPushButton, QFrame, QHBoxLayout, QSpacerItem, QSizePolicy

from qutewindow.Icon import Icon

# Never remove the following resources_rc import, it is used to load title bar icons
import qutewindow.platforms.windows.title_bar.resources_rc
from qutewindow.platforms.windows.utils import startSystemMove


class MaximizeButtonIcon(str, Enum):
    RESTORE = "restore"
    MAXIMIZE = "maximize"


class TitleBarButton(QPushButton):
    def __init__(self, parent: Optional[QWidget]) -> None:
        super(TitleBarButton, self).__init__(parent)
        self.setFixedSize(QSize(40, 28))
        self.setIconSize(QSize(24, 24))


class MaximizeButtonState(IntEnum):
    HOVER = auto()
    NORMAL = auto()


class MaximizeButton(TitleBarButton):
    def __init__(self, parent: Optional[QWidget]) -> None:
        super(MaximizeButton, self).__init__(parent)
        self.setStyleSheet("""
        QPushButton {
        	background-position: center;
            background-repeat: no-repeat;
        	border: none;
        	outline: none;
        	color: #d1d3d2;
        }

        QPushButton::hover {
        	background-color: #1D1D24;
        }
        """)

        self.setIcon(Icon(u":/icons/title-bar/maximize.png"))

    def setState(self, state: MaximizeButtonState) -> None:
        if state == MaximizeButtonState.HOVER:
                self.setStyleSheet("""
                    QPushButton {
                        background-position: center;
                        background-repeat: no-repeat;
                        border: none;
                        outline: none;
                        color: #d1d3d2;
                        background-color: #1D1D24;
                    }
                    """)
        elif state == MaximizeButtonState.NORMAL:
                 self.setStyleSheet("""
                    QPushButton {
                        background-position: center;
                        background-repeat: no-repeat;
                        border: none;
                        outline: none;
                        color: #d1d3d2;
                        background: transparent;
                    }
                    """)
        self.update()


class MinimizeButton(TitleBarButton):
    def __init__(self, parent: Optional[QWidget]) -> None:
        super(MinimizeButton, self).__init__(parent)
        self.setStyleSheet("""
                QPushButton {
        	background-position: center;
            background-repeat: no-repeat;
        	border: none;
        	outline: none;
        	color: #d1d3d2;
        }

        QPushButton::hover {
        	background-color: #1D1D24;
        }
        """)
        self.setIcon(Icon(u":/icons/title-bar/minimize.png"))


class CloseButton(TitleBarButton):
    def __init__(self, parent: Optional[QWidget]) -> None:
        super(CloseButton, self).__init__(parent)
        self.setStyleSheet("""
        QPushButton {
        	background-position: center;
            background-repeat: no-repeat;
        	border: none;
        	outline: none;
        	color: #d1d3d2;
        }

        QPushButton:hover {
        	background-color: #e81123;
        }""")
        self.setIcon(Icon(u":/icons/title-bar/close.png"))


class TitleBar(QFrame):
    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super(TitleBar, self).__init__(parent)
        self.setFixedHeight(28)

        self.button_box = QWidget(self)

        self.maximize_button = MaximizeButton(self.button_box)
        self.minimize_button = MinimizeButton(self.button_box)
        self.close_button = CloseButton(self.button_box)

        self.button_box_horizontalLayout = QHBoxLayout(self.button_box)
        self.button_box_horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.button_box_horizontalLayout.setSpacing(0)
        for btn in [self.minimize_button, self.maximize_button, self.close_button]:
            self.button_box_horizontalLayout.addWidget(btn)

        self.horizontalLayout = QHBoxLayout(self)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalSpacer = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addSpacerItem(self.horizontalSpacer)
        self.horizontalLayout.addWidget(self.button_box)

        self.minimize_button.clicked.connect(self.on_minimize_button_clicked)
        self.maximize_button.clicked.connect(self.on_maximize_button_clicked)
        self.close_button.clicked.connect(self.on_close_button_clicked)

        self.window().installEventFilter(self)

    def on_close_button_clicked(self) -> None:
        self.window().close()

    def on_maximize_button_clicked(self):
        status = self.topLevelWidget().isMaximized()
        if status:
            self.window().showNormal()
            self.set_maximize_button_icon(MaximizeButtonIcon.MAXIMIZE)
        else:
            self.window().showMaximized()
            self.set_maximize_button_icon(MaximizeButtonIcon.RESTORE)

    def on_minimize_button_clicked(self) -> None:
        self.window().showMinimized()

    def set_maximize_button_icon(self, icon) -> None:
        if icon == MaximizeButtonIcon.MAXIMIZE:
            self.maximize_button.setIcon(Icon(u":/icons/title-bar/maximize.png"))
        elif icon == MaximizeButtonIcon.RESTORE:
            self.maximize_button.setIcon(Icon(u":/icons/title-bar/restore.png"))

    def eventFilter(self, obj, e):
        if obj is self.window():
            if e.type() == QEvent.WindowStateChange:
                status = self.window().isMaximized()
                if not status:
                    self.set_maximize_button_icon(MaximizeButtonIcon.MAXIMIZE)
                else:
                    self.set_maximize_button_icon(MaximizeButtonIcon.RESTORE)

        return super().eventFilter(obj, e)

    def mouseMoveEvent(self, event: QMouseEvent) -> None:
        startSystemMove(self.window(), event.globalPos())
