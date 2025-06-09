from PySide6.QtWidgets import (
    QWidget,
    QPushButton,
    QVBoxLayout,
    QLabel,
)
from PySide6.QtCore import Qt

from castoranalytics.ui.settings import Settings
from castoranalytics.core import Core
from castoranalytics.core.logging import LogManager
from castoranalytics.ui.utils import to_main_thread, BusyOverlay

LOG = LogManager()


class BasePage(QWidget):
    def __init__(self, name):
        super(BasePage, self).__init__()
        self._name = name
        self._router = None
        self._settings = Settings()
        # self._go_to_settings_button = None
        self._settings_label = None
        self._busy_overlay = None
        self._page_layout = None
        self._core = None
        self.init_internal()

    def init_internal(self):
        # self._go_to_settings_button = QPushButton('Go to settings', self)
        # self._go_to_settings_button.clicked.connect(self.handle_go_to_settings)
        self._settings_label = QLabel()
        if not self.get_core().ready():
            self._settings_label.setText('It looks like your API settings are incomplete. Please go to settings.')
        self._busy_overlay = BusyOverlay(self)
        self._page_layout = QVBoxLayout(self)
        self._page_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        # self._page_layout.addWidget(self._go_to_settings_button)
        self._page_layout.addWidget(self._settings_label)
        self.setLayout(self._page_layout)

    def get_core(self):
        if self._core is None:
            self._core = Core()
        if not self._core.ready():
            self._core.update_settings(
                self.get_setting('castoranalytics.client_id', None),
                self.get_setting('castoranalytics.client_secret', None),
                self.get_setting('castoranalytics.token_url', None),
                self.get_setting('castoranalytics.api_base_url', None),
            )
        return self._core

    def get_layout(self):
        return self._page_layout
    
    def load_data(self, func_name, *args, **kwargs):
        func_name = func_name if func_name.endswith('_async') else func_name + '_async'
        try:
            func = getattr(self.get_core(), func_name)
            self._busy_overlay.show_overlay()
            func(callback=to_main_thread(self.data_ready_internal), *args, **kwargs)
        except Exception as e:
            self._busy_overlay.hide_overlay()
            LOG.error(e)

    def data_ready_internal(self, result, error):
        self.data_ready(result, error)
        self._busy_overlay.hide_overlay()

    def data_ready(self, result, error):
        raise NotImplementedError('Must be implemented in child class')

    def set_router(self, router):
        self._router = router

    def back(self):
        if self._router:
            self._router.back()

    def navigate(self, path):
        if self._router:
            self._router.navigate(path)

    def get_setting(self, name, default=None):
        return self._settings.get(name, default)
    
    def set_setting(self, name, value):
        self._settings.set(name, value)

    def on_navigate(self, params):
        pass

    def handle_go_to_settings(self):
        self.navigate('/settings')