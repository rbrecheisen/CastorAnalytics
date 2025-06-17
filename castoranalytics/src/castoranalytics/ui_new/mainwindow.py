from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
)
from PySide6.QtGui import (
    QGuiApplication,
    QIcon,
    QAction,
)
from PySide6.QtCore import Qt, QByteArray

import castoranalytics.ui_new.constants as constants
from castoranalytics.ui_new.settings import Settings


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self._settings = self.init_settings()
        self.init_geometry_and_state()

    # INITIALIZATION

    def init_settings(self):
        return Settings()

    def init_geometry_and_state(self):
        if not self.load_geometry_and_state():
            self.set_default_size_and_position()

    # GET

    def get_settings(self):
        return self._settings

    # EVENTS

    def closeEvent(self, event):
        self.save_geometry_and_state()
        return super().closeEvent(event)

    # MISCELLANEOUS

    def load_geometry_and_state(self):
        geometry = self.get_settings().get('window/geometry', None)
        state = self.get_settings().get('window/state', None)
        if isinstance(geometry, QByteArray) and self.restoreGeometry(geometry):
            if isinstance(state, QByteArray):
                self.restoreState(state)
            return True
        return False

    def save_geometry_and_state(self):
        self.get_settings().set('window/geometry', self.saveGeometry())
        self.get_settings().set('window/state', self.saveState())

    def set_default_size_and_position(self):
        self.resize(constants.CASTOR_ANALYTICS_WINDOW_W, constants.CASTOR_ANALYTICS_WINDOW_H)
        self.center_window()

    def center_window(self):
        screen = QGuiApplication.primaryScreen().geometry()
        x = (screen.width() - self.geometry().width()) / 2
        y = (screen.height() - self.geometry().height()) / 2
        self.move(int(x), int(y))