from importlib.resources import files
from PySide6.QtWidgets import (
    QMainWindow,
    QStackedWidget,
    QStackedLayout,
    QWidget,
    QVBoxLayout,
    QPushButton,
    QMenu,
    QListWidget,
    QLabel,
    QMessageBox,
    QSizePolicy,
)
from PySide6.QtGui import (
    QGuiApplication,
    QAction,
    QPixmap,
    QPainter, 
    QColor,
)
from PySide6.QtCore import Qt

from castoranalytics.ui.router import Router
from castoranalytics.ui.pages.homepage import HomePage
from castoranalytics.ui.pages.settingspage import SettingsPage
from castoranalytics.core.logging import LogManager

CASTOR_ANALYTICS_WINDOW_TITLE = 'Castor Analytics'
CASTOR_ANALYTICS_WINDOW_W = 1024
CASTOR_ANALYTICS_WINDOW_H = 600
CASTOR_ANALYTICS_RESOURCES_DIR = 'castoranalytics.resources'
CASTOR_ANALYTICS_RESOURCES_IMAGES_DIR = 'castoranalytics.resources.images'
CASTOR_ANALYTICS_RESOURCES_BACKGROUND_IMAGE = 'home.png'
CASTOR_ANALYTICS_RESOURCES_BACKGROUND_IMAGE_OPACITY = 0.25

LOG = LogManager()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self._central_widget = None
        self._central_layout = None
        self._background_label = None
        self._background_label_pixmap = None
        self._router = None
        self._pages_widget = None
        self._pages_widget_layout = None
        self._crumbs = None

        self.init_background()
        self.init_pages()
        self.init_main_window()

    # INITIALIZATION

    def init_background(self):
        LOG.info('Initializing background image...')
        self._background_label = QLabel()
        self._background_label.setAlignment(Qt.AlignCenter)
        self._background_label.setScaledContents(True)
        self._background_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        image_path = files(CASTOR_ANALYTICS_RESOURCES_IMAGES_DIR) / CASTOR_ANALYTICS_RESOURCES_BACKGROUND_IMAGE
        self._background_label.setPixmap(self.apply_opacity_to_pixmap(QPixmap(image_path), CASTOR_ANALYTICS_RESOURCES_BACKGROUND_IMAGE_OPACITY))
        self._background_label.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents, True) # should not handle events!

    def init_pages(self):
        LOG.info('Initializing pages...')
        self._router = Router()
        self._router.add_page(HomePage(), '/home')
        self._router.add_page(SettingsPage(), '/settings')
        self._router.navigate('/home')
        self.init_pages_layout()

    def init_pages_layout(self):
        self._pages_widget = QWidget()
        layout = QStackedLayout(self._pages_widget)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setStackingMode(QStackedLayout.StackAll)
        layout.addWidget(self._background_label)
        layout.addWidget(self._router)
        self._pages_widget_layout = QVBoxLayout()
        self._pages_widget_layout.addWidget(self._router.crumbs())
        self._pages_widget_layout.addWidget(self._pages_widget)

    def init_main_window(self):
        LOG.info('Initializing main window...')
        self._central_widget = QWidget()
        self._central_widget.setLayout(self._pages_widget_layout)
        self.setWindowTitle(CASTOR_ANALYTICS_WINDOW_TITLE)
        self.setCentralWidget(self._central_widget)
        self.resize(CASTOR_ANALYTICS_WINDOW_W, CASTOR_ANALYTICS_WINDOW_H)
        self.center_window()
        self.show()

    # EVENT HANDLERS



    # QT EVENT HANDLERS

    def resizeEvent(self, event):
        if self._background_label_pixmap:
            scaled_pixmap = self._background_label_pixmap.scaled(
                self._background_label.size(), aspectMode=Qt.AspectRatioMode.IgnoreAspectRatio, mode=Qt.TransformationMode.SmoothTransformation)
            self._background_label.setPixmap(
                self.apply_opacity_to_pixmap(
                    scaled_pixmap, CASTOR_ANALYTICS_RESOURCES_BACKGROUND_IMAGE_OPACITY))
        return super().resizeEvent(event)

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