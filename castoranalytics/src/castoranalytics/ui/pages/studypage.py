from PySide6.QtWidgets import (
    QPushButton,
)

from castoranalytics.ui.pages.basepage import BasePage
from castoranalytics.core.logging import LogManager

LOG = LogManager()


class StudyPage(BasePage):
    def __init__(self):
        super(StudyPage, self).__init__(name='Study')
        self._back_button = None
        self.init()

    def init(self):
        self._back_button = QPushButton('Back', self)
        self._back_button.clicked.connect(self.handle_back)
        self.get_layout().addWidget(self._back_button)

    def handle_back(self):
        self.back()