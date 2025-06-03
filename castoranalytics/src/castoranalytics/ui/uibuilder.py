class UiBuilder:
    def __init__(self, parent, title):
        self._parent = parent
        self._title = title

    def build(self):
        self._parent.setWindowTitle(self._title)