import os

from PySide6.QtWidgets import (
    QMainWindow,
)
from PySide6.QtGui import (
    QGuiApplication,
    QIcon,
    QAction,
)
from PySide6.QtCore import Qt, QByteArray

import castoranalytics.ui.constants as constants

from castoranalytics.ui.settings import Settings
from castoranalytics.ui.components.mainpanel import MainPanel
from castoranalytics.ui.components.loggingdockwidget import LoggingDockWidget
from castoranalytics.ui.components.studytreedockwidget import StudyTreeDockerWidget
from castoranalytics.ui.components.toolbar import ToolBar
from castoranalytics.ui.components.statusindicator import StatusIndicator
from castoranalytics.ui.utils import resource_path


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self._settings = Settings()
        self._main_panel = MainPanel()
        self._study_tree_dock_widget = StudyTreeDockerWidget()
        self._logging_dock_widget = LoggingDockWidget()
        self.init_window()

    # INITIALIZATION

    def init_toolbar(self):
        self.addToolBar(ToolBar())

    def init_status_indicator(self):
        self.setStatusBar(StatusIndicator())

    def init_window(self):
        self.init_toolbar()
        self.init_status_indicator()
        self.setWindowTitle(constants.CASTOR_ANALYTICS_WINDOW_TITLE)
        self.setWindowIcon(QIcon(resource_path(os.path.join(
            constants.CASTOR_ANALYTICS_RESOURCES_IMAGES_ICONS_DIR, constants.CASTOR_ANALYTICS_RESOURCES_ICON))))
        if not self.load_geometry_and_state():
            self.set_default_size_and_position()
        self.addDockWidget(
            Qt.DockWidgetArea.LeftDockWidgetArea, self.get_study_tree_dock_widget())
        self.addDockWidget(
            Qt.DockWidgetArea.BottomDockWidgetArea, self.get_logging_dock_widget())
        self.setCentralWidget(self.get_main_panel())

    # GET

    def get_settings(self):
        return self._settings
    
    def get_main_panel(self):
        return self._main_panel
    
    def get_study_tree_dock_widget(self):
        return self._study_tree_dock_widget
    
    def get_logging_dock_widget(self):
        return self._logging_dock_widget

    # EVENTS

    def closeEvent(self, event):
        self.save_geometry_and_state()
        return super().closeEvent(event)

    # MISCELLANEOUS

    def load_geometry_and_state(self):
        geometry = self.get_settings().get(constants.CASTOR_ANALYTICS_WINDOW_GEOMETRY_KEY)
        state = self.get_settings().get(constants.CASTOR_ANALYTICS_WINDOW_STATE_KEY)
        if isinstance(geometry, QByteArray) and self.restoreGeometry(geometry):
            if isinstance(state, QByteArray):
                self.restoreState(state)
            return True
        return False

    def save_geometry_and_state(self):
        self.get_settings().set(
            constants.CASTOR_ANALYTICS_WINDOW_GEOMETRY_KEY, self.saveGeometry())
        self.get_settings().set(
            constants.CASTOR_ANALYTICS_WINDOW_STATE_KEY, self.saveState())

    def set_default_size_and_position(self):
        self.resize(constants.CASTOR_ANALYTICS_WINDOW_W, constants.CASTOR_ANALYTICS_WINDOW_H)
        self.center_window()

    def center_window(self):
        screen = QGuiApplication.primaryScreen().geometry()
        x = (screen.width() - self.geometry().width()) / 2
        y = (screen.height() - self.geometry().height()) / 2
        self.move(int(x), int(y))