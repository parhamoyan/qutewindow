import ctypes
from ctypes import wintypes
from enum import IntEnum, auto
from typing import Optional

import win32con
import win32gui

from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon, QPixmap, QImage
from PySide6.QtWidgets import QWidget, QPushButton, QFrame, QHBoxLayout, QSpacerItem, QSizePolicy, QStyleFactory, QStyle

import qutewindow.platforms.windows.title_bar.resources_rc
from Icon import Icon


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
        match state:
            case MaximizeButtonState.HOVER:
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
            case MaximizeButtonState.NORMAL:
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
