import sys

from PySide6.QtWidgets import QApplication
from qutewindow import QuteWindow, QuteMainWindow


if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = QuteMainWindow()
    demo.show()
    sys.exit(app.exec())
