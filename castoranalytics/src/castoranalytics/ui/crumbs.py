from PySide6.QtWidgets import QLabel


class Crumbs(QLabel):
    def __init__(self):
        super(Crumbs, self).__init__()

    def update(self, path):
        self.setText(path)