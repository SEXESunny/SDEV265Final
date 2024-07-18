from PySide6.QtUiTools import QUiLoader
from PySide6 import QtWidgets, QtCore
from Models.database import Database
from Controllers.associate_controller import *
from Models.associate import *
from Windows.scale_window import ScaleUI
from Windows.current_view_window import *


class LogInWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(LogInWindow, self).__init__()
        loader = QUiLoader()
        ui_file = QtCore.QFile("Windows/LogIn.ui")
        if not ui_file.exists():
            print(f"Unable to find {ui_file.fileName()}")
        ui_file.open(QtCore.QFile.ReadOnly)
        self.ui = loader.load(ui_file, None)
        ui_file.close()

        # Set the UI elements as the central widget
        self.setCentralWidget(self.ui)

        ScaleUI(self, 1.5)

        # Ensure the main window has a reasonable minimum size
        self.setMinimumSize(1080, 800)

        # Connect the log_in button
        self.ui.findChild(QtWidgets.QPushButton, 'log_in_button').clicked.connect(self.log_in)

        # Show the main window
        self.show()

    # Open logged in window if badge number is valid
    def log_in(self):
        database = Database('TimesRecord.db')
        associate_db = Associate(database)
        associates = associate_db.get_all_associates()
        badge_numbers = [item[0] for item in associates]
        if int(self.ui.badge_number_input.text()) in badge_numbers:
            self.hide()
            self.deleteLater()
            self.main_window = CurrentViewWindow()
