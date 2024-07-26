from PySide6 import QtCore, QtGui, QtWidgets, QtUiTools
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtWidgets import QTableView, QLineEdit, QHeaderView, QHeaderView, QPushButton, QStackedWidget, QWidget
from PySide6.QtCore import Qt, QSortFilterProxyModel, QModelIndex, QRegularExpression, QFile
from PySide6.QtUiTools import QUiLoader
import os
import sys
from Windows.scale_window import ScaleUI
from Windows.AddAssociatesDialog import AddAssociateDialog


# Admin window to add and remove associates.
class AdminWindow(QtWidgets.QMainWindow):

    # Inherit our controllers from the parent.
    def __init__(self, parent, current_week_controller, previous_week_controller, associate_controller):
        super(AdminWindow, self).__init__(parent)
        self.parent = parent
        self.current_week_controller = current_week_controller
        self.previous_week_controller = previous_week_controller
        self.associate_controller = associate_controller

        # Same load file logic that all Qt windows need.
        loader = QtUiTools.QUiLoader()
        ui_file_path = resource_path('Windows\\AdminWindow.ui')
        ui_file = QtCore.QFile(ui_file_path)
        ui_file.open(QtCore.QFile.ReadOnly)
        self.ui = loader.load(ui_file, None)
        ui_file.close()

        # Set the UI as the central widget. This is needed or else it will not render.
        self.setCentralWidget(self.ui)

        # Scale UI
        ScaleUI(self, 1.5)

        # Initialize our UI.
        self.init_ui()
        # Set up our tableview.
        self.setup_tables()
        # Populate the tableview with info.
        self.load_table_data()

        # Connect buttons to their respective functions
        try:
            self.ui.back_button.clicked.connect(self.back_to_current_view)
            self.ui.add_button.clicked.connect(self.open_add_associate_dialog)
            self.ui.remove_button.clicked.connect(self.remove_selected_associate)

        except Exception as e:
            print(f"Error connecting buttons: {e}")

        # Show the main window
        self.show()

    # Basic UI initialization to assign our buttons to fields within the class.
    def init_ui(self):
        self.table_view = self.ui.findChild(QTableView, 'admin_table_view')
        self.back_button = self.ui.findChild(QPushButton, 'back_button')
        self.add_button = self.ui.findChild(QPushButton, 'add_button')
        self.remove_button = self.ui.findChild(QPushButton, 'remove_button')
        if not self.remove_button:
            raise ValueError("Remove button 'remove_button' not found in the UI file.")
        if not self.table_view:
            raise ValueError("TableView 'admin_table_view' not found in the UI file.")

    # Logic to set up the table. For some reason, even though all of these fields were set in our
    def setup_tables(self):
        # Create a model with columns matching your database table. There's only 3 columns for the associate table.
        # Set rows to 0, as our load method will handle populating the rows.
        self.model = QStandardItemModel(0, 3)
        self.model.setHorizontalHeaderLabels(['Badge Number', 'Name', 'Department'])

        # Assign the model to the QTableView
        self.table_view.setModel(self.model)

        # Configure the QTableView properties. This is also done in the UI but I was getting frustrated using the UI
        # designer and just ended up doing it here.
        self.table_view.setSelectionBehavior(QTableView.SelectRows)
        self.table_view.setEditTriggers(
            QTableView.DoubleClicked | QTableView.SelectedClicked | QTableView.EditKeyPressed)
        self.table_view.setAlternatingRowColors(True)
        self.table_view.horizontalHeader().setStretchLastSection(True)
        self.table_view.verticalHeader().setSectionResizeMode(QHeaderView.Fixed)

        # Set width of the vertical header
        self.table_view.verticalHeader().setFixedWidth(40)
        # Badge Column
        self.table_view.setColumnWidth(0, 140)
        # Name Column
        self.table_view.setColumnWidth(1, 140)

    # Set our current widget view to the Current View Window.
    def back_to_current_view(self):
        self.parent.stacked_widget.setCurrentWidget(self.parent.current_week_view)  # Switch back to main view
        self.parent.load_table_data()

    # Load table data method.
    def load_table_data(self):
        # Get all of our entries.
        entries = self.parent.associate_controller.get_associates()
        # Clear our current data.
        self.model.setRowCount(0)

        # Loop through each entry.
        for entry in entries:
            # List comprehension to turn each item within the tuple to a QStandardItem object. This is needed for the
            # table to display the items.
            items = [QStandardItem(str(item)) for item in entry]
            # Append the list to the table as a row.
            self.model.appendRow(items)

    # Loads our god forsaken dialog window.
    def open_add_associate_dialog(self):
        # Assign the dialog object as a field. Also we HAVE to pass in self as a parameter. Will not render without it.
        self.addAssociateWindow = AddAssociateDialog(self)
        # DON'T REMOVE THIS EITHER! THIS BREAKS THE DIALOG! EVEN IF THE BUTTON IS NEVER PRESSED IT WILL NOT RENDER
        # WITHOUT IT! It is used to call the method to add the associate based off the provided info.
        self.addAssociateWindow.associate_added_signal.connect(
            self.add_associate_to_backend)
        # Close our window after adding the associate.
        self.addAssociateWindow.close()

    # Add our assocaite to the table.
    def add_associate_to_backend(self, badge_num, name, department):
        # Call the controller to add the associate
        self.associate_controller.add_associate(badge_num, name, department)
        # Refresh our table.
        self.load_table_data()
        # Add the associate to the current weekly entries, so they can fill out their worked hours.
        self.add_associate_blank_entries(badge_num)

    # Remove the currently selected associate.
    def remove_selected_associate(self):
        # Get index of current selection.
        selected_indexes = self.table_view.selectedIndexes()
        if selected_indexes:
            # Only delete the first selected row. I think it could be pretty dangerous to allow a mass delete.
            selected_row = selected_indexes[0].row()
            # Get the badge number of the selected row to pass in to the remove associate method.
            badge_num = self.model.item(selected_row, 0).text()
            # Call the controller to remove the associate
            self.associate_controller.remove_associate(badge_num)
            # Remove the row from the table
            self.model.removeRow(selected_row)
            # Refresh the table.
            self.load_table_data()

    # Method to populate our weekly entries with blank entries for the newly added associate.
    def add_associate_blank_entries(self, badge_num):
        # Get dates of current week.
        dates = self.current_week_controller.get_current_week_dates()
        for date in dates:
            # Format in Y-M-D format.
            date_str = date.strftime('%Y-%m-%d')
            # Add the blank entry.
            self.current_week_controller.add_entry(badge_num, date_str, '', '', '')

# Ignore this, PyInstaller needs it.
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    return os.path.join(base_path, relative_path)
