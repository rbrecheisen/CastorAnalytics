import os
import requests

from PySide6.QtWidgets import (
    QMainWindow,
    QStackedLayout,
    QWidget,
    QVBoxLayout,
    QLabel,
    QSizePolicy,
)
from PySide6.QtGui import (
    QGuiApplication,
    QPixmap,
    QPainter, 
    QColor,
    QIcon,
    QAction,
)
from PySide6.QtCore import Qt

import castoranalytics.ui.constants as constants

from castoranalytics.ui.pages.router import Router
from castoranalytics.ui.pages.studylistpage import StudyListPage
from castoranalytics.ui.pages.studypage import StudyPage
from castoranalytics.ui.pages.studysitelistpage import StudySiteListPage
from castoranalytics.ui.pages.settingspage import SettingsPage
from castoranalytics.ui.utils import Label, resource_path
from castoranalytics.core.logging import LogManager

LOG = LogManager()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        result = requests.get('http://localhost:8000/api/licenses/1234/')
        if result.status_code != 200:
            print(result.json().get('message'))
            return
        self._version = self.init_version()
        self._app_label_text = constants.CASTOR_ANALYTICS_WINDOW_TITLE + f' {self._version}'
        self._background_label = self.init_background_label()
        self._background_label_pixmap = None
        self._router = self.init_router()
        self._file_menu = self.init_file_menu()
        self._page_layout = self.init_page_layout(self._app_label_text, self._background_label, self._router)
        self.init_main_window(self._app_label_text, self._page_layout)

    # INITIALIZATION

    def init_version(self):
        with open(resource_path(os.path.join(constants.CASTOR_ANALYTICS_RESOURCES_DIR, 'VERSION')), 'r') as f:
            version = f.readline().strip()
            return version

    def init_background_label(self):
        label = QLabel()
        label.setAlignment(Qt.AlignCenter)
        label.setScaledContents(True)
        label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        image_path = resource_path(os.path.join(
            constants.CASTOR_ANALYTICS_RESOURCES_IMAGES_DIR, constants.CASTOR_ANALYTICS_RESOURCES_BACKGROUND_IMAGE))
        label.setPixmap(self.apply_opacity_to_pixmap(QPixmap(image_path), constants.CASTOR_ANALYTICS_RESOURCES_BACKGROUND_IMAGE_OPACITY))
        label.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents, True) # should not handle events!
        return label

    def init_router(self):
        router = Router()
        router.add_page(StudyListPage(), '/studies')
        router.add_page(StudyPage(), '/studies/:study_id')
        router.add_page(StudySiteListPage(), '/studies/:study_id/sites')
        router.add_page(SettingsPage(), '/settings')
        router.navigate('/studies')
        return router

    def init_file_menu(self):
        menu = self.menuBar().addMenu('File')
        menu_settings_action = QAction('Settings', self)
        menu_settings_action.triggered.connect(self.on_open_settings_page)
        menu_exit_action = QAction('Exit', self)
        menu_exit_action.triggered.connect(self.close)
        menu.addAction(menu_settings_action)
        menu.addAction(menu_exit_action)
        return menu

    def init_page_layout(self, app_label_text, background_label, router):
        app_label = Label(app_label_text, type=Label.HEADING1)
        app_label.setAlignment(Qt.AlignCenter)
        page_widget = QWidget()
        layout = QStackedLayout(page_widget)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setStackingMode(QStackedLayout.StackAll)
        layout.addWidget(background_label)
        layout.addWidget(router)
        page_layout = QVBoxLayout()
        page_layout.addWidget(app_label)
        page_layout.addWidget(page_widget)
        return page_layout

    def init_main_window(self, app_label_text, page_layout):
        widget = QWidget()
        widget.setLayout(page_layout)
        self.setWindowTitle(app_label_text)
        self.setWindowIcon(QIcon(resource_path(os.path.join(
            constants.CASTOR_ANALYTICS_RESOURCES_IMAGES_ICONS_DIR, constants.CASTOR_ANALYTICS_RESOURCES_ICON))))
        self.setCentralWidget(widget)
        self.resize(constants.CASTOR_ANALYTICS_WINDOW_W, constants.CASTOR_ANALYTICS_WINDOW_H)
        self.center_window()
        self.show()

    # EVENT HANDLERS

    def resizeEvent(self, event):
        if self._background_label_pixmap:
            scaled_pixmap = self._background_label_pixmap.scaled(
                self._background_label.size(), aspectMode=Qt.AspectRatioMode.IgnoreAspectRatio, mode=Qt.TransformationMode.SmoothTransformation)
            self._background_label.setPixmap(
                self.apply_opacity_to_pixmap(
                    scaled_pixmap, constants.CASTOR_ANALYTICS_RESOURCES_BACKGROUND_IMAGE_OPACITY))
        return super().resizeEvent(event)

    def on_open_settings_page(self):
        self._router.navigate('/settings')

    # MISCELLANEOUS

    def apply_opacity_to_pixmap(self, pixmap, opacity):
        transparent_pixmap = QPixmap(pixmap.size())
        transparent_pixmap.fill(QColor(0, 0, 0, 0))
        painter = QPainter(transparent_pixmap)
        painter.setOpacity(opacity)
        painter.drawPixmap(0, 0, pixmap)
        painter.end()
        return transparent_pixmap

    def center_window(self):
        screen = QGuiApplication.primaryScreen().geometry()
        x = (screen.width() - self.geometry().width()) / 2
        y = (screen.height() - self.geometry().height()) / 2
        self.move(int(x), int(y))