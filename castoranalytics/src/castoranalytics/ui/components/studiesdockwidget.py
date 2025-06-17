from PySide6.QtWidgets import QDockWidget, QVBoxLayout

import castoranalytics.ui.constants as constants

from castoranalytics.ui.components.studieswidget import StudiesWidget

# TODO: Show warning if API credentials are not configured


class StudiesDockWidget(QDockWidget):
    def __init__(self):
        super(StudiesDockWidget, self).__init__(
            constants.CASTOR_ANALYTICS_STUDIES_DOCK_WIDGET_TITLE)
        self.setObjectName(constants.CASTOR_ANALYTICS_STUDIES_DOCK_WIDGET_OBJECT_NAME)
        self.setWidget(StudiesWidget())