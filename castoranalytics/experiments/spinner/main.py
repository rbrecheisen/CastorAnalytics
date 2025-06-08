from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QApplication, QHBoxLayout, QFrame
from PySide6.QtCore import Qt, QEvent
import sys

class BusyOverlay(QWidget):
    def __init__(self, parent=None, message="Please wait..."):
        super().__init__(parent)

        self.setAttribute(Qt.WA_TransparentForMouseEvents, False)
        self.setAttribute(Qt.WA_NoSystemBackground)
        self.setAttribute(Qt.WA_StyledBackground)
        self.setWindowFlags(Qt.Widget | Qt.FramelessWindowHint)

        # Semi-transparent background for the whole overlay
        self.setStyleSheet("""
            background-color: rgba(0, 0, 0, 128);
        """)

        # Create a small "message box" frame
        box = QFrame(self)
        box.setStyleSheet("""
            background-color: rgba(256, 256, 256, 200);
            color: white;
            border-radius: 10px;
            padding: 15px;
        """)
        box.setFrameShape(QFrame.StyledPanel)

        label = QLabel(message, box)
        label.setStyleSheet("font-size: 16px;")
        label.setAlignment(Qt.AlignCenter)

        box_layout = QVBoxLayout(box)
        box_layout.addWidget(label)

        # Main layout centers the box
        main_layout = QHBoxLayout(self)
        main_layout.addStretch()
        vbox = QVBoxLayout()
        vbox.addStretch()
        vbox.addWidget(box, alignment=Qt.AlignCenter)
        vbox.addStretch()
        main_layout.addLayout(vbox)
        main_layout.addStretch()

        self.setLayout(main_layout)

        # Keep in sync with parent resize
        if parent:
            parent.installEventFilter(self)

        self.hide()

    def show_overlay(self):
        if self.parent():
            self.resize(self.parent().size())
        self.show()
        self.raise_()

    def hide_overlay(self):
        self.hide()

    def eventFilter(self, obj, event):
        if obj == self.parent() and event.type() == QEvent.Resize:
            self.resize(self.parent().size())
        return super().eventFilter(obj, event)

# Example usage:

if __name__ == "__main__":
    app = QApplication(sys.argv)
    from PySide6.QtWidgets import QMainWindow, QPushButton

    class MainWindow(QMainWindow):
        def __init__(self):
            super().__init__()
            self.setWindowTitle("Main Window")
            self.resize(600, 400)

            btn = QPushButton("Start Long Task", self)
            btn.clicked.connect(self.start_long_task)
            self.setCentralWidget(btn)

            self.busy_overlay = BusyOverlay(self)

        def start_long_task(self):
            self.busy_overlay.show_overlay()

            # Simulate a background task using a timer
            from PySide6.QtCore import QTimer
            QTimer.singleShot(3000, self.task_finished)

        def task_finished(self):
            self.busy_overlay.hide_overlay()

    window = MainWindow()
    window.show()
    sys.exit(app.exec())

# from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QApplication
# from PySide6.QtCore import Qt, QEvent
# import sys

# class BusyOverlay(QWidget):
#     def __init__(self, parent=None, message="Please wait..."):
#         super().__init__(parent)

#         self.setAttribute(Qt.WA_TransparentForMouseEvents, False)
#         self.setAttribute(Qt.WA_NoSystemBackground)
#         self.setAttribute(Qt.WA_StyledBackground)
#         self.setWindowFlags(Qt.Widget | Qt.FramelessWindowHint)

#         self.setStyleSheet("""
#             background-color: rgba(0, 0, 0, 128);
#         """)

#         label = QLabel(message, self)
#         label.setStyleSheet("""
#             color: white;
#             font-size: 18px;
#         """)
#         label.setAlignment(Qt.AlignCenter)

#         layout = QVBoxLayout(self)
#         layout.addStretch()
#         layout.addWidget(label)
#         layout.addStretch()
#         self.setLayout(layout)

#         # Keep in sync with parent resize
#         if parent:
#             parent.installEventFilter(self)

#         self.hide()

#     def show_overlay(self):
#         """Show the overlay covering the parent."""
#         if self.parent():
#             self.resize(self.parent().size())
#         self.show()
#         self.raise_()

#     def hide_overlay(self):
#         self.hide()

#     def eventFilter(self, obj, event):
#         if obj == self.parent() and event.type() == QEvent.Resize:
#             self.resize(self.parent().size())
#         return super().eventFilter(obj, event)

# # Example usage:

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     from PySide6.QtWidgets import QMainWindow, QPushButton

#     class MainWindow(QMainWindow):
#         def __init__(self):
#             super().__init__()
#             self.setWindowTitle("Main Window")
#             self.resize(600, 400)

#             btn = QPushButton("Start Long Task", self)
#             btn.clicked.connect(self.start_long_task)
#             self.setCentralWidget(btn)

#             self.busy_overlay = BusyOverlay(self)

#         def start_long_task(self):
#             self.busy_overlay.show_overlay()

#             # Simulate a background task using a timer
#             from PySide6.QtCore import QTimer
#             QTimer.singleShot(3000, self.task_finished)

#         def task_finished(self):
#             self.busy_overlay.hide_overlay()

#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec())
