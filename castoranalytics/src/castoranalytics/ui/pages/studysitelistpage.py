from PySide6.QtWidgets import (
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


class StudySiteListPage(BasePage):
    def __init__(self):
        super(StudySiteListPage, self).__init__(name='Studies sites')
        self._study_site_list_label = None
        self._study_id = None
        self._table_widget = None
        self.init()

    def init(self):
        self._study_site_list_label = Label('Study sites', type=Label.HEADING1)
        self._table_widget = QTableWidget()
        self._table_widget.setSortingEnabled(True)
        self._table_widget.horizontalHeader().setVisible(False)
        self._table_widget.verticalHeader().setVisible(False)
        self._table_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self._table_widget.itemClicked.connect(self.handle_study_site_selected)
        self.get_layout().addWidget(self._study_site_list_label)
        self.get_layout().addWidget(self._table_widget)

    def handle_study_site_selected(self, item):
        # self.navigate(f'/studies/{item.data(Qt.UserRole).get_id()}')
        pass

    def on_navigate(self, params):
        self._table_widget.clearContents()
        self._study_id = params.get('study_id', None)
        if self._study_id:
            self.load_data('get_study_sites', self._study_id)
    
    def on_data_ready(self, study_sites, error):
        self._table_widget.setRowCount(len(study_sites))
        self._table_widget.setColumnCount(4)
        for row, study_site in enumerate(study_sites):
            self._table_widget.setItem(row, 0, QTableWidgetItem(study_site.get_abbreviation()))
            self._table_widget.setItem(row, 1, QTableWidgetItem(str(study_site.get_country_id())))
            self._table_widget.setItem(row, 2, QTableWidgetItem(str(study_site.get_nr_participants())))
            self._table_widget.setItem(row, 3, QTableWidgetItem(str(study_site.get_average_completion_percentage())))
        self._table_widget.setHorizontalHeaderLabels(['Site abbreviation', 'Country code', 'Nr. participants', 'Complete %'])
        self._table_widget.setAlternatingRowColors(True)
        self._table_widget.sortItems(0, Qt.AscendingOrder)
        self._table_widget.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
        self._table_widget.horizontalHeader().setDefaultAlignment(Qt.AlignLeft | Qt.AlignVCenter)