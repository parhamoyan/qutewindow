import sys

from PySide6.QtWidgets import QApplication

from examples.LoginDialog import LoginDialog


if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = LoginDialog()
    demo.setStyleSheet("background-color: #333333;")
    demo.show()
    sys.exit(app.exec())
