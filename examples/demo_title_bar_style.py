import sys

from PySide6.QtWidgets import QApplication

from qutewindow import CuteWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = CuteWindow()
    demo.setStyleSheet("#TitleBar { background-color: red; }")
    demo.show()
    sys.exit(app.exec())
