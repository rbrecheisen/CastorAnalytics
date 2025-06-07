from PySide6.QtWidgets import QStackedWidget

from castoranalytics.ui.crumbs import Crumbs


class Router(QStackedWidget):
    def __init__(self):
        super(Router, self).__init__()
        self._crumbs = Crumbs()
        self._pages = {}
        self._prev_path = None
        self._curr_path = None

    def crumbs(self):
        return self._crumbs

    def add_page(self, page, path):
        if path not in self._pages.keys():
            self._pages[path] = page
            self._pages[path].set_router(self)
            self.addWidget(page)

    def back(self):
        self.navigate(self._prev_path)

    def navigate(self, path):
        if path in self._pages.keys():
            if path != self._curr_path:
                self._prev_path = self._curr_path
                self._curr_path = path
                self.setCurrentWidget(self._pages[self._curr_path])
                self._crumbs.update(self._curr_path)
