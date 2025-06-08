from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget
from PySide6.QtCore import QThread, Signal, Slot, Qt
from PySide6.QtGui import QMovie
import time

# Example worker running in background thread
class Worker(QThread):
    finished = Signal()

    def run(self):
        # Simulate long-running task
        time.sleep(5)
        self.finished.emit()

# Main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Background Task with Animated Indicator")

        # Layout
        layout = QVBoxLayout()

        # Button to start task
        self.button = QPushButton("Start Task")
        self.button.clicked.connect(self.start_task)
        layout.addWidget(self.button)

        # Animated indicator (initially hidden)
        self.loading_label = QLabel(self)
        self.loading_movie = QMovie("D:\\SoftwareDevelopment\\GitHub\\CastorAnalytics\\castoranalytics\\experiments\\spinner\\spinner.gif")  # Use your spinner GIF here
        self.loading_label.setMovie(self.loading_movie)
        self.loading_label.setVisible(False)  # Hide initially
        layout.addWidget(self.loading_label, alignment=Qt.AlignCenter)

        # Central widget
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def start_task(self):
        # Show animation
        self.loading_label.setVisible(True)
        self.loading_movie.start()

        # Start worker thread
        self.worker = Worker()
        self.worker.finished.connect(self.task_done)
        self.worker.start()

    @Slot()
    def task_done(self):
        # Hide animation
        self.loading_movie.stop()
        self.loading_label.setVisible(False)
        self.worker.deleteLater()

# Main entry point
if __name__ == "__main__":
    app = QApplication([])

    window = MainWindow()
    window.resize(400, 300)
    window.show()

    app.exec()
