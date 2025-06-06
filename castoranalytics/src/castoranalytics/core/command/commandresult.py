from enum import Enum


class CommandResult:
    class Status(Enum):
        INIT = 0
        OK = 1

    def __init__(self):
        self._status = self.Status.INIT
        self._dict = {}
    
    def get_status(self):
        return self._status
    
    def set_status(self, status):
        self._status = status
    
    def get(self, name, default=None):
        return self._dict.get(name, default)
    
    def set(self, name, object):
        self._dict[name] = object