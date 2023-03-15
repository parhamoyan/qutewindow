import sys

from PySide6.QtWidgets import QApplication
from qute_frameless_window import QuteWindow


if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = QuteWindow()
    demo.show()
    sys.exit(app.exec())
