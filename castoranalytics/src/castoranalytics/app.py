"""
Desktop application to view summary statistics and advanced visualizations of your Castor EDC studies
"""

import sys
import importlib.metadata

from PySide6 import QtWidgets

from castoranalytics.ui.uibuilder import UiBuilder


class CastorAnalytics(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self._ui_builder = UiBuilder(self, title='Castor Analytics')
        self._ui_builder.build()
        self.show()


def main():
    # Linux desktop environments use an app's .desktop file to integrate the app
    # in to their application menus. The .desktop file of this app will include
    # the StartupWMClass key, set to app's formal name. This helps associate the
    # app's windows to its menu item.
    #
    # For association to work, any windows of the app must have WMCLASS property
    # set to match the value set in app's desktop file. For PySide6, this is set
    # with setApplicationName().

    # Find the name of the module that was used to start the app
    app_module = sys.modules["__main__"].__package__
    # Retrieve the app's metadata
    metadata = importlib.metadata.metadata(app_module)

    QtWidgets.QApplication.setApplicationName(metadata["Formal-Name"])

    app = QtWidgets.QApplication(sys.argv)
    main_window = CastorAnalytics()
    sys.exit(app.exec())
