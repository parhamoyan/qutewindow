import sys

from PySide6.QtWidgets import QApplication
from qutewindow import QuteWindow


if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = QuteWindow()
    demo.setStyleSheet("background-color: #333333;")
    demo.show()
    sys.exit(app.exec())
