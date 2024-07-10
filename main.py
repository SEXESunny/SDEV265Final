from Controllers.dummy_data_controller import DummyDataController
from PyQt5.QtWidgets import *
from Windows.log_in_window import *;


def main():

    
    # Remove the comment lines if you wish to delete the entries
    # db_path = 'TimesRecord.db'
    # dummy_data_controller = DummyDataController(db_path)
    # dummy_data_controller.clear_all_associates()
    # dummy_data_controller.clear_all_previous_entries()

    # Initialize DummyDataController and create tables and populate data
    # dummy_data_controller.populate_dummy_data()

    app = QApplication([])

    window = LogInWindow()

    window.show()
    app.exec_()
   

if __name__ == "__main__":
    main()
