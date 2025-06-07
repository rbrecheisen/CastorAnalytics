from PySide6.QtWidgets import (
    QPushButton,
    QVBoxLayout,
    QLabel,
)
from PySide6.QtCore import Qt

from castoranalytics.ui.pages.basepage import BasePage
from castoranalytics.core import Core


class StudyListPage(BasePage):
    def __init__(self):
        super(StudyListPage, self).__init__(name='Studies')
        self._settings_button = None
        self._layout = None
        self._study_list_layout = None

        self.init_settings_button()
        self.init_study_list_layout()
        self.init_main_page()

    def init_settings_button(self):
        self._settings_button = QPushButton('Go to settings', self)
        self._settings_button.clicked.connect(self.handle_go_to_settings)

    def init_study_list_layout(self):
        self._study_list_layout = QVBoxLayout()

    def init_main_page(self):
        self._layout = QVBoxLayout(self)
        self._layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self._layout.addWidget(self._settings_button)
        self._layout.addLayout(self._study_list_layout)
        self.setLayout(self._layout)

    def handle_go_to_settings(self):
        self.navigate('/settings')

    def showEvent(self, event):
        # Clear all widget in study list layout
        while self._study_list_layout.count():
            item = self._study_list_layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.setParent(None)
        # Check if API credentials available
        client_id = self.get_setting('castoranalytics.client_id', None)
        client_secret = self.get_setting('castoranalytics.client_secret', None)
        if client_id is None or client_secret is None:
            self._study_list_layout.addWidget(QLabel('It looks like your API settings are incomplete. Please go to settings.'))
        else:
            studies = Core().get_studies()
            for study in studies:
                self._study_list_layout.addWidget(QLabel(study))
        return super().showEvent(event)