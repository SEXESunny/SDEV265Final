from Controllers.dummy_data_controller import DummyDataController
from PySide6 import QtCore, QtGui, QtWidgets
from Windows.log_in_window import LogInWindow
from PySide6.QtUiTools import QUiLoader

def main():
    # Remove the comment lines if you wish to delete the entries
    # db_path = 'TimesRecord.db'
    # dummy_data_controller = DummyDataController(db_path)
    # dummy_data_controller.clear_all_associates()
    # dummy_data_controller.clear_all_previous_entries()

    # Initialize DummyDataController and create tables and populate data
    # dummy_data_controller.populate_dummy_data()
    loader = QUiLoader()
    app = QtWidgets.QApplication([])

    window = LogInWindow()

    window.show()
    app.exec()


if __name__ == "__main__":
    main()