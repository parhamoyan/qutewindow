import sys

from PySide6.QtWidgets import QApplication
from qutewindow import QuteWindow, QuteMainWindow, QuteDialog


if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = QuteDialog()
    demo.show()
    sys.exit(app.exec())
