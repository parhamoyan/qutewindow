"""
Enhanced Icon class for CuteWindow with automatic high-DPI support.

This class extends QIcon to provide automatic high-DPI icon loading
by selecting appropriate @2x.png files when needed.
"""

from typing import Optional, Union

from PySide6.QtCore import QSize
from PySide6.QtGui import QGuiApplication, QIcon, QPixmap


class Icon(QIcon):
    """
    Enhanced QIcon with automatic high-DPI support.

    This class automatically detects the screen's pixel ratio and loads
    appropriate high-resolution icons (@2x.png) when available.

    Args:
        icon_path: Path to icon file or QPixmap object. If None, creates empty icon.

    Raises:
        ValueError: If icon_path is neither a string nor QPixmap.
    """

    def __init__(self, icon_path: Union[str, QPixmap, None] = None) -> None:
        super().__init__()

        if icon_path is None:
            return
        elif isinstance(icon_path, str):
            processed_path = self._process_icon_path(icon_path)
            super().__init__(processed_path)
        elif isinstance(icon_path, QPixmap):
            super().__init__(icon_path)
        else:
            raise ValueError(f"Expected str or QPixmap, got {type(icon_path).__name__}")

    def _process_icon_path(self, icon_path: str) -> str:
        """
        Process icon path for high-DPI displays.

        Args:
            icon_path: Original icon path.

        Returns:
            Processed icon path with @2x suffix if needed.
        """
        if not hasattr(QGuiApplication, "primaryScreen"):
            return icon_path

        screen = QGuiApplication.primaryScreen()
        if screen and 1 < screen.devicePixelRatio() < 2:
            return icon_path.replace(".png", "@2x.png")
        return icon_path

    def addFile(
        self,
        fileName: str,
        size: Optional[QSize] = None,
        mode: Optional[QIcon.Mode] = None,
        state: Optional[QIcon.State] = None,
    ) -> None:
        """
        Add an icon file with automatic high-DPI processing.

        Args:
            fileName: Path to the icon file.
            size: Size of the icon (optional).
            mode: Mode of the icon (optional).
            state: State of the icon (optional).
        """
        processed_file = self._process_icon_path(fileName)
        super().addFile(
            processed_file,
            QSize() if size is None else size,
            QIcon.Normal if mode is None else mode,
            QIcon.Off if state is None else state,
        )
