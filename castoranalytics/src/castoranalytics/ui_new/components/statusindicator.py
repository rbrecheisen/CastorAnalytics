from PySide6.QtWidgets import QStatusBar

import castoranalytics.ui_new.constants as constants


class StatusIndicator(QStatusBar):
    def __init__(self):
        super(StatusIndicator, self).__init__()
        self.setObjectName(constants.CASTOR_ANALYTICS_STATUS_INDICATOR_OBJECT_NAME)
        self.showMessage(constants.CASTOR_ANALYTICS_STATUS_READY)