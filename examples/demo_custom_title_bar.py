import sys
from typing import Optional

from PySide6.QtWidgets import QApplication, QWidget

from examples.LoginDialog import LoginDialog
from cutewindow import TitleBar


class CustomTitleBar(TitleBar):
    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super().__init__(parent)
        self.setStyleSheet("background-color: gray;")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = LoginDialog()
    demo.setTitleBar(CustomTitleBar(demo))
    demo.setStyleSheet("background-color: #333333;")
    demo.show()
    sys.exit(app.exec())
