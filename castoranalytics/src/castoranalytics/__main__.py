from PySide6.QtWidgets import QApplication
from castoranalytics.app import CastorAnalytics


def main():
    app = QApplication([])
    window = CastorAnalytics()
    window.show()
    app.exec()


if __name__ == "__main__":
    main()