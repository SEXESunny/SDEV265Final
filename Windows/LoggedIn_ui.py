# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'LoggedIn.ui'
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
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QTableWidget, QTableWidgetItem,
    QWidget)

class Ui_UserViewWindow(object):
    def setupUi(self, UserViewWindow):
        if not UserViewWindow.objectName():
            UserViewWindow.setObjectName(u"UserViewWindow")
        UserViewWindow.resize(1109, 635)
        UserViewWindow.setStyleSheet(u"background-color:#333")
        self.centralwidget = QWidget(UserViewWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.department_label = QLabel(self.centralwidget)
        self.department_label.setObjectName(u"department_label")
        self.department_label.setGeometry(QRect(430, 70, 271, 31))
        self.department_label.setStyleSheet(u"background-color: white; color: black; font-size: 15px;")
        self.name_label = QLabel(self.centralwidget)
        self.name_label.setObjectName(u"name_label")
        self.name_label.setGeometry(QRect(430, 20, 271, 31))
        self.name_label.setStyleSheet(u"background-color: white; color: black; font-size: 15px;")
        self.clock_in_out_button = QPushButton(self.centralwidget)
        self.clock_in_out_button.setObjectName(u"clock_in_out_button")
        self.clock_in_out_button.setGeometry(QRect(510, 180, 121, 41))
        self.clock_in_out_button.setStyleSheet(u"background-color: white; color: black; border-radius: 5px;")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(460, 130, 251, 31))
        self.label_3.setStyleSheet(u"background-color: none; font-size: 15px; color: white; font-weight: 700;")
        self.past_week_time_table = QTableWidget(self.centralwidget)
        self.past_week_time_table.setObjectName(u"past_week_time_table")
        self.past_week_time_table.setGeometry(QRect(20, 300, 541, 311))
        self.past_week_time_table.setStyleSheet(u"background-color: white")
        self.current_week_time_table = QTableWidget(self.centralwidget)
        self.current_week_time_table.setObjectName(u"current_week_time_table")
        self.current_week_time_table.setGeometry(QRect(590, 300, 501, 311))
        self.current_week_time_table.setStyleSheet(u"background-color: white")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(210, 240, 111, 31))
        self.label_4.setStyleSheet(u" font-size: 20px; text-align: center; color: white;")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(780, 230, 131, 31))
        self.label_5.setStyleSheet(u" font-size: 20px; text-align: center; color: white;")
        self.back_button = QPushButton(self.centralwidget)
        self.back_button.setObjectName(u"back_button")
        self.back_button.setGeometry(QRect(40, 20, 121, 41))
        self.back_button.setStyleSheet(u"background-color: white; color: black; font-size: 20px; border-radius: 5px;")
        self.admin_view_button = QPushButton(self.centralwidget)
        self.admin_view_button.setObjectName(u"admin_view_button")
        self.admin_view_button.setGeometry(QRect(970, 20, 121, 41))
        self.admin_view_button.setStyleSheet(u"background-color: white; color: black; font-size: 16px; border-radius: 5px;")
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
        self.clock_in_out_button.setText(QCoreApplication.translate("UserViewWindow", u"Clock in/out", None))
        self.label_3.setText(QCoreApplication.translate("UserViewWindow", u"Currently: NOT CLOCKED IN", None))
        self.label_4.setText(QCoreApplication.translate("UserViewWindow", u"Past Week", None))
        self.label_5.setText(QCoreApplication.translate("UserViewWindow", u"Current Week", None))
        self.back_button.setText(QCoreApplication.translate("UserViewWindow", u"Back", None))
        self.admin_view_button.setText(QCoreApplication.translate("UserViewWindow", u"Admin View", None))
    # retranslateUi

