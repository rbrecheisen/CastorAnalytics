from PySide6.QtCore import QSettings


class Settings(QSettings):
    def __init__(self):
        super(Settings, self).__init__(organisation='com.rbeesoft', application='castoranalytics')