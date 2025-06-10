from PySide6.QtWidgets import (
    QPushButton,
    QFormLayout,
    QLineEdit,
    QSizePolicy,
    QSpacerItem,
)

import castoranalytics.ui.constants as constants

from castoranalytics.ui.pages.basepage import BasePage
from castoranalytics.ui.utils import Label


class SettingsPage(BasePage):
    def __init__(self):
        super(SettingsPage, self).__init__(name='Settings')
        self._api_settings_label = None
        self._back_button = None
        self._client_id_field = None
        self._client_secret_field = None
        self._token_url_field = None
        self._api_base_url_field = None
        self._form = None
        self._spacer = None
        self._save_button = None
        self.init()

    def init(self):
        self._back_button = QPushButton('Back', self)
        self._back_button.clicked.connect(self.handle_back)
        self._api_settings_label = Label('API settings', type=Label.HEADING1)
        self._client_id_field = QLineEdit(self.get_setting(constants.CASTOR_ANALYTICS_SETTINGS_KEY_CLIENT_ID))
        self._client_secret_field = QLineEdit(self.get_setting(constants.CASTOR_ANALYTICS_SETTINGS_KEY_CLIENT_SECRET))
        self._token_url_field = QLineEdit(self.get_setting(
            constants.CASTOR_ANALYTICS_SETTINGS_KEY_TOKEN_URL, default=constants.CASTOR_ANALYTICS_SETTINGS_KEY_TOKEN_URL_DEFAULT))
        self._api_base_url_field = QLineEdit(self.get_setting(
            constants.CASTOR_ANALYTICS_SETTINGS_KEY_API_BASE_URL, default=constants.CASTOR_ANALYTICS_SETTINGS_KEY_API_BASE_URL_DEFAULT))
        self._form = QFormLayout()
        self._form.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow) # needed on MacOS
        self._form.addRow('Client ID:', self._client_id_field)
        self._form.addRow('Client secret:', self._client_secret_field)
        self._form.addRow('Token URL: ', self._token_url_field)
        self._form.addRow('API base URL:', self._api_base_url_field)
        self._save_button = QPushButton('Save settings', self)
        self._save_button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        self._save_button.clicked.connect(self.handle_save)
        self.get_layout().addWidget(self._back_button)
        self.get_layout().addWidget(self._api_settings_label)
        self.get_layout().addLayout(self._form)
        self.get_layout().addItem(QSpacerItem(0, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))
        self.get_layout().addWidget(self._save_button)

    def handle_back(self):
        self.back()

    def handle_save(self):
        self._settings.setValue(
            constants.CASTOR_ANALYTICS_SETTINGS_KEY_CLIENT_ID, self._client_id_field.text())
        self._settings.setValue(
            constants.CASTOR_ANALYTICS_SETTINGS_KEY_CLIENT_SECRET, self._client_secret_field.text())
        self._settings.setValue(
            constants.CASTOR_ANALYTICS_SETTINGS_KEY_TOKEN_URL, self._token_url_field.text())
        self._settings.setValue(
            constants.CASTOR_ANALYTICS_SETTINGS_KEY_API_BASE_URL, self._api_base_url_field.text())
        self.back()