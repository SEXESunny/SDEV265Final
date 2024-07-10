from PyQt5.QtWidgets import *
from Models.database import Database;
from Controllers.associate_controller import *
from Models.associate import *
from PyQt5 import uic
from Windows.scale_window import ScaleUI
from Windows.logged_in_window import *

class LogInWindow(QMainWindow):
    
    def __init__(self):
        super(LogInWindow, self).__init__()
        uic.loadUi("Windows/LogIn.ui", self)
        ScaleUI(self, 1.5)
        self.show()
        self.log_in_button.clicked.connect(self.log_in)

    # Open logged in window if badge number if valid
    def log_in(self):
        database = Database('TimesRecord.db')
        associate_db = Associate(database)
        associates = associate_db.get_all_associates()
        badge_numbers = [item[0] for item in associates]
        if int(self.badge_number_input.text()) in badge_numbers:
            self.hide()
            self.deleteLater()
            self.main_window = LoggedInWindow(int(self.badge_number_input.text()))


