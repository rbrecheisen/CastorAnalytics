from PySide6.QtWidgets import (
    QPushButton,
    QVBoxLayout,
    QLabel,
    QTableWidget,
    QTableWidgetItem,
    QHeaderView,
    QSizePolicy,
)
from PySide6.QtCore import Qt

from castoranalytics.ui.pages.basepage import BasePage
from castoranalytics.core import Core
from castoranalytics.core.logging import LogManager

LOG = LogManager()


class StudyListPage(BasePage):
    def __init__(self):
        super(StudyListPage, self).__init__(name='Studies')
        self._settings_button = None
        self._layout = None
        self._study_list_layout = None
        self._table_widget = None
        self.init()

    def init(self):
        self._settings_button = QPushButton('Go to settings', self)
        self._settings_button.clicked.connect(self.handle_go_to_settings)
        self._table_widget = QTableWidget()
        self._table_widget.setSortingEnabled(True)
        self._table_widget.verticalHeader().setVisible(False)
        self._table_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self._table_widget.itemClicked.connect(self.handle_row_selected)
        self._layout = QVBoxLayout(self)
        self._layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self._layout.addWidget(self._settings_button)
        self._layout.addWidget(self._table_widget)
        self.setLayout(self._layout)

    def handle_go_to_settings(self):
        self.navigate('/settings')

    def handle_row_selected(self, item):
        self.navigate(f'/studies/{item.data(Qt.UserRole).get_id()}')

    def clear_layout(self):
        self._table_widget.clearContents()

    def get_api_settings(self):
        return (
            self.get_setting('castoranalytics.token_url', None),
            self.get_setting('castoranalytics.api_base_url', None),
            self.get_setting('castoranalytics.client_id', None),
            self.get_setting('castoranalytics.client_secret', None),
        )
    
    def update_study_list(self, client_id, client_secret, token_url, api_base_url):
        try:
            core = Core(client_id, client_secret, token_url, api_base_url)
            studies = core.get_studies()
            self._table_widget.setRowCount(len(studies))
            self._table_widget.setColumnCount(1)
            for row, study in enumerate(studies):
                item = QTableWidgetItem(study.get_name())
                item.setData(Qt.UserRole, study)
                self._table_widget.setItem(row, 0, item)
            self._table_widget.setHorizontalHeaderLabels(['Study Name'])
            self._table_widget.setAlternatingRowColors(True)
            self._table_widget.sortItems(0, Qt.AscendingOrder)
            self._table_widget.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
            self._table_widget.horizontalHeader().setDefaultAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        except Exception as e:
            LOG.error(e)

    def showEvent(self, event):
        self.clear_layout()
        token_url, api_base_url, client_id, client_secret = self.get_api_settings()
        if token_url is None or api_base_url is None or client_id is None or client_secret is None:
            self._study_list_layout.addWidget(QLabel('It looks like your API settings are incomplete. Please go to settings.'))
        else:
            self.update_study_list(client_id, client_secret, token_url, api_base_url)