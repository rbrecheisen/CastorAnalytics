from PySide6.QtWidgets import QListWidget


class LogsWidget(QListWidget):
    def __init__(self):
        super(LogsWidget, self).__init__()
        self.addItems([
            '17-06-2025/14:07:45 [INFO] Some logging text',
            '17-06-2025/14:07:45 [INFO] Some logging text',
            '17-06-2025/14:07:45 [INFO] Some logging text',
        ])