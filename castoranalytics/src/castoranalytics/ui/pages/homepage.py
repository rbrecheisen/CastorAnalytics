from PySide6.QtWidgets import (
    QPushButton,
    QVBoxLayout,
)
from PySide6.QtCore import Qt

from castoranalytics.ui.pages.basepage import BasePage


class HomePage(BasePage):
    def __init__(self):
        super(HomePage, self).__init__(name='Home')
        button = QPushButton('Go to settings', self)
        button.clicked.connect(self.handle_go_to_settings)
        self._layout = QVBoxLayout(self)
        self._layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self._layout.addWidget(button)
        self.setLayout(self._layout)

    def handle_go_to_settings(self):
        self.navigate('/settings')