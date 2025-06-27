import os

from typing import Any

from PySide6.QtWidgets import (
    QMainWindow,
)
from PySide6.QtGui import (
    QGuiApplication,
    QAction,
    QIcon,
)
from PySide6.QtCore import Qt, QByteArray

import castoranalytics.ui.constants as constants

from castoranalytics.ui.settings import Settings
from castoranalytics.ui.panels.mainpanel import MainPanel
from castoranalytics.ui.utils import resource_path, version, is_macos


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super(MainWindow, self).__init__()
        self._settings = None
        self._main_panel = None
        self._view = None
        self.init_window()

    def init_window(self) -> None:
        self.setWindowTitle(f'{constants.CASTORANALYTICS_WINDOW_TITLE} {version()}')
        self.setWindowIcon(QIcon(resource_path(os.path.join(
            constants.CASTORANALYTICS_RESOURCES_IMAGES_ICONS_DIR, constants.CASTORANALYTICS_RESOURCES_ICON))))
        if not self.load_geometry_and_state():
            self.set_default_size_and_position()
        self.init_menus()
        self.init_status_bar()
        self.setCentralWidget(self.main_panel())

    def init_menus(self) -> None:
        self.init_app_menu()
        self.init_data_menu()
        if is_macos():            
            self.menuBar().setNativeMenuBar(False)

    def init_app_menu(self) -> None:
        app_menu_open_settings_action = QAction(constants.CASTORANALYTICS_APP_MENU_ITEM_SETTINGS, self)
        app_menu_open_settings_action.triggered.connect(self.handle_open_settings)
        app_menu_exit_action = QAction(constants.CASTORANALYTICS_APP_MENU_ITEM_EXIT, self)
        app_menu_exit_action.triggered.connect(self.close)
        app_menu = self.menuBar().addMenu(constants.CASTORANALYTICS_APP_MENU)
        app_menu.addAction(app_menu_open_settings_action)
        app_menu.addAction(app_menu_exit_action)

    def init_data_menu(self) -> None:
        data_menu = self.menuBar().addMenu(constants.CASTORANALYTICS_DATA_MENU)

    def init_status_bar(self) -> None:
        self.set_status(constants.CASTORANALYTICS_STATUS_READY)

    # GETTERS

    def settings(self) -> Settings:
        if not self._settings:
            self._settings = Settings()
        return self._settings
    
    def main_panel(self) -> MainPanel:
        if not self._main_panel:
            self._main_panel = MainPanel(self)
        return self._main_panel
    
    # SETTERS

    def set_status(self, message: str) -> None:
        self.statusBar().showMessage(message)

    # EVENT HANDLERS

    def handle_open_settings(self) -> None:
        pass

    def closeEvent(self, event: Any) -> None:
        self.save_geometry_and_state()
        return super().closeEvent(event)
    
    # MISCELLANEOUS

    def load_geometry_and_state(self) -> None:
        geometry = self.settings().get(constants.CASTORANALYTICS_WINDOW_GEOMETRY_KEY)
        state = self.settings().get(constants.CASTORANALYTICS_WINDOW_STATE_KEY)
        if isinstance(geometry, QByteArray) and self.restoreGeometry(geometry):
            if isinstance(state, QByteArray):
                self.restoreState(state)
            return True
        return False

    def save_geometry_and_state(self) -> None:
        self.settings().set(
            constants.CASTORANALYTICS_WINDOW_GEOMETRY_KEY, self.saveGeometry())
        self.settings().set(
            constants.CASTORANALYTICS_WINDOW_STATE_KEY, self.saveState())

    def set_default_size_and_position(self) -> None:
        self.resize(constants.CASTORANALYTICS_WINDOW_W, constants.CASTORANALYTICS_WINDOW_H)
        self.center_window()

    def center_window(self) -> None:
        screen = QGuiApplication.primaryScreen().geometry()
        x = (screen.width() - self.geometry().width()) / 2
        y = (screen.height() - self.geometry().height()) / 2
        self.move(int(x), int(y))