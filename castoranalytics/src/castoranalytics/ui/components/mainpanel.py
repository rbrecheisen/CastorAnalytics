from PySide6.QtWidgets import (
    QTabWidget,
    QTextEdit,
)

import castoranalytics.ui.constants as constants


class MainPanel(QTabWidget):
    def __init__(self):
        super(MainPanel, self).__init__()
        # Move tabs to separate classes
        self.addTab(QTextEdit(''), constants.CASTOR_ANALYTICS_MAIN_TAB_DETAILS_TITLE)
        self.addTab(QTextEdit(''), constants.CASTOR_ANALYTICS_MAIN_TAB_STATISTICS_TITLE)
        self.addTab(QTextEdit(''), constants.CASTOR_ANALYTICS_MAIN_TAB_VISUALIZATIONS_TITLE)