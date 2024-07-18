from datetime import datetime, timedelta
from Models.database import Database
from Controllers.associate_controller import *
from Windows.scale_window import ScaleUI
from Models.current_week_sign_in_sign_out import CurrentWeekSignInSignOut
from Controllers.current_week_controller import *
from Controllers.previous_week_controller import *
import sys
import os
from PySide6 import QtCore, QtGui, QtWidgets, QtUiTools
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtWidgets import QTableView, QLineEdit, QHeaderView, QHeaderView, QPushButton
from PySide6.QtCore import Qt, QSortFilterProxyModel, QModelIndex, QRegularExpression
from PySide6.QtCore import QDate
from PySide6.QtWidgets import QDateEdit


class PastWindow(QtWidgets.QMainWindow):

    def __init__(self, parent, current_week_controller, previous_week_controller, associate_controller):
        super(PastWindow, self).__init__(parent)  # Pass parent to super
        self.parent = parent  # Store the parent reference
        self.current_week_controller = current_week_controller
        self.previous_week_controller = previous_week_controller
        self.associate_controller = associate_controller

        # Normal UI loading logic that all QWindows need.
        loader = QtUiTools.QUiLoader()
        ui_file_path = resource_path('Windows\\PastWindow.ui')
        ui_file = QtCore.QFile(ui_file_path)
        ui_file.open(QtCore.QFile.ReadOnly)
        self.ui = loader.load(ui_file, None)
        ui_file.close()

        # Set the UI as the central widget
        self.setCentralWidget(self.ui)

        # Scale UI
        ScaleUI(self, 1.5)

        # Initialize UI.
        self.init_ui()

        # Set default dates, set up our tables, load them and setup filtering.
        self.set_default_dates()
        self.setup_tables()
        self.load_tables_data()
        self.setup_filtering()

        # Connect buttons to their respective functions
        try:
            self.ui.back_button.clicked.connect(self.back_to_current_view)
            self.ui.begin_date.dateChanged.connect(self.load_tables_data)
            self.ui.end_date.dateChanged.connect(self.load_tables_data)
            self.update_button.clicked.connect(self.update_changes)
        except Exception as e:
            print(f"Error connecting buttons: {e}")

        # Changed_entries is used to see what entries have changes made to them. This is needed for our update method
        self.changed_entries = {}
        # QStandardItem has a handy dataChanged event we can use!
        self.model.dataChanged.connect(self.data_changed)

        # Show the main window
        self.show()

    # Initialize UI by finding child elements and attaching them to fields.
    def init_ui(self):
        self.table_view = self.ui.findChild(QTableView, 'past_week_time_table')
        if not self.table_view:
            raise ValueError("TableView 'current_week_time_table' not found in the UI file.")
        self.name_filter = self.ui.findChild(QLineEdit, 'name_filter')
        self.department_filter = self.ui.findChild(QLineEdit, 'department_filter')
        self.update_button = self.ui.findChild(QPushButton, 'update_button')

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

    # Set the stack widget back to the current week view.
    def back_to_current_view(self):
        self.parent.stacked_widget.setCurrentWidget(self.parent.current_week_view)  # Switch back to main view
        self.parent.load_table_data()

    # Set up our data table
    def setup_tables(self):
        # Our past weekly view has 7 total columns
        self.model = QStandardItemModel(0, 7)
        self.model.setHorizontalHeaderLabels(
            ['Associate', 'Department', 'Badge Number', 'Date', 'Time In', 'Time Out', 'Notes'])

        # Assign the model to the QTableView
        self.table_view.setModel(self.model)

        # Configure the QTableView properties
        self.table_view.setSelectionBehavior(QTableView.SelectRows)
        self.table_view.setEditTriggers(
            QTableView.DoubleClicked | QTableView.SelectedClicked | QTableView.EditKeyPressed)
        self.table_view.setAlternatingRowColors(True)
        self.table_view.horizontalHeader().setStretchLastSection(True)
        self.table_view.verticalHeader().setSectionResizeMode(QHeaderView.Fixed)

        # Set width of the vertical header
        self.table_view.verticalHeader().setFixedWidth(40)  # Adjust the width value as needed
        self.table_view.setColumnWidth(0, 140)
    # Load Data
    def load_tables_data(self):

        # Get qdates
        qdate_begin = self.ui.begin_date.date()
        qdate_end = self.ui.end_date.date()

        # Convert qdates to datetime
        begin_date = datetime(qdate_begin.year(), qdate_begin.month(), qdate_begin.day())
        end_date = datetime(qdate_end.year(), qdate_end.month(), qdate_end.day())

        # Get this week's entries and previous week's entries within date range
        all_entries = self.previous_week_controller.get_entries_for_week(begin_date, end_date)

        # Clear existing data in the model
        self.model.setRowCount(0)

        # Populate table with data from entries within the date range
        for entry in all_entries:
            # Unpack our tuple.
            record_id, badge_num, date, sign_in_time, sign_out_time, notes = entry
            # Parse the date and format it correctly.
            sql_date = datetime.strptime(date, '%Y-%m-%d')

            # If our date is between the two ranges, then display the data.
            if begin_date <= sql_date <= end_date:
                # Get associate info since it isn't present in the previous weeks table.
                associate_info = self.associate_controller.get_associate_by_badge(badge_num)
                if associate_info:
                    # Unpack the tuple.
                    name, department = associate_info
                    # Assign each item into a list.
                    row_data = [name, department, badge_num, date, sign_in_time, sign_out_time, notes]
                    # Convert the items to a QStandardItem.
                    items = [QStandardItem(str(item)) for item in row_data]
                    # Also include the record_
                    items[0].setData(record_id, Qt.UserRole)
                    # Append the row.
                    self.model.appendRow(items)

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
            self.previous_week_controller.update_entry(record_id, sign_in_time, sign_out_time, additional_notes)

        # Clear the table.
        self.changed_entries.clear()
        # Reload the table.
        self.load_tables_data()
# Method for PyInstaller
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    return os.path.join(base_path, relative_path)
