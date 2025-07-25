import webbrowser

from PySide6.QtWidgets import (
    QWidget,
    QPushButton,
    QVBoxLayout,
)

import castoranalytics.ui.constants as constants

from castoranalytics.ui.settings import Settings
from castoranalytics.ui.panels.logpanel import LogPanel
from castoranalytics.core.logging import LogManager

LOG = LogManager()


class MainPanel(QWidget):
    def __init__(self, parent):
        super(MainPanel, self).__init__(parent)
        self._settings = None
        self._donate_button = None
        self._log_panel = None
        self.init_panel()

    def init_panel(self):
        layout = QVBoxLayout()
        layout.addWidget(self.donate_button())
        layout.addWidget(self.log_panel())
        self.setLayout(layout)

    # GETTERS

    def settings(self):
        if not self._settings:
            self._settings = Settings()
        return self._settings
    
    def donate_button(self):
        if not self._donate_button:
            self._donate_button = QPushButton(constants.CASTORANALYTICS_DONATE_BUTTON_TEXT)
            self._donate_button.setStyleSheet(constants.CASTORANALYTICS_DONATE_BUTTON_STYLESHEET)
            self._donate_button.clicked.connect(self.handle_donate)
        return self._donate_button

    def log_panel(self):
        if not self._log_panel:
            self._log_panel = LogPanel()
        return self._log_panel

    # EVENT HANDLERS

    def handle_donate(self):
        webbrowser.open(constants.CASTORANALYTICS_DONATE_URL)