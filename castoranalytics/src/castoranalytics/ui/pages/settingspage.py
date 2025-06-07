from PySide6.QtWidgets import (
    QPushButton,
    QVBoxLayout,
    QFormLayout,
    QLineEdit,
    QLabel,
    QMessageBox,
    QSizePolicy,
    QSpacerItem,
)
from PySide6.QtCore import Qt

from castoranalytics.ui.pages.basepage import BasePage
from castoranalytics.ui.settings import Settings


class SettingsPage(BasePage):
    def __init__(self):
        super(SettingsPage, self).__init__(name='Settings')
        self._settings = Settings()
        self._api_settings_label = None
        self._go_back_button = None
        self._token_url_field = None
        self._base_url_field = None
        self._client_id_field = None
        self._client_secret_field = None
        self._form = None
        self._spacer = None
        self._save_button = None
        self.init()

    def get_setting(self, name, default=None):
        value = self._settings.value(name)
        if value is None or value == '':
            return default
        return value

    def init(self):
        self._api_settings_label = QLabel('API settings', self)
        self._api_settings_label.setStyleSheet('font-size: 14px; font-weight: bold;')
        self._go_back_button = QPushButton('Go back', self)
        self._go_back_button.clicked.connect(self.handle_go_back)
        self._token_url_field = QLineEdit(self.get_setting('castoranalytics.token_url', default='https://data.castoredc.com/oauth/token'))
        self._base_url_field = QLineEdit(self.get_setting('castoranalytics.base_url', default='https://data.castoredc.com/api'))
        self._client_id_field = QLineEdit(self.get_setting('castoranalytics.client_id'))
        self._client_secret_field = QLineEdit(self.get_setting('castoranalytics.client_secret'))
        self._form = QFormLayout()
        self._form.addRow('API token URL: ', self._token_url_field)
        self._form.addRow('API base URL:', self._base_url_field)
        self._form.addRow('Client ID:', self._client_id_field)
        self._form.addRow('Client secret:', self._client_secret_field)
        self._save_button = QPushButton('Save settings', self)
        self._save_button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        self._save_button.clicked.connect(self.handle_save)
        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        layout.addWidget(self._go_back_button)
        layout.addWidget(self._api_settings_label)
        layout.addLayout(self._form)
        layout.addItem(QSpacerItem(0, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))
        layout.addWidget(self._save_button)
        self.setLayout(layout)

    def handle_go_back(self):
        self.back()

    def handle_save(self):
        self._settings.setValue('castoranalytics.token_url', self._token_url_field.text())
        self._settings.setValue('castoranalytics.base_url', self._base_url_field.text())
        self._settings.setValue('castoranalytics.client_id', self._client_id_field.text())
        self._settings.setValue('castoranalytics.client_secret', self._client_secret_field.text())
        # QMessageBox.information(self, 'Success', 'Settings saved successfully')
        self.back()