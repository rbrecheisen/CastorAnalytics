from PySide6.QtWidgets import (
    QDialog,
    QLineEdit,
    QFormLayout,
    QDialogButtonBox,
    QVBoxLayout,
)


class SettingsDialog(QDialog):
    def __init__(self, parent=None):
        super(SettingsDialog, self).__init__(parent)
        self.setWindowTitle('Settings')
        api_token_url_field = QLineEdit('https://data.castoredc.com/oauth/token')
        api_base_url_field = QLineEdit('https://data.castoredc.com/api')
        client_id_field = QLineEdit()
        client_secret_field = QLineEdit()
        form_layout = QFormLayout()
        form_layout.addrow('API token URL: ', None)
        form_layout.addRow('API base URL:', None)
        form_layout.addRow('Client ID:', client_id_field)
        form_layout.addRow('Client secret:', client_secret_field)
        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        layout = QVBoxLayout()
        layout.addLayout(form_layout)
        layout.addWidget(buttons)
        self.setLayout(layout)