from Controllers.dummy_data_controller import DummyDataController
from Controllers.associate_controller import AssociateController
from Controllers.previous_week_controller import PreviousWeekController
from Controllers.current_week_controller import CurrentWeekController
from Windows.current_view_window import CurrentViewWindow
from Windows.past_window import PastWindow
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QStackedWidget
import resources_rc
import sys


def main():
    # Remove the comment lines if you wish to delete the entries
    # db_path = 'TimesRecord.db'
    # dummy_data_controller = DummyDataController(db_path)
    # dummy_data_controller.clear_all_associates()
    # dummy_data_controller.clear_all_previous_entries()

    # Initialize DummyDataController and create tables and populate data
    # dummy_data_controller.populate_dummy_data()

    loader = QUiLoader()
    # Create an instance of QApplication which manages application-wide resources
    app = QtWidgets.QApplication(sys.argv)
    window = CurrentViewWindow()
    window.show()
    # Start the main event loop and pass its return value to sys.exit() to exit the application correctly
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
