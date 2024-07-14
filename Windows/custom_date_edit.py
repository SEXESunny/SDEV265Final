from PySide6.QtWidgets import QDateEdit
from PySide6.QtCore import Qt, QRect, QEvent
from PySide6.QtGui import QMouseEvent

class CustomDateEdit(QDateEdit):
    def __init__(self, parent=None):
        super(CustomDateEdit, self).__init__(parent)
        self.setButtonSymbols(QDateEdit.UpDownArrows)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            rect = self.rect()
            width = rect.width()
            height = rect.height()
            arrow_height = height // 2

            # Up arrow
            up_arrow_rect = QRect(rect.right() - 20, 0, 20, arrow_height)
            if up_arrow_rect.contains(event.pos()):
                self.stepBy(1)
                event.accept()
                return

            # Down arrow
            down_arrow_rect = QRect(rect.right() - 20, arrow_height, 20, height - arrow_height)
            if down_arrow_rect.contains(event.pos()):
                self.stepBy(-1)
                event.accept()
                return

        super(CustomDateEdit, self).mousePressEvent(event)