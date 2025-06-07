from PySide6.QtWidgets import (
    QPushButton,
    QVBoxLayout,
)
from PySide6.QtCore import Qt

from castoranalytics.ui.pages.basepage import BasePage


class SettingsPage(BasePage):
    def __init__(self):
        super(SettingsPage, self).__init__(name='Settings')
        button = QPushButton('Go to home', self)
        button.clicked.connect(self.handle_go_to_home)
        self._layout = QVBoxLayout(self)
        self._layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self._layout.addWidget(button)
        self.setLayout(self._layout)

    def handle_go_to_home(self):
        self.navigate('/home')