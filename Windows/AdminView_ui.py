# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AdminView.ui'
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
from PySide6.QtWidgets import (QApplication, QDateEdit, QHeaderView, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QTableWidget,
    QTableWidgetItem, QWidget)

class Ui_AdminWindow(object):
    def setupUi(self, AdminWindow):
        if not AdminWindow.objectName():
            AdminWindow.setObjectName(u"AdminWindow")
        AdminWindow.resize(951, 763)
        AdminWindow.setStyleSheet(u"background-color: #333; border-radius: 5px;")
        self.centralwidget = QWidget(AdminWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.back_button = QPushButton(self.centralwidget)
        self.back_button.setObjectName(u"back_button")
        self.back_button.setGeometry(QRect(30, 20, 101, 31))
        self.back_button.setStyleSheet(u"background-color: black; color: white; font-size: 20px;")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(430, 0, 161, 51))
        self.label.setStyleSheet(u"font-size: 30px; color: white;")
        self.begin_date = QDateEdit(self.centralwidget)
        self.begin_date.setObjectName(u"begin_date")
        self.begin_date.setGeometry(QRect(30, 140, 121, 31))
        self.begin_date.setStyleSheet(u"background-color: white; font-size: 12px;")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(220, 150, 91, 31))
        self.label_2.setStyleSheet(u"font-size: 20px; color: white; font-style: 20px;")
        self.end_date = QDateEdit(self.centralwidget)
        self.end_date.setObjectName(u"end_date")
        self.end_date.setGeometry(QRect(360, 140, 121, 31))
        self.end_date.setStyleSheet(u"background-color: white; font-size: 12px;")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(40, 100, 121, 21))
        self.label_3.setStyleSheet(u"color: white; font-size: 25px;")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(360, 100, 121, 21))
        self.label_4.setStyleSheet(u"color: white; font-size: 25px;")
        self.schedule_table = QTableWidget(self.centralwidget)
        self.schedule_table.setObjectName(u"schedule_table")
        self.schedule_table.setGeometry(QRect(10, 190, 541, 551))
        self.schedule_table.setStyleSheet(u"background-color: white")
        AdminWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(AdminWindow)

        QMetaObject.connectSlotsByName(AdminWindow)
    # setupUi

    def retranslateUi(self, AdminWindow):
        AdminWindow.setWindowTitle(QCoreApplication.translate("AdminWindow", u"MainWindow", None))
        self.back_button.setText(QCoreApplication.translate("AdminWindow", u"Back", None))
        self.label.setText(QCoreApplication.translate("AdminWindow", u"Admin View", None))
        self.label_2.setText(QCoreApplication.translate("AdminWindow", u"Schedule", None))
        self.label_3.setText(QCoreApplication.translate("AdminWindow", u"Start Date", None))
        self.label_4.setText(QCoreApplication.translate("AdminWindow", u"End Date", None))
    # retranslateUi

