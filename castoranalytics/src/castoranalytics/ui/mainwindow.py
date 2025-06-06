from PySide6.QtWidgets import (
    QMainWindow,
    QStackedWidget,
    QWidget,
    QVBoxLayout,
    QPushButton,
    QListWidget,
    QLabel,
    QMessageBox,
)
from PySide6.QtGui import QAction

from castoranalytics.ui.dialogs.settingsdialog import SettingsDialog
from castoranalytics.ui.settings.settings import Settings
from castoranalytics.ui.settings.settingsmanager import SettingsManager


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self._stacked_widget = QStackedWidget(self)

        """
        Create class variables
        Create init methods
        Create handlers
        """

        # Menu
        menu_bar = self.menuBar()

        file_menu = menu_bar.addMenu('File')

        open_file_action = QAction('Open', self)
        open_file_action.triggered.connect(self.handle_open_file)

        exit_action = QAction('Exit', self)
        exit_action.triggered.connect(self.handle_exit)
        
        file_menu.addAction(open_file_action)
        file_menu.addAction(exit_action)

        settings_menu = menu_bar.addMenu('Settings')
        
        open_settings_action = QAction('Settings', self)
        open_settings_action.triggered.connect(self.handle_open_settings)

        settings_menu.addAction(open_settings_action)

        help_menu = menu_bar.addMenu('Help')

        about_action = QAction('About', self)
        about_action.triggered.connect(self.handle_about)

        help_menu.addAction(about_action)

        # Home page
        self._home_page = QWidget()
        self._home_page_layout = QVBoxLayout()
        self._home_page_study_list = QListWidget()
        self.init_home_page()

        # Study details page
        self._study_details_page = QWidget()
        self.init_study_details_page()

        # Main window
        self._stacked_widget.addWidget(self._home_page)
        self._stacked_widget.addWidget(self._study_details_page)
        self.setCentralWidget(self._stacked_widget)
        self.setWindowTitle('Castor Analytics')
        self.show()

    def init_home_page(self):
        self._home_page_study_list.itemClicked.connect(self.handle_study_selected)
        self._home_page_layout.addWidget(self._home_page_study_list)
        self._home_page.setLayout(self._home_page_layout)

    def init_study_details_page(self):
        pass

    def handle_open_file(self):
        pass

    def handle_exit(self):
        self.close()

    def handle_about(self):
        pass

    def handle_open_settings(self):
        settings_dialog = SettingsDialog(self)
        if settings_dialog.exec():
            pass

    def handle_study_selected(self):
        pass