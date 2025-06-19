from PySide6.QtWidgets import QToolBar

import castoranalytics.ui_new.constants as constants


class ToolBar(QToolBar):
    def __init__(self):
        super(ToolBar, self).__init__()
        self.setObjectName(constants.CASTOR_ANALYTICS_TOOLBAR_OBJECT_NAME)
        self.addAction('Action 1')
        self.addAction('Action 2')
