from typing import Optional

from PySide6.QtWidgets import QWidget

from cutewindow import CuteDialog
from examples.Ui_LoginDialog import Ui_LoginDialog


class LoginDialog(Ui_LoginDialog, CuteDialog):
    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super().__init__(parent)
        self.setupUi(self)
