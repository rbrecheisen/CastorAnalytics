from PySide6.QtWidgets import QApplication, QPushButton, QLabel, QVBoxLayout, QWidget
from PySide6.QtCore import QFutureWatcher, Slot
from PySide6.QtConcurrent import run
import time

# Background function (your core logic)
def long_running_task():
    time.sleep(3)
    return "Finished result"

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.button = QPushButton("Start Task")
        self.label = QLabel("Ready")
        layout = QVBoxLayout()
        layout.addWidget(self.button)
        layout.addWidget(self.label)
        self.setLayout(layout)

        self.button.clicked.connect(self.start_task)

    def start_task(self):
        self.label.setText("Running...")

        # Create the watcher
        self.watcher = QFutureWatcher()

        # Connect the finished signal
        self.watcher.finished.connect(self.on_task_finished)

        # Run the function in a background thread
        future = run(long_running_task)
        self.watcher.setFuture(future)

    @Slot()
    def on_task_finished(self):
        # Retrieve the result safely
        result = self.watcher.future().result()
        self.label.setText(f"Result: {result}")

app = QApplication([])
window = MainWindow()
window.show()
app.exec()
