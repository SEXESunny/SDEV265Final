# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'LoggedIn.ui'
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
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QTableWidget, QTableWidgetItem,
    QWidget)

class Ui_UserViewWindow(object):
    def setupUi(self, UserViewWindow):
        if not UserViewWindow.objectName():
            UserViewWindow.setObjectName(u"UserViewWindow")
        UserViewWindow.resize(1080, 800)
        UserViewWindow.setMinimumSize(QSize(1080, 800))
        UserViewWindow.setMaximumSize(QSize(1080, 800))
        font = QFont()
        font.setFamilies([u"Tahoma"])
        UserViewWindow.setFont(font)
        UserViewWindow.setStyleSheet(u"background-color: white;")
        self.centralwidget = QWidget(UserViewWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.department_label = QLabel(self.centralwidget)
        self.department_label.setObjectName(u"department_label")
        self.department_label.setGeometry(QRect(340, 80, 400, 40))
        self.department_label.setMinimumSize(QSize(50, 0))
        self.department_label.setFont(font)
        self.department_label.setStyleSheet(u"border: 2px solid #555; \n"
"background-color: white; \n"
"color: black; \n"
"font-size: 20px;")
        self.name_label = QLabel(self.centralwidget)
        self.name_label.setObjectName(u"name_label")
        self.name_label.setGeometry(QRect(340, 30, 400, 40))
        self.name_label.setFont(font)
        self.name_label.setStyleSheet(u"border: 2px solid #555; \n"
"background-color: white; \n"
"color: black; \n"
"font-size: 20px;")
        self.clock_in_out_button = QPushButton(self.centralwidget)
        self.clock_in_out_button.setObjectName(u"clock_in_out_button")
        self.clock_in_out_button.setGeometry(QRect(440, 230, 200, 65))
        font1 = QFont()
        font1.setFamilies([u"Tahoma"])
        font1.setWeight(QFont.ExtraBold)
        self.clock_in_out_button.setFont(font1)
        self.clock_in_out_button.setStyleSheet(u"border: 2px solid #555; \n"
"border-radius: 14px;\n"
"background-color: rgb(78, 149, 213); \n"
"color: white; \n"
"letter-spacing: 1px; \n"
"font-size: 25px;")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(330, 150, 420, 60))
        self.label_3.setMinimumSize(QSize(420, 60))
        self.label_3.setMaximumSize(QSize(420, 60))
        font2 = QFont()
        font2.setFamilies([u"Tahoma"])
        font2.setBold(True)
        self.label_3.setFont(font2)
        self.label_3.setStyleSheet(u"border: 2px solid rgb(185, 184, 186);\n"
"border-radius: 14px;\n"
"background-color: rgb(228, 226, 229); \n"
"color: black; \n"
"letter-spacing: 0.6px; \n"
"font-size: 25px;")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.past_week_time_table = QTableWidget(self.centralwidget)
        self.past_week_time_table.setObjectName(u"past_week_time_table")
        self.past_week_time_table.setGeometry(QRect(13, 360, 541, 311))
        self.past_week_time_table.setFont(font)
        self.past_week_time_table.setStyleSheet(u"background-color: rgb(242, 241, 243);\n"
"border: 2px solid rgb(185, 184, 186);\n"
"")
        self.current_week_time_table = QTableWidget(self.centralwidget)
        self.current_week_time_table.setObjectName(u"current_week_time_table")
        self.current_week_time_table.setGeometry(QRect(567, 360, 501, 311))
        self.current_week_time_table.setFont(font)
        self.current_week_time_table.setStyleSheet(u"background-color: rgb(242, 241, 243);\n"
"border: 2px solid rgb(133, 193, 111); \n"
"")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(160, 300, 230, 50))
        self.label_4.setMinimumSize(QSize(50, 50))
        self.label_4.setMaximumSize(QSize(230, 40))
        self.label_4.setFont(font2)
        self.label_4.setStyleSheet(u"border: 2px solid rgb(185, 184, 186);\n"
"background-color: white; \n"
"color: black; \n"
"letter-spacing: 0.6px; \n"
"font-size: 25px;")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.back_button = QPushButton(self.centralwidget)
        self.back_button.setObjectName(u"back_button")
        self.back_button.setGeometry(QRect(20, 20, 140, 60))
        self.back_button.setMinimumSize(QSize(140, 60))
        self.back_button.setMaximumSize(QSize(140, 60))
        font3 = QFont()
        font3.setFamilies([u"Tahoma"])
        font3.setWeight(QFont.DemiBold)
        self.back_button.setFont(font3)
        self.back_button.setStyleSheet(u"border-radius: 14px;\n"
"background-color: rgb(199, 86, 79);\n"
"color: white; \n"
"letter-spacing: 0.6px; \n"
"font-size: 26px;\n"
"letter-spacing: .7px; \n"
"\n"
"\n"
"")
        self.admin_view_button = QPushButton(self.centralwidget)
        self.admin_view_button.setObjectName(u"admin_view_button")
        self.admin_view_button.setGeometry(QRect(860, 20, 200, 40))
        self.admin_view_button.setMinimumSize(QSize(200, 0))
        self.admin_view_button.setFont(font3)
        self.admin_view_button.setStyleSheet(u"border: 2px solid #555; \n"
"border-radius: 14px;\n"
"background-color:rgb(207, 67, 74); \n"
"color: white; \n"
"letter-spacing: 0.7px; \n"
"font-size: 25px;")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(440, 690, 200, 90))
        self.label_2.setMinimumSize(QSize(200, 90))
        self.label_2.setMaximumSize(QSize(200, 90))
        font4 = QFont()
        font4.setKerning(True)
        self.label_2.setFont(font4)
        self.label_2.setPixmap(QPixmap(u"../IMGs/subbaroo_long_name.jpg"))
        self.label_2.setScaledContents(True)
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(140, 300, 50, 50))
        self.label_6.setMinimumSize(QSize(50, 50))
        self.label_6.setMaximumSize(QSize(40, 40))
        self.label_6.setFont(font4)
        self.label_6.setStyleSheet(u"border: 2px solid rgb(185, 184, 186);\n"
"")
        self.label_6.setPixmap(QPixmap(u"../IMGs/past_week.png"))
        self.label_6.setScaledContents(True)
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(720, 300, 260, 50))
        self.label_7.setMinimumSize(QSize(50, 50))
        self.label_7.setMaximumSize(QSize(260, 40))
        self.label_7.setFont(font2)
        self.label_7.setStyleSheet(u"border: 2px solid #555; \n"
"background-color: rgb(133, 193, 111);\n"
"color: white; \n"
"letter-spacing: 0.6px; \n"
"font-size: 25px;\n"
"")
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(700, 300, 50, 50))
        self.label_8.setMinimumSize(QSize(50, 50))
        self.label_8.setMaximumSize(QSize(40, 40))
        self.label_8.setFont(font4)
        self.label_8.setStyleSheet(u"border: 2px solid #555; \n"
"")
        self.label_8.setPixmap(QPixmap(u"../IMGs/current_week.png"))
        self.label_8.setScaledContents(True)
        UserViewWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(UserViewWindow)

        QMetaObject.connectSlotsByName(UserViewWindow)
    # setupUi

    def retranslateUi(self, UserViewWindow):
        UserViewWindow.setWindowTitle(QCoreApplication.translate("UserViewWindow", u"User View", None))
#if QT_CONFIG(accessibility)
        UserViewWindow.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.department_label.setText(QCoreApplication.translate("UserViewWindow", u"Department: ", None))
        self.name_label.setText(QCoreApplication.translate("UserViewWindow", u"Name: ", None))
        self.clock_in_out_button.setText(QCoreApplication.translate("UserViewWindow", u"Clock In/Out", None))
        self.label_3.setText(QCoreApplication.translate("UserViewWindow", u"Currently: NOT CLOCKED IN", None))
        self.label_4.setText(QCoreApplication.translate("UserViewWindow", u"  Past Week", None))
        self.back_button.setText(QCoreApplication.translate("UserViewWindow", u"Back", None))
        self.admin_view_button.setText(QCoreApplication.translate("UserViewWindow", u"Admin View", None))
        self.label_2.setText("")
        self.label_6.setText("")
        self.label_7.setText(QCoreApplication.translate("UserViewWindow", u"  Current Week", None))
        self.label_8.setText("")
    # retranslateUi

