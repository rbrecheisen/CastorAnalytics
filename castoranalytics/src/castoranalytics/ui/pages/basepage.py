from PySide6.QtWidgets import QWidget

from castoranalytics.ui.settings import Settings


class BasePage(QWidget):
    def __init__(self, name):
        super(BasePage, self).__init__()
        self._name = name
        self._router = None
        self._settings = Settings()

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