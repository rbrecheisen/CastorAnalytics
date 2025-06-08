from PySide6.QtCore import QSettings


class Settings(QSettings):
    def __init__(self):
        super(Settings, self).__init__(QSettings.IniFormat, QSettings.UserScope, 'com.rbeesoft', 'castoranalytics')

    def get(self, name, default=None):
        value = self.value(name)
        if value is None or value == '':
            return default
        return value

    def set(self, name, value):
        self.setValue(name, value)