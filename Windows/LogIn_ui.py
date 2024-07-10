# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'LogIn.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QWidget)

class Ui_LogInWindow(object):
    def setupUi(self, LogInWindow):
        if not LogInWindow.objectName():
            LogInWindow.setObjectName(u"LogInWindow")
        LogInWindow.resize(1105, 724)
        LogInWindow.setAutoFillBackground(False)
        LogInWindow.setStyleSheet(u"background-color:#333;")
        self.centralwidget = QWidget(LogInWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.badge_number_input = QLineEdit(self.centralwidget)
        self.badge_number_input.setObjectName(u"badge_number_input")
        self.badge_number_input.setGeometry(QRect(440, 300, 271, 61))
        self.badge_number_input.setStyleSheet(u"background-color: white; color: black; font-size: 30px;")
        self.badge_label = QLabel(self.centralwidget)
        self.badge_label.setObjectName(u"badge_label")
        self.badge_label.setGeometry(QRect(400, 180, 511, 51))
        self.badge_label.setStyleSheet(u"color: white; font-size: 50px;")
        self.log_in_button = QPushButton(self.centralwidget)
        self.log_in_button.setObjectName(u"log_in_button")
        self.log_in_button.setGeometry(QRect(460, 420, 221, 51))
        self.log_in_button.setStyleSheet(u"background-color: white; color: black; font-size: 27px;")
        LogInWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(LogInWindow)

        QMetaObject.connectSlotsByName(LogInWindow)
    # setupUi

    def retranslateUi(self, LogInWindow):
        LogInWindow.setWindowTitle(QCoreApplication.translate("LogInWindow", u"Log In", None))
        self.badge_number_input.setText("")
        self.badge_label.setText(QCoreApplication.translate("LogInWindow", u"Enter Badge Number: ", None))
        self.log_in_button.setText(QCoreApplication.translate("LogInWindow", u"Log In", None))
    # retranslateUi

