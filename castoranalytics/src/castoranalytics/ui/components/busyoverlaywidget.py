from PySide6.QtWidgets import (
    QWidget,
    QFrame,
    QLabel,
    QVBoxLayout,
    QHBoxLayout,
)
from PySide6.QtCore import Qt, QEvent


class BusyOverlayWidget(QWidget):
    def __init__(self, parent, message="Loading..."):
        super(BusyOverlayWidget, self).__init__(parent)
        self.setAttribute(Qt.WA_TransparentForMouseEvents, False)
        self.setAttribute(Qt.WA_NoSystemBackground)
        self.setAttribute(Qt.WA_StyledBackground)
        self.setWindowFlags(Qt.Widget | Qt.FramelessWindowHint)
        self.setStyleSheet("""
            background-color: rgba(0, 0, 0, 128);
        """)
        box = QFrame(self)
        box.setStyleSheet("""
            background-color: rgba(0, 0, 0, 128);
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
        main_layout = QHBoxLayout(self)
        main_layout.addStretch()
        vbox = QVBoxLayout()
        vbox.addStretch()
        vbox.addWidget(box, alignment=Qt.AlignCenter)
        vbox.addStretch()
        main_layout.addLayout(vbox)
        main_layout.addStretch()
        self.setLayout(main_layout)
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