from importlib.resources import files
from PySide6.QtWidgets import (
    QMainWindow,
    QStackedWidget,
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


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self._file_menu = None
        self._file_menu_exit_action = None
        self._file_menu_open_settings_page_action = None
        self._home_page = None
        self._home_page_layout = None
        self._home_page_background_image_label = None
        self._home_page_background_image_pixmap = None
        self._home_page_background_image = None
        self._study_list_page = None
        self._study_list_page_layout = None
        self._study_list_page_study_list_widget = None
        self._study_page = None
        self._stacked_widget = None

        self.init_menus()
        self.init_home_page()
        self.init_study_list_page()
        self.init_study_page()
        self.init_main()

    # INITIALIZATION

    def init_menus(self):
        self.init_file_menu()

    def init_file_menu(self):
        self._file_menu = QMenu('File', self)
        self.init_file_menu_open_settings_page_action()
        self.init_file_menu_exit_action()
        self.menuBar().addMenu(self._file_menu)

    def init_file_menu_open_settings_page_action(self):
        self._file_menu_open_settings_page_action = QAction('Settings...', self)
        self._file_menu_open_settings_page_action.triggered.connect(self.handle_open_settings)
        self._file_menu.addAction(self._file_menu_open_settings_page_action)

    def init_file_menu_exit_action(self):
        self._file_menu_exit_action = QAction('Exit', self)
        self._file_menu_exit_action.triggered.connect(self.handle_exit)
        self._file_menu.addAction(self._file_menu_exit_action)

    def init_home_page(self):
        self._home_page = QWidget()
        self._home_page_layout = QVBoxLayout()
        self._home_page_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._home_page_background_image_label = QLabel()
        self._home_page_background_image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._home_page_background_image_label.setScaledContents(True)
        self._home_page_background_image_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        image_path = files('castoranalytics.resources.images') / 'home.png'
        pixmap = QPixmap(image_path)
        self._home_page_background_image_pixmap = pixmap
        self._home_page_background_image_label.setPixmap(self.apply_opacity_to_pixmap(pixmap, 0.5))
        self._home_page_layout.addWidget(self._home_page_background_image_label)
        self._home_page.setLayout(self._home_page_layout)

    def init_study_list_page(self):
        self._study_list_page = QWidget()
        self._study_list_page_layout = QVBoxLayout()
        self._study_list_page_study_list_widget = QListWidget()
        self._study_list_page_study_list_widget.itemClicked.connect(self.handle_study_selected)
        self._study_list_page_layout.addWidget(self._study_list_page_study_list_widget)
        self._study_list_page.setLayout(self._study_list_page_layout)

    def init_study_page(self):
        self._study_page = QWidget()

    def init_main(self):
        self._stacked_widget = QStackedWidget()
        self._stacked_widget.addWidget(self._home_page)
        self._stacked_widget.addWidget(self._study_list_page)
        self._stacked_widget.addWidget(self._study_page)
        self._stacked_widget.setCurrentWidget(self._home_page)
        self.setCentralWidget(self._stacked_widget)
        self.setWindowTitle(CASTOR_ANALYTICS_WINDOW_TITLE)
        self.resize(800, 600)
        self.center_window()
        self.show()

    # EVENT HANDLERS

    def handle_exit(self):
        self.close()

    def handle_open_settings(self):
        pass

    def handle_study_selected(self):
        pass

    # QT EVENT HANDLERS

    def resizeEvent(self, event):
        if self._home_page_background_image_pixmap:
            scaled_pixmap = self._home_page_background_image_pixmap.scaled(
                self._home_page_background_image_label.size(),
                aspectMode=Qt.AspectRatioMode.KeepAspectRatioByExpanding,
                mode=Qt.TransformationMode.SmoothTransformation,
            )
            self._home_page_background_image_label.setPixmap(self.apply_opacity_to_pixmap(scaled_pixmap, 0.5))
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