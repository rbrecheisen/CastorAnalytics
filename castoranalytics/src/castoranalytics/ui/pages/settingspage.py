from PySide6.QtWidgets import (
    QPushButton,
    QVBoxLayout,
    QFormLayout,
    QLineEdit,
    QLabel,
    QSizePolicy,
    QSpacerItem,
)
from PySide6.QtCore import Qt

from castoranalytics.ui.pages.basepage import BasePage


class SettingsPage(BasePage):
    def __init__(self):
        super(SettingsPage, self).__init__(name='Settings')
        self._api_settings_label = None
        self._back_button = None
        self._token_url_field = None
        self._base_url_field = None
        self._client_id_field = None
        self._client_secret_field = None
        self._form = None
        self._spacer = None
        self._save_button = None

        self.init_back_button()
        self.init_form()
        self.init_save_button()
        self.init_main_page()

    def init_back_button(self):
        self._back_button = QPushButton('Back', self)
        self._back_button.clicked.connect(self.handle_back)

    def init_form(self):
        self._api_settings_label = QLabel('API settings', self)
        self._api_settings_label.setStyleSheet('font-size: 14px; font-weight: bold;')
        self._token_url_field = QLineEdit(self.get_setting('castoranalytics.token_url', default='https://data.castoredc.com/oauth/token'))
        self._base_url_field = QLineEdit(self.get_setting('castoranalytics.base_url', default='https://data.castoredc.com/api'))
        self._client_id_field = QLineEdit(self.get_setting('castoranalytics.client_id'))
        self._client_secret_field = QLineEdit(self.get_setting('castoranalytics.client_secret'))
        self._form = QFormLayout()
        self._form.addRow('API token URL: ', self._token_url_field)
        self._form.addRow('API base URL:', self._base_url_field)
        self._form.addRow('Client ID:', self._client_id_field)
        self._form.addRow('Client secret:', self._client_secret_field)

    def init_save_button(self):
        self._save_button = QPushButton('Save settings', self)
        self._save_button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        self._save_button.clicked.connect(self.handle_save)

    def init_main_page(self):
        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        layout.addWidget(self._back_button)
        layout.addWidget(self._api_settings_label)
        layout.addLayout(self._form)
        layout.addItem(QSpacerItem(0, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))
        layout.addWidget(self._save_button)
        self.setLayout(layout)

    def handle_back(self):
        self.back()

    def handle_save(self):
        self._settings.setValue('castoranalytics.token_url', self._token_url_field.text())
        self._settings.setValue('castoranalytics.base_url', self._base_url_field.text())
        self._settings.setValue('castoranalytics.client_id', self._client_id_field.text())
        self._settings.setValue('castoranalytics.client_secret', self._client_secret_field.text())
        self.back()