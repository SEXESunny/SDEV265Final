from datetime import datetime
from Models.database import Database
from Controllers.associate_controller import *
from Models.associate import *
import os
import sys
import shutil
from Windows.scale_window import ScaleUI
from Controllers.current_week_controller import *
from Controllers.previous_week_controller import *
from Controllers.date_transfer_controller import *
from Windows.past_window import PastWindow
from Windows.admin_window import AdminWindow
from PySide6 import QtCore, QtGui, QtWidgets, QtUiTools
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtWidgets import QTableView, QLineEdit, QHeaderView, QHeaderView, QPushButton, QStackedWidget, QWidget, QApplication
from PySide6.QtCore import Qt, QSortFilterProxyModel, QModelIndex, QRegularExpression


# This is our main window for all the stack widgets to reside in. It makes the most sense to me since this is the view
# that most employees will interact with.
class CurrentViewWindow(QtWidgets.QMainWindow):
    # Inherit from the QMainWindow
    def __init__(self):
        super(CurrentViewWindow, self).__init__()

        self.setStyleSheet("background-color: white;") #White color added since there is a weird gap on the left and top borders showing gray space.
        self.setWindowTitle("Clock In / Clock Out")
        # Normal UI loading logic that all QWindows need.
        loader = QtUiTools.QUiLoader()
        ui_file_path = resource_path('Windows//CurrentView.ui')
        ui_file = QtCore.QFile(ui_file_path)
        if not ui_file.exists():
            print(f"Unable to find {ui_file.fileName()}")
        ui_file.open(QtCore.QFile.ReadOnly)

        # LEAVE THE SECOND ARGUMENT AS NONE!
        self.ui = loader.load(ui_file, None)
        ui_file.close()

        # In order to make the application feel more like a single window instead of a bunch of different windows
        # popping up on every click, we can use a QStackedWidget and add all the other views to this stack.
        # Then set the main widget to whatever view is selected.
        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        # Initialize our controllers.
        # Define the path to the database file in the current directory
        # All of the following pathing logic was just for my network drive at work. It is not relevant for the actual
        # project.
        self.db_name = 'TimesRecord.db'
        self.db_dir = os.path.join(os.path.abspath("."), 'Database')
        self.db_path = os.path.join(self.db_dir, self.db_name)

        # Ensure the Database directory exists in the current directory
        if not os.path.exists(self.db_dir):
            os.makedirs(self.db_dir)

        # Ensure the database is only copied from resources if it does not already exist
        if not os.path.exists(self.db_path):
            shutil.copy(resource_path(f'Database/{self.db_name}'), self.db_path)
        self.current_week_controller = CurrentWeekController(self.db_path)
        self.previous_week_controller = PreviousWeekController(self.db_path)
        self.associate_controller = AssociateController(self.db_path)
        self.date_transfer_controller = DataTransferController(self.db_path)

        # Check if it's a new week, if so populate it with blank entries and transfer current entries to the past.
        self.date_transfer_controller.check_and_update_week()

        # Initialize main view
        self.current_week_view = QWidget()
        # Assign our view a QVBoxLayout. This was needed or else it wouldn't render.
        current_week_layout = QtWidgets.QVBoxLayout()
        # Set the layout
        self.current_week_view.setLayout(current_week_layout)
        current_week_layout.addWidget(self.ui)

        # Initialize other views
        self.past_view = PastWindow(self, self.current_week_controller, self.previous_week_controller,
                                    self.associate_controller)
        self.admin_view = AdminWindow(self, self.current_week_controller, self.previous_week_controller,
                                      self.associate_controller)

        # Add views to the QStackedWidget
        self.stacked_widget.addWidget(self.current_week_view)
        self.stacked_widget.addWidget(self.past_view)
        self.stacked_widget.addWidget(self.admin_view)

        # Set the initial view
        self.stacked_widget.setCurrentWidget(self.current_week_view)

        # Enforce a fixed size for the main window
        self.setFixedSize(1095, 800)

        ScaleUI(self, 1.5)

        # Call our UI initialization.
        self.init_ui()

        # Connect buttons to their respective functions
        self.ui.past_view_button.clicked.connect(self.switch_to_past_view)
        self.ui.admin_view_button.clicked.connect(self.switch_to_admin_view)
        self.update_button.clicked.connect(self.update_changes)
        self.day_toggle_button.toggled.connect(self.on_toggle)

        # Set up tables and load data
        self.setup_tables()
        self.load_table_data()
        self.setup_filtering()

        # Changed_entries is used to see what entries have changes made to them. This is needed for our update method.
        self.changed_entries = {}
        # QStandardItem has a handy dataChanged event we can use!
        self.model.dataChanged.connect(self.data_changed)

        # Show the main window
        self.show()

    # Change the text and button styling depending on toggle state.
    def on_toggle(self, checked):
        if checked:
            self.day_toggle_button.setText("Today Toggle: ON")
            self.day_toggle_button.setStyleSheet(self.get_stylesheet(True))
        else:
            self.day_toggle_button.setText("Today Toggle: OFF")
            self.day_toggle_button.setStyleSheet(self.get_stylesheet(False))
        self.filter_table_by_day(checked)

    # Push custom styling to the button depending on if it's toggled or not.
    def get_stylesheet(self, checked):
        if checked:
            return """
                QPushButton {
                    border: None; 
                    border-radius: 5px;
                    border-right: 2.7px solid rgb(43, 43, 43); 
                    border-bottom: 2.7px solid rgb(43, 43, 43);
                    background-color: #5AA86F;  /* Pastel green */
                    color: white;
                    letter-spacing: 1px;
                    font-size: 25px;
                }
                QPushButton:checked {
                    background-color: #5AA86F;  /* Pastel green */
                }
                QPushButton:hover {
                    color: rgb(238, 237, 240);  /* Gray */
                    background-color: #79B679;  /* Dark Pastel green */
                }
            """
        else:
            return """
                QPushButton {
                    border: None; 
                    border-radius: 5px;
                    border-right: 2.7px solid rgb(43, 43, 43); 
                    border-bottom: 2.7px solid rgb(43, 43, 43);
                    background-color: rgb(78, 149, 213);  /* Original blue */
                    color: white;
                    letter-spacing: 1px;
                    font-size: 25px;
                }
                QPushButton:checked {
                    background-color: #5AA86F;  /* Pastel green */
                }
                QPushButton:hover {
                    color: rgb(238, 237, 240);      /* Gray */
                    background-color: rgb(44, 112, 160);   /* Luh Darky Bluey */
                }
            """

    # If our past views button is pressed, set the stack widget to focus on the past views.
    def switch_to_past_view(self):
        self.stacked_widget.setCurrentWidget(self.past_view)

        # Refresh data if needed.
        self.past_view.load_tables_data()

    # If the admin view is pressed, set the stack widget to focus on the admin view.
    def switch_to_admin_view(self):
        self.stacked_widget.setCurrentWidget(self.admin_view)

        # Refresh data if needed.
        self.admin_view.load_table_data()

    # The login is not used anymore. After displaying the application to employees at work, everyone agreed that it was
    # more of a nuisance. The logic will be left in place if it is ever needed again.
    def back_to_log_in(self):
        self.stacked_widget.setCurrentWidget(self.log_in_view)

    # Initialize UI by finding child elements and attaching them to fields.
    def init_ui(self):
        self.table_view = self.ui.findChild(QTableView, 'current_week_time_table')
        if not self.table_view:
            raise ValueError("TableView 'current_week_time_table' not found in the UI file.")
        self.name_filter = self.ui.findChild(QLineEdit, 'name_filter')
        self.department_filter = self.ui.findChild(QLineEdit, 'department_filter')
        self.update_button = self.ui.findChild(QPushButton, 'update_button')
        self.day_toggle_button = self.ui.findChild(QPushButton, 'day_toggle_button')
        self.day_toggle_button.setCheckable(True)
        self.day_toggle_button.setStyleSheet(self.get_stylesheet(False))

    # Set up our data table.
    def setup_tables(self):
        # Our current weekly view has 7 total columns.
        self.model = QStandardItemModel(0, 7)
        self.model.setHorizontalHeaderLabels(
            ['Associate', 'Department', 'Badge Number', 'Date', 'Time In', 'Time Out', 'Notes'])

        # Assign the model to the QTableView
        self.table_view.setModel(self.model)

        # Configuring properties here. Got lazy using the editor, and it was easier to force certain properties via code.
        self.table_view.setSelectionBehavior(QTableView.SelectRows)
        self.table_view.setEditTriggers(
            QTableView.DoubleClicked | QTableView.SelectedClicked | QTableView.EditKeyPressed)
        self.table_view.setAlternatingRowColors(True)
        self.table_view.horizontalHeader().setStretchLastSection(True)
        self.table_view.verticalHeader().setSectionResizeMode(QHeaderView.Fixed)

        # Set width of the vertical header
        self.table_view.verticalHeader().setFixedWidth(40)  # Adjust the width value as needed
        # Set width of our name column to be longer since this will be our longest column next to the notes section.
        self.table_view.setColumnWidth(0, 140)

    # Load data.
    def load_table_data(self):
        # Get each entry from the controller.
        entries = self.current_week_controller.get_all_entries()
        self.model.setRowCount(0)

        for entry in entries:
            # Unpack our retrieved tuple
            record_id, badge_num, date, sign_in_time, sign_out_time, notes = entry
            # Since our current week controller doesn't record names, we need to also grab a name and department to
            # display.
            associate_info = self.associate_controller.get_associate_by_badge(badge_num)
            # If the name is valid
            if associate_info:
                # Retrieve the name and department.
                name, department = associate_info
                # Recombine the tuple
                row_data = [name, department, badge_num, date, sign_in_time, sign_out_time, notes]
                # Turn each item into a QStandardItem.
                items = [QStandardItem(str(item)) for item in row_data]
                # We need the record ID to interact with the controller, but we don't want to display it. That's why
                # we will use UserRole.
                items[0].setData(record_id, Qt.UserRole)
                # Append the row to the table.
                self.model.appendRow(items)

    # Logic to set our filtering up.
    def setup_filtering(self):
        # A proxy model is needed to filter. This is the layer between the view and the model.
        self.proxy_model = QSortFilterProxyModel()
        # Set our source model as the standard item model defined in our setup tables method.
        self.proxy_model.setSourceModel(self.model)
        # -1 means apply to ALL columns.
        self.proxy_model.setFilterKeyColumn(0)

        # Set our TableView's model to the proxy model made here.
        self.table_view.setModel(self.proxy_model)
        # Connect our text changed event to the filter table method.
        self.name_filter.textChanged.connect(self.filter_table)
        self.department_filter.textChanged.connect(self.filter_table)

    # Filtering method.
    def filter_table(self):
        # Grab the text from the filter fields and assign them to our class' fields
        name_filter_text = self.name_filter.text()
        department_filter_text = self.department_filter.text()

        # Create regular expressions for both filters. We want to pass in our filtered text, and we don't want case
        # sensitivity.
        name_reg_exp = QRegularExpression(name_filter_text, QRegularExpression.CaseInsensitiveOption)
        department_reg_exp = QRegularExpression(department_filter_text, QRegularExpression.CaseInsensitiveOption)

        # Logic to handle what filter to apply depending on which
        if name_filter_text and department_filter_text:
            # Filter using both name and department. This shouldn't happen so just pass in an empty regular expression.
            self.proxy_model.setFilterRegularExpression(QRegularExpression())
            # Apply it to all columns.
            # You can in fact build a custom filter proxy model but I am not worried about it right now.
            self.proxy_model.setFilterKeyColumn(-1)
            # Just pick the department since that's likely the last thing they'll enter if both fields are filled out.
            self.proxy_model.setFilterFixedString(department_filter_text)
        elif name_filter_text:
            # Filter using name only
            self.proxy_model.setFilterKeyColumn(0)
            # Apply our name_reg_exp
            self.proxy_model.setFilterRegularExpression(name_reg_exp)
        elif department_filter_text:
            # Filter using department only
            self.proxy_model.setFilterKeyColumn(1)  # Assuming department is in the second column
            # Apply our department_reg_exp.
            self.proxy_model.setFilterRegularExpression(department_reg_exp)
        else:
            # No filter
            self.proxy_model.setFilterRegularExpression(QRegularExpression())
        # Since the filter is called when a new letter is typed, we also need to check if the day button is toggled.
        self.filter_table_by_day(self.day_toggle_button.isChecked())

    # Filter our table and only show results for today. Makes it easier to find your day to sign out if the table is
    # big.
    def filter_table_by_day(self, show_today):
        if not show_today:
            for row in range(self.model.rowCount()):
                self.table_view.setRowHidden(row, False)
            return

        today_start, today_end = self.get_today_range()

        for row in range(self.model.rowCount()):
            # Get date
            date_str = self.model.item(row, 3).text()
            # Turn it into a datetime object.
            event_date = datetime.strptime(date_str, "%Y-%m-%d")
            # The get_today_range method handles returning a valid day range. We ONLY care about the events that match
            # the start date. This is because if it's 2:00 AM of the next day, it'll filter and only show the next day
            # results.
            if today_start.date() == event_date.date():
                self.table_view.setRowHidden(row, False)
            else:
                self.table_view.setRowHidden(row, True)

    # Data changed method. The dataChanged event takes these exact arguments.
    def data_changed(self, top_left, bottom_right, roles):
        # For each row from the top left to the bottom right + 1 since range doesn't include the end.
        for row in range(top_left.row(), bottom_right.row() + 1):
            # For each column within the row
            for column in range(top_left.column(), bottom_right.column() + 1):
                # Get the index of our iteration.
                index = self.model.index(row, column)
                # Get the text value at the index.
                value = self.model.data(index, Qt.DisplayRole)
                # If our row isn't already a part of the changed_entries field, allot the row.
                if row not in self.changed_entries:
                    self.changed_entries[row] = {}
                # Set the value at this index.
                self.changed_entries[row][column] = value

    # Update our changes.
    def update_changes(self):
        # For each row and column that needs to be changed.
        for row, columns in self.changed_entries.items():
            # Get the index of our record_id.
            record_id_index = self.model.index(row, 0)
            # Sign in time index
            sign_in_time_index = self.model.index(row, 4)
            # Sign out time index
            sign_out_time_index = self.model.index(row, 5)
            # Additional notes index
            additional_notes_index = self.model.index(row, 6)

            # Get the record number after providing the QModelIndex of it.
            record_id = self.model.data(record_id_index, Qt.UserRole)
            # Get sign in time data
            sign_in_time = self.model.data(sign_in_time_index, Qt.DisplayRole)
            # Get sign out time data
            sign_out_time = self.model.data(sign_out_time_index, Qt.DisplayRole)
            # Get additional notes data.
            additional_notes = self.model.data(additional_notes_index, Qt.DisplayRole)

            # Call our update entry method from the controller.
            self.current_week_controller.update_entry(record_id, sign_in_time, sign_out_time, additional_notes)

        # Clear the table.
        self.changed_entries.clear()
        # Reload the table.
        self.load_table_data()

    # 1st shift associates start at 6:00 AM. 2nd shift associates start at 4:30 PM but clock out anywhere between
    # 1:00 AM and 4:00 AM of the next day. This logic will return the date range of a full workday.
    def get_today_range(self):
        now = datetime.now()
        # Calculate the start of today as 6:00 AM of the current date
        today_start = datetime.combine(now.date(), datetime.min.time()) + timedelta(hours=6)
        # Calculate the end of today as 4:00 AM of the next day
        today_end = today_start + timedelta(hours=22)
        # If the current time is before 6:00 AM, adjust to the previous day.
        if now < today_start:
            today_start -= timedelta(days=1)
            today_end -= timedelta(days=1)
        return today_start, today_end


# Necessary method for pyinstaller to work at my workplace.
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    return os.path.join(base_path, relative_path)
