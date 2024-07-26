from PySide6 import QtCore, QtGui, QtWidgets, QtUiTools
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtWidgets import QTableView, QLineEdit, QHeaderView, QHeaderView, QPushButton, QStackedWidget, QWidget, \
    QVBoxLayout, QDialog, QDialogButtonBox, QLabel, QLineEdit, QDialogButtonBox
from PySide6.QtCore import Qt, QSortFilterProxyModel, QModelIndex, QRegularExpression, QFile
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import Signal, Slot
from Windows.scale_window import ScaleUI
import os
import sys


# While attempting to make a dialog box, I've had NOTHING but issues. A separate empty window would pop up alongside
# the dialog window. This was horrible to get working.
class AddAssociateDialog(QDialog):
    # Signal to be sent to the admin window upon accepting a finished entry.
    associate_added_signal = Signal(str, str, str)

    def __init__(self, parent=None):
        # Inherit from the admin window so we can pass signals to it.
        super(AddAssociateDialog, self).__init__(parent)
        # THIS HAS TO BE PLACED HERE FOR SOME REASON!!! THE DIALOG WILL NOT RENDER IF THIS IS NOT IN THIS EXACT SPOT!
        self.show()

        # Load our UI after showing the dialogue window.
        self.load_ui()

    def load_ui(self):
        # Call the laoder
        loader = QtUiTools.QUiLoader()
        # Provide pathing
        ui_file_path = resource_path('Windows\\AddAssociate.ui')
        ui_file = QtCore.QFile(ui_file_path)
        # Create a file in memory based off the path.
        # Debug print statements. Will leave this here for now.
        if not ui_file.exists():
            return
        # Open the file in read only mode.
        ui_file.open(QFile.ReadOnly)
        # Load the UI up using the read in file.
        self.ui = loader.load(ui_file, self)
        # Close the file after the UI successfully loads.
        ui_file.close()

        # Yet another thing that is NEEDED for the dialogue to work. I was trying to treat it like a main window
        # and it would not render. Even though I have the widgets all laid out in their own layouts, we for some reason
        # need to wrap the whole dialogue in YET ANOTHER LAYOUT FOR SOME REASON. AHHHHHHHHHHHHHHH!
        self.layout = QVBoxLayout(self)
        # Don't forget to add our layout as a widget.
        self.layout.addWidget(self.ui)

        # DO NOT DELETE THIS LOGIC! FOR SOME REASON IT IS REQUIRED OR ELSE A RANDOM EMPTY WINDOW POPS UP UPON
        # OPENING THE DIALOG. I DONT UNDERSTAND WHY BUT IT IS REQUIRED!!!!!!!!!!!!!!!
        self.button_box = self.ui.findChild(QDialogButtonBox, 'buttonBox')
        if self.button_box:
            # If the child object is found, connect our buttons.
            self.button_box.accepted.connect(self.on_ok_clicked)
            self.button_box.rejected.connect(self.reject)

    # On OK clicked event. This is yet again another thing that has to be here. When I tried to remove it and build
    # a different method, the random ghost window would pop back up. Much like everything else in this python file
    # DO NOT REMOVE!!!!!!
    def on_ok_clicked(self):
        # Retrieve form data
        badge_num = self.ui.findChild(QLineEdit, 'badge_num_edit').text()
        name = self.ui.findChild(QLineEdit, 'associate_name_edit').text()
        department = self.ui.findChild(QLineEdit, 'department_edit').text()

        # Trigger the signal and pass in the associate's info.
        self.associate_added_signal.emit(badge_num, name, department)
        # Closes the dialogue.
        self.accept()


# Ignore this, PyInstaller needs it.
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    return os.path.join(base_path, relative_path)
