import sys
import importlib.metadata

from PySide6 import QtWidgets

from castoranalytics.ui.mainwindow import MainWindow
from castoranalytics.ui.bootstrap import BOOTSTRAP_CSS


def main():
    app_module = sys.modules["__main__"].__package__
    metadata = importlib.metadata.metadata(app_module)
    QtWidgets.QApplication.setApplicationName(metadata["Formal-Name"])
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(BOOTSTRAP_CSS)
    main_window = MainWindow() # you need to create a variable!
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
