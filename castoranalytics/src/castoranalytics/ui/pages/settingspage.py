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
        self._token_url_field = QLineEdit(self.get_setting('castoranalytics.token_url', default='https://data.castoredc.com/oauth/token'))
        self._api_base_url_field = QLineEdit(self.get_setting('castoranalytics.api_base_url', default='https://data.castoredc.com/api'))
        self._client_id_field = QLineEdit(self.get_setting('castoranalytics.client_id'))
        self._client_secret_field = QLineEdit(self.get_setting('castoranalytics.client_secret'))
        self._form = QFormLayout()
        self._form.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow) # needed on MacOS
        self._form.addRow('Token URL: ', self._token_url_field)
        self._form.addRow('API base URL:', self._api_base_url_field)
        self._form.addRow('Client ID:', self._client_id_field)
        self._form.addRow('Client secret:', self._client_secret_field)
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
        self._settings.setValue('castoranalytics.token_url', self._token_url_field.text())
        self._settings.setValue('castoranalytics.api_base_url', self._api_base_url_field.text())
        self._settings.setValue('castoranalytics.client_id', self._client_id_field.text())
        self._settings.setValue('castoranalytics.client_secret', self._client_secret_field.text())
        self.back()