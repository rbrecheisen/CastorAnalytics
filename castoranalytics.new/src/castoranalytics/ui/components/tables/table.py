from PySide6.QtWidgets import (
    QWidget,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
)


class Table(QWidget):
    def __init__(self):
        self._table_widget = None

    def table_widget(self):
        if not self._table_widget:
            self._table_widget = QTableWidget()
        return self._table_widget

    def load_data(self):
        raise NotImplementedError()