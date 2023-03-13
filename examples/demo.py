import sys

from PySide6.QtWidgets import QApplication
from platforms import FramelessWindow


if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = FramelessWindow()
    demo.show()
    sys.exit(app.exec())