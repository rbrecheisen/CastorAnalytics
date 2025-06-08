from PySide6.QtWidgets import (
    QPushButton,
    QVBoxLayout,
    QLabel,
    QTableWidget,
    QTableWidgetItem,
    QHeaderView,
    QSizePolicy,
)
from PySide6.QtCore import Qt

from castoranalytics.ui.pages.basepage import BasePage
from castoranalytics.core import Core
from castoranalytics.core.logging import LogManager

LOG = LogManager()


class StudyPage(BasePage):
    def __init__(self):
        super(StudyPage, self).__init__(name='Study')
        self._back_button = None
        self._layout = None
        self.init()

    def init(self):
        self._back_button = QPushButton('Back', self)
        self._back_button.clicked.connect(self.handle_back)
        self._layout = QVBoxLayout(self)
        self._layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self._layout.addWidget(self._back_button)
        self.setLayout(self._layout)

    def handle_back(self):
        self.back()