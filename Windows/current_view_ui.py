# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CurrentView.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QGridLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QTableView, QVBoxLayout,
    QWidget)

class Ui_UserViewWindow(object):
    def setupUi(self, UserViewWindow):
        if not UserViewWindow.objectName():
            UserViewWindow.setObjectName(u"UserViewWindow")
        UserViewWindow.resize(1080, 800)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(UserViewWindow.sizePolicy().hasHeightForWidth())
        UserViewWindow.setSizePolicy(sizePolicy)
        UserViewWindow.setMinimumSize(QSize(1080, 800))
        UserViewWindow.setMaximumSize(QSize(1080, 800))
        font = QFont()
        font.setFamilies([u"Tahoma"])
        UserViewWindow.setFont(font)
        UserViewWindow.setStyleSheet(u"background-color: white;")
        self.centralwidget = QWidget(UserViewWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(1080, 800))
        self.centralwidget.setMaximumSize(QSize(1080, 800))
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer_7 = QSpacerItem(15, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_7, 4, 0, 1, 1)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(10, -1, 10, -1)
        self.update_button = QPushButton(self.centralwidget)
        self.update_button.setObjectName(u"update_button")
        sizePolicy.setHeightForWidth(self.update_button.sizePolicy().hasHeightForWidth())
        self.update_button.setSizePolicy(sizePolicy)
        self.update_button.setMinimumSize(QSize(200, 40))
        self.update_button.setMaximumSize(QSize(200, 40))
        font1 = QFont()
        font1.setFamilies([u"Tahoma"])
        font1.setWeight(QFont.ExtraBold)
        self.update_button.setFont(font1)
        self.update_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.update_button.setStyleSheet(u"\n"
"QPushButton {\n"
"border: None; \n"
"border-radius: 5px;\n"
"border-right: 2.7px solid rgb(43, 43, 43); \n"
"border-bottom: 2.7px solid rgb(43, 43, 43);\n"
"background-color: rgb(80, 150, 210); \n"
"color: white; \n"
"letter-spacing: 1px; \n"
"font-size: 25px;\n"
"}\n"
"\n"
"QPushButton:hover {;\n"
"color: rgb(238, 237, 240);\n"
"background-color: rgb(44, 112, 160);\n"
"}\n"
"")

        self.gridLayout_8.addWidget(self.update_button, 0, 0, 1, 1)


        self.verticalLayout_4.addLayout(self.gridLayout_8)


        self.gridLayout.addLayout(self.verticalLayout_4, 4, 4, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(15, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_4, 0, 0, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_8, 4, 6, 1, 1)

        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setHorizontalSpacing(0)
        self.gridLayout_7.setVerticalSpacing(20)
        self.gridLayout_7.setContentsMargins(-1, 0, -1, -1)
        self.past_view_button = QPushButton(self.centralwidget)
        self.past_view_button.setObjectName(u"past_view_button")
        self.past_view_button.setMinimumSize(QSize(200, 40))
        self.past_view_button.setMaximumSize(QSize(200, 40))
        font2 = QFont()
        font2.setFamilies([u"Tahoma"])
        font2.setWeight(QFont.DemiBold)
        self.past_view_button.setFont(font2)
        self.past_view_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.past_view_button.setStyleSheet(u"QPushButton {\n"
"border: None; \n"
"border-radius: 5px;\n"
"border-right: 2.7px solid rgb(43, 43, 43); \n"
"border-bottom: 2.7px solid rgb(43, 43, 43);\n"
"background-color:rgb(207, 67, 74); \n"
"color: white; \n"
"letter-spacing: 0.7px; \n"
"font-size: 25px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"color: rgb(238, 237, 240);\n"
"background-color: rgb(165, 48, 55);\n"
"}\n"
"")

        self.gridLayout_7.addWidget(self.past_view_button, 0, 0, 1, 1)

        self.admin_view_button = QPushButton(self.centralwidget)
        self.admin_view_button.setObjectName(u"admin_view_button")
        self.admin_view_button.setMinimumSize(QSize(200, 40))
        self.admin_view_button.setMaximumSize(QSize(200, 40))
        self.admin_view_button.setFont(font2)
        self.admin_view_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.admin_view_button.setStyleSheet(u"QPushButton {\n"
"border: None; \n"
"border-radius: 5px;\n"
"border-right: 2.7px solid rgb(43, 43, 43); \n"
"border-bottom: 2.7px solid rgb(43, 43, 43);\n"
"background-color:rgb(207, 67, 74); \n"
"color: white; \n"
"letter-spacing: 0.7px; \n"
"font-size: 25px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"color: rgb(238, 237, 240);\n"
"background-color: rgb(165, 48, 55);\n"
"}\n"
"")

        self.gridLayout_7.addWidget(self.admin_view_button, 1, 0, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_7, 0, 4, 1, 1)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setHorizontalSpacing(0)
        self.gridLayout_5.setVerticalSpacing(20)
        self.name_label = QLabel(self.centralwidget)
        self.name_label.setObjectName(u"name_label")
        sizePolicy.setHeightForWidth(self.name_label.sizePolicy().hasHeightForWidth())
        self.name_label.setSizePolicy(sizePolicy)
        self.name_label.setMinimumSize(QSize(130, 40))
        self.name_label.setMaximumSize(QSize(130, 40))
        self.name_label.setFont(font)
        self.name_label.setStyleSheet(u"border: 2px solid #555; \n"
"background-color: white; \n"
"color: black; \n"
"font-size: 20px;")
        self.name_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_5.addWidget(self.name_label, 0, 0, 1, 1)

        self.department_label = QLabel(self.centralwidget)
        self.department_label.setObjectName(u"department_label")
        sizePolicy.setHeightForWidth(self.department_label.sizePolicy().hasHeightForWidth())
        self.department_label.setSizePolicy(sizePolicy)
        self.department_label.setMinimumSize(QSize(130, 40))
        self.department_label.setMaximumSize(QSize(130, 40))
        self.department_label.setFont(font)
        self.department_label.setStyleSheet(u"border: 2px solid #555; \n"
"background-color: white; \n"
"color: black; \n"
"font-size: 20px;")
        self.department_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_5.addWidget(self.department_label, 1, 0, 1, 1)

        self.department_filter = QLineEdit(self.centralwidget)
        self.department_filter.setObjectName(u"department_filter")
        sizePolicy.setHeightForWidth(self.department_filter.sizePolicy().hasHeightForWidth())
        self.department_filter.setSizePolicy(sizePolicy)
        self.department_filter.setMinimumSize(QSize(180, 40))
        self.department_filter.setMaximumSize(QSize(180, 40))
        self.department_filter.setFont(font)
        self.department_filter.setStyleSheet(u"border: 2px solid #555; \n"
"background-color: rgb(242, 241, 244); \n"
"color: black; \n"
"font-size: 20px;\n"
"padding-left: 8px;")

        self.gridLayout_5.addWidget(self.department_filter, 1, 1, 1, 1)

        self.name_filter = QLineEdit(self.centralwidget)
        self.name_filter.setObjectName(u"name_filter")
        sizePolicy.setHeightForWidth(self.name_filter.sizePolicy().hasHeightForWidth())
        self.name_filter.setSizePolicy(sizePolicy)
        self.name_filter.setMinimumSize(QSize(180, 40))
        self.name_filter.setMaximumSize(QSize(180, 40))
        self.name_filter.setFont(font)
        self.name_filter.setStyleSheet(u"border: 2px solid #555; \n"
"background-color: rgb(242, 241, 244); \n"
"color: black; \n"
"font-size: 20px;\n"
"padding-left: 8px;")

        self.gridLayout_5.addWidget(self.name_filter, 0, 1, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout_5, 2, 0, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_4, 0, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 6, 6, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 0, 6, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 4, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_5, 1, 0, 1, 7)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.gridLayout_9 = QGridLayout()
        self.gridLayout_9.setSpacing(0)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(0, -1, 20, -1)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(211, 100))
        self.label.setPixmap(QPixmap(u":/IMGs/subbaroo_long_name.jpg"))
        self.label.setScaledContents(True)

        self.gridLayout_9.addWidget(self.label, 0, 0, 1, 1)


        self.verticalLayout_7.addLayout(self.gridLayout_9)


        self.gridLayout.addLayout(self.verticalLayout_7, 0, 2, 1, 2)

        self.current_week_time_table = QTableView(self.centralwidget)
        self.current_week_time_table.setObjectName(u"current_week_time_table")
        self.current_week_time_table.setMaximumSize(QSize(2000, 16777215))
        font3 = QFont()
        font3.setFamilies([u"Tahoma"])
        font3.setBold(False)
        font3.setItalic(False)
        self.current_week_time_table.setFont(font3)
        self.current_week_time_table.setStyleSheet(u"QTableView {\n"
"    color: black;\n"
"    gridline-color: black;\n"
"    border: 2px solid black;  /* Outer border of the whole table */\n"
"    font: 10px;\n"
"	font-size: 12px;\n"
"}\n"
"QTableView::item {\n"
"    border-top: 1px solid black;  /* Borders for each cell */\n"
"    border-bottom: 1px solid black;\n"
"    border-left: 1px solid black;\n"
"    border-right: 1px solid #555;\n"
"}\n"
"QTableCornerButton::section {\n"
"    background-color: rgb(78, 149, 213);\n"
"}\n"
"QTableView::item:selected {\n"
"    background-color: rgb(144, 144, 144);  /* Background color for selected item */\n"
"    color: black;  /* Text color for selected item */\n"
"}\n"
"QTableView::item:focus {\n"
"    border: 2px solid rgb(242, 128, 133);\n"
"    background-color: rgb(144, 144, 144);\n"
"}\n"
"QHeaderView::section {\n"
"    background-color: rgb(78, 149, 213);\n"
"    color: white;\n"
"    height: 35px;\n"
"    font: 14px;\n"
"}\n"
"QScrollBar:vertical {\n"
"    background: rgb(188, 224, 235);\n"
"}\n"
"QScrollBar::ha"
                        "ndle:vertical {\n"
"    background: rgb(71, 153, 176);\n"
"}\n"
"QScrollBar:horizontal {\n"
"    background: rgb(188, 224, 235);\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(71, 153, 176);\n"
"}\n"
"QLineEdit {\n"
"    color: black;  /* Text color for QLineEdit (editor) */\n"
"}")
        self.current_week_time_table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.current_week_time_table.setCornerButtonEnabled(False)

        self.gridLayout.addWidget(self.current_week_time_table, 6, 1, 1, 4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(17, 0, 60, 10)
        self.current_week_icon = QLabel(self.centralwidget)
        self.current_week_icon.setObjectName(u"current_week_icon")
        sizePolicy.setHeightForWidth(self.current_week_icon.sizePolicy().hasHeightForWidth())
        self.current_week_icon.setSizePolicy(sizePolicy)
        self.current_week_icon.setMinimumSize(QSize(50, 50))
        self.current_week_icon.setMaximumSize(QSize(40, 40))
        font4 = QFont()
        font4.setKerning(True)
        self.current_week_icon.setFont(font4)
        self.current_week_icon.setStyleSheet(u"border: 2px solid #555; \n"
"")
        self.current_week_icon.setPixmap(QPixmap(u":/IMGs/current_week.png"))
        self.current_week_icon.setScaledContents(True)
        self.current_week_icon.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.current_week_icon, 0, 0, 1, 1)

        self.current_week_label = QLabel(self.centralwidget)
        self.current_week_label.setObjectName(u"current_week_label")
        sizePolicy.setHeightForWidth(self.current_week_label.sizePolicy().hasHeightForWidth())
        self.current_week_label.setSizePolicy(sizePolicy)
        self.current_week_label.setMinimumSize(QSize(290, 50))
        self.current_week_label.setMaximumSize(QSize(290, 40))
        font5 = QFont()
        font5.setFamilies([u"Tahoma"])
        font5.setBold(True)
        self.current_week_label.setFont(font5)
        self.current_week_label.setStyleSheet(u"border: 2px solid #555; \n"
"background-color: rgb(133, 193, 111);\n"
"color: white; \n"
"letter-spacing: 0.6px; \n"
"font-size: 25px;\n"
"")
        self.current_week_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.current_week_label, 0, 1, 1, 1)


        self.verticalLayout_5.addLayout(self.gridLayout_2)


        self.gridLayout.addLayout(self.verticalLayout_5, 4, 2, 1, 2)

        self.horizontalSpacer = QSpacerItem(15, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 6, 0, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.day_toggle_button = QPushButton(self.centralwidget)
        self.day_toggle_button.setObjectName(u"day_toggle_button")
        self.day_toggle_button.setEnabled(True)
        sizePolicy.setHeightForWidth(self.day_toggle_button.sizePolicy().hasHeightForWidth())
        self.day_toggle_button.setSizePolicy(sizePolicy)
        self.day_toggle_button.setMinimumSize(QSize(300, 40))
        self.day_toggle_button.setMaximumSize(QSize(300, 40))
        self.day_toggle_button.setFont(font5)
        self.day_toggle_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.day_toggle_button.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.day_toggle_button.setStyleSheet(u"QPushButton {\n"
"border: None; \n"
"border-radius: 5px;\n"
"border-right: 2.7px solid rgb(43, 43, 43); \n"
"border-bottom: 2.7px solid rgb(43, 43, 43);\n"
"background-color: rgb(80, 150, 210); \n"
"color: white; \n"
"letter-spacing: 1px; \n"
"font-size: 25px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"color: rgb(238, 237, 240);\n"
"background-color: rgb(44, 112, 160);\n"
"}\n"
"")
        self.day_toggle_button.setCheckable(False)

        self.gridLayout_6.addWidget(self.day_toggle_button, 0, 0, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout_6)


        self.gridLayout.addLayout(self.verticalLayout_2, 4, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer, 7, 2, 1, 2)

        UserViewWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(UserViewWindow)

        QMetaObject.connectSlotsByName(UserViewWindow)
    # setupUi

    def retranslateUi(self, UserViewWindow):
        UserViewWindow.setWindowTitle(QCoreApplication.translate("UserViewWindow", u"User View", None))
#if QT_CONFIG(accessibility)
        UserViewWindow.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.update_button.setText(QCoreApplication.translate("UserViewWindow", u"Update", None))
        self.past_view_button.setText(QCoreApplication.translate("UserViewWindow", u"Past View", None))
        self.admin_view_button.setText(QCoreApplication.translate("UserViewWindow", u"Admin View", None))
        self.name_label.setText(QCoreApplication.translate("UserViewWindow", u"Name", None))
        self.department_label.setText(QCoreApplication.translate("UserViewWindow", u"Department", None))
        self.department_filter.setText("")
        self.name_filter.setText("")
        self.label.setText("")
        self.current_week_icon.setText("")
        self.current_week_label.setText(QCoreApplication.translate("UserViewWindow", u"  Current Week", None))
        self.day_toggle_button.setText(QCoreApplication.translate("UserViewWindow", u"Today Toggle: OFF", None))
    # retranslateUi

