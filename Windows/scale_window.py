from PySide6 import QtCore, QtGui, QtWidgets


class ScaleUI:

    def __init__(self, window, scale_factor):
        self.window = window
        self.scale_factor = scale_factor
        self.scale_ui()

    def scale_ui(self):
        # Resize the main window
        self.window.resize(int(self.window.width() * self.scale_factor), int(self.window.height() * self.scale_factor))

        # Scale all child widgets
        for widget in self.window.findChildren(QtWidgets.QWidget):
            widget.resize(int(widget.width() * self.scale_factor), int(widget.height() * self.scale_factor))
            widget.move(int(widget.x() * self.scale_factor), int(widget.y() * self.scale_factor))

