from PySide6.QtWidgets import QWidget


class BasePage(QWidget):
    def __init__(self, name):
        super(BasePage, self).__init__()
        self._name = name
        self._router = None

    def set_router(self, router):
        self._router = router

    def back(self):
        if self._router:
            self._router.back()

    def navigate(self, path):
        if self._router:
            self._router.navigate(path)