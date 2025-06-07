import sys

from PySide6 import QtWidgets

from castoranalytics.ui.mainwindow import MainWindow


def main():
    QtWidgets.QApplication.setApplicationName('Castor Analytics')
    app = QtWidgets.QApplication(sys.argv)
    # main_window = MainWindow()
    main_window = QtWidgets.QMainWindow()
    main_window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()