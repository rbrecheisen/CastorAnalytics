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
        self._study_id = None
        self._study_site_list_label = self.init_study_site_list_label()
        self._table_widget = self.init_table_widget()
        self.init_page_layout()

    # INITIALIZATION

    def init_study_site_list_label(self):
        label = Label('', type=Label.HEADING1)
        return label
    
    def init_table_widget(self):
        widget = QTableWidget()
        widget.setSortingEnabled(True)
        widget.horizontalHeader().setVisible(False)
        widget.verticalHeader().setVisible(False)
        widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        widget.itemClicked.connect(self.on_study_site_selected)
        return widget

    def init_page_layout(self):
        self.get_layout().addWidget(self._study_site_list_label)
        self.get_layout().addWidget(self._table_widget)

    # TABLE

    def update_study_site_list_label(self, error):
        if error:
            self._study_site_list_label.setText(error)
        else:
            self._study_site_list_label.setText('Study sites')

    def update_table_widget(self, study_sites):
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
        
    # EVENT HANDLERS

    def on_study_site_selected(self, item):
        # self.navigate(f'/studies/{item.data(Qt.UserRole).get_id()}')
        pass

    def on_navigate(self, params):
        self._study_site_list_label.setText('')
        self._table_widget.clearContents()
        self._study_id = params.get('study_id', None)
        if self._study_id:
            # self.load_data('get_study_sites', self._study_id)
            pass
    
    def on_data_ready(self, study_sites, error):
        self.update_study_site_list_label(error)
        self.update_table_widget(study_sites)