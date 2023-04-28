# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_LoginDialog.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_LoginDialog(object):
    def setupUi(self, LoginDialog):
        if not LoginDialog.objectName():
            LoginDialog.setObjectName(u"LoginDialog")
        LoginDialog.resize(414, 495)
        self.containerLayout = QVBoxLayout(LoginDialog)
        self.containerLayout.setSpacing(0)
        self.containerLayout.setObjectName(u"containerLayout")
        self.containerLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(LoginDialog)
        self.pushButton.setObjectName(u"pushButton")

        self.containerLayout.addWidget(self.pushButton)


        self.retranslateUi(LoginDialog)

        QMetaObject.connectSlotsByName(LoginDialog)
    # setupUi

    def retranslateUi(self, LoginDialog):
        LoginDialog.setWindowTitle("")
        self.pushButton.setText(QCoreApplication.translate("LoginDialog", u"PushButton", None))
    # retranslateUi

