from typing import Union

import PySide6
from PySide6.QtCore import QSize
from PySide6.QtGui import QGuiApplication, QIcon, QPixmap


class Icon(QIcon):
    def __init__(self, icon_path: Union[str, QPixmap] = None):
        if icon_path is None:
            super(Icon, self).__init__()
            return
        elif isinstance(icon_path, str):
            if 1 < QGuiApplication.primaryScreen().devicePixelRatio() < 2:
                icon_path = icon_path.replace(".png", "@2x.png")
            super(Icon, self).__init__(icon_path)
        elif isinstance(icon_path, QPixmap):
            super(Icon, self).__init__(icon_path)
        else:
            raise ValueError(f"{type(icon_path)} is not a valid argument type.")

    def addFile(self, fileName: str, size: PySide6.QtCore.QSize = None,
                mode: PySide6.QtGui.QIcon.Mode = None, state: PySide6.QtGui.QIcon.State = None) -> None:
        if 1 < QGuiApplication.primaryScreen().devicePixelRatio() < 2:
            fileName = fileName.replace(".png", "@2x.png")
        super(Icon, self).addFile(fileName, QSize(), QIcon.Normal, QIcon.Off)
