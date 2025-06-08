from PySide6.QtCore import QObject, QEvent, QCoreApplication


class FunctionEvent(QEvent):
    EVENT_TYPE = QEvent.Type(QEvent.registerEventType())

    def __init__(self, func, *args, **kwargs):
        super().__init__(FunctionEvent.EVENT_TYPE)
        self.func = func
        self.args = args
        self.kwargs = kwargs


class EventDispatcher(QObject):
    def event(self, event):
        if isinstance(event, FunctionEvent):
            event.func(*event.args, **event.kwargs)
            return True
        return super().event(event)


_dispatcher = EventDispatcher()


def to_main_thread(func):
    def wrapper(*args, **kwargs):
        QCoreApplication.postEvent(_dispatcher, FunctionEvent(func, *args, **kwargs))
    return wrapper