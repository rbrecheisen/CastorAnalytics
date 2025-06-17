from PySide6.QtWidgets import QDockWidget

import castoranalytics.ui.constants as constants


class LoggingDockWidget(QDockWidget):
    def __init__(self):
        super(LoggingDockWidget, self).__init__(
            constants.CASTOR_ANALYTICS_LOGGING_DOCK_WIDGET_TITLE)
        self.setObjectName(constants.CASTOR_ANALYTICS_LOGGING_DOCK_WIDGET_OBJECT_NAME)