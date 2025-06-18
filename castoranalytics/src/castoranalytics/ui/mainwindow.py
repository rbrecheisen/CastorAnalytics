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
from castoranalytics.ui.components.logsdockwidget import LogsDockWidget
from castoranalytics.ui.components.studiesdockwidget import StudiesDockWidget
from castoranalytics.ui.components.busyoverlaywidget import BusyOverlayWidget
from castoranalytics.ui.components.toolbar import ToolBar
from castoranalytics.ui.components.statusindicator import StatusIndicator
from castoranalytics.ui.utils import resource_path

# TODO: https://chatgpt.com/g/g-p-6842b66a6fa48191ba9efa9f3d8878e4-castor-analytics/c/68515b87-c8c8-800b-9acc-b1f3aa86435f (Model/View events)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self._settings = Settings()
        self._main_panel = MainPanel()
        self._studies_dock_widget = StudiesDockWidget()
        self._logs_dock_widget = LogsDockWidget()
        self._busy_overlay = BusyOverlayWidget(self)
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
            Qt.DockWidgetArea.LeftDockWidgetArea, self.get_studies_dock_widget())
        self.addDockWidget(
            Qt.DockWidgetArea.BottomDockWidgetArea, self.get_logs_dock_widget())
        self.setCentralWidget(self.get_main_panel())
        # self.get_busy_overlay().show_overlay()

    # GET

    def get_settings(self):
        return self._settings
    
    def get_main_panel(self):
        return self._main_panel
    
    def get_studies_dock_widget(self):
        return self._studies_dock_widget
    
    def get_logs_dock_widget(self):
        return self._logs_dock_widget
    
    def get_busy_overlay(self):
        return self._busy_overlay

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