from PySide6.QtWidgets import (
    QPushButton,
    QTableWidget,
    QTableWidgetItem,
    QHeaderView,
    QSizePolicy,
)
from PySide6.QtCore import Qt

from castoranalytics.ui.pages.basepage import BasePage
from castoranalytics.ui.utils import Label
from castoranalytics.core.logging import LogManager

LOG = LogManager()


class StudyPage(BasePage):
    def __init__(self):
        super(StudyPage, self).__init__(name='Study')
        self._back_button = None
        self._study_id = None
        self._study_name_label = None
        self._table_widget = None
        self._sites_warning_label = None
        self._show_sites_button = None
        self.init()

    def init(self):
        self._back_button = QPushButton('Back', self)
        self._back_button.clicked.connect(self.handle_back)
        self._study_name_label = Label('', type=Label.HEADING1)
        self._table_widget = QTableWidget()
        self._table_widget.setSelectionMode(QTableWidget.NoSelection)
        self._table_widget.horizontalHeader().setVisible(False)
        self._table_widget.verticalHeader().setVisible(False)
        self._table_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        self._table_widget.setFocusPolicy(Qt.NoFocus)
        self._sites_warning_label = Label('Your study has >10 sites. Loading these will take some time.', type=Label.HEADING1, style='color: red;')
        self._sites_warning_label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self._sites_warning_label.setContentsMargins(0, 0, 0, 20)
        self._sites_warning_label.setVisible(False)
        self._show_sites_button = QPushButton('Get sites', self)
        self._show_sites_button.clicked.connect(self.handle_show_sites)
        self._show_sites_button.setVisible(False)
        self.get_layout().addWidget(self._back_button)
        self.get_layout().addWidget(self._study_name_label)
        self.get_layout().addWidget(self._table_widget)
        self.get_layout().addWidget(self._sites_warning_label)
        self.get_layout().addWidget(self._show_sites_button)

    def handle_back(self):
        self.back()

    def handle_show_sites(self):
        self.navigate(f'/studies/{self._study_id}/sites')

    def on_navigate(self, params):
        self._study_name_label.setText('')
        self._table_widget.clearContents()
        self._sites_warning_label.setVisible(False)
        self._show_sites_button.setVisible(False)
        self._study_id = params.get('study_id', None)
        if self._study_id:
            self.load_data('get_study', self._study_id)

    def on_data_ready(self, study, error):
        if error:
            self._study_name_label.setText(error)
            return
        self._study_name_label.setText(study.get_name())
        self._table_widget.setRowCount(5)
        self._table_widget.setColumnCount(2)
        self._table_widget.setItem(0, 0, QTableWidgetItem('Study ID'))
        self._table_widget.setItem(0, 1, QTableWidgetItem(study.get_id()))
        self._table_widget.setItem(1, 0, QTableWidgetItem('Number of sites'))
        self._table_widget.setItem(1, 1, QTableWidgetItem(str(study.get_nr_sites())))
        self._table_widget.setItem(2, 0, QTableWidgetItem('Number of participants'))
        self._table_widget.setItem(2, 1, QTableWidgetItem(str(study.get_nr_participants())))
        self._table_widget.setItem(3, 0, QTableWidgetItem('Number of fields'))
        self._table_widget.setItem(3, 1, QTableWidgetItem(str(study.get_nr_fields())))
        self._table_widget.setItem(4, 0, QTableWidgetItem('Created on'))
        self._table_widget.setItem(4, 1, QTableWidgetItem(str(study.get_created_on())))
        self._table_widget.setAlternatingRowColors(True)
        self._table_widget.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
        self._table_widget.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        self._table_widget.horizontalHeader().setDefaultAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        if study.get_nr_sites() > 10:
            self._sites_warning_label.setVisible(True)
        self._show_sites_button.setVisible(True)