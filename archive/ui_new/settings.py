from PySide6.QtCore import QSettings

import castoranalytics.ui_new.constants as constants


class Settings(QSettings):
    def __init__(self):
        super(Settings, self).__init__(
            QSettings.IniFormat, 
            QSettings.UserScope, 
            constants.CASTOR_ANALYTICS_BUNDLE_IDENTIFIER, 
            constants.CASTOR_ANALYTICS_NAME,
        )

    def prepend_bundle_identifier_and_name(self, name):
        return '{}.{}.{}'.format(
            constants.CASTOR_ANALYTICS_BUNDLE_IDENTIFIER,
            constants.CASTOR_ANALYTICS_NAME,
            name,
        )

    def get(self, name, default=None):
        name = self.prepend_bundle_identifier_and_name(name)
        value = self.value(name)
        if value is None or value == '':
            return default
        return value

    def set(self, name, value):
        name = self.prepend_bundle_identifier_and_name(name)
        self.setValue(name, value)