# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AdminView.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
        AdminWindow.resize(1080, 800)
        AdminWindow.setStyleSheet(u"background-color: white;")
        self.centralwidget = QWidget(AdminWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.back_button = QPushButton(self.centralwidget)
        self.back_button.setObjectName(u"back_button")
        self.back_button.setGeometry(QRect(20, 20, 140, 60))
        self.back_button.setMinimumSize(QSize(140, 60))
        self.back_button.setMaximumSize(QSize(140, 60))
        font = QFont()
        font.setFamilies([u"Tahoma"])
        font.setWeight(QFont.DemiBold)
        self.back_button.setFont(font)
        self.back_button.setStyleSheet(u"border-radius: 14px;\n"
"background-color: rgb(199, 86, 79); \n"
"color: white; letter-spacing: 0.6px; \n"
"font-size: 26px; \n"
"letter-spacing: .7px;")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(340, 10, 420, 69))
        self.label.setMinimumSize(QSize(420, 60))
        self.label.setMaximumSize(QSize(420, 69))
        self.label.setFont(font)
        self.label.setStyleSheet(u"font-size: 39px;\n"
"color: black;")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.begin_date = QDateEdit(self.centralwidget)
        self.begin_date.setObjectName(u"begin_date")
        self.begin_date.setGeometry(QRect(80, 300, 121, 31))
        font1 = QFont()
        font1.setFamilies([u"Tahoma"])
        self.begin_date.setFont(font1)
        self.begin_date.setStyleSheet(u"background-color: rgb(242, 241, 243);\n"
"color: black;\n"
"border: 2px solid rgb(185, 184, 186);\n"
"")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(460, 163, 170, 40))
        font2 = QFont()
        font2.setFamilies([u"Tahoma"])
        font2.setWeight(QFont.Black)
        self.label_2.setFont(font2)
        self.label_2.setStyleSheet(u"font-size: 30px;\n"
"color: black; \n"
"\n"
"letter-spacing: .7px;")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.end_date = QDateEdit(self.centralwidget)
        self.end_date.setObjectName(u"end_date")
        self.end_date.setGeometry(QRect(80, 530, 121, 31))
        self.end_date.setFont(font1)
        self.end_date.setStyleSheet(u"background-color: rgb(242, 241, 243);\n"
"color: black;\n"
"border: 2px solid rgb(185, 184, 186);\n"
"")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(80, 260, 150, 30))
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"color: black; \n"
"font-size: 25px;\n"
"letter-spacing: .5px;")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(80, 490, 130, 30))
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"color: black; \n"
"letter-spacing: .5px;\n"
"font-size: 25px;")
        self.schedule_table = QTableWidget(self.centralwidget)
        self.schedule_table.setObjectName(u"schedule_table")
        self.schedule_table.setGeometry(QRect(280, 210, 540, 550))
        self.schedule_table.setFont(font1)
        self.schedule_table.setStyleSheet(u"background-color: rgb(242, 241, 243);\n"
"border: 2px solid rgb(185, 184, 186);\n"
"")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(870, 700, 200, 90))
        self.label_5.setMinimumSize(QSize(200, 90))
        self.label_5.setMaximumSize(QSize(200, 90))
        font3 = QFont()
        font3.setKerning(True)
        self.label_5.setFont(font3)
        self.label_5.setPixmap(QPixmap(u"../IMGs/subbaroo_long_name.jpg"))
        self.label_5.setScaledContents(True)
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(620, 160, 50, 50))
        self.label_6.setMinimumSize(QSize(50, 50))
        self.label_6.setMaximumSize(QSize(50, 50))
        self.label_6.setFont(font3)
        self.label_6.setPixmap(QPixmap(u"../IMGs/edit_time.png"))
        self.label_6.setScaledContents(True)
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
        self.label_5.setText("")
        self.label_6.setText("")
    # retranslateUi

