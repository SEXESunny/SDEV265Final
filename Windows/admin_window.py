from datetime import datetime, timedelta
from Models.database import Database
from Controllers.associate_controller import *
from Windows.scale_window import ScaleUI
from Models.current_week_sign_in_sign_out import CurrentWeekSignInSignOut
from Controllers.current_week_controller import *
from Controllers.previous_week_controller import *
from PySide6 import QtCore, QtGui, QtWidgets, QtUiTools
from PySide6.QtCore import QDate
from PySide6.QtWidgets import QDateEdit
from Windows.custom_date_edit import CustomDateEdit  # Ensure this is correctly imported


class AdminWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(AdminWindow, self).__init__()
        loader = QtUiTools.QUiLoader()
        ui_file = QtCore.QFile("Windows/AdminView.ui")
        ui_file.open(QtCore.QFile.ReadOnly)
        # The second argument for loader.load needs to be None, not self. It will not render if you don't do this
        # for some reason.
        self.ui = loader.load(ui_file, None)
        ui_file.close()



        # Set the UI as the central widget
        self.setCentralWidget(self.ui)

        # Enforce a reasonable size for the main window
        self.setMinimumSize(800, 600)
        self.setMaximumSize(9999, 9999)

        # Scale UI
        ScaleUI(self, 1.5)


        # Connect buttons to their respective functions
        try:
            self.ui.back_button.clicked.connect(self.back_to_log_in)
            self.ui.begin_date.dateChanged.connect(self.load_tables_data)
            self.ui.end_date.dateChanged.connect(self.load_tables_data)
            print("Buttons connected successfully")
        except Exception as e:
            print(f"Error connecting buttons: {e}")

        # Set default dates and set up the table
        self.set_default_dates()
        self.setup_tables()
        self.load_tables_data()

        # Show the main window
        self.show()
        print("Main window shown")

    # Set default dates for date edit widgets
    def set_default_dates(self):
        # Get current date
        current_date = datetime.now()

        # Move date back 7 days
        new_date = current_date - timedelta(days=7)

        # Convert the date to qdate
        qdate_begin = QtCore.QDate(new_date.year, new_date.month, new_date.day)
        qdate_end = QtCore.QDate(current_date.year, current_date.month, current_date.day)

        # Set the dates on the date edits
        self.ui.begin_date.setDate(qdate_begin)
        self.ui.end_date.setDate(qdate_end)

    # Opens log in window
    def back_to_log_in(self):
        print("Back to login button clicked")
        from Windows.log_in_window import LogInWindow
        self.hide()
        self.deleteLater()
        self.main_window = LogInWindow()

    # Formats the schedule table
    def setup_tables(self):
        # Set number of columns
        self.ui.schedule_table.setColumnCount(7)
        # Set horizontal labels
        self.ui.schedule_table.setHorizontalHeaderLabels(['Record', 'Name', 'Badge#', 'Date', "Time In", "Time Out", "Notes"])
        self.ui.schedule_table.horizontalHeader().setStretchLastSection(True)

    # Get associate based on badge number
    def get_associate(self, badgeNum):
        associate_controller = AssociateController('TimesRecord.db')
        # Get all associates data
        associate_names = associate_controller.get_associates()

        # Find associate name that is associated with badge number
        for item in associate_names:
            if item[0] == badgeNum:
                return item[1]

    # Get all entries within provided date in date widgets and displays them onto the schedule table
    def load_tables_data(self):
        print("Loading table data")
        # Create controllers
        current_week_controller = CurrentWeekController('TimesRecord.db')
        previous_week_controller = PreviousWeekController('TimesRecord.db')
        associate_controller = AssociateController('TimesRecord.db')

        # Get all associates data
        associate_names = associate_controller.get_associates()
        # Filter associate names to only include the name
        associate_names = [associate[1] for associate in associate_names]

        # Get qdates
        qdate_begin = self.ui.begin_date.date()
        qdate_end = self.ui.end_date.date()

        # Convert qdates to datetime
        begin_date = datetime(qdate_begin.year(), qdate_begin.month(), qdate_begin.day())
        end_date = datetime(qdate_end.year(), qdate_end.month(), qdate_end.day())

        # Get this week's entries and previous week's entries within date
        all_entries = current_week_controller.get_all_entries()
        all_entries += previous_week_controller.get_entries_for_week(begin_date, end_date)

        self.ui.schedule_table.clearContents()
        # Set number of rows
        self.ui.schedule_table.setRowCount(len(all_entries))

        # Keep track of what rows we skipped
        row_skip = 0

        # Populate table with data from current_employee_entries list and associate names
        for row_index, row_data in enumerate(all_entries):
            for col_index, col_data in enumerate(row_data):
                sql_date = datetime.strptime(row_data[2], '%Y-%m-%d')

                if sql_date >= begin_date and sql_date <= end_date:
                    if col_index == 0:
                        self.ui.schedule_table.setItem(row_index - row_skip, col_index, QtWidgets.QTableWidgetItem(str(col_data)))
                    elif col_index == 1:
                        self.ui.schedule_table.setItem(row_index - row_skip, col_index, QtWidgets.QTableWidgetItem(str(self.get_associate(row_data[1]))))
                        self.ui.schedule_table.setItem(row_index - row_skip, col_index + 1, QtWidgets.QTableWidgetItem(str(col_data)))
                    else:
                        self.ui.schedule_table.setItem(row_index - row_skip, col_index + 1, QtWidgets.QTableWidgetItem(str(col_data)))
                else:
                    row_skip += 1