from PySide6.QtWidgets import QListWidget


class StudiesWidget(QListWidget):
    def __init__(self):
        super(StudiesWidget, self).__init__()
        self.addItems([
            'Study 1',
            'Study 2',
            'Study 3',
        ])