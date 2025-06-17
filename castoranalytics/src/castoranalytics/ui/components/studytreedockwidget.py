from PySide6.QtWidgets import QDockWidget

import castoranalytics.ui.constants as constants


class StudyTreeDockerWidget(QDockWidget):
    def __init__(self):
        super(StudyTreeDockerWidget, self).__init__(
            constants.CASTOR_ANALYTICS_STUDY_TREE_DOCK_WIDGET_TITLE)
        self.setObjectName(constants.CASTOR_ANALYTICS_STUDY_TREE_DOCK_WIDGET_OBJECT_NAME)