from PySide6.QtWidgets import QDockWidget

import castoranalytics.ui_new.constants as constants

from castoranalytics.ui_new.components.logswidget import LogsWidget


class LogsDockWidget(QDockWidget):
    def __init__(self):
        super(LogsDockWidget, self).__init__(
            constants.CASTOR_ANALYTICS_LOGS_DOCK_WIDGET_TITLE)
        self.setObjectName(constants.CASTOR_ANALYTICS_LOGS_DOCK_WIDGET_OBJECT_NAME)
        self.setWidget(LogsWidget())