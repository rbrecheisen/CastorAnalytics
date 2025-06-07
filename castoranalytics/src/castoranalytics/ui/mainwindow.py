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
)
from PySide6.QtGui import (
    QGuiApplication,
    QAction,
)

CASTOR_ANALYTICS_WINDOW_TITLE = 'Castor Analytics'


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self._file_menu = None
        self._file_menu_exit_action = None
        self._file_menu_open_settings_page_action = None
        self._study_list_page = None
        self._study_list_page_layout = None
        self._study_list_page_study_list_widget = None
        self._study_page = None
        self._stacked_widget = None

        self.init_menus()
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
        self._stacked_widget.addWidget(self._study_list_page)
        self._stacked_widget.addWidget(self._study_page)
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

    # MISCELLANEOUS

    def center_window(self):
        screen = QGuiApplication.primaryScreen().geometry()
        x = (screen.width() - self.geometry().width()) / 2
        y = (screen.height() - self.geometry().height()) / 2
        self.move(int(x), int(y))