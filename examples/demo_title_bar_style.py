import sys

from PySide6.QtWidgets import QApplication
from qutewindow import QuteWindow


if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = QuteWindow()
    demo.setStyleSheet("#TitleBar { background-color: red; }")
    demo.show()
    sys.exit(app.exec())
