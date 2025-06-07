import sys

from importlib.resources import files
from PySide6.QtWidgets import (
    QApplication,
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
    QGraphicsOpacityEffect,
)
from PySide6.QtGui import (
    QGuiApplication,
    QAction,
    QPixmap,
    QPainter, 
    QColor,
)
from PySide6.QtCore import Qt

CASTOR_ANALYTICS_WINDOW_TITLE = 'Castor Analytics'
CASTOR_ANALYTICS_RESOURCES_DIR = 'castoranalytics.resources'
CASTOR_ANALYTICS_RESOURCES_IMAGES_DIR = 'castoranalytics.resources.images'
CASTOR_ANALYTICS_RESOURCES_BACKGROUND_IMAGE = 'home.png'
CASTOR_ANALYTICS_RESOURCES_BACKGROUND_IMAGE_OPACITY = 0.5


class BreadCrumbsWidget(QWidget):
    pass


class Page(QWidget):
    def __init__(self, name):
        self._name = name
        self._name_label = QLabel(self._name, self)
        self._layout = QVBoxLayout(self)
        self._layout.addWidget(self._name_label)
        self.setLayout(self._layout)


class PageRouter:
    def __init__(self, stacked_widget):
        self._stacked_widget = stacked_widget
        self._pages = {}

    def add_page(self, page, path):
        if path not in self._pages.keys():
            self._pages[path] = page
            self._stacked_widget.addWidget(page)

    def navigate(self, path):
        if path in self._pages.keys():
            self._stacked_widget.setCurrentWidget(self._pages[path])


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('X')
        self.resize(800, 600)
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        central_layout = QStackedLayout(central_widget)
        central_layout.setContentsMargins(0, 0, 0, 0)
        central_layout.setStackingMode(QStackedLayout.StackAll)
        background_label = QLabel()
        background_label.setAlignment(Qt.AlignCenter)
        background_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        image_path = files(CASTOR_ANALYTICS_RESOURCES_IMAGES_DIR) / CASTOR_ANALYTICS_RESOURCES_BACKGROUND_IMAGE
        background_label.setPixmap(self.apply_opacity_to_pixmap(QPixmap(image_path), CASTOR_ANALYTICS_RESOURCES_BACKGROUND_IMAGE_OPACITY))
        stacked_widget = QStackedWidget()
        page = Page('Home')
        stacked_widget.addWidget(page)
        central_layout.addWidget(background_label)
        central_layout.addWidget(stacked_widget)
        stacked_widget.setCurrentIndex(0)
        self.show()

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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())