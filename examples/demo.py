import sys

from PySide6.QtWidgets import QApplication

from cutewindow import CuteWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = CuteWindow()
    demo.show()
    sys.exit(app.exec())
