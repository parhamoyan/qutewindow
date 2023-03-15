# qute-window
Cross-platform frameless window based on Python and Qt

## Examples

### Qute Window on macOS
<p align="center">
  <img src="readme/mac_qute_window.gif")>
</p>

### Qute Window on Windows
<p align="center">
  <img src="readme/win32_qute_window.gif")>
</p>

## Features
* Moving (the title bar area is draggable)
* Stretching
* Native window shadow
* Native window animations
* Win11 snap layout

## Installing via PIP
```shell
pip install qutewindow
```

## Usage
Here is a minimal example:

```python
from typing import Optional

from PySide6.QtWidgets import QApplication, QWidget
from qutewindow import QuteWindow
import sys


class Window(QuteWindow):
    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super().__init__(parent)
        self.setWindowTitle("Qute Window")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Window()
    demo.show()
    sys.exit(app.exec())

```
