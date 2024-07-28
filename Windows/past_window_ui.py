# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PastWindow.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractSpinBox, QApplication, QDateEdit,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QTableView, QVBoxLayout, QWidget)

class Ui_PastWindow(object):
    def setupUi(self, PastWindow):
        if not PastWindow.objectName():
            PastWindow.setObjectName(u"PastWindow")
        PastWindow.resize(1144, 800)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(PastWindow.sizePolicy().hasHeightForWidth())
        PastWindow.setSizePolicy(sizePolicy)
        PastWindow.setMinimumSize(QSize(1144, 800))
        PastWindow.setMaximumSize(QSize(1144, 800))
        PastWindow.setStyleSheet(u"background-color: white;")
        self.centralwidget = QWidget(PastWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 5, -1, 20)
        self.end_date_label = QLabel(self.centralwidget)
        self.end_date_label.setObjectName(u"end_date_label")
        self.end_date_label.setMaximumSize(QSize(126, 16777215))
        font = QFont()
        font.setFamilies([u"Tahoma"])
        font.setWeight(QFont.DemiBold)
        self.end_date_label.setFont(font)
        self.end_date_label.setStyleSheet(u"color: black; \n"
"letter-spacing: .5px;\n"
"font-size: 25px;")
        self.end_date_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.end_date_label)

        self.end_date = QDateEdit(self.centralwidget)
        self.end_date.setObjectName(u"end_date")
        sizePolicy.setHeightForWidth(self.end_date.sizePolicy().hasHeightForWidth())
        self.end_date.setSizePolicy(sizePolicy)
        self.end_date.setMinimumSize(QSize(100, 30))
        self.end_date.setMaximumSize(QSize(100, 30))
        self.end_date.setSizeIncrement(QSize(0, 0))
        self.end_date.setBaseSize(QSize(0, 0))
        font1 = QFont()
        font1.setFamilies([u"Tahoma"])
        self.end_date.setFont(font1)
        self.end_date.setCursor(QCursor(Qt.CursorShape.IBeamCursor))
        self.end_date.setMouseTracking(True)
        self.end_date.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.end_date.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.end_date.setStyleSheet(u"background-color: rgb(242, 241, 243);\n"
"color: black;\n"
"border: 2px solid rgb(185, 184, 186);\n"
"padding-left:10px;\n"
"padding-bottom: 6px;")
        self.end_date.setInputMethodHints(Qt.InputMethodHint.ImhDate)
        self.end_date.setWrapping(True)
        self.end_date.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.end_date.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.end_date.setKeyboardTracking(False)

        self.verticalLayout_2.addWidget(self.end_date)


        self.gridLayout.addLayout(self.verticalLayout_2, 3, 3, 1, 1)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_4, 0, 0, 1, 1)

        self.update_button = QPushButton(self.centralwidget)
        self.update_button.setObjectName(u"update_button")
        sizePolicy.setHeightForWidth(self.update_button.sizePolicy().hasHeightForWidth())
        self.update_button.setSizePolicy(sizePolicy)
        self.update_button.setMinimumSize(QSize(180, 60))
        self.update_button.setMaximumSize(QSize(180, 60))
        font2 = QFont()
        font2.setFamilies([u"Tahoma"])
        font2.setBold(True)
        self.update_button.setFont(font2)
        self.update_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.update_button.setStyleSheet(u"QPushButton {\n"
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

        self.gridLayout_2.addWidget(self.update_button, 0, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_3, 0, 2, 1, 1)


        self.verticalLayout_5.addLayout(self.gridLayout_2)


        self.gridLayout.addLayout(self.verticalLayout_5, 3, 1, 1, 1)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setHorizontalSpacing(0)
        self.gridLayout_6.setVerticalSpacing(15)
        self.gridLayout_6.setContentsMargins(0, -1, 40, -1)
        self.name_label = QLabel(self.centralwidget)
        self.name_label.setObjectName(u"name_label")
        sizePolicy.setHeightForWidth(self.name_label.sizePolicy().hasHeightForWidth())
        self.name_label.setSizePolicy(sizePolicy)
        self.name_label.setMinimumSize(QSize(130, 40))
        self.name_label.setMaximumSize(QSize(130, 40))
        self.name_label.setFont(font1)
        self.name_label.setStyleSheet(u"border: 2px solid #555; \n"
"background-color: white; \n"
"color: black; \n"
"font-size: 20px;")

        self.gridLayout_6.addWidget(self.name_label, 0, 0, 1, 1)

        self.department_label = QLabel(self.centralwidget)
        self.department_label.setObjectName(u"department_label")
        sizePolicy.setHeightForWidth(self.department_label.sizePolicy().hasHeightForWidth())
        self.department_label.setSizePolicy(sizePolicy)
        self.department_label.setMinimumSize(QSize(130, 40))
        self.department_label.setMaximumSize(QSize(130, 40))
        self.department_label.setFont(font1)
        self.department_label.setStyleSheet(u"border: 2px solid #555; \n"
"background-color: white; \n"
"color: black; \n"
"font-size: 20px;")

        self.gridLayout_6.addWidget(self.department_label, 1, 0, 1, 1)

        self.name_filter = QLineEdit(self.centralwidget)
        self.name_filter.setObjectName(u"name_filter")
        sizePolicy.setHeightForWidth(self.name_filter.sizePolicy().hasHeightForWidth())
        self.name_filter.setSizePolicy(sizePolicy)
        self.name_filter.setMinimumSize(QSize(250, 40))
        self.name_filter.setMaximumSize(QSize(250, 40))
        self.name_filter.setFont(font1)
        self.name_filter.setStyleSheet(u"border: 2px solid #555; \n"
"background-color: rgb(242, 241, 244); \n"
"color: black; \n"
"font-size: 20px;\n"
"padding-left: 8px;")

        self.gridLayout_6.addWidget(self.name_filter, 0, 1, 1, 1)

        self.department_filter = QLineEdit(self.centralwidget)
        self.department_filter.setObjectName(u"department_filter")
        sizePolicy.setHeightForWidth(self.department_filter.sizePolicy().hasHeightForWidth())
        self.department_filter.setSizePolicy(sizePolicy)
        self.department_filter.setMinimumSize(QSize(250, 40))
        self.department_filter.setMaximumSize(QSize(250, 40))
        self.department_filter.setFont(font1)
        self.department_filter.setStyleSheet(u"border: 2px solid #555; \n"
"background-color: rgb(242, 241, 244); \n"
"color: black; \n"
"font-size: 20px;\n"
"padding-left: 8px;")

        self.gridLayout_6.addWidget(self.department_filter, 1, 1, 1, 1)


        self.verticalLayout_7.addLayout(self.gridLayout_6)


        self.gridLayout.addLayout(self.verticalLayout_7, 1, 1, 1, 1)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(-1, 0, -1, -1)
        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(220, 120))
        self.label_2.setPixmap(QPixmap(u":/IMGs/subbaroo_long_name.jpg"))
        self.label_2.setScaledContents(True)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_8.addWidget(self.label_2, 0, 0, 1, 1)


        self.verticalLayout_10.addLayout(self.gridLayout_8)


        self.gridLayout.addLayout(self.verticalLayout_10, 7, 1, 1, 1)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.begin_date_label = QLabel(self.centralwidget)
        self.begin_date_label.setObjectName(u"begin_date_label")
        self.begin_date_label.setMinimumSize(QSize(145, 30))
        self.begin_date_label.setMaximumSize(QSize(145, 30))
        self.begin_date_label.setFont(font)
        self.begin_date_label.setStyleSheet(u"color: black; \n"
"font-size: 25px;\n"
"letter-spacing: .5px;")
        self.begin_date_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_9.addWidget(self.begin_date_label)

        self.begin_date = QDateEdit(self.centralwidget)
        self.begin_date.setObjectName(u"begin_date")
        self.begin_date.setMinimumSize(QSize(100, 30))
        self.begin_date.setMaximumSize(QSize(100, 30))
        self.begin_date.setSizeIncrement(QSize(0, 0))
        self.begin_date.setFont(font1)
        self.begin_date.setCursor(QCursor(Qt.CursorShape.IBeamCursor))
        self.begin_date.setStyleSheet(u"background-color: rgb(242, 241, 243);\n"
"color: black;\n"
"border: 2px solid rgb(185, 184, 186);\n"
"padding-left:10px;\n"
"padding-bottom: 6px;")
        self.begin_date.setFrame(False)
        self.begin_date.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.begin_date.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.begin_date.setCorrectionMode(QAbstractSpinBox.CorrectionMode.CorrectToPreviousValue)
        self.begin_date.setProperty("showGroupSeparator", True)

        self.verticalLayout_9.addWidget(self.begin_date)


        self.gridLayout.addLayout(self.verticalLayout_9, 1, 3, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 3, 4, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 4, 1, 1)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")

        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.past_week_time_table = QTableView(self.centralwidget)
        self.past_week_time_table.setObjectName(u"past_week_time_table")
        self.past_week_time_table.setMaximumSize(QSize(2000, 16777215))
        font3 = QFont()
        font3.setFamilies([u"Tahoma"])
        font3.setBold(False)
        font3.setItalic(False)
        self.past_week_time_table.setFont(font3)
        self.past_week_time_table.setStyleSheet(u"QTableView {\n"
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
        self.past_week_time_table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.past_week_time_table.setCornerButtonEnabled(False)

        self.verticalLayout_3.addWidget(self.past_week_time_table)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)


        self.gridLayout.addLayout(self.verticalLayout_4, 6, 0, 1, 7)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.back_button = QPushButton(self.centralwidget)
        self.back_button.setObjectName(u"back_button")
        sizePolicy.setHeightForWidth(self.back_button.sizePolicy().hasHeightForWidth())
        self.back_button.setSizePolicy(sizePolicy)
        self.back_button.setMinimumSize(QSize(140, 60))
        self.back_button.setMaximumSize(QSize(140, 60))
        self.back_button.setFont(font)
        self.back_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.back_button.setStyleSheet(u"QPushButton {\n"
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
"}")

        self.gridLayout_3.addWidget(self.back_button, 0, 0, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(180, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_5, 0, 1, 1, 1)


        self.verticalLayout_6.addLayout(self.gridLayout_3)


        self.gridLayout.addLayout(self.verticalLayout_6, 1, 0, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.past_weeks_label = QLabel(self.centralwidget)
        self.past_weeks_label.setObjectName(u"past_weeks_label")
        self.past_weeks_label.setMinimumSize(QSize(110, 60))
        self.past_weeks_label.setMaximumSize(QSize(350, 69))
        self.past_weeks_label.setFont(font)
        self.past_weeks_label.setStyleSheet(u"border: 2px solid #555; \n"
"background-color: rgb(231, 143, 80);\n"
"color: white; \n"
"letter-spacing: 0.6px; \n"
"font-size: 33px;\n"
"")
        self.past_weeks_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_4.addWidget(self.past_weeks_label, 0, 1, 1, 1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QSize(69, 69))
        self.label.setMaximumSize(QSize(69, 69))
        self.label.setStyleSheet(u"border: 2px solid #555; \n"
"")
        self.label.setPixmap(QPixmap(u":/IMGs/past_week.png"))
        self.label.setScaledContents(True)

        self.gridLayout_4.addWidget(self.label, 0, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_4)


        self.gridLayout.addLayout(self.verticalLayout, 3, 0, 1, 1)

        PastWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(PastWindow)

        QMetaObject.connectSlotsByName(PastWindow)
    # setupUi

    def retranslateUi(self, PastWindow):
        PastWindow.setWindowTitle(QCoreApplication.translate("PastWindow", u"MainWindow", None))
        self.end_date_label.setText(QCoreApplication.translate("PastWindow", u"End Date", None))
        self.update_button.setText(QCoreApplication.translate("PastWindow", u"Update", None))
        self.name_label.setText(QCoreApplication.translate("PastWindow", u"Name: ", None))
        self.department_label.setText(QCoreApplication.translate("PastWindow", u"Department: ", None))
        self.label_2.setText("")
        self.begin_date_label.setText(QCoreApplication.translate("PastWindow", u"Start Date", None))
        self.back_button.setText(QCoreApplication.translate("PastWindow", u"Back", None))
        self.past_weeks_label.setText(QCoreApplication.translate("PastWindow", u"Past Weeks", None))
        self.label.setText("")
    # retranslateUi

