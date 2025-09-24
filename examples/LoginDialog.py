from typing import Optional

from PySide6.QtWidgets import QWidget

from examples.Ui_LoginDialog import Ui_LoginDialog
from cutewindow import CuteDialog


class LoginDialog(Ui_LoginDialog, CuteDialog):
    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super().__init__(parent)
        self.setupUi(self)
