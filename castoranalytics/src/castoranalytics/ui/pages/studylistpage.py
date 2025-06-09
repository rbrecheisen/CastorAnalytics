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


class StudyListPage(BasePage):
    def __init__(self):
        super(StudyListPage, self).__init__(name='Studies')
        self._study_list_label = None
        self._table_widget = None
        self.init()

    def init(self):
        self._study_list_label = Label('Studies', type=Label.HEADING1)
        self._table_widget = QTableWidget()
        self._table_widget.setSortingEnabled(True)
        self._table_widget.horizontalHeader().setVisible(False)
        self._table_widget.verticalHeader().setVisible(False)
        self._table_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self._table_widget.itemClicked.connect(self.handle_study_selected)
        self.get_layout().addWidget(self._study_list_label)
        self.get_layout().addWidget(self._table_widget)

    def handle_study_selected(self, item):
        self.navigate(f'/studies/{item.data(Qt.UserRole).get_id()}')

    def on_data_ready(self, studies, error):
        self._table_widget.setRowCount(len(studies))
        self._table_widget.setColumnCount(1)
        for row, study in enumerate(studies):
            item = QTableWidgetItem(study.get_name())
            item.setData(Qt.UserRole, study)
            self._table_widget.setItem(row, 0, item)
        self._table_widget.setHorizontalHeaderLabels(['Study name'])
        self._table_widget.setAlternatingRowColors(True)
        self._table_widget.sortItems(0, Qt.AscendingOrder)
        self._table_widget.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
        self._table_widget.horizontalHeader().setDefaultAlignment(Qt.AlignLeft | Qt.AlignVCenter)

    def on_navigate(self, params):
        self._table_widget.clearContents()
        self.load_data('get_studies')