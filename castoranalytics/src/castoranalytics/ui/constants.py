from PySide6.QtWidgets import QStyle

from castoranalytics.ui.utils import is_macos


CASTORANALYTICS_WINDOW_TITLE = 'Castor Analytics'
CASTORANALYTICS_NAME = 'castoranalytics'
CASTORANALYTICS_BUNDLE_IDENTIFIER = 'com.rbeesoft'
CASTORANALYTICS_WINDOW_W = 1024
CASTORANALYTICS_WINDOW_H = 600
CASTORANALYTICS_WINDOW_GEOMETRY_KEY = 'window/geometry'
CASTORANALYTICS_WINDOW_STATE_KEY = 'window/state'
CASTORANALYTICS_STATUS_READY = 'Ready'
CASTORANALYTICS_DONATE_URL = 'https://rbeesoft.nl/wordpress/'
CASTORANALYTICS_DONATE_BUTTON_TEXT = 'Please donate!'
CASTORANALYTICS_DONATE_BUTTON_STYLESHEET = 'background-color: blue; color: white; font-weight: bold;'
CASTORANALYTICS_RESOURCES_DIR = 'castoranalytics/resources'
CASTORANALYTICS_RESOURCES_IMAGES_DIR = 'castoranalytics/resources/images'
CASTORANALYTICS_RESOURCES_IMAGES_ICONS_DIR = 'castoranalytics/resources/images/icons'
CASTORANALYTICS_RESOURCES_ICON = 'castoranalytics.icns' if is_macos() else 'castoranalytics.ico'
CASTORANALYTICS_LAST_DIRECTORY_KEY = 'castoranalytics/last_directory'
CASTORANALYTICS_APP_MENU = 'Application'
CASTORANALYTICS_APP_MENU_ITEM_SETTINGS = 'Settings...'
CASTORANALYTICS_APP_MENU_ITEM_EXIT = 'Exit'
CASTORANALYTICS_DATA_MENU = 'Data'
CASTORANALYTICS_LOG_PANEL_TITLE = 'Output log'
CASTORANALYTICS_LOG_PANEL_CLEAR_LOGS_BUTTON = 'Clear logs'

# https://www.pythonguis.com/faq/built-in-qicons-pyqt/#qt-standard-icons
CASTORANALYTICS_ICON_EXIT = QStyle.SP_MessageBoxCritical
CASTORANALYTICS_ICON_SETTINGS = QStyle.SP_VistaShield