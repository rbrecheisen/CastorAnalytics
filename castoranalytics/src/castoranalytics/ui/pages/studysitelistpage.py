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

    def on_data_ready(self, sites, error):
        self._table_widget.setRowCount(len(sites))
        self._table_widget.setColumnCount(4)
        # for row, study in enumerate(studies):
        #     item = QTableWidgetItem(study.get_name())
        #     item.setData(Qt.UserRole, study)
        #     self._table_widget.setItem(row, 0, item)
        self._table_widget.setHorizontalHeaderLabels(['Site abbreviation', 'Country', 'Nr. participants', 'Complete %'])
        self._table_widget.setAlternatingRowColors(True)
        self._table_widget.sortItems(0, Qt.AscendingOrder)
        self._table_widget.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
        self._table_widget.horizontalHeader().setDefaultAlignment(Qt.AlignLeft | Qt.AlignVCenter)

    def on_navigate(self, params):
        self._table_widget.clearContents()
        self.load_data('get_study_sites')